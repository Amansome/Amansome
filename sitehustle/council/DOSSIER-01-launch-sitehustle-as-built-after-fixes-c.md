# DOSSIER 01: Launch SiteHustle as built, after fixes, changed, or not at all

**Convened:** 2026-11-27. **Question:** In what form, if any, should the user switch on SiteHustle?

This is the identical factual record every member works from. **Check it and report where it is
wrong, incomplete or mis-posed.** Later numbered addenda (ADDENDUM-01A, 01B, ...) win where
they conflict with this file.

## 0. The question in one line

Should the user switch on SiteHustle, an automated "find restaurants with weak websites, build a preview,
cold-email, sell for $500" system, as it is now, after changes, in a different form, or not at all?

## 1. Options on the table

These are starting options; members may propose others.

| Option | What it means | Reversible? | Rough cost / time |
|---|---|---|---|
| A. Do nothing | Don't switch it on | Yes | $0 |
| B. Launch as built | Set up accounts, one trial week of approved daily batches (up to 15 emails/day), then automatic sending | Partly: sent emails and a burned domain can't be undone | About $20 setup + about $7/month; 45 min setup; 2 min/day for one week |
| C. Launch after fixes | As B, after specific changes the council identifies | Partly | As B + build time |
| D. Change the model | E.g. different price structure, a different channel (phone, walk-in, mail), or keep a human in the sales step permanently | Yes | Varies; more of the user's time |
| E. Small test first | A capped test (e.g. 20 to 30 pitches, all approved by hand) before deciding on B/C/D | Yes | Setup + about 1 hour of the user's time over 2 to 3 weeks |

## 2. Market or domain

- **Target:** independent (non-chain) restaurants, cafes, diners, pizzerias and bars within about 9 km of
  Mechanicsburg, PA (config `targeting.areas`), which is where the user lives. Later expansion to more areas is possible.
- **Discovery test (2026-11-27):** a web-search-only pass found candidate names, addresses and phones for about
  15 independent places. For most, no official website was confirmed by search; several appeared to have only
  Facebook or a third-party ordering page (Slice, Toast, order.online). Fetching restaurant sites was not possible
  in that session (network/permission blocks), so **no site has actually been scored yet**. Source: the discovery
  subagent's report in this session; not independently verified.
- **Alternatives restaurants already have (by type):** DIY builders (Wix, Squarespace, GoDaddy), POS-provider
  online-ordering pages (Square Online, Toast), delivery-app listings, Google Business Profile, Facebook pages, and
  local freelance designers. Prices and features of these are **not** stated here; members should check public pricing.

## 3. Goal, constraints and success measures

- **Goal (user's words):** "I do not want to be involved in anything besides receiving payment, this would be a side hustle."
- **Measure of success:** paid sales at $500 each with near-zero user time and no legal/platform/reputation damage.
  No revenue target given.
- **Constraints:** small budget; the user will do 45 min of setup and approve daily for one week (the user chose "auto
  after a trial week"); runs as a scheduled AI agent in a cloud container; outreach is in the user's own town.
- **Who decides, and by when:** the user, at their convenience. No deadline.

## 4. Facts

### 4a. Facts about the system (source: files in `sitehustle/` on branch `claude/friendly-pascal-r0rno3`)

| # | Fact | Source |
|---|---|---|
| F1 | Pipeline statuses: new → researched → built → deployed → queued → (approved) → contacted → followed_up → replied/paid/launched/lost/unsubscribed | `scripts/hustle.py` `STATUSES` |
| F2 | Sending uses the Resend email API from an address on a new domain the user buys; replies go to that inbox, which the user forwards to their personal Gmail; the AI agent reads Gmail through a connector | `scripts/hustle.py` `send_email`; `README.md` setup step 1; `RUNBOOK.md` §1 |
| F3 | Limits: 15 emails/day (config), weekdays 9:00 to 16:00 US Eastern, 20 s between sends, 1 follow-up after 5 days, then stop | `config.yaml` `outreach`; `hustle.py` `cmd_send`, `cmd_followups` |
| F4 | Trial mode until 2026-12-07: emails are sent only after the owner replies APPROVE to a daily digest. On that date the script switches itself to automatic sending | `config.yaml`; `hustle.py` `cmd_send` |
| F5 | Every outreach email includes the business name, a postal address, and "Reply 'unsubscribe' and you won't hear from me again"; a `List-Unsubscribe` mailto header is set. Unsubscribes are handled when the daily agent reads the reply and runs `mark ... unsubscribed` | `templates/email/outreach.txt.j2`; `hustle.py`; `RUNBOOK.md` §1 |
| F6 | The outreach email opens: "I live nearby and {{compliment}}." The runbook tells the agent to write the compliment "from real reviews or their story". The sample lead's compliment is "my family loves your vodka rigatoni" | `templates/email/outreach.txt.j2`; `RUNBOOK.md` §4.6; `examples/sample-lead.json` |
| F7 | Preview sites are published publicly at `preview-<slug>.netlify.app`, carry a "Free concept preview made for <restaurant> by <studio>. Not live." bar, a `noindex` meta tag and a robots.txt disallowing all crawlers. They use the restaurant's name, menu, hours, address and, optionally, up to 2 of the restaurant's own photos referenced by URL from its site | `templates/site/index.html.j2`; `hustle.py` `cmd_build`; `RUNBOOK.md` §4.5 |
| F8 | Payment: a single Stripe Payment Link for $500 with `client_reference_id=<lead id>` appended; the agent polls Stripe Checkout Sessions to match payments. No terms of service, refund policy or written agreement is shown or linked | `hustle.py` `claim_url`, `cmd_payments`; `config.yaml` `offer` |
| F9 | Offer as written: mobile-friendly site with menu/hours/map/click-to-call, connecting their domain (the restaurant must change its own DNS records), two rounds of edits, "Free hosting (no monthly fee)". Hosting is on the user's Netlify account with no end date stated | `config.yaml` `offer.includes`; `templates/email/launched.txt.j2` |
| F10 | Price negotiation rule: the agent may go down to $400 if price is the only blocker; extra edit rounds quoted at $75 | `RUNBOOK.md` §1 |
| F11 | Lead data (`data/leads.json`: names, emails, phones, notes, payment status), generated sites and outbox emails are committed to the git repository `amansome/amansome`. That repository is the user's GitHub profile repository (it contains the profile README); GitHub shows a profile README only when the repository is public. Visibility was not checked directly | repo contents; GitHub profile README documentation |
| F12 | Scoring rubric for "bad website": start at 10, subtract for not mobile-friendly (-3), PDF/image/no menu (-2), dated look (-2), no HTTPS (-1), hard-to-find info (-1), broken (-1), slow/popups (-1). Pitch if ≤ 5; no website = 2 | `RUNBOOK.md` §4.3; `config.yaml` |
| F13 | The agent does research, scoring, content writing, reply handling and negotiation; the script does storage, build, deploy, send, follow-up and payment matching. Ambiguous or risky situations are emailed to the owner | `RUNBOOK.md`; `hustle.py` docstring |
| F14 | Credentials (Resend, Netlify, Stripe keys) are injected by the cloud environment's network proxy and are not stored in the repo | `hustle.py` `PLACEHOLDER_AUTH`; README |
| F15 | Testing so far: one fictional sample lead built and screenshotted; queue/approve/follow-up/unsubscribe flow simulated offline; one duplicate-follow-up bug found and fixed. No real deploy, email or payment has been executed | this session |
| F16 | In this session, fetching arbitrary restaurant websites was blocked (first by the network policy, then by a permission check after the network was opened). The OpenStreetMap data source (Overpass API) repeatedly dropped connections. Web search worked | this session |
| F17 | The daily scheduled run has not been created yet; it needs the user's accounts and config first | this session |

### 4b. Facts about the outside world (members and the verifier should check these against primary sources)

| # | Fact (as understood) | Source to check | Date |
|---|---|---|---|
| W1 | CAN-SPAM applies to all commercial email, including business-to-business. It requires non-deceptive headers and subject lines, identifying the message as an ad, a valid physical postal address, and an opt-out that is honoured within 10 business days. It does not require prior consent | FTC, "CAN-SPAM Act: A Compliance Guide for Business" | as published |
| W2 | CAN-SPAM civil penalties can exceed $50,000 per violating email (inflation-adjusted figure) | FTC compliance guide / Federal Register inflation adjustments | current year |
| W3 | Since February 2024, Gmail requires all senders to have SPF or DKIM and to keep reported spam rates below 0.3%; senders of 5,000+/day to Gmail have stricter rules (DMARC, one-click unsubscribe) | Google "Email sender guidelines" | 2024 |
| W4 | Stripe's standard US card fee is 2.9% + $0.30 per successful charge (about $14.80 on $500) | stripe.com/pricing | current |
| W5 | Pennsylvania requires registering a fictitious (assumed) name when doing business under a name other than the owner's legal name | 54 Pa.C.S. Chapter 3 (Fictitious Names Act); PA Department of State | current |

## 5. Estimates and assumptions

| # | Estimate or assumption | Basis or method | What would falsify it |
|---|---|---|---|
| E1 | Cold-email reply rates for small local B2B outreach are often in the low single-digit percent, with fewer replies turning into sales | Commonly cited industry ranges; not specific to restaurants or to emails that include a personalised preview | A measured test |
| E2 | Supply of leads: of ~100 to 200 independent places within 9 km, a minority will both score ≤ 5 and publish a business email | Assumption; the discovery test found most candidates had no confirmed own site and no published email was collected | Running discovery and research on 50 places |
| E3 | A personalised, already-built preview converts better than a generic pitch | Assumption (common claim among "build first" web agencies) | A measured test |
| E4 | The AI agent's time per researched lead is a few minutes; daily run costs come from the user's Claude plan usage | Assumption; not measured | Measuring one full run |
| E5 | Restaurant owners mostly read email on a phone during off-hours and are pitched by many vendors | Assumption | Owner interviews |

## 6. What is not known

- Whether Resend's (or any chosen provider's) acceptable-use policy permits cold/unsolicited outreach. **Not checked.**
- Whether Netlify's free plan terms permit hosting client sites commercially and what its current free limits are. **Not checked.**
- The real share of local restaurants with a weak site and a published email (E2). **Not measured.**
- Any real reply or close rate for this offer. **No test has been run.**
- Whether the user has registered a business or plans to; whether PA sales tax applies to website design services. **Not researched; refer to a professional.**
- What the user would do if a restaurant complains, disputes a charge or wants changes in a year. **Not specified beyond the runbook's "email the owner".**
- How the restaurant updates its own menu or prices after launch. **Not specified; every change would go through the agent.**

## 7. Positions already held

- The user's stated preference is near-zero involvement and automatic sending after one trial week. **Position to test.**
- The builder of the system (the AI that wrote it) designed for compliance with CAN-SPAM and believes the main
  remaining blockers are the user's account setup. **Position to test.**

## 8. What the council is asked

1. Should the user launch, and in which form (A to E or another)?
2. What, if anything, in the system as built is wrong, risky or deceptive and must change before any email is sent?
3. Is "zero involvement besides receiving payment" achievable? If not, what is the minimum honest involvement?
4. Is $500 one-time, with free hosting and no end date, the right offer? What would a restaurant owner actually want?
5. What happens over 12 months after a sale (hosting, edits, menu changes, support), and who carries that?
6. What is the cheapest step that would settle the biggest open question, and what result would change the decision?
