#!/usr/bin/env python3
"""SiteHustle: find restaurants with weak websites, build them a better one,
pitch it for a flat fee, and launch it when they pay.

The daily Claude run (see RUNBOOK.md) does the judgment work: researching a
restaurant, scoring its site and writing its content. This script does the
mechanical work: storing leads, building and deploying sites, sending email,
following up and matching Stripe payments.

Credentials are never stored here. The cloud environment's network proxy adds
the Netlify, Resend and Stripe keys to requests on the way out, so the
script sends a placeholder Authorization header.

Usage: python3 scripts/hustle.py <command> [args]   (run from sitehustle/)
  status                      Pipeline summary
  discover                    Pull restaurant candidates from OpenStreetMap
  upsert <lead.json>          Add or update a researched lead (from the Claude run)
  build <id> [--final]        Render the site to sites/<slug>/
  deploy <id>                 Publish sites/<slug>/ to Netlify
  queue                       Write outreach emails for deployed previews
  digest                      Email the owner today's queue for approval (trial mode)
  approve                     Mark everything in the queue approved
  send                        Send approved (trial) or queued (auto) emails, within limits
  followups                   Queue one follow-up for leads that went quiet
  payments                    Check Stripe and mark paid leads
  launch <id>                 Final build, deploy, and send the "you're live" email
  mark <id> <status> [note]   Set a status by hand (replied, lost, unsubscribed...)
  suppress <email|domain>     Never contact this address or domain again
"""
from __future__ import annotations

import datetime as dt
import io
import json
import re
import sys
import time
import urllib.parse
import zipfile
from pathlib import Path
from zoneinfo import ZoneInfo

import requests
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
LEADS = ROOT / "data" / "leads.json"
SUPPRESS = ROOT / "data" / "suppression.txt"
SITES = ROOT / "sites"
OUTBOX = ROOT / "outbox"
TZ = ZoneInfo("America/New_York")
PLACEHOLDER_AUTH = {"Authorization": "Bearer injected-by-proxy"}

STATUSES = [
    "new",          # found, not researched yet
    "skipped",      # good site already, chain, no contact, etc.
    "researched",   # content gathered, ready to build
    "built",        # preview rendered locally
    "deployed",     # preview is live on Netlify
    "queued",       # outreach email written, waiting to send / approve
    "approved",     # owner approved (trial mode)
    "contacted",    # first email sent
    "followed_up",  # follow-up sent
    "replied",      # they wrote back (Claude handles the conversation)
    "paid",         # Stripe payment matched
    "launched",     # final site live
    "lost",         # said no
    "unsubscribed", # asked to stop
]

THEMES = {
    "italian":  dict(bg="#fbf7f1", surface="#f3ece1", ink="#2a1d16", muted="#6f5e52", accent="#b4382a", accent_ink="#fff", line="#e3d7c6", hero_a="#3b1f17", hero_b="#8c2f22", display_font="Playfair Display", body_font="Inter"),
    "pizza":    dict(bg="#fffaf2", surface="#fff1dc", ink="#1f1a17", muted="#6a5f57", accent="#d6421f", accent_ink="#fff", line="#f0dcc0", hero_a="#2b140c", hero_b="#c2401c", display_font="Bricolage Grotesque", body_font="Inter"),
    "greek":    dict(bg="#f7fafc", surface="#eaf1f7", ink="#13283d", muted="#52677b", accent="#1d5fa0", accent_ink="#fff", line="#d3e0ec", hero_a="#0f2a47", hero_b="#2f73b3", display_font="Cormorant Garamond", body_font="Inter"),
    "mexican":  dict(bg="#fffaf3", surface="#fdeeda", ink="#2b1b12", muted="#71594a", accent="#c2410c", accent_ink="#fff", line="#f1dcc1", hero_a="#3a1406", hero_b="#b45309", display_font="Fraunces", body_font="Inter"),
    "asian":    dict(bg="#faf8f5", surface="#f1ece4", ink="#1c1917", muted="#655d56", accent="#b91c1c", accent_ink="#fff", line="#e5ddd2", hero_a="#1c1917", hero_b="#7f1d1d", display_font="Shippori Mincho", body_font="Inter"),
    "cafe":     dict(bg="#f8f5f0", surface="#efe8dd", ink="#2b2420", muted="#6e6259", accent="#7a5230", accent_ink="#fff", line="#e1d6c6", hero_a="#2f241d", hero_b="#8a6141", display_font="DM Serif Display", body_font="DM Sans"),
    "diner":    dict(bg="#fffdf7", surface="#fff3d6", ink="#1d2633", muted="#5a6577", accent="#c81e3a", accent_ink="#fff", line="#f1e3bd", hero_a="#13213a", hero_b="#c81e3a", display_font="Alfa Slab One", body_font="Inter"),
    "bar":      dict(bg="#121212", surface="#1c1c1c", ink="#f3efe8", muted="#a49d93", accent="#e0a43a", accent_ink="#121212", line="#2c2c2c", hero_a="#0b0b0b", hero_b="#3a2a12", display_font="Oswald", body_font="Inter"),
    "bbq":      dict(bg="#faf6f1", surface="#f0e6da", ink="#21160f", muted="#6b5b4e", accent="#9a3412", accent_ink="#fff", line="#e1d1bf", hero_a="#1a0f08", hero_b="#7c2d12", display_font="Bitter", body_font="Inter"),
    "default":  dict(bg="#faf9f7", surface="#f1eee9", ink="#1e1b18", muted="#67605a", accent="#0f766e", accent_ink="#fff", line="#e2ddd5", hero_a="#13201f", hero_b="#0f766e", display_font="Fraunces", body_font="Inter"),
}
THEME_KEYWORDS = [
    ("pizza", ["pizza", "pizzeria"]), ("italian", ["italian", "pasta", "trattoria"]),
    ("greek", ["greek", "mediterranean", "gyro", "lebanese"]),
    ("mexican", ["mexican", "taco", "latin", "tex-mex", "cantina"]),
    ("asian", ["chinese", "japanese", "sushi", "thai", "vietnamese", "pho", "korean", "indian", "asian", "ramen"]),
    ("cafe", ["cafe", "coffee", "bakery", "tea", "brunch"]), ("diner", ["diner", "breakfast", "family"]),
    ("bar", ["bar", "pub", "brewery", "tavern", "taproom", "wine"]), ("bbq", ["bbq", "barbecue", "smokehouse", "steak"]),
]
DOW = {"sun": 0, "mon": 1, "tue": 2, "wed": 3, "thu": 4, "fri": 5, "sat": 6}


# ---------- storage ----------
def cfg() -> dict:
    return yaml.safe_load((ROOT / "config.yaml").read_text())


def save_cfg(c: dict) -> None:
    text = (ROOT / "config.yaml").read_text()
    # Only the outreach mode is ever changed by code; edit it in place to keep comments.
    text = re.sub(r"(?m)^(\s*mode:\s*)\w+", rf"\g<1>{c['outreach']['mode']}", text, count=1)
    (ROOT / "config.yaml").write_text(text)


def load() -> list[dict]:
    return json.loads(LEADS.read_text())


def save(leads: list[dict]) -> None:
    LEADS.write_text(json.dumps(leads, indent=2, ensure_ascii=False) + "\n")


def now() -> str:
    return dt.datetime.now(TZ).isoformat(timespec="seconds")


def log(lead: dict, event: str) -> None:
    lead.setdefault("history", []).append({"at": now(), "event": event})


def find(leads: list[dict], lead_id: str) -> dict:
    for l in leads:
        if l["id"] == lead_id or l.get("slug") == lead_id:
            return l
    sys.exit(f"No lead {lead_id!r}")


def slugify(s: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")[:40]


def suppressed(email: str | None) -> bool:
    if not email:
        return False
    email = email.lower().strip()
    lines = {x.strip().lower() for x in SUPPRESS.read_text().splitlines() if x.strip() and not x.startswith("#")}
    return email in lines or email.split("@")[-1] in lines


def require_live_config(c: dict) -> None:
    missing = [k for k, v in {**c["business"], "stripe_payment_link": c["offer"]["stripe_payment_link"]}.items()
               if isinstance(v, str) and v.startswith("TODO")]
    if missing:
        sys.exit("Fill these in config.yaml before sending: " + ", ".join(missing))


# ---------- discovery ----------
def cmd_discover() -> None:
    c, leads = cfg(), load()
    known = {(l["name"].lower(), (l.get("address") or "")[:12].lower()) for l in leads}
    known_osm = {l.get("osm_id") for l in leads}
    added = 0
    for area in c["targeting"]["areas"]:
        q = (f'[out:json][timeout:90];nwr["amenity"~"^(restaurant|cafe|bar|pub|fast_food|ice_cream)$"]'
             f'(around:{area["radius_m"]},{area["lat"]},{area["lon"]});out center tags;')
        r = None
        for attempt in range(4):
            try:
                r = requests.post("https://overpass-api.de/api/interpreter", data={"data": q},
                                  headers={"User-Agent": "sitehustle/1.0"}, timeout=120)
                r.raise_for_status()
                break
            except requests.RequestException as e:
                print(f"  overpass attempt {attempt + 1} failed: {e}")
                time.sleep(5 * (attempt + 1))
        if r is None or not r.ok:
            print(f"Could not reach OpenStreetMap for {area['name']}. Use web search instead (see RUNBOOK).")
            continue
        for e in r.json().get("elements", []):
            t = e.get("tags", {})
            name = t.get("name")
            if not name or (c["targeting"]["skip_chains"] and ("brand" in t or "brand:wikidata" in t)):
                continue
            osm_id = f'{e["type"]}/{e["id"]}'
            addr = " ".join(filter(None, [t.get("addr:housenumber"), t.get("addr:street")]))
            city = t.get("addr:city") or area["name"].split(",")[0]
            full = f"{addr}, {city}, PA {t.get('addr:postcode', '')}".strip(", ") if addr else ""
            if osm_id in known_osm or (name.lower(), full[:12].lower()) in known:
                continue
            leads.append({
                "id": f"L{len(leads) + 1:04d}", "slug": slugify(name), "name": name, "status": "new",
                "osm_id": osm_id, "area": area["name"], "city": city, "address": full,
                "phone": t.get("phone") or t.get("contact:phone"),
                "website": t.get("website") or t.get("contact:website"),
                "email": t.get("email") or t.get("contact:email"),
                "cuisine": (t.get("cuisine") or t.get("amenity", "")).replace("_", " "),
                "facebook": t.get("contact:facebook"), "history": [{"at": now(), "event": "discovered via OSM"}],
            })
            added += 1
    save(leads)
    print(f"Added {added} new candidates. Total leads: {len(leads)}")


def cmd_upsert(path: str) -> None:
    """Merge a researched lead (written by the Claude run) into leads.json."""
    data = json.loads(Path(path).read_text())
    items = data if isinstance(data, list) else [data]
    leads = load()
    for d in items:
        existing = next((l for l in leads if l["id"] == d.get("id") or
                         (d.get("name") and l["name"].lower() == d["name"].lower() and
                          (l.get("address") or "")[:12].lower() == (d.get("address") or "")[:12].lower())), None)
        if existing:
            hist = existing.get("history", [])
            existing.update({k: v for k, v in d.items() if k != "history"})
            existing["history"] = hist
            log(existing, f"updated -> {existing.get('status')}")
            print(f"Updated {existing['id']} {existing['name']} ({existing['status']})")
        else:
            d.setdefault("id", f"L{len(leads) + 1:04d}")
            d.setdefault("slug", slugify(d["name"]))
            d.setdefault("status", "researched")
            d["history"] = [{"at": now(), "event": f"added -> {d['status']}"}]
            leads.append(d)
            print(f"Added {d['id']} {d['name']} ({d['status']})")
    save(leads)


# ---------- build ----------
def pick_theme(lead: dict) -> dict:
    key = lead.get("theme")
    if key not in THEMES:
        hay = f"{lead.get('cuisine', '')} {lead.get('name', '')}".lower()
        key = next((k for k, words in THEME_KEYWORDS if any(w in hay for w in words)), "default")
    t = dict(THEMES[key])
    t["display_font_url"] = t["display_font"].replace(" ", "+") + ":wght@400;700"
    t["body_font_url"] = t["body_font"].replace(" ", "+") + ":wght@400;500;600;700"
    return t


def claim_url(c: dict, lead: dict) -> str:
    link = c["offer"]["stripe_payment_link"]
    if link.startswith("TODO"):
        return "#"
    sep = "&" if "?" in link else "?"
    params = {"client_reference_id": lead["id"]}
    if lead.get("email"):
        params["prefilled_email"] = lead["email"]
    return link + sep + urllib.parse.urlencode(params)


def parse_dow(days: str) -> str:
    """'Mon-Thu' -> '1,2,3,4'; 'Fri & Sat' -> '5,6'; 'Daily' -> all."""
    s = days.lower()
    if "daily" in s or "every day" in s or "7 days" in s:
        return "0,1,2,3,4,5,6"
    found = set()
    for a, b in re.findall(r"(sun|mon|tue|wed|thu|fri|sat)\w*\s*[-–to]+\s*(sun|mon|tue|wed|thu|fri|sat)", s):
        i, j = DOW[a], DOW[b]
        rng = range(i, j + 1) if i <= j else list(range(i, 7)) + list(range(0, j + 1))
        found.update(rng)
    found.update(DOW[d] for d in re.findall(r"(sun|mon|tue|wed|thu|fri|sat)", s))
    return ",".join(str(x) for x in sorted(found))


def cmd_build(lead_id: str, final: bool = False) -> None:
    c, leads = cfg(), load()
    lead = find(leads, lead_id)
    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html", "j2"]))
    r = dict(lead)
    r["phone_tel"] = re.sub(r"[^\d+]", "", r.get("phone") or "")
    r["claim_url"] = claim_url(c, lead)
    r.setdefault("tagline", f"Fresh, made-from-scratch food in the heart of {r.get('city', 'town')}.")
    r.setdefault("meta_description", f"{r['name']}: menu, hours, location and online ordering. {r.get('address', '')}")
    if isinstance(r.get("about"), str):
        r["about"] = [p.strip() for p in r["about"].split("\n\n") if p.strip()]
    for h in r.get("hours") or []:
        h.setdefault("dow", parse_dow(h.get("days", "")))
    r["address_short"] = (r.get("address") or "").split(",")[0]
    r["jsonld"] = json.dumps({
        "@context": "https://schema.org", "@type": "Restaurant", "name": r["name"],
        "address": r.get("address"), "telephone": r.get("phone"), "servesCuisine": r.get("cuisine"),
        "url": r.get("live_url") or r.get("preview_url"),
    }).replace("</", "<\\/")
    html = env.get_template("site/index.html.j2").render(
        r=r, theme=pick_theme(lead), biz=c["business"], preview=not final, year=dt.date.today().year)
    out = SITES / lead["slug"]
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(html)
    (out / "robots.txt").write_text("User-agent: *\nDisallow: /\n" if not final else "User-agent: *\nAllow: /\n")
    if lead["status"] in ("researched", "new"):
        lead["status"] = "built"
    log(lead, "built final site" if final else "built preview")
    save(leads)
    print(f"Built {out / 'index.html'}")


# ---------- deploy (Netlify) ----------
def netlify(method: str, path: str, **kw) -> requests.Response:
    r = requests.request(method, f"https://api.netlify.com/api/v1{path}",
                         headers={**PLACEHOLDER_AUTH, **kw.pop("headers", {})}, timeout=120, **kw)
    if r.status_code == 401:
        sys.exit("Netlify rejected the request: add a Netlify token for api.netlify.com in the environment.")
    r.raise_for_status()
    return r


def cmd_deploy(lead_id: str) -> None:
    c, leads = cfg(), load()
    lead = find(leads, lead_id)
    folder = SITES / lead["slug"]
    if not (folder / "index.html").exists():
        sys.exit("Build it first.")
    if not lead.get("netlify_site_id"):
        base = c["hosting"]["site_name_prefix"] + lead["slug"]
        for suffix in ["", "-pa", f"-{lead['id'].lower()}"]:
            r = requests.post("https://api.netlify.com/api/v1/sites", headers=PLACEHOLDER_AUTH,
                              json={"name": (base + suffix)[:63]}, timeout=60)
            if r.status_code == 422:  # name taken
                continue
            if r.status_code == 401:
                sys.exit("Netlify rejected the request: add a Netlify token for api.netlify.com in the environment.")
            r.raise_for_status()
            site = r.json()
            lead["netlify_site_id"], lead["netlify_subdomain"] = site["id"], site["name"]
            break
        else:
            sys.exit("Could not get a free Netlify site name.")
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for f in folder.rglob("*"):
            if f.is_file():
                z.write(f, f.relative_to(folder))
    d = netlify("POST", f"/sites/{lead['netlify_site_id']}/deploys", data=buf.getvalue(),
                headers={"Content-Type": "application/zip"}).json()
    url = d.get("ssl_url") or f"https://{lead['netlify_subdomain']}.netlify.app"
    if lead["status"] in ("built", "researched"):
        lead["preview_url"] = url
        lead["status"] = "deployed"
    log(lead, f"deployed {url}")
    save(leads)
    print(f"Deployed {lead['name']}: {url}")


# ---------- email (Resend) ----------
def send_email(c: dict, to: str, subject: str, body: str, reply_headers: dict | None = None) -> str:
    biz = c["business"]
    payload = {
        "from": f"{biz['sender_name']} <{biz['sender_email']}>", "to": [to], "subject": subject,
        "text": body, "reply_to": biz["reply_to"],
        "headers": {"List-Unsubscribe": f"<mailto:{biz['reply_to']}?subject=unsubscribe>", **(reply_headers or {})},
    }
    r = requests.post("https://api.resend.com/emails", headers=PLACEHOLDER_AUTH, json=payload, timeout=60)
    if r.status_code in (401, 403):
        sys.exit("Resend rejected the request: add a Resend API key for api.resend.com in the environment.")
    r.raise_for_status()
    return r.json().get("id", "")


def render_email(c: dict, lead: dict, kind: str) -> tuple[str, str]:
    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=False)
    p = lead.get("pitch", {})
    problems = p.get("problems") or ["it's hard to read on a phone"]
    if len(problems) == 1:
        ps = problems[0] + "."
    else:
        ps = ", ".join(problems[:-1]) + ", and " + problems[-1] + "."
    highlights = p.get("highlights") or ["your full menu", "hours", "a map", "one-tap calling on phones"]
    hs = ", ".join(highlights[:-1]) + " and " + highlights[-1] if len(highlights) > 1 else highlights[0]
    r = dict(lead, claim_url=claim_url(c, lead))
    text = env.get_template(f"email/{kind}.txt.j2").render(
        r=r, biz=c["business"], offer=c["offer"],
        greeting=p.get("greeting") or f"{lead['name']} team",
        compliment=p.get("compliment") or f"have heard good things about {lead['name']}",
        problems_sentence=ps, highlights_sentence=hs,
        subject=p.get("subject") or f"A new website for {lead['name']}",
    )
    subject, _, body = text.partition("\n")
    return subject.removeprefix("Subject: ").strip(), body.lstrip("\n")


def write_outbox(lead: dict, kind: str, subject: str, body: str) -> Path:
    path = OUTBOX / f"{lead['id']}-{kind}.json"
    path.write_text(json.dumps({"lead": lead["id"], "kind": kind, "to": lead["email"],
                                "subject": subject, "body": body, "approved": False}, indent=2))
    return path


def cmd_queue() -> None:
    c, leads = cfg(), load()
    n = 0
    for lead in leads:
        if lead["status"] != "deployed":
            continue
        if not lead.get("email") or suppressed(lead["email"]):
            lead["status"] = "skipped"
            log(lead, "skipped: no usable email")
            continue
        subject, body = render_email(c, lead, "outreach")
        write_outbox(lead, "outreach", subject, body)
        lead["status"] = "queued"
        log(lead, "outreach queued")
        n += 1
    save(leads)
    print(f"Queued {n} outreach emails.")


def outbox_items() -> list[tuple[Path, dict]]:
    return [(p, json.loads(p.read_text())) for p in sorted(OUTBOX.glob("*.json"))]


def cmd_digest() -> None:
    c = cfg()
    require_live_config(c)
    items = [i for _, i in outbox_items() if not i["approved"]]
    if not items:
        print("Nothing waiting for approval.")
        return
    leads = {l["id"]: l for l in load()}
    parts = [f"{len(items)} emails are ready to send. Reply APPROVE to send them all, or reply "
             f"\"SKIP L0003, L0007\" to hold some back.\n"]
    for i in items:
        l = leads[i["lead"]]
        parts.append(f"\n==== {l['id']} | {l['name']} | design score {l.get('audit', {}).get('score', '?')}/10\n"
                     f"Old site: {l.get('website') or 'none'}\nNew preview: {l.get('preview_url')}\n"
                     f"To: {i['to']}\nSubject: {i['subject']}\n\n{i['body']}")
    mid = send_email(c, c["business"]["owner_digest_email"],
                     f"[SiteHustle] {len(items)} emails ready to approve ({dt.date.today():%b %d})", "\n".join(parts))
    print(f"Digest sent ({mid}).")


def cmd_approve(skip: list[str] | None = None) -> None:
    skip = {s.upper() for s in (skip or [])}
    for p, i in outbox_items():
        if i["lead"].upper() not in skip:
            i["approved"] = True
            p.write_text(json.dumps(i, indent=2))
    print("Approved." + (f" Held back: {', '.join(sorted(skip))}" if skip else ""))


def sent_today(leads: list[dict]) -> int:
    today = dt.datetime.now(TZ).date().isoformat()
    return sum(1 for l in leads for e in l.get("emails", []) if e["at"].startswith(today))


def cmd_send(force_window: bool = False) -> None:
    c, leads = cfg(), load()
    require_live_config(c)
    o = c["outreach"]
    t = dt.datetime.now(TZ)
    if o["mode"] == "trial" and t.date().isoformat() >= str(o["trial_ends"]):
        o["mode"] = "auto"
        save_cfg(c)
        print("Trial period over: switched outreach to auto mode.")
    lo, hi = o["send_window_hours_local"]
    if not force_window and (t.weekday() >= 5 or not lo <= t.hour < hi):
        print(f"Outside the send window ({lo}:00-{hi}:00 ET, weekdays). Nothing sent.")
        return
    budget = o["daily_send_limit"] - sent_today(leads)
    by_id = {l["id"]: l for l in leads}
    sent = 0
    for p, item in outbox_items():
        if budget <= 0:
            print("Daily send limit reached.")
            break
        if o["mode"] == "trial" and not item["approved"]:
            continue
        lead = by_id[item["lead"]]
        if suppressed(item["to"]) or lead["status"] in ("unsubscribed", "lost", "replied", "paid", "launched"):
            p.unlink()
            continue
        prev = next((e for e in lead.get("emails", []) if e["type"] == "outreach"), None)
        headers = {"In-Reply-To": prev["message_id"], "References": prev["message_id"]} if prev and item["kind"] == "followup" else None
        mid = send_email(c, item["to"], item["subject"], item["body"], headers)
        lead.setdefault("emails", []).append({"at": now(), "type": item["kind"], "message_id": mid, "subject": item["subject"]})
        lead["status"] = "contacted" if item["kind"] == "outreach" else "followed_up"
        log(lead, f"sent {item['kind']}")
        p.unlink()
        sent += 1
        budget -= 1
        save(leads)
        time.sleep(20)  # spread sends out; bursts look like spam
    print(f"Sent {sent} emails.")


def cmd_followups() -> None:
    c, leads = cfg(), load()
    o = c["outreach"]
    cutoff = dt.datetime.now(TZ) - dt.timedelta(days=o["followup_after_days"])
    n = 0
    for lead in leads:
        if lead["status"] != "contacted":
            continue
        emails = lead.get("emails", [])
        if sum(e["type"] == "followup" for e in emails) >= o["max_followups"]:
            continue
        if (OUTBOX / f"{lead['id']}-followup.json").exists():
            continue
        if dt.datetime.fromisoformat(emails[-1]["at"]) > cutoff:
            continue
        subject, body = render_email(c, lead, "followup")
        write_outbox(lead, "followup", subject, body)
        log(lead, "follow-up queued")
        n += 1
    save(leads)
    print(f"Queued {n} follow-ups.")


# ---------- payments (Stripe) ----------
def cmd_payments() -> None:
    c, leads = cfg(), load()
    by_id = {l["id"]: l for l in leads}
    r = requests.get("https://api.stripe.com/v1/checkout/sessions", headers=PLACEHOLDER_AUTH,
                     params={"status": "complete", "limit": 100}, timeout=60)
    if r.status_code in (401, 403):
        sys.exit("Stripe rejected the request: add a restricted Stripe key for api.stripe.com in the environment.")
    r.raise_for_status()
    newly = []
    for s in r.json().get("data", []):
        ref = s.get("client_reference_id")
        lead = by_id.get(ref or "")
        if not lead or lead.get("paid_at") or s.get("payment_status") != "paid":
            continue
        lead["paid_at"] = now()
        lead["stripe_session"] = s["id"]
        lead["amount_paid"] = (s.get("amount_total") or 0) / 100
        lead["status"] = "paid"
        log(lead, f"paid ${lead['amount_paid']:.2f}")
        newly.append(lead)
    save(leads)
    for l in newly:
        print(f"PAID: {l['id']} {l['name']} ${l['amount_paid']:.2f}")
    if newly and not c["business"]["owner_digest_email"].startswith("TODO"):
        send_email(c, c["business"]["owner_digest_email"], f"[SiteHustle] You got paid: {len(newly)} new sale(s)",
                   "\n".join(f"{l['name']}: ${l['amount_paid']:.2f}" for l in newly) +
                   "\n\nClaude is launching their sites now. Nothing for you to do.")
    if not newly:
        print("No new payments.")


def cmd_launch(lead_id: str) -> None:
    c = cfg()
    lead = find(load(), lead_id)
    if lead["status"] != "paid" and "--force" not in sys.argv:
        sys.exit(f"{lead['name']} hasn't paid (status {lead['status']}). Add --force to launch anyway.")
    cmd_build(lead_id, final=True)
    cmd_deploy(lead_id)
    leads = load()
    lead = find(leads, lead_id)
    if lead.get("domain"):
        try:
            netlify("PATCH", f"/sites/{lead['netlify_site_id']}", json={"custom_domain": lead["domain"]})
        except requests.HTTPError as e:
            print(f"Could not attach custom domain yet: {e}")
    lead["live_url"] = f"https://{lead['netlify_subdomain']}.netlify.app"
    lead["status"] = "launched"
    subject, body = render_email(c, lead, "launched")
    if lead.get("email"):
        mid = send_email(c, lead["email"], subject, body)
        lead.setdefault("emails", []).append({"at": now(), "type": "launched", "message_id": mid, "subject": subject})
    log(lead, "launched")
    save(leads)
    print(f"Launched {lead['name']} at {lead['live_url']}")


# ---------- misc ----------
def cmd_status() -> None:
    c, leads = cfg(), load()
    counts = {s: 0 for s in STATUSES}
    for l in leads:
        counts[l["status"]] = counts.get(l["status"], 0) + 1
    revenue = sum(l.get("amount_paid", 0) for l in leads)
    print(f"Mode: {c['outreach']['mode']} (trial ends {c['outreach']['trial_ends']})  "
          f"Sent today: {sent_today(leads)}/{c['outreach']['daily_send_limit']}  Revenue: ${revenue:,.0f}")
    print("  ".join(f"{k}:{v}" for k, v in counts.items() if v))
    pending = len(outbox_items())
    if pending:
        print(f"Outbox: {pending} emails waiting")


def cmd_mark(lead_id: str, status: str, note: str = "") -> None:
    if status not in STATUSES:
        sys.exit(f"Unknown status. Use one of: {', '.join(STATUSES)}")
    leads = load()
    lead = find(leads, lead_id)
    lead["status"] = status
    log(lead, f"marked {status}" + (f": {note}" if note else ""))
    if status == "unsubscribed" and lead.get("email"):
        cmd_suppress(lead["email"])
    for p in OUTBOX.glob(f"{lead['id']}-*.json"):
        if status in ("unsubscribed", "lost", "replied", "paid"):
            p.unlink()
    save(leads)
    print(f"{lead['name']} -> {status}")


def cmd_suppress(value: str) -> None:
    if not suppressed(value):
        with SUPPRESS.open("a") as f:
            f.write(value.strip().lower() + "\n")
    print(f"Suppressed {value}")


def main() -> None:
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help", "help"):
        print(__doc__)
        return
    cmd, rest = a[0], [x for x in a[1:] if not x.startswith("--")]
    flags = {x for x in a[1:] if x.startswith("--")}
    table = {
        "status": lambda: cmd_status(), "discover": lambda: cmd_discover(),
        "upsert": lambda: cmd_upsert(rest[0]), "build": lambda: cmd_build(rest[0], "--final" in flags),
        "deploy": lambda: cmd_deploy(rest[0]), "queue": lambda: cmd_queue(), "digest": lambda: cmd_digest(),
        "approve": lambda: cmd_approve(rest), "send": lambda: cmd_send("--now" in flags),
        "followups": lambda: cmd_followups(), "payments": lambda: cmd_payments(),
        "launch": lambda: cmd_launch(rest[0]), "mark": lambda: cmd_mark(rest[0], rest[1], " ".join(rest[2:])),
        "suppress": lambda: cmd_suppress(rest[0]),
    }
    if cmd not in table:
        sys.exit(f"Unknown command {cmd!r}. Run with --help.")
    table[cmd]()


if __name__ == "__main__":
    main()
