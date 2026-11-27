# ROUND 1: Email deliverability and anti-spam compliance specialist (deliverability)

**Dossier:** DOSSIER-01-launch-sitehustle-as-built-after-fixes-c.md. **Addenda read:** none (no ADDENDUM-01*.md existed when this was written).
**Round 1, independent:** no other member's report was read before this one was written.

**Position:** Do not launch B or C as designed. The sending provider the system is built on (Resend) explicitly bans cold outreach in its terms. I support only E: a capped test of 20 to 30 first-touch emails, every one approved by hand, sent through a channel whose terms permit it, after the fixes in section 6. A human approves every first-touch email for good, not only in week one.
**Confidence:** high on the provider blocker (I read the policy text myself). Medium on the rest.

## 1. Position and why

1. **The provider forbids this exact use, so the system as built breaks my red line.** Resend's Acceptable Use Policy (page dated "Last update: October 13th, 2026", fetched today) says: "Spamming: You are prohibited from sending unsolicited messages of any kind, including cold outreach, purchased lists, or scraped contact data." It also says: "All mail must be sent to recipients who have explicitly opted in ... Sending to unsolicited recipients is not permitted on Resend." It reserves the right to "terminate your account at any time". SiteHustle's whole outreach step (`send_email` in `scripts/hustle.py`, which POSTs to `api.resend.com/emails`) is cold outreach to people who never opted in. No fix inside the code makes this compliant. Only a change of provider or channel does.
2. **A Resend ban would take the whole business down, not only outreach.** The same `send_email` function sends the owner's approval digest, the "you got paid" alert, the agent's replies to prospects (RUNBOOK §1), and the "you're live" email to paying customers (`cmd_launch`). If the account is closed, the system loses its customer-service channel to people who have already paid. This is a single point of failure, and the trigger is in the provider's written terms.
3. **At this volume, complaint and bounce rates can't be measured, so "keep it under the threshold" can't be done.** Resend's stated limits are a complaint rate under 0.08% and a bounce rate under 4% (AUP and docs). The local market probably yields only tens of sendable leads (dossier E2), so perhaps 40 to 120 emails in total. One spam report in 120 emails is 0.83%, about ten times the limit. Resend's own docs also say Gmail and Google Workspace do not return complaint events. So complaints from what are probably most recipients stay invisible to the user, while one complaint from a Yahoo or Microsoft recipient breaches the threshold. My persona card's own test ("complaint rate under 0.1%") can't be passed or failed with numbers this small. Section 5 replaces it with a count-based test.
4. **Volume is not the problem. Per-message quality and honesty are.** 15 a day is far below Resend's new-domain warm-up table, which allows up to 150 on day 1. The risk is that each email is cold, from a domain only days old, links to a free-hosting subdomain plus a payment page, and contains a first-person claim that may be false (section 2). Any of these can turn one recipient into a spam report, and at this scale one report matters.
5. **Turning on automatic sending is the wrong direction for my seat.** At 5 to 15 emails a day, human review costs about 2 minutes. Unreviewed AI-written compliments and "problems" are the biggest source of complaints the system has. The trial also ends on a fixed calendar date, not after a number of reviewed days (section 2), so it can end up shorter than a week or skipped entirely.
6. **What my seat gains and loses:** I am judged on whether the domain and account survive and on complaints avoided. Option A costs my seat nothing. Option B is close to the worst case: a terms violation from day one, unmeasurable complaints, and the risk lands on the user's local reputation in their own town. A small, hand-sent, permitted test is the only option where I can measure anything at all.

## 2. Where the dossier is wrong, incomplete or mis-posed

- **§6 "Whether Resend's AUP permits cold outreach. Not checked."** This can now be settled, and it is the decisive fact for my seat. I fetched `https://resend.com/legal/acceptable-use` with curl through the session proxy (HTTP 200) and read the text. It prohibits cold outreach by name. This belongs in an addendum, and option B's description ("Set up accounts ...") should not read as if the only blockers left are account setup (dossier §7, the builder's position).
- **The options table treats the sending provider as a setup detail.** It is a gating decision. The council needs a missing option: **"email only after contact"**. The first touch is in person, by phone or by postcard (the user lives locally). The preview link is emailed only once the owner says "send it". That email is then solicited, and Resend's terms would plausibly allow it. It costs user time, which conflicts with the user's goal, and I say so openly.
- **F4 is incomplete: the trial can be shorter than a week, or zero.** `cmd_send` switches to `auto` when `today >= trial_ends` (the fixed date "2026-12-07" in `config.yaml`). Setup on Dec 3 means 2 to 3 reviewed weekdays. Setup on or after Dec 7 means the first send run switches to auto and sends with no review at all. (Fact, read from code.)
- **F4/F5 are incomplete: a stale APPROVE can approve a batch nobody reviewed.** RUNBOOK §1 tells the agent to search `newer_than:2d` and run `approve` on any owner reply that says APPROVE. `cmd_approve` marks *every* item in the outbox approved, and it isn't tied to a particular digest. An APPROVE sent on day 1 can still be inside the 2-day window on day 3, when the outbox holds day 2's queue. Whether this happens depends on the agent's judgment, and nothing in the runbook stops it. (Fact for the code path. Estimate that it happens: plausible, not measured.)
- **F5 is incomplete: bounces are not handled at all.** Resend uses the `send` subdomain as the default Return-Path (Resend docs, custom-return-path page), so bounces go to Resend, not to the reply-to inbox the agent reads. The script never queries Resend for bounces or suppressions, so a bounced lead stays `contacted` and gets a follow-up. Resend's docs say it auto-suppresses hard bounces. What the API returns for a suppressed recipient, and therefore whether the script records a follow-up that was never delivered, was not checked.
- **F5 is incomplete: unsubscribes can fall through gaps.** (a) The inbox search is `newer_than:2d` on weekday runs only. A reply that arrives on Friday after the Friday run but before about the same time on Saturday is outside the window when the Monday run looks back 48 hours. It is never processed. (Fact from the runbook wording. Exact edges depend on run time.) (b) Nothing makes `send` conditional on the inbox step succeeding. If the Gmail connector fails but Resend works, follow-ups go out to people who already asked to stop. (c) `mark <id> lost` does not add the address to `suppression.txt`. Only `unsubscribed` does (`cmd_mark`). A "no thanks" lead that is rediscovered with a different name or address string could be pitched again.
- **F5/F6: the footer contradicts the sequence.** The outreach footer says "You got this one-time note", but `cmd_followups` sends a second email 5 days later. This is a small misstatement in a commercial email, and it is exactly what makes a recipient press "report spam" on the follow-up.
- **F6 is mis-described as a style question. It is a deception and complaint risk.** The template hard-codes "I live nearby and {{compliment}}". The runbook tells the agent to take the compliment "from real reviews". The sample turns a stranger's review into "my family loves your vodka rigatoni", which is a false first-person claim. And "I live nearby" stays in the template when `targeting.areas` expands. CAN-SPAM's deception rules cover headers and subject lines. Body deception falls under the FTC Act's general rules and is the lawyer's call, but for my seat it drives complaints.
- **W1 is incomplete.** The FTC guide (as quoted in search results) also requires that (a) the message be disclosed "clearly and conspicuously" as an advertisement, which the template never does in so many words; (b) a PO box counts as the postal address only if it is registered with USPS or a commercial mail receiving agency. The `config.yaml` comment "A PO box or virtual mailbox is fine" holds only for a box that is registered that way. (c) The opt-out must keep working for 30 days after sending (my recollection of the guide; the FTC page returned 404 to curl, so I did not see this passage myself). (d) Both the sender and the business being promoted can be held liable. Resend's AUP is stricter than the law on timing: opt-outs honoured "within 7 days", against CAN-SPAM's 10 business days.
- **W2 is consistent.** Search results quote the current FTC guide at "up to $53,088" per violating email. I could not fetch the FTC page directly (HTTP 404 to curl, probably bot blocking).
- **W3 is right but needs a qualifier.** Google's sender-guidelines page (fetched, HTTP 200) applies to "personal Gmail accounts", meaning addresses ending in @gmail.com or @googlemail.com. The 0.3% figure is "spam rates reported in Postmaster Tools". At this volume, Postmaster Tools will very probably show no data (assumption: it reports only above a minimum volume; not checked today). So the user has no way to see their Gmail spam rate.
- **F11 can now be settled.** I ran `gh api repos/amansome/amansome`. It returned `private: false`, `visibility: public`. Lead emails, the suppression list and outbox drafts committed there would be public, which exposes recipients' addresses to harvesting. `data/leads.json` is currently `[]`, so nothing has leaked yet.
- **README omission.** It describes Resend as "free for 3,000/mo". Resend's docs also set a free-plan cap of 100 a day and count received emails toward the quota. This doesn't bind at 15 a day. The terms are what bind.
- **E1 is mis-posed.** A reply rate is conditional on reaching the inbox. A test through a provider that filters or bans the sender measures deliverability, not demand. The test has to log inbox placement separately (section 5).

## 3. Evidence

| Claim | Type | Source or method |
|---|---|---|
| Resend's AUP prohibits "unsolicited messages of any kind, including cold outreach, purchased lists, or scraped contact data" and requires explicit opt-in for all mail | fact | `https://resend.com/legal/acceptable-use`, fetched 2026-11-27 via curl, page dated Oct 13, 2026; text extracted and read |
| Resend thresholds: complaint rate < 0.08%, bounce rate < 4%; account "may be shut down without warning" above them; opt-outs within 7 days for bulk sending | fact | Same AUP page; `resend.com/docs/knowledge-base/warming-up.md` |
| Resend free plan: 100/day, 3,000/month; received emails count toward the quota | fact | `resend.com/docs/knowledge-base/account-quotas-and-limits.md`, fetched |
| Resend's new-domain warm-up allows up to 150 emails on day 1, so 15 a day is not a volume risk | fact | warming-up doc, fetched |
| Gmail and Google Workspace do not return complaint events to Resend | fact | `resend.com/docs/dashboard/emails/email-suppressions.md`, fetched |
| Resend's default Return-Path is the `send` subdomain, so bounces do not reach the reply-to inbox | fact (docs) / inference (where bounces end up) | `resend.com/docs/dashboard/domains/custom-return-path.md`, fetched |
| The script never ingests bounces or complaints | fact | Read `scripts/hustle.py` in full: no Resend webhook or suppression API call |
| Every outbound email (outreach, digest, replies, payment alerts, launch emails) goes through the same Resend function | fact | `send_email` and its callers in `hustle.py`; RUNBOOK §1 |
| The trial ends on a fixed calendar date; setup after Dec 7 means no trial at all | fact | `cmd_send` date comparison; `config.yaml` `trial_ends` |
| `approve` approves every outbox item and is not tied to a digest; the runbook re-reads APPROVE replies from a 2-day window | fact (code and runbook) / estimate (that it misfires) | `cmd_approve`; RUNBOOK §1 |
| A Friday-afternoon reply can fall outside the Monday `newer_than:2d` window | fact (wording) / estimate (exact edges depend on run time) | RUNBOOK §1 |
| `lost` does not add the address to the suppression list | fact | `cmd_mark` |
| Outreach footer says "one-time note" while a follow-up is sent | fact | `templates/email/outreach.txt.j2`; `cmd_followups` |
| The first email contains a `*.netlify.app` link and a `buy.stripe.com` payment link carrying the recipient's email address | fact | `claim_url` (adds `prefilled_email`); outreach template |
| A days-old domain plus a free-hosting subdomain link plus a payment link in a cold first email resembles phishing patterns and raises filtering and complaint risk | estimate | Professional heuristic for this seat; not measured; seed tests (section 5) would measure it |
| The repo `amansome/amansome` is public | fact | `gh api repos/amansome/amansome` returned `private: false`, `visibility: public` |
| Gmail's 2024 requirements apply to personal @gmail.com and @googlemail.com accounts; spam rate measured in Postmaster Tools below 0.3%; DMARC and one-click unsubscribe only at 5,000+/day | fact | `support.google.com/a/answer/81126`, fetched |
| Postmaster Tools will show no data at this volume | assumption | Not checked today |
| FTC: up to $53,088 per violating email; clear and conspicuous ad disclosure; a PO box must be registered with USPS or a CMRA | fact (secondary) | Web search results quoting the FTC CAN-SPAM guide; direct fetch returned 404 |
| Google Workspace's AUP prohibits using it "to generate, distribute, publish or facilitate unsolicited mass email, promotions, advertisements, or other solicitations ('spam')" | fact | `workspace.google.com/terms/use_policy/`, fetched |
| Whether a handful of individually written one-to-one emails from a Workspace mailbox counts as "mass" under that wording | unknown | Text is ambiguous; not a clean permission; ask the provider or a lawyer |
| Total sendable volume over the campaign is about 40 to 120 emails | estimate | Dossier E2 (100 to 200 places, a minority with a weak site and a published email) × 2 emails each; unmeasured |
| Bounce rate on emails gathered from Facebook pages and old sites may exceed 4% | assumption | General experience with small-business contact data; unmeasured |
| Cold-email-oriented sending tools exist whose terms permit B2B cold outreach | assumption | Not checked for any specific vendor in this session; each one's terms must be read before use |

## 4. Risks from this seat

- **A. Do nothing:** no risk to my seat. The only loss is the user's upside.
- **B. Launch as built:** a terms violation from the first send. The account can be closed at any time without warning, which also cuts off replies and launch emails to paying customers. Complaints from Gmail and Workspace recipients are invisible, so the user may be filtered to spam silently and read the silence as "no demand". **This is the quiet failure: low replies look like a weak market when the cause is the spam folder.** Unhandled bounces push the bounce rate up unseen. The fixed-date trial can mean zero human review. All of this happens under the user's own name, in their own town.
- **C. Launch after fixes, still on Resend:** the code fixes do not cure the terms problem. Same ban risk, slightly fewer complaints.
- **C on a different provider, then auto:** legally workable if the terms permit it. But unreviewed AI-written first-person content stays the main complaint driver, and the user still can't measure complaints at this volume.
- **D. Email only after contact (in person, phone or postcard first):** the cleanest option for deliverability, and Resend's terms are then plausibly met. The cost is the user's time, against the user's stated goal.
- **E. Small hand-approved test:** acceptable if sent through a permitted channel. The residual risk is a few complaints. These should be counted, not turned into rates.

## 5. The cheapest decisive step

**Biggest question for my seat:** is there any sending path whose terms permit this outreach? (Resend's terms are already settled: they don't.)

**Step (about 30 minutes, $0):** before anything is sent, pick the sending path for first-touch emails, read its acceptable-use terms, and get a written answer from its support to this exact question: "Can I send about 5 to 15 individually written emails a day to restaurants' publicly listed business addresses, one email plus one follow-up, with CAN-SPAM opt-out?" Do the same with Resend support if the user wants to keep Resend.

**Result decided now that would change my position:** if Resend support confirms in writing that this use is allowed, I drop the provider objection, and my position becomes "C after the section 6 fixes, with human approval kept on first-touch emails". If no permitted provider can be found, my position becomes D (email only after contact) or A.

**Second step, once a provider is chosen (an hour, $0):** send 5 seed emails in the real format to Gmail, Outlook.com and Yahoo test inboxes that the user controls. Check SPF, DKIM and DMARC pass in the headers, and note inbox versus spam placement, once with the netlify.app and Stripe links and once with a single link on the user's own domain. If the two-link version lands in spam and the one-link version does not, the one-link format becomes a hard condition.

**Replacement for my card's untestable "complaint rate under 0.1%":** in the 20 to 30 test sends, zero spam complaints and zero abuse reports, and at most 1 hard bounce. Any complaint stops sending until the cause is understood.

## 6. Conditions and red lines

**Red lines (I will not support an option that has any of these):**
- First-touch cold email sent through a provider whose terms forbid it. That rules out Resend today.
- Email addresses taken from directories or sites that carry a no-solicitation or no-harvesting notice. Each lead must record where its email came from.
- No working unsubscribe path, or sending while the inbox step that processes unsubscribes has failed.
- Unreviewed automatic first-touch sending of AI-written personal claims.

**Conditions for supporting E, or C on a permitted path:**
1. First-touch email goes through a channel whose terms permit it, with a written answer from the provider where the terms are ambiguous. Resend stays limited to solicited and transactional mail: replies to people who wrote in, the digest, and launch emails.
2. The domain is set up with SPF and DKIM passing, plus a DMARC record (`p=none` is fine), all checked in seed-test headers. Ideally the domain gets a simple real website first and a week or two of age before any sends.
3. One link per first email, on the user's own domain (e.g. `preview.<studio>.com/<slug>`), not `*.netlify.app`. No payment link and no `prefilled_email` until the owner replies.
4. Template fixes: delete the false first-person compliment and "I live nearby" unless literally true for the sender; frame praise as "your reviews mention ..."; add a plain line saying it is a sales offer; remove "one-time note" or drop the follow-up.
5. Code fixes: tie approval to a specific digest (a digest ID, not a 2-day search); make the trial a count of approved batches, not a calendar date; skip `send` if the inbox step failed; add `lost` addresses to suppression; check for an MX record and record `email_source` before queueing; ingest bounces and complaints, or at minimum stop follow-ups to anything the provider reports as bounced.
6. Human approval of every first-touch email stays permanent at this volume (about 2 minutes a day). Follow-ups can be automatic once the first email was approved.
7. Lead data moves out of the public repo before any real email address is stored there.
8. The PO box or mailbox is registered with USPS or a commercial mail receiving agency.

## 7. One line

Resend's own policy bans cold outreach, so SiteHustle can't launch as built. Run only a hand-approved test of 20 to 30 emails through a channel that allows it, after fixing the honesty, bounce, unsubscribe and trial-logic gaps, and count complaints one by one.
