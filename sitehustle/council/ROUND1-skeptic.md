# ROUND 1: Skeptic (argues for not doing it, or doing less) (skeptic)

**Dossier:** DOSSIER-01-launch-sitehustle-as-built-after-fixes-c.md. **Addenda read:** none (I listed `council/` on 2026-11-27 and found no ADDENDUM-01* file).
**Round 1, independent:** no other member's report was read before this one was written.

**Position:** Do not launch as built (B), and do not promise yourself a hands-off business. At most run Option E as a small test sent by hand, in your own name, through an email setup whose terms allow it. If that test produces nothing, stop (A).
**Confidence:** high that B must not run; medium on E versus A.

## 1. Position and why

1. **The headline promise is not true, and the README presents it as if it were.** `README.md` says "Your only job is getting paid (plus about 2 minutes a day approving emails for the first week)". The system's own runbook says otherwise: legal threats, angry replies, refund requests and payments it cannot match all go to the owner (`RUNBOOK.md`, ground rules). The $400 discount it lets the agent offer cannot be taken with the tools provided: there is one $500 Payment Link (`config.yaml`), and the Stripe key is read-only (Checkout Sessions: Read, `README.md` step 4), so someone has to create a $400 link by hand. Domain and DNS help (`launched.txt.j2`) depends on a stranger doing DNS by email, one message a day. Stripe identity checks, a fictitious-name registration if the studio name is used (W5), taxes, disputes, and "free hosting" with no end date are all the user's to carry. A plan that sells "zero involvement" when it isn't zero is my red line.
2. **The email service bans this use, from the first email.** I fetched `resend.com/legal/acceptable-use` with curl on 2026-11-27. It reads: "You are prohibited from sending unsolicited messages of any kind, including cold outreach, purchased lists, or scraped contact data", and "Your complaint rate must be lower than 0.08% … your account may be shut down without warning." The dossier lists this as "Not checked" (§6). It is now checked: the system as built breaks its provider's terms on every outreach email. With a local list of a few dozen addresses, a single complaint puts the rate far above 0.08%.
3. **The private data would be published, and the code already is.** I ran `gh api repos/amansome/amansome` on 2026-11-27 and got `"private": false, "visibility": "public"`. `git ls-remote origin` shows the branch `claude/friendly-pascal-r0rno3` (with SiteHustle on it) already pushed. The runbook tells the daily agent to "commit and push `data/`, `sites/` and `outbox/`". Once it runs, that means restaurant emails, phones, notes, payment status, the do-not-contact list and the full text of every pitch are public on the user's own GitHub profile. The `noindex` on the previews protects nothing if the same HTML sits in a public repo.
4. **The emails speak in the user's first person, the content is made up, and nobody reads them after the trial.** The template opens "I live nearby and {{compliment}}" (`templates/email/outreach.txt.j2`). The sample compliment is "my family loves your vodka rigatoni" (`examples/sample-lead.json`). That claims a personal customer experience, which breaks the runbook's own rule "Never claim to be … a customer". Any compliment drawn from reviews turns into a first-person claim inside that sentence frame. After trial week the user never sees what is said in their name to restaurant owners in their own town. That town is where the user lives, eats and will meet these people.
5. **The "trial week" is set by a calendar date, not by how many emails the user has reviewed.** `cmd_send` switches to auto when `today >= trial_ends` (hard-coded `2026-12-07`, a Monday). If setup happens on Monday 30 Nov, the trial covers at most 5 weekdays, fewer after the first research day. If setup happens on or after 7 Dec, there is **no trial at all** and unreviewed email goes out on the first run. This failure is quiet: nothing warns the user.
6. **The upside is small, and an automated mistake burns it for good.** The whole addressable list in the user's town is probably a few dozen restaurants (estimate, §3). Each can be pitched only once. That number can be sent by hand in an afternoon, so the automation adds little, while it can spoil every one of those leads, and the user's local name, in two or three weeks at 15 a day. "Doing less" costs almost nothing here.

## 2. Where the dossier is wrong, incomplete or mis-posed

- **F11 / §6 "visibility was not checked":** now checked. The repository is public (gh API, above), and the SiteHustle branch is already pushed to it. This should be stated as a fact and a blocker, not a maybe.
- **§6 "Resend AUP not checked":** checked. Cold outreach is explicitly banned and the complaint threshold is 0.08% (curl of the live AUP page, above). The option table's cost row for B and C leaves out the cost of switching provider. It also leaves out that no mainstream transactional email API is likely to permit this (assumption; I checked only Resend's terms).
- **Option B's "2 min/day for one week" is mis-stated.** An honest review means reading up to 15 emails and opening up to 15 previews to check that the menus, prices and hours are right. That takes about 15 to 30 minutes a day (estimate: 1 to 2 minutes per pitch). The ongoing involvement after week 1 (item 1 above) is left out entirely.
- **F4 is incomplete.** It does not say that trial length depends on the setup date, or that a setup on or after 7 Dec 2026 means no trial (code, `cmd_send`).
- **F10 is incomplete.** The $400 discount cannot be taken with the single $500 link and a read-only key (code, `claim_url`, `cmd_payments`; README step 4). Either the user steps in or the restaurant is promised a price it cannot pay.
- **F6 understates the problem.** The template forces a first-person claim, and the sample breaks the runbook's own "never claim to be a customer" rule. The dossier lists this as a neutral fact.
- **F16 is not followed through.** If the scheduled agent meets the same block on fetching sites, it either produces nothing, which is safe, or writes menus and prices from search snippets, which publishes wrong menus under the restaurant's name. That second path is the owner seat's red line. No site has been scored yet, so the scoring step itself is untested.
- **Missing from the dossier:** the agent reads the user's *personal* Gmail through a connector. RUNBOOK §1 falls back to "search by the business domain if the label is missing". It also acts on text written by strangers (replies). The dossier does not mention that exposure, or that an inbound email could push the agent into doing something unintended (an assumption about the risk; I did not test it).
- **Missing copy issues:** the footer says "this one-time note" although a follow-up is always queued (`outreach.txt.j2`, `cmd_followups`). For leads with no website, scored 2, the template still says "I was looking at {{name}}'s website and noticed …". Neither email says plainly that it is an advertisement. I flag that last one for the lawyer against W1; I have not judged it.
- **Mis-posed scale:** E2 is treated as a footnote, but it decides the question. If the list is roughly 25 to 70 leads, the right comparison is "automated sending" against "one afternoon by hand", not "15 a day against 40 a day".
- **Missing option:** a local, by-hand version. The user (or the agent drafting for the user) picks 10 to 20 places, builds the previews, and pitches by personal email, phone or walk-in with the preview on a phone. Option D mentions "walk-in" in passing but does not treat it as the cheap, low-risk default that it is for someone who lives there.
- **Hosting terms:** the dossier says Netlify's terms are unchecked. A web search found Netlify forum staff answers: commercial use and handing a site off are fine on Free, but "if you plan on billing other people for sites you deploy", a paid plan is required. Over-limit sites are suspended for the rest of the month. These are staff forum posts, not the terms of service, and I could not confirm the current site cap. The offer bundles "free hosting" into a $500 sale, so it may fall on the wrong side of that line.

## 3. Evidence

| Claim | Type | Source or method |
|---|---|---|
| Resend prohibits cold outreach; complaint rate must be <0.08%; accounts may be shut down without warning | fact | curl of resend.com/legal/acceptable-use, 2026-11-27 (text quoted above) |
| The repo holding SiteHustle is public; the branch is pushed | fact | `gh api repos/amansome/amansome` returned `private:false`; `git ls-remote origin` lists `refs/heads/claude/friendly-pascal-r0rno3` |
| Daily run commits and pushes lead data, sites and outbox | fact | `RUNBOOK.md` intro and §6 |
| Auto mode starts on 2026-12-07 whatever the setup date; that date is a Monday | fact | `config.yaml` `trial_ends`; `hustle.py` `cmd_send`; Python `date(2026,12,7).strftime('%A')` |
| Only one $500 Payment Link; Stripe key is read-only, so the $400 offer has no automatic path | fact | `config.yaml` `offer`; `hustle.py` `claim_url`; `README.md` step 4; `RUNBOOK.md` §1 |
| Template frames the compliment in first person; sample claims "my family loves your vodka rigatoni" | fact | `templates/email/outreach.txt.j2`; `examples/sample-lead.json` |
| Runbook forbids claiming to be a customer | fact | `RUNBOOK.md` ground rules |
| Risky cases (legal threat, refunds, unmatched payments) go to the owner | fact | `RUNBOOK.md` ground rules |
| Footer says "one-time note" while a follow-up is always queued | fact | `outreach.txt.j2`; `hustle.py` `cmd_followups`; `config.yaml` `max_followups: 1` |
| Netlify Free allows commercial and handed-off client sites; billing others for hosted sites needs a paid plan; over-limit sites are suspended | fact, secondary | Netlify forum staff answers and Netlify blog via web search, 2026-11-27; ToS not read; current site cap not confirmed |
| ~150 to 200 independent food places within 9 km | estimate | Area population ~100k to 130k (Mechanicsburg, Hampden, Silver Spring, Upper/Lower Allen, Camp Hill; from memory, not verified) ÷ ~1 food place per 350 to 500 people × ~50% independent. Agrees with E2 |
| 25 to 70 of them both score ≤5 and publish an email | estimate | 15% to 35% of the above; low because Facebook-only places (the "best" leads) rarely publish an email that can be fetched, and discovery collected none (dossier §2) |
| 0 to 1 paid sales expected from the whole local list (central about 0.3 to 0.5) | estimate | 50 pitches × 1% to 8% reply × 10% to 30% of replies paying. The reply range is widened above E1 for the personalised preview. Not measured |
| Honest daily digest review takes 15 to 30 min, not 2 | estimate | 1 to 2 min per pitch × up to 15 pitches, with menu and price spot-checks |
| Ongoing support after the first sales (edits, menus, DNS, disputes) is 1 to 3 h/month at low volume, plus incidents | estimate | Count of the runbook's escalation paths and offer terms; no data |
| An inbound email can steer the agent | assumption | General AI-agent risk; not tested here |
| No mainstream transactional email API permits cold outreach | assumption | Checked only Resend |

## 4. Risks from this seat

- **B (launch as built):** the Resend account is likely closed after the first complaint, and the new domain's reputation is damaged. Restaurant contact data and pitches become public on the user's GitHub profile. Neighbours receive first-person claims the user never made ("my family loves …"). Wrong menus or prices may be published under a restaurant's name. A late setup means no trial at all. Most of these failures are **quiet**: the user is told only when someone pays or something "needs a human", so the first sign of trouble may be a complaint, a closed account or a word-of-mouth reputation hit in town.
- **C (after fixes):** better. But it keeps the false premise of zero involvement. Each fix (a new provider, a private repo, review gates) adds involvement or cost, and the upside stays capped by a list of a few dozen leads. Quiet risk: the fixes get done and the "auto after a week" switch stays in place.
- **D (change the model):** honest about involvement. Risk: the user does not want the time cost and drops it halfway, leaving customers with sites they paid for and no one to maintain them.
- **E (small manual test):** low risk if done by hand from a normal mailbox in the user's own name, previews checked by the user, and no public data. Quiet risk: the "test" is run through the automated system, so it is really B with a smaller number.
- **A (do nothing):** loses an expected value I estimate at well under $500 over 3 months. Nothing irreversible happens. That is the baseline every other option has to beat after counting the user's time.
- **After any sale:** "free hosting, no end date" on the user's personal Netlify account means the user can never cleanly stop without leaving paying customers stranded. That is a 12-month-plus liability bought for one $500 payment.

## 5. The cheapest decisive step

**Step 0 (free, no outreach, no risk, about 1 hour of agent time):** research the first 30 independent places within 9 km and count how many both score ≤5 and publish a business email, recording the source for each. If fewer than 10 of 30 qualify, the full local list is under ~60. Automation is then pointless, and only a by-hand version makes sense.

**Step 1, the decisive one:** a hand-run test of 20 to 30 pitches. Previews are built by the agent and checked by the user for every menu item and price. Emails are sent by the user from an ordinary mailbox in their real name, not through Resend. There is no first-person compliment unless it is literally true. Nothing is committed to the public repo. Where possible, a few are walk-ins with the preview on a phone. Run it over 2 to 3 weeks.

**Decided now:**
- If it produces **at least 1 paid sale, or at least 3 serious replies** (asking about price, changes or timing), I move to supporting C with a person permanently in the loop: the user approves every send, uses a provider whose terms allow it, keeps the repo private, and offers honest terms with a stated hosting period.
- If it produces **0 sales and at most 1 serious reply**, I support A, and the user should stop.
- If it produces **any formal complaint or abuse report**, I support A whatever the replies.

## 6. Conditions and red lines

I will support an option only if all of these are true:
- Nothing is sent through a provider whose terms ban cold outreach. Resend as configured fails this.
- Lead data, outbox emails and generated sites are kept out of any public repository. Today they would go into a public one.
- No email claims a personal experience the user did not have. "I live nearby" stays only if it is true and the user has seen it. "My family loves …" style lines go.
- Automatic sending is not switched on by date. If it is ever switched on, it happens only after a set number of user-reviewed sends **and** a measured result from step 1. My own preference is never.
- The user is told the honest minimum involvement in writing before setup. Estimate: honest review time while sending, plus 1 to 3 hours a month and incident handling afterwards, plus business registration, tax and Stripe paperwork.
- The offer states a hosting period and what happens after it, and a buyer gets simple terms and a refund policy before paying.

I will not accept: B in any form, or any plan described as "zero involvement".

## 7. One line

As built, SiteHustle breaks its email provider's terms, would publish its leads on a public GitHub profile, speaks in first-person claims to the user's own neighbours with no one reading after a calendar-date "trial", and sells a "zero involvement" that is not real. Run a 20 to 30 pitch test by hand, or do nothing.
