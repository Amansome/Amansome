# SiteHustle

An automated side hustle: find local restaurants with weak websites, build each one a better site
for free, email the owner the link, and charge **$500** to make it theirs.

Your only job is getting paid (plus about 2 minutes a day approving emails for the first week).

```
 Discover ─► Score site ─► Build preview ─► Deploy (Netlify) ─► Email owner ─► Follow up once
 (OSM + web)   (1-10)     (template + their    (preview-x.        (Resend, from     │
                           real menu/hours)     netlify.app)       your domain)      ▼
                                                        Stripe payment ◄── owner clicks "make it yours"
                                                               │
                                              Launch final site + DNS instructions + 2 edit rounds
```

| Piece | What does it |
|---|---|
| `scripts/hustle.py` | Engine: stores leads, builds/deploys sites, sends email, follows up, matches payments |
| `RUNBOOK.md` | What the daily scheduled Claude run does (research, scoring, replies, judgment calls) |
| `templates/site/` | The restaurant website template (10 themes picked from the cuisine) |
| `templates/email/` | Outreach, follow-up and "you're live" emails, with the CAN-SPAM footer |
| `config.yaml` | Your business details, price, area, send limits, trial/auto mode |
| `data/leads.json` | The CRM: every restaurant and where it is in the pipeline |
| `data/suppression.txt` | Do-not-contact list |

## One-time setup (about 45 minutes, about $20)

1. **Domain + inbox.** Buy a short domain for your studio (e.g. Namecheap/Cloudflare, about $12/yr). Create an inbox
   on it, like `hello@yourdomain.com` (Google Workspace about $7/mo, or free forwarding from Cloudflare/ImprovMX).
   **Forward that inbox to your Gmail** and add a Gmail filter that labels it `sitehustle`, so the daily run can
   read replies.
2. **Resend** (sends the email; free for 3,000/mo): sign up at resend.com, add and verify your domain (it gives you
   DNS records to paste in), then create an API key.
3. **Netlify** (hosts the sites; free): sign up, then User settings → Applications → *New access token*.
4. **Stripe** (gets you paid): create an account and connect your bank. Make a **Payment Link** for $500
   ("Restaurant website: build + launch"). Then create a **restricted key** with *Checkout Sessions: Read* only.
5. **Fill in `config.yaml`**: studio name, your first name, sender and reply-to address, your personal email for
   digests, a mailing address (a PO box is fine, and the law requires one), and the Stripe link.
6. **Tell Claude you're done.** Claude will ask for the three keys through a secure form. They're stored in the
   cloud environment and never in this repo. Claude then runs a test, and creates the weekday scheduled task.

## Day to day
- **Week 1 (trial):** each weekday you get a digest email with every pitch and its preview link. Reply `APPROVE`
  (or `SKIP L0004` to hold one back). That's it.
- **After `trial_ends`:** emails send automatically. You get an email only when someone pays, or if something needs a human.
- **Money:** Stripe pays out to your bank automatically.

## Commands
```
python3 scripts/hustle.py status | discover | upsert <file> | build <id> [--final] | deploy <id>
                          queue | digest | approve [SKIP_IDS] | send | followups | payments
                          launch <id> | mark <id> <status> [note] | suppress <email|domain>
```

## Ground rules (built in)
- Only contacts businesses at emails they publish; one email plus one follow-up, max; honors unsubscribes forever.
- Every email has your real name, business, postal address, and an unsubscribe line (CAN-SPAM).
- Starts at 15 emails per weekday so the new domain builds a good sending reputation.
- Previews say "concept preview" and are hidden from Google until the restaurant pays.
- Never makes up menu items, prices, or reviews.
- Pay tax on the income: it's self-employment income, so set aside about 25-30%.
