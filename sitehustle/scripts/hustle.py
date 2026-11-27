#!/usr/bin/env python3
"""SiteHustle: find independent restaurants with weak or missing websites, build a
concept preview, and pitch it, with a person approving every outgoing email.

Claude does the judgment work (research, scoring, writing content and drafts; see
RUNBOOK.md). This script does the mechanical work, and it fails closed:
  * nothing is sent unless outreach.mode is exactly "manual" (default "paused");
  * an email goes out only after the owner approves the specific digest that showed it;
  * a restaurant can never get a second first-touch email;
  * a site launches only after a matching payment AND written confirmation from the restaurant.

Keys come from a local .env file or environment variables (RESEND_API_KEY,
NETLIFY_TOKEN, STRIPE_SECRET_KEY). In a cloud session with no key set, a placeholder
header is sent and the session's network proxy adds the real key.

Usage: python3 scripts/hustle.py <command> [args]   (run from sitehustle/)
  status                         Pipeline summary
  count                          Supply count: leads grouped by site type and email
  discover                       Pull restaurant candidates from OpenStreetMap
  upsert <lead.json>             Add or update researched leads (never moves a status backwards)
  build <id> [--final]           Render a site to sites/<slug>/
  publish-previews               Deploy every current preview to the one shared preview site
  cleanup                        Remove previews for lost/unsubscribed/stale leads, then republish
  queue                          Write first-touch emails for published previews (needs approval)
  reply <id> <draft.txt>         Queue a drafted reply (first line "Subject: ...") for approval
  offer <id>                     Queue the details + payment email for a lead that replied
  digest [--print]               Email the owner every unapproved item plus a status line
  approve <digest-id> [SKIP ...] Approve only the items in that digest (each digest once)
  send                           Send approved items, within the daily limit and send window
  followups                      Queue at most one follow-up for leads that went quiet
  payments                       Match Stripe payments (amount must equal the price)
  confirm <id> <note>            Record the restaurant's written go-ahead
  launch <id>                    Final build on its own site; queues the "you're live" email
  mark <id> <status> [note]      Set a status by hand (replied, hold, lost, unsubscribed, bounced...)
  suppress <email|domain>        Never contact this address or domain again
  failures                       List emails that failed to send
"""
from __future__ import annotations

import datetime as dt
import hashlib
import io
import json
import os
import re
import secrets
import shutil
import sys
import time
import urllib.parse
import zipfile
from pathlib import Path
from zoneinfo import ZoneInfo

import requests
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
LEADS = DATA / "leads.json"
SUPPRESS = DATA / "suppression.txt"
DIGESTS = DATA / "digests.json"
SITES = ROOT / "sites"
BUNDLE = SITES / "_preview_bundle"
OUTBOX = ROOT / "outbox"
FAILED = OUTBOX / "failed"
TZ = ZoneInfo("America/New_York")

# Order matters: upsert never moves a lead to an earlier status.
FLOW = ["new", "researched", "built", "previewed", "queued", "contacted", "followed_up",
        "replied", "offered", "confirmed", "paid", "launched"]
# Statuses that stop all outreach. upsert never overwrites them.
STOPPED = ["skipped", "hold", "lost", "unsubscribed", "bounced"]
STATUSES = FLOW + STOPPED
SUPPRESS_ON = {"lost", "unsubscribed", "bounced"}
NO_CONTACT = set(STOPPED) | {"replied", "offered", "confirmed", "paid", "launched"}  # no cold emails
MODES = {"paused", "manual"}

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


class SendError(Exception):
    """A send that failed for this item only (bad address, rejected message)."""


# ---------- config, secrets, storage ----------
def _merge(a: dict, b: dict) -> dict:
    out = dict(a)
    for k, v in (b or {}).items():
        out[k] = _merge(out[k], v) if isinstance(v, dict) and isinstance(out.get(k), dict) else v
    return out


def cfg() -> dict:
    """config.yaml (shareable defaults) overlaid with config.local.yaml (your details; git-ignored)."""
    c = yaml.safe_load((ROOT / "config.yaml").read_text())
    local = ROOT / "config.local.yaml"
    if local.exists():
        c = _merge(c, yaml.safe_load(local.read_text()) or {})
    return c


def load_env() -> None:
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def auth(var: str) -> dict:
    key = os.environ.get(var)
    return {"Authorization": f"Bearer {key}" if key else "Bearer injected-by-proxy"}


def ensure_dirs() -> None:
    for d in (DATA, SITES, OUTBOX, FAILED):
        d.mkdir(parents=True, exist_ok=True)
    if not LEADS.exists():
        LEADS.write_text("[]\n")
    if not SUPPRESS.exists():
        SUPPRESS.write_text("# One email address or domain per line. Never contacted again.\n")
    if not DIGESTS.exists():
        DIGESTS.write_text("{}\n")


def load() -> list[dict]:
    return json.loads(LEADS.read_text())


def save(leads: list[dict]) -> None:
    tmp = LEADS.with_suffix(".tmp")
    tmp.write_text(json.dumps(leads, indent=2, ensure_ascii=False) + "\n")
    tmp.replace(LEADS)  # atomic: a crash never leaves a half-written file


def now() -> str:
    return dt.datetime.now(TZ).isoformat(timespec="seconds")


def log(lead: dict, event: str) -> None:
    lead.setdefault("history", []).append({"at": now(), "event": event})


def find(leads: list[dict], lead_id: str) -> dict:
    for l in leads:
        if l["id"].lower() == lead_id.lower() or l.get("slug") == lead_id:
            return l
    sys.exit(f"No lead {lead_id!r}")


def slugify(s: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")[:40] or "lead"


def unique_slug(leads: list[dict], name: str, own_id: str | None = None) -> str:
    base, n = slugify(name), 1
    taken = {l.get("slug") for l in leads if l["id"] != own_id}
    slug = base
    while slug in taken:
        n += 1
        slug = f"{base}-{n}"
    return slug


def next_id(leads: list[dict]) -> str:
    nums = [int(l["id"][1:]) for l in leads if re.fullmatch(r"L\d+", l["id"])]
    return f"L{(max(nums) + 1) if nums else 1:04d}"


def suppressed(email: str | None) -> bool:
    if not email:
        return False
    email = email.lower().strip()
    lines = {x.strip().lower() for x in SUPPRESS.read_text().splitlines() if x.strip() and not x.startswith("#")}
    return email in lines or email.split("@")[-1] in lines


def add_suppression(value: str) -> None:
    if value and not suppressed(value):
        with SUPPRESS.open("a") as f:
            f.write(value.strip().lower() + "\n")


def todo_fields(c: dict) -> list[str]:
    fields = {**c["business"], "stripe_payment_link": c["offer"]["stripe_payment_link"],
              "terms_url": c["offer"]["terms_url"]}
    return [k for k, v in fields.items() if isinstance(v, str) and (v.startswith("TODO") or not v.strip())
            and k not in ("website", "based_in")]


def require_live_config(c: dict, for_offer: bool = False) -> None:
    missing = [m for m in todo_fields(c) if for_offer or m not in ("stripe_payment_link", "terms_url")]
    if missing:
        sys.exit("Fill these in config.local.yaml first: " + ", ".join(missing))


def env(strict: bool = True) -> Environment:
    """Emails render strictly (a missing field is an error, never a blank); site pages tolerate optional fields."""
    kw = {"undefined": StrictUndefined} if strict else {}
    return Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html"]),
                       keep_trailing_newline=True, **kw)


# ---------- discovery and supply ----------
def cmd_discover() -> None:
    c, leads = cfg(), load()
    known_osm = {l.get("osm_id") for l in leads}
    known = {(l["name"].lower(), (l.get("address") or "")[:12].lower()) for l in leads}
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
                r = None
                time.sleep(5 * (attempt + 1))
        if r is None:
            print(f"Could not reach OpenStreetMap for {area['name']}. Use web search instead (RUNBOOK step 3).")
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
            lid = next_id(leads)
            leads.append({
                "id": lid, "slug": unique_slug(leads, name), "name": name, "status": "new",
                "osm_id": osm_id, "area": area["name"], "city": city, "address": full,
                "phone": t.get("phone") or t.get("contact:phone"),
                "website": t.get("website") or t.get("contact:website"),
                "cuisine": (t.get("cuisine") or t.get("amenity", "")).replace("_", " "),
                "history": [{"at": now(), "event": "discovered via OSM (email not collected; research it)"}],
            })
            added += 1
    save(leads)
    print(f"Added {added} new candidates. Total leads: {len(leads)}")


def cmd_count() -> None:
    """The council's supply gate: how many leads are actually pitchable, and by which channel."""
    leads = [l for l in load() if l["status"] != "new"]
    groups = {"own decent site": 0, "POS / ordering-vendor site": 0,
              "no or broken site + published email": 0, "no or broken site, no email": 0, "not classified": 0}
    for l in leads:
        t = l.get("site_type")
        if t == "own_decent":
            groups["own decent site"] += 1
        elif t == "vendor":
            groups["POS / ordering-vendor site"] += 1
        elif t in ("none", "broken", "weak"):
            groups["no or broken site + published email" if l.get("email") else "no or broken site, no email"] += 1
        else:
            groups["not classified"] += 1
    print(f"Researched leads: {len(leads)}")
    for k, v in groups.items():
        print(f"  {k:<40} {v}")
    target = groups["no or broken site + published email"]
    if len(leads) >= 30:
        share = target / len(leads)
        verdict = ("stop (council: 2 or fewer of 30 -> do nothing, or in person only)" if share <= 2 / 30 else
                   "small: in-person test, or email only with a written provider OK" if share < 10 / 30 else
                   "enough for a hand-approved test")
        print(f"Email-reachable target share: {share:.0%} -> {verdict}")
    else:
        print("Research at least 30 places before reading this against the council's thresholds.")


def cmd_upsert(path: str) -> None:
    data = json.loads(Path(path).read_text())
    items = data if isinstance(data, list) else [data]
    leads = load()
    for d in items:
        d = dict(d)
        d.pop("history", None)
        existing = None
        if d.get("id"):
            existing = next((l for l in leads if l["id"] == d["id"]), None)
            if existing is None:
                print(f"Rejected {d['id']} ({d.get('name')}): ids are assigned by the script. Remove 'id' to add it as new.")
                continue
        elif d.get("name"):
            existing = next((l for l in leads if l["name"].lower() == d["name"].lower() and
                             (l.get("address") or "")[:12].lower() == (d.get("address") or "")[:12].lower()), None)
        if existing:
            new_status = d.pop("status", None)
            for protected in ("slug", "emails", "preview_token", "netlify_site_id", "paid_at", "amount_paid",
                              "confirmed_at", "stripe_session", "live_url", "preview_url"):
                d.pop(protected, None)
            existing.update(d)
            cur = existing["status"]
            if new_status and new_status != cur:
                if cur in STOPPED or cur not in FLOW or new_status not in STATUSES:
                    print(f"  kept {existing['id']} at '{cur}' (won't change it to '{new_status}' via upsert; use mark)")
                elif new_status in FLOW and FLOW.index(new_status) < FLOW.index(cur):
                    print(f"  kept {existing['id']} at '{cur}' (won't move back to '{new_status}')")
                else:
                    existing["status"] = new_status
            log(existing, f"updated (status {existing['status']})")
            print(f"Updated {existing['id']} {existing['name']} ({existing['status']})")
        else:
            d["id"] = next_id(leads)
            d["slug"] = unique_slug(leads, d["name"])
            if d.get("status") not in ("new", "researched", "skipped"):
                d["status"] = "researched"
            d["history"] = [{"at": now(), "event": f"added ({d['status']})"}]
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


def parse_dow(days: str) -> str:
    """'Mon-Thu' -> '1,2,3,4'; 'Fri & Sat' -> '5,6'; 'Daily' -> all."""
    s = days.lower()
    if "daily" in s or "every day" in s or "7 days" in s:
        return "0,1,2,3,4,5,6"
    found = set()
    for a, b in re.findall(r"(sun|mon|tue|wed|thu|fri|sat)\w*\s*(?:-|–|to)\s*(sun|mon|tue|wed|thu|fri|sat)", s):
        i, j = DOW[a], DOW[b]
        found.update(range(i, j + 1) if i <= j else list(range(i, 7)) + list(range(0, j + 1)))
    found.update(DOW[d] for d in re.findall(r"(sun|mon|tue|wed|thu|fri|sat)", s))
    return ",".join(str(x) for x in sorted(found))


def cmd_build(lead_id: str, final: bool = False) -> None:
    c, leads = cfg(), load()
    lead = find(leads, lead_id)
    if lead["status"] in STOPPED:
        sys.exit(f"{lead['name']} is '{lead['status']}'. Not building.")
    if not lead.get("menu") and not lead.get("hours"):
        sys.exit("No menu or hours on this lead. Research them first (never invent them).")
    r = dict(lead)
    r["phone_tel"] = re.sub(r"[^\d+]", "", r.get("phone") or "")
    r.setdefault("tagline", None)
    r.setdefault("headline", None)
    r.setdefault("menu_intro", None)
    r["meta_description"] = r.get("meta_description") or (
        f"{r['name']}: menu, hours and location." + (" Order online." if r.get("order_url") else ""))
    if isinstance(r.get("about"), str):
        r["about"] = [p.strip() for p in r["about"].split("\n\n") if p.strip()]
    # Third-party material only with the restaurant's permission (or on its own paid site).
    perms = r.get("permissions", {})
    if not (final or perms.get("photos")):
        r["hero_image"] = r["about_image"] = None
    if not (final and perms.get("reviews")):
        r["reviews"] = None
    for h in r.get("hours") or []:
        h.setdefault("dow", parse_dow(h.get("days", "")))
    r["address_short"] = (r.get("address") or "").split(",")[0]
    r["jsonld"] = json.dumps({
        "@context": "https://schema.org", "@type": "Restaurant", "name": r["name"],
        "address": r.get("address"), "telephone": r.get("phone"), "servesCuisine": r.get("cuisine"),
        "url": r.get("live_url"),
    }).replace("</", "<\\/")
    for k in ("cuisine_label", "city", "about", "about_title", "menu", "order_url", "reservation_url",
              "phone", "email", "address", "social", "hero_image", "about_image", "reviews", "hours"):
        r.setdefault(k, None)
    html = env(strict=False).get_template("site/index.html.j2").render(
        r=r, theme=pick_theme(lead), biz=c["business"], preview=not final, year=dt.date.today().year)
    out = SITES / lead["slug"] / ("final" if final else "preview")
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(html)
    if final:
        (out / "robots.txt").write_text("User-agent: *\nAllow: /\n")
    if lead["status"] in ("new", "researched"):
        lead["status"] = "built"
    log(lead, "built final site" if final else "built preview")
    save(leads)
    print(f"Built {out / 'index.html'}")


# ---------- hosting (Netlify) ----------
def netlify(method: str, path: str, **kw) -> requests.Response:
    r = requests.request(method, f"https://api.netlify.com/api/v1{path}",
                         headers={**auth("NETLIFY_TOKEN"), **kw.pop("headers", {})}, timeout=120, **kw)
    if r.status_code == 401:
        sys.exit("Netlify rejected the request: set NETLIFY_TOKEN in .env.")
    r.raise_for_status()
    return r


def netlify_site(name: str, existing_id: str | None = None) -> dict:
    if existing_id:
        return netlify("GET", f"/sites/{existing_id}").json()
    for suffix in ["", "-" + secrets.token_hex(2), "-" + secrets.token_hex(3)]:
        r = requests.post("https://api.netlify.com/api/v1/sites", headers=auth("NETLIFY_TOKEN"),
                          json={"name": (name + suffix)[:63]}, timeout=60)
        if r.status_code == 422:
            continue
        if r.status_code == 401:
            sys.exit("Netlify rejected the request: set NETLIFY_TOKEN in .env.")
        r.raise_for_status()
        return r.json()
    sys.exit(f"Could not get a free Netlify site name near {name!r}.")


def netlify_deploy(site_id: str, folder: Path) -> dict:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for f in folder.rglob("*"):
            if f.is_file():
                z.write(f, f.relative_to(folder))
    return netlify("POST", f"/sites/{site_id}/deploys", data=buf.getvalue(),
                   headers={"Content-Type": "application/zip"}).json()


def preview_base(c: dict) -> str:
    if c["hosting"].get("preview_base_url"):
        return c["hosting"]["preview_base_url"].rstrip("/")
    state_file = DATA / "hosting.json"
    state = json.loads(state_file.read_text()) if state_file.exists() else {}
    if not state.get("preview_site_name"):
        sys.exit("No shared preview site yet. Run publish-previews.")
    return f"https://{state['preview_site_name']}.netlify.app"


def cmd_publish_previews() -> None:
    """One shared preview site, unguessable paths, no payment links: one deploy per batch, not per lead."""
    c, leads = cfg(), load()
    state_file = DATA / "hosting.json"
    state = json.loads(state_file.read_text()) if state_file.exists() else {}
    live = [l for l in leads if l["status"] in FLOW[2:-1] and not l.get("preview_removed")
            and (SITES / l["slug"] / "preview" / "index.html").exists()]
    if BUNDLE.exists():
        shutil.rmtree(BUNDLE)
    BUNDLE.mkdir(parents=True)
    (BUNDLE / "index.html").write_text("<!doctype html><meta name=robots content=noindex><title>Previews</title>")
    (BUNDLE / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
    (BUNDLE / "_headers").write_text("/*\n  X-Robots-Tag: noindex, nofollow, noarchive\n")
    for l in live:
        l.setdefault("preview_token", secrets.token_urlsafe(9).replace("_", "").replace("-", "")[:12])
        dest = BUNDLE / l["preview_token"]
        dest.mkdir()
        shutil.copy(SITES / l["slug"] / "preview" / "index.html", dest / "index.html")
    if not state.get("preview_site_id"):
        site = netlify_site(c["hosting"].get("preview_site_prefix", "previews-") + secrets.token_hex(3))
        state["preview_site_id"], state["preview_site_name"] = site["id"], site["name"]
        state_file.write_text(json.dumps(state, indent=2))
        print(f"Created the shared preview site {site['name']}.")
    netlify_deploy(state["preview_site_id"], BUNDLE)
    base = preview_base(c)
    for l in live:
        l["preview_url"] = f"{base}/{l['preview_token']}/"
        if l["status"] == "built":
            l["status"] = "previewed"
            log(l, f"preview published {l['preview_url']}")
    save(leads)
    print(f"Published {len(live)} previews to one site ({base}).")


def cmd_cleanup() -> None:
    c, leads = cfg(), load()
    ttl = dt.timedelta(days=c["hosting"].get("preview_ttl_days", 30))
    removed = 0
    for l in leads:
        if l.get("preview_removed"):
            continue
        last = max((e["at"] for e in l.get("emails", [])), default=None)
        stale = l["status"] in ("contacted", "followed_up") and last and dt.datetime.now(TZ) - dt.datetime.fromisoformat(last) > ttl
        if l["status"] in ("lost", "unsubscribed", "bounced", "skipped", "launched") or stale:
            l["preview_removed"] = True
            shutil.rmtree(SITES / l["slug"] / "preview", ignore_errors=True)
            log(l, "preview removed")
            removed += 1
    save(leads)
    print(f"Removed {removed} previews.")
    if removed:
        cmd_publish_previews()


# ---------- outbox and email ----------
def outbox_items() -> list[tuple[Path, dict]]:
    return [(p, json.loads(p.read_text())) for p in sorted(OUTBOX.glob("*.json"))]


def write_outbox(lead: dict, kind: str, subject: str, body: str) -> Path:
    path = OUTBOX / f"{lead['id']}-{kind}.json"
    if path.exists():
        sys.exit(f"{path.name} is already waiting. Approve, send or delete it first.")
    path.write_text(json.dumps({"lead": lead["id"], "kind": kind, "to": lead["email"], "subject": subject,
                                "body": body, "digest": None, "approved": False, "created": now()}, indent=2))
    return path


def join_list(items: list[str]) -> str:
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " and " + items[-1]


def render_email(c: dict, lead: dict, kind: str, extra: dict | None = None) -> tuple[str, str]:
    p = lead.get("pitch", {})
    has_site = lead.get("site_type") not in ("none", None) and bool(lead.get("website"))
    observation = p.get("observation") if p.get("observation_source") else None  # facts only, with a source
    ctx = dict(
        r=lead, biz=c["business"], offer=c["offer"], has_site=has_site,
        greeting=p.get("greeting") or f"{lead['name']} team",
        observation=observation,
        problems=join_list(p.get("problems") or ["it's hard to read on a phone"]),
        presence=p.get("presence") or "listings on other sites",
        highlights=join_list(p.get("highlights") or ["your menu", "hours", "a map", "one-tap calling on phones"]),
        subject=p.get("subject") or f"A website idea for {lead['name']}",
        **(extra or {}),
    )
    text = env().get_template(f"email/{kind}.txt.j2").render(**ctx)
    subject, _, body = text.partition("\n")
    return subject.removeprefix("Subject: ").strip(), body.lstrip("\n")


def cmd_queue() -> None:
    c, leads = cfg(), load()
    require_live_config(c)
    emailed = {e["to"].lower() for l in leads for e in l.get("emails", []) if e.get("to")}
    n = 0
    for lead in leads:
        if lead["status"] != "previewed":
            continue
        email = (lead.get("email") or "").lower()
        if not email:
            lead["status"] = "skipped"
            log(lead, "skipped for email: no published business email (in-person list)")
            continue
        if not lead.get("email_source"):
            print(f"  {lead['id']}: record email_source (where the address is published) before queueing")
            continue
        if suppressed(email) or email in emailed or any(e["type"] == "outreach" for e in lead.get("emails", [])):
            lead["status"] = "skipped"
            log(lead, "skipped: address suppressed or already contacted")
            continue
        subject, body = render_email(c, lead, "outreach")
        write_outbox(lead, "outreach", subject, body)
        lead["status"] = "queued"
        log(lead, "outreach queued for approval")
        n += 1
    save(leads)
    print(f"Queued {n} first-touch emails for approval.")


def cmd_reply(lead_id: str, draft: str) -> None:
    leads = load()
    lead = find(leads, lead_id)
    text = Path(draft).read_text()
    subject, _, body = text.partition("\n")
    if not subject.startswith("Subject:"):
        sys.exit("The draft's first line must be 'Subject: ...'.")
    write_outbox(lead, "reply", subject.removeprefix("Subject:").strip(), body.lstrip("\n"))
    log(lead, "reply drafted for approval")
    save(leads)
    print(f"Queued reply to {lead['name']} for approval.")


def claim_url(c: dict, lead: dict) -> str:
    link = c["offer"]["stripe_payment_link"]
    sep = "&" if "?" in link else "?"
    return link + sep + urllib.parse.urlencode({"client_reference_id": lead["id"]})


def cmd_offer(lead_id: str) -> None:
    c, leads = cfg(), load()
    require_live_config(c, for_offer=True)
    lead = find(leads, lead_id)
    if lead["status"] != "replied":
        sys.exit(f"Send details only after the restaurant replies (status is {lead['status']}).")
    subject, body = render_email(c, lead, "offer", {"claim_url": claim_url(c, lead)})
    write_outbox(lead, "offer", subject, body)
    lead["status"] = "offered"
    log(lead, "offer queued for approval")
    save(leads)
    print(f"Queued details + payment email to {lead['name']} for approval.")


def send_email(c: dict, to: str, subject: str, body: str, headers: dict | None = None,
               idempotency_key: str | None = None) -> str:
    biz = c["business"]
    payload = {
        "from": f"{biz['sender_name']} <{biz['sender_email']}>", "to": [to], "subject": subject,
        "text": body, "reply_to": biz["reply_to"],
        "headers": {"List-Unsubscribe": f"<mailto:{biz['reply_to']}?subject=unsubscribe>", **(headers or {})},
    }
    h = dict(auth("RESEND_API_KEY"))
    if idempotency_key:
        h["Idempotency-Key"] = idempotency_key
    r = requests.post("https://api.resend.com/emails", headers=h, json=payload, timeout=60)
    if r.status_code == 401:
        sys.exit("The email API rejected the key: set RESEND_API_KEY in .env.")
    if r.status_code == 403:
        sys.exit("The email API refused the account (403). Stop and check the account's status before sending anything.")
    if 400 <= r.status_code < 500:
        raise SendError(f"{r.status_code}: {r.text[:300]}")
    r.raise_for_status()
    return r.json().get("id", "")


def status_line(c: dict, leads: list[dict]) -> str:
    counts: dict[str, int] = {}
    for l in leads:
        counts[l["status"]] = counts.get(l["status"], 0) + 1
    revenue = sum(l.get("amount_paid", 0) for l in leads)
    stuck = [l["id"] for l in leads if l["status"] == "paid"]
    held = [l["id"] for l in leads if l["status"] == "hold"]
    failed = len(list(FAILED.glob("*.json")))
    parts = [f"mode {c['outreach']['mode']}", f"sent today {sent_today(leads)}/{c['outreach']['daily_send_limit']}",
             f"revenue ${revenue:,.0f}", " ".join(f"{k}:{v}" for k, v in counts.items())]
    if stuck:
        parts.append(f"PAID BUT NOT LAUNCHED: {', '.join(stuck)}")
    if held:
        parts.append(f"ON HOLD (needs you): {', '.join(held)}")
    if failed:
        parts.append(f"FAILED SENDS: {failed} (run `failures`)")
    return " | ".join(parts)


def cmd_digest(print_only: bool = False) -> None:
    """Daily email to the owner: the items to approve plus a status line. A missing digest is the alarm."""
    c, leads = cfg(), load()
    items = [(p, i) for p, i in outbox_items() if not i["approved"]]
    by_id = {l["id"]: l for l in leads}
    digests = json.loads(DIGESTS.read_text())
    lines = [f"Status: {status_line(c, leads)}", ""]
    did = None
    if items:
        did = dt.datetime.now(TZ).strftime("%m%d") + "-" + hashlib.sha1(
            "".join(p.name for p, _ in items).encode() + now().encode()).hexdigest()[:5]
        lines.append(f"{len(items)} emails are waiting. To send ALL of them, reply:  APPROVE {did}")
        lines.append(f"To hold some back:  APPROVE {did} SKIP L0003 L0007")
        lines.append("Nothing else will send. Check each preview against the restaurant's real menu first.\n")
        for p, i in items:
            l = by_id[i["lead"]]
            i["digest"] = did
            p.write_text(json.dumps(i, indent=2))
            lines.append(f"\n==== {l['id']} | {i['kind']} | {l['name']}\n"
                         f"Their site: {l.get('website') or 'none'}  (score {l.get('audit', {}).get('score', '?')}/10)\n"
                         f"Preview: {l.get('preview_url') or '-'}\n"
                         f"Menu/hours source: {l.get('content_source') or 'NOT RECORDED: do not approve'}\n"
                         f"Email found at: {l.get('email_source') or '-'}\n"
                         f"To: {i['to']}\nSubject: {i['subject']}\n\n{i['body']}")
        digests[did] = {"created": now(), "items": [p.name for p, _ in items], "processed": False}
        DIGESTS.write_text(json.dumps(digests, indent=2))
    else:
        lines.append("Nothing waiting for approval today.")
    body = "\n".join(lines)
    subject = f"[SiteHustle] {len(items)} to approve" + (f" (digest {did})" if did else "") + f", {dt.date.today():%b %d}"
    if print_only or todo_fields(c) and set(todo_fields(c)) & {"owner_digest_email", "sender_email"}:
        print(subject + "\n\n" + body)
        return
    send_email(c, c["business"]["owner_digest_email"], subject, body)
    print(f"Digest sent{f' ({did})' if did else ''}.")


def cmd_approve(digest_id: str, skip: list[str]) -> None:
    digests = json.loads(DIGESTS.read_text())
    d = digests.get(digest_id)
    if not d:
        sys.exit(f"No digest {digest_id!r}. Approvals must name the digest id from the email.")
    if d["processed"]:
        sys.exit(f"Digest {digest_id} was already processed on {d['processed']}. Each approval is used once.")
    skip = {s.upper() for s in skip if s.upper() != "SKIP"}
    approved = 0
    for name in d["items"]:
        p = OUTBOX / name
        if not p.exists():
            continue
        i = json.loads(p.read_text())
        if i.get("digest") != digest_id:
            continue
        if i["lead"].upper() in skip:
            p.unlink()
            continue
        i["approved"] = True
        p.write_text(json.dumps(i, indent=2))
        approved += 1
    d["processed"] = now()
    DIGESTS.write_text(json.dumps(digests, indent=2))
    print(f"Approved {approved} items from digest {digest_id}." + (f" Removed: {', '.join(sorted(skip))}" if skip else ""))


def sent_today(leads: list[dict]) -> int:
    today = dt.datetime.now(TZ).date().isoformat()
    return sum(1 for l in leads for e in l.get("emails", []) if e["at"].startswith(today) and e["type"] in ("outreach", "followup"))


def cmd_send() -> None:
    c, leads = cfg(), load()
    o = c["outreach"]
    if o.get("mode") not in MODES:
        sys.exit(f"Unknown outreach.mode {o.get('mode')!r}. Nothing sent. Use 'paused' or 'manual'.")
    if o["mode"] != "manual":
        print("Outreach is paused. Nothing sent.")
        return
    require_live_config(c)
    t = dt.datetime.now(TZ)
    lo, hi = o["send_window_hours_local"]
    if (t.weekday() >= 5 and not o.get("send_weekends")) or not lo <= t.hour < hi:
        print(f"Outside the send window ({lo}:00-{hi}:00 ET, weekdays). Nothing sent.")
        return
    by_id = {l["id"]: l for l in leads}
    emailed = {e["to"].lower() for l in leads for e in l.get("emails", []) if e.get("to") and e["type"] == "outreach"}
    budget = o["daily_send_limit"] - sent_today(leads)
    sent = failed = 0
    for p, item in outbox_items():
        if not item["approved"]:
            continue
        lead = by_id.get(item["lead"])
        to = item["to"].lower()
        cold = item["kind"] in ("outreach", "followup")
        if lead is None or suppressed(to) or lead["status"] in SUPPRESS_ON | {"hold"}:
            p.unlink()
            continue
        if cold and lead["status"] in NO_CONTACT:
            p.unlink()  # they replied or something changed: no cold email
            continue
        if item["kind"] == "outreach" and (to in emailed or any(e["type"] == "outreach" for e in lead.get("emails", []))):
            p.unlink()
            log(lead, "blocked duplicate first-touch email")
            continue
        if cold and budget <= 0:
            print("Daily send limit reached.")
            break
        prev = next((e for e in lead.get("emails", []) if e["type"] == "outreach"), None)
        headers = {"In-Reply-To": prev["message_id"], "References": prev["message_id"]} \
            if prev and prev.get("message_id") and item["kind"] != "outreach" else None
        try:
            mid = send_email(c, item["to"], item["subject"], item["body"], headers,
                             idempotency_key=f"{lead['id']}-{item['kind']}-{item.get('digest')}")
        except SendError as e:
            item["error"] = str(e)
            item["failed_at"] = now()
            (FAILED / p.name).write_text(json.dumps(item, indent=2))
            p.unlink()
            log(lead, f"send failed ({item['kind']}): {e}")
            save(leads)
            failed += 1
            continue
        lead.setdefault("emails", []).append({"at": now(), "type": item["kind"], "to": to,
                                              "message_id": mid, "subject": item["subject"]})
        if item["kind"] == "outreach":
            lead["status"] = "contacted"
            emailed.add(to)
        elif item["kind"] == "followup":
            lead["status"] = "followed_up"
        log(lead, f"sent {item['kind']}")
        p.unlink()
        save(leads)  # saved after every send
        sent += 1
        if cold:
            budget -= 1
        time.sleep(20)
    print(f"Sent {sent}. Failed {failed}." + (" Run `failures`." if failed else ""))


def cmd_followups() -> None:
    c, leads = cfg(), load()
    o = c["outreach"]
    cutoff = dt.datetime.now(TZ) - dt.timedelta(days=o["followup_after_days"])
    n = 0
    for lead in leads:
        if lead["status"] != "contacted" or suppressed(lead.get("email")):
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
        log(lead, "follow-up queued for approval")
        n += 1
    save(leads)
    print(f"Queued {n} follow-ups for approval.")


def cmd_failures() -> None:
    items = sorted(FAILED.glob("*.json"))
    if not items:
        print("No failed sends.")
    for p in items:
        i = json.loads(p.read_text())
        print(f"{i['lead']} {i['kind']} to {i['to']}: {i.get('error')}  ({p})")


# ---------- payments and launch ----------
def cmd_payments() -> None:
    c, leads = cfg(), load()
    by_id = {l["id"]: l for l in leads}
    price_cents = int(round(c["offer"]["price_usd"] * 100))
    params: dict = {"status": "complete", "limit": 100}
    newly, issues = [], []
    while True:
        r = requests.get("https://api.stripe.com/v1/checkout/sessions", headers=auth("STRIPE_SECRET_KEY"),
                         params=params, timeout=60)
        if r.status_code in (401, 403):
            sys.exit("Stripe rejected the request: set STRIPE_SECRET_KEY (a restricted, read-only key) in .env.")
        r.raise_for_status()
        page = r.json()
        for s in page.get("data", []):
            lead = by_id.get(s.get("client_reference_id") or "")
            if not lead or lead.get("stripe_session") == s["id"] or s.get("payment_status") != "paid":
                continue
            payer = ((s.get("customer_details") or {}).get("email") or "").lower()
            if s.get("amount_total") != price_cents or (s.get("currency") or "usd") != "usd":
                if lead.get("payment_issue") != s["id"]:
                    lead["payment_issue"] = s["id"]
                    lead["status"] = "hold"
                    log(lead, f"payment amount mismatch ({s.get('amount_total')} cents): on hold for the owner")
                    issues.append(lead)
                continue
            lead["paid_at"], lead["stripe_session"] = now(), s["id"]
            lead["amount_paid"], lead["payer_email"] = s["amount_total"] / 100, payer
            if lead["status"] not in STOPPED:
                lead["status"] = "paid"
            log(lead, f"paid ${lead['amount_paid']:.2f} by {payer or 'unknown'}")
            newly.append(lead)
        if not page.get("has_more") or not page.get("data"):
            break
        params["starting_after"] = page["data"][-1]["id"]
    save(leads)
    for l in newly:
        note = "" if l.get("confirmed_at") else "  (needs written confirmation from the restaurant before launch)"
        print(f"PAID: {l['id']} {l['name']} ${l['amount_paid']:.2f}{note}")
    for l in issues:
        print(f"PAYMENT ISSUE: {l['id']} {l['name']}: amount doesn't match the price. Refund or sort it out in Stripe.")
    if not newly and not issues:
        print("No new payments.")


def cmd_confirm(lead_id: str, note: str) -> None:
    leads = load()
    lead = find(leads, lead_id)
    if not note:
        sys.exit("Say what the confirmation was, e.g. 'reply from info@their.com on Dec 3: go ahead'.")
    lead["confirmed_at"], lead["confirmation"] = now(), note
    if lead["status"] in ("replied", "offered"):
        lead["status"] = "confirmed"
    log(lead, f"restaurant confirmed: {note}")
    save(leads)
    print(f"Recorded confirmation for {lead['name']}.")


def cmd_launch(lead_id: str) -> None:
    c = cfg()
    leads = load()
    lead = find(leads, lead_id)
    if lead["status"] != "paid" or not lead.get("stripe_session"):
        sys.exit(f"{lead['name']} has no matched payment (status {lead['status']}).")
    if not lead.get("confirmed_at"):
        sys.exit(f"{lead['name']} paid, but the restaurant hasn't confirmed in writing. Run `confirm` first.")
    cmd_build(lead_id, final=True)
    leads = load()
    lead = find(leads, lead_id)
    site = netlify_site(lead["slug"], lead.get("netlify_site_id"))  # its own site, no "preview" in the name
    lead["netlify_site_id"], lead["netlify_subdomain"] = site["id"], site["name"]
    save(leads)
    netlify_deploy(site["id"], SITES / lead["slug"] / "final")
    if lead.get("domain"):
        try:
            netlify("PATCH", f"/sites/{site['id']}", json={"custom_domain": lead["domain"]})
        except requests.HTTPError as e:
            print(f"Could not attach custom domain yet: {e}")
    lead["live_url"] = f"https://{lead['domain']}" if lead.get("domain") else f"https://{site['name']}.netlify.app"
    lead["launched_at"] = now()
    lead["hosting_until"] = (dt.date.today() + dt.timedelta(days=30 * c["offer"]["hosting_months"])).isoformat()
    lead["status"] = "launched"
    log(lead, f"launched {lead['live_url']}")
    save(leads)
    subject, body = render_email(c, lead, "launched")
    write_outbox(lead, "launched", subject, body)
    print(f"Launched {lead['name']} at {lead['live_url']}. The 'you're live' email is waiting for approval.")
    cmd_cleanup()


# ---------- misc ----------
def cmd_status() -> None:
    print(status_line(cfg(), load()))
    pending = outbox_items()
    if pending:
        print(f"Outbox: {len(pending)} ({sum(i['approved'] for _, i in pending)} approved)")
    missing = todo_fields(cfg())
    if missing:
        print("Not configured yet (config.local.yaml): " + ", ".join(missing))


def cmd_mark(lead_id: str, status: str, note: str = "") -> None:
    if status not in STATUSES:
        sys.exit(f"Unknown status. Use one of: {', '.join(STATUSES)}")
    leads = load()
    lead = find(leads, lead_id)
    lead["status"] = status
    log(lead, f"marked {status}" + (f": {note}" if note else ""))
    if status in SUPPRESS_ON and lead.get("email"):
        add_suppression(lead["email"])
    if status in STOPPED or status == "replied":
        for p in OUTBOX.glob(f"{lead['id']}-*.json"):
            if status != "replied" or json.loads(p.read_text())["kind"] in ("outreach", "followup"):
                p.unlink()
    save(leads)
    print(f"{lead['name']} -> {status}")


def main() -> None:
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help", "help"):
        print(__doc__)
        return
    load_env()
    ensure_dirs()
    cmd, rest = a[0], [x for x in a[1:] if not x.startswith("--")]
    flags = {x for x in a[1:] if x.startswith("--")}

    def need(n: int) -> list[str]:
        if len(rest) < n:
            sys.exit(f"`{cmd}` needs {n} argument(s). Run with --help.")
        return rest

    table = {
        "status": lambda: cmd_status(), "count": lambda: cmd_count(), "discover": lambda: cmd_discover(),
        "upsert": lambda: cmd_upsert(need(1)[0]), "build": lambda: cmd_build(need(1)[0], "--final" in flags),
        "publish-previews": lambda: cmd_publish_previews(), "cleanup": lambda: cmd_cleanup(),
        "queue": lambda: cmd_queue(), "reply": lambda: cmd_reply(*need(2)[:2]), "offer": lambda: cmd_offer(need(1)[0]),
        "digest": lambda: cmd_digest("--print" in flags), "approve": lambda: cmd_approve(need(1)[0], rest[1:]),
        "send": lambda: cmd_send(), "followups": lambda: cmd_followups(), "failures": lambda: cmd_failures(),
        "payments": lambda: cmd_payments(), "confirm": lambda: cmd_confirm(need(1)[0], " ".join(rest[1:])),
        "launch": lambda: cmd_launch(need(1)[0]),
        "mark": lambda: cmd_mark(need(2)[0], rest[1], " ".join(rest[2:])),
        "suppress": lambda: add_suppression(need(1)[0]) or print(f"Suppressed {rest[0]}"),
    }
    if cmd not in table:
        sys.exit(f"Unknown command {cmd!r}. Run with --help.")
    table[cmd]()


if __name__ == "__main__":
    main()
