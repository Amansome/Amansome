# SiteHustle

Finds independent restaurants with weak or missing websites, builds each a free concept preview, and helps you
pitch it for **$500 one time** (12 months of hosting and menu updates included, then renewal or a free handover).

**This is a small part-time business, not passive income.** An advisory council reviewed the first version
(`council/RECOMMENDATION.md`) and every seat rejected running it unattended. This version is rebuilt around their
findings. Claude does the research, building and drafting, and **you approve every email before it goes out.**
Expect about 3 to 8 hours over the first 3 months, plus 1 to 2 hours per sale.

## Safety built in (each has a regression test in `tests/`)

- **Nothing sends by default.** `outreach.mode` is `paused`; the only sending mode is `manual`, and any other value
  sends nothing. There is no automatic mode or date switch.
- **Approval covers only what you saw.** An approval names a digest id and is used once.
- **No double emails.** A restaurant can never get a second first-touch email. Re-importing a lead never moves it
  backwards, and lead ids and site names can't collide.
- **Stopping is easy.** `hold` stops everything for a lead; `lost`, `unsubscribed` and `bounced` suppress it forever.
- **Failures are reported.** One bad address doesn't block the rest; failures and paid-but-not-launched sites show in
  the daily status line.
- **No launch on payment alone.** It needs the exact price **and** the restaurant's written go-ahead.
- **Honest emails.** No "I live nearby" or fake compliments. Each is labelled as a sales email, with your real name,
  phone and postal address. The first email has no payment link.
- **Honest previews.** No payment link, no invented copy, and no photos or review quotes without permission. Each
  preview is labelled "not affiliated", unindexed, and on one shared site at an unguessable address. It comes down
  after 30 days.
- **Private data.** Leads, previews, emails, keys and your details never go into git.

## Run it on your own computer

```bash
git clone <your repo> && cd <repo>/sitehustle
python3 -m pip install requests pyyaml jinja2
cp config.local.example.yaml config.local.yaml   # your name, phone, address, digest email
cp .env.example .env                              # keys, once you have them
python3 -m unittest discover -s tests             # should print OK
python3 scripts/hustle.py status
```

Then open Claude Code in `sitehustle/` and say: *"Follow RUNBOOK.md. Start with the supply count."*

## What to do, in order (the council's plan)

1. **Free supply count (no contact).** Claude researches 30+ nearby places and runs `count`. If 2 or fewer of 30
   have no or a broken site plus a published email, stop there, or try in person only.
2. **In-person test (recommended first).** Show 5 previews on your phone to owners between 2 and 4 pm, and ask
   whether they'd pay. Claude writes the list in `data/in_person.md`.
3. **Email test, only with a written yes.** Ask an email provider in writing whether this exact use is allowed.
   Resend's policy bans cold outreach. If a provider says yes, add its key and set `mode: manual`. Then send 20 to 30
   emails you approve, starting with a few to your own test inboxes to check they don't land in spam.
4. **Before the first payment:**
   - a one-page terms and refund page (`offer.terms_url`; have a PA attorney look at it);
   - decide whether to trade under your own name or file a fictitious name;
   - ask a tax professional about PA sales tax.

The council's stop rules: 0 sales and fewer than 2 interested replies after 30 pitches, or any complaint → stop.

## Accounts (only when you get to step 3)

- **Email:** a provider that confirms in writing that this use is allowed, sending from a new domain (about $12/yr)
  with SPF, DKIM and DMARC set up.
- **Netlify** (hosting, `NETLIFY_TOKEN`): one shared preview site keeps you inside the free plan. Each paid site gets
  its own site, so consider a paid plan or hand sites over to the restaurant.
- **Stripe:** a $500 Payment Link, plus a restricted key with *Checkout Sessions: Read* only.

## Commands

```
python3 scripts/hustle.py status | count | discover | upsert <file> | build <id> [--final]
  publish-previews | cleanup | queue | reply <id> <draft> | offer <id> | digest [--print]
  approve <digest-id> [SKIP ids] | send | followups | payments | confirm <id> <note>
  launch <id> | mark <id> <status> [note] | suppress <email|domain> | failures
```
