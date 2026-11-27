# ROUND 2: Email deliverability and anti-spam compliance specialist (deliverability)

**Read:** ROUND1-TALLY.md, every ADDENDUM-01*, and all Round 1 reports.

**Vote:** B
**Changed from round 1:** no
**Confidence:** high on the channel gate and on "no automatic first-touch sending in the 3-month horizon"; medium on whether a provider that permits this use will answer yes in writing.

## 1. Vote and reason

**B: fix, then a hand-approved email test. The vote holds only while a sending channel whose terms permit this use is confirmed in writing. If none is, my vote becomes D (human-first contact; email only after the owner asks for it). It does not go to the user's own mailbox, and it does not go to A.**

Why B, from this seat's mandate (account survival, compliance, complaints avoided):

1. **The channel is the gate, and nothing that came out of Round 1 changes that.** Resend's acceptable-use policy bans "unsolicited messages of any kind, including cold outreach" (fact: ADDENDUM-01A item 1; V28, V57). Every other fix is wasted if the first send breaches the sender's contract. B is the only option that puts "a permitted sending channel, confirmed in writing" first in its list and still lets the test run by email. C contains the same test, but it comes after an offer redesign that is outside my mandate. D is safer for my seat but costs the user much more time, so it is my fallback, not my first choice.
2. **A 20 to 30 email test is the only volume where this seat can read anything, and only in counts.** One complaint in 30 sends is 3.3%, about 41 times Resend's 0.08% limit. One in 25 is 4% (fact: arithmetic on the AUP threshold). Gmail and Google Workspace send no complaint events (fact: V55), and Postmaster Tools shows no data at low volume (fact: V59). So the test cannot prove a complaint rate. It can show zero complaints, zero abuse reports and at most one hard bounce, which is the stop rule I proposed in Round 1 and keep.
3. **The test must log inbox placement as well as replies, or a null result means nothing.** If the emails land in spam, "0 replies" measures the filter, not demand. Five seed sends to Gmail, Outlook.com and Yahoo inboxes the user controls, before the real sends, separate the two (estimate: about 1 hour, $0). This condition is part of my vote, because finance's and the skeptic's stop rules (go to A after 0 sales) rest on it.
4. **Refinements to my Round 1 conditions, each tied to named evidence:**
   - *Follow-ups are hand-approved too during the test.* In Round 1 I allowed automatic follow-ups after an approved first email. Ops' T8 (escalated leads still get the follow-up, reproduced in ADDENDUM-01B item 10) and the weekend unsubscribe gap (V53, confirmed) mean an automatic follow-up can reach someone who complained or asked to stop. That is a CAN-SPAM opt-out failure and the most likely complaint the system can produce. Until ops' `hold` status and the suppression fixes exist, the follow-up goes in the same digest as the first emails.
   - *The review time is longer than I said.* I wrote "about 2 minutes a day". The owner seat's arithmetic (about 8 seconds an email) and the skeptic's 1 to 2 minutes per pitch are right: a review that short is not a review. I withdraw "2 minutes a day" (see Q5).
   - *Withdrawn as a fact:* "Resend allows 150 emails on day 1 of warm-up" (V56, unverified). Restated as an estimate: 5 a day or fewer from a new domain during the test is conservative by ordinary warm-up practice. The argument does not depend on it, because the risk is per-message honesty, not volume.
   - *A permanent send error must not wedge the queue.* One permanent Resend error blocks every later send, every run (ADDENDUM-01B item 10, ops' T7). A suppressed or bounced address is exactly the kind that returns such an error. Per-item error handling is therefore a deliverability fix, not only a reliability one.

**Answers to the tally's Round 2 questions (section G):**

**Q1. Channel.** If no provider confirms in writing, I choose **D**: first contact in person, by phone or by postcard, and the preview link emailed only after the owner says "send it". That email is solicited, so it plausibly meets even Resend's terms, and complaint risk falls to near zero (estimate). I do not choose the user's own mailbox, for two reasons:
- *A Workspace mailbox is not a clean permission.* Google Workspace's AUP prohibits using it "to generate, distribute, publish or facilitate unsolicited mass email, promotions, advertisements, or other solicitations" (fact: V58). Whether 20 to 30 individually written emails count as "mass" is not settled by the text (V58).
- *A personal Gmail account has the worst blast radius on the table.* A suspended new business domain costs about $12. A suspended personal Google account takes the user's personal email, files and every service signed in with it (assumption: Google applies its spam rules to the whole account; not checked this session). This seat will not put that at risk for a $500 sale.
- The narrow exception I would accept: a dedicated mailbox on the new business domain, typed and sent by the user one email at a time, 5 a day or fewer, **and** a written answer from that mailbox provider (or the lawyer seat's reading of its terms) that this is not prohibited. Sent through the script's API, it is B, not an "ordinary mailbox", and B's rules apply.

**Does a written "yes" resolve my channel objection?** Yes for the terms objection, with two conditions. (a) The "yes" must come from the party that actually transmits the mail and must answer the exact use: about 5 individually written emails a day to restaurants' published business addresses, one email plus one follow-up, with an opt-out. (b) Outreach tools often send through a connected Workspace or Microsoft mailbox (assumption; no specific vendor checked). If so, that mailbox provider's terms bind too, and the tool's permission does not cure them. Even with a yes, the seed test, the count-based stop rule and the fixes in B still apply.

**Q2. Offer.** It depends on whether the item appears in the email.
- *Before the test:* anything the first email states. The outreach template lists `offer.includes` in the email body, including "Free hosting (no monthly fee)", and the follow-up repeats "no monthly fees" (fact: `templates/email/outreach.txt.j2`, `followup.txt.j2`). The hosting is not actually free at the configured volume (ADDENDUM-01A item 2). A promise in a commercial email that the sender cannot keep is a deception and complaint risk, so it must become true (a stated term) or be removed. Also before: no payment link and no `prefilled_email` in the first touch, and one link on the user's own domain (Round 1 condition 3). That also removes the public-payment-link problem the lawyer raised.
- *Before the test, for complaint reasons:* the competitor's targeting rule. Pitching a site to a restaurant that already has a Square, Slice or Toast site is an irrelevant pitch, and irrelevant pitches are what recipients mark as spam (estimate: professional heuristic, not measured). Excluding them costs nothing.
- *After the test:* price structure, care plan versus handover, and the menu-update path. These are outside my mandate. I defer to competitor, finance and owner on them, provided the email states only what is true.

**Q3. Supply count as a gate.** Yes, before any outreach. It sends nothing, so it costs this seat nothing, and it can do two of my Round 1 checks at the same time: record each lead's `email_source` and check that the domain has an MX record. My threshold is the test's own floor: **fewer than 20 sendable leads** in the reachable area means the 20 to 30 email test cannot run as specified, so go to D. A sendable lead has a published business address, a valid MX record, a recorded source, and no "no harvesting" notice where the address was found. That last condition is the lawyer's "aggravated violation" point. Where the line between D and A falls is finance's call, and I accept its thresholds (under 15 local and under 60 reachable).

**Q4. Automation.** Evidence that would make automatic first-touch sending acceptable to this seat, all of it required:
1. A written permission from the transmitting provider that covers automated cold sending, not only individually sent emails.
2. At least 100 hand-approved first-touch sends with zero spam complaints, zero abuse reports and hard bounces under 2%. The owner seat's 50 is too few for my seat: one complaint in 50 is still 2%.
3. Seed placement in the inbox at Gmail, Outlook.com and Yahoo, re-run monthly.
4. A working complaint signal for the largest group of recipients. Gmail and Workspace provide none at this volume (V55, V59).

Item 4 cannot be met at this scale. Item 2 cannot be met locally either, because finance estimates 8 to 48 pitchable leads (ESTIMATE, recomputed in ADDENDUM-01B). **So in practice: no automatic first-touch sending within the 3-month horizon, under any option.** Follow-ups may become automatic only after ops' `hold` status, suppression of `lost` addresses, bounce ingestion, and "skip sending if the inbox step failed" are built and tested.

**Q5. Honest minimum involvement under B** (estimates, built from my own and other seats' figures):
- Setup: about 45 minutes, plus about 30 minutes for SPF, DKIM and DMARC and the written question to the provider, plus about 1 hour for the seed test.
- Review: 20 to 30 emails and their previews at 1 to 2 minutes each, about 0.5 to 1.5 hours over 2 to 3 weeks. Follow-ups are reviewed the same way.
- Replies and unsubscribes: about 5 minutes on each sending weekday, about 1 hour in total.
- Total for the test: **about 3.5 to 5 hours over 2 to 3 weeks**, plus 1 to 2 hours per sale (finance's estimate). This is more than the tally's "1 to 3 hours", and the user should be told the larger figure before setup. Under the D fallback it is about 2 hours for the first 5 visits (tally), and more to scale.

## 2. Response to other members

| Member | Point | Agree / disagree | Why |
|---|---|---|---|
| skeptic | Automation adds little because the local list can be sent by hand in an afternoon | Agree | Finance's 8 to 48 lead estimate supports it, and from my seat a smaller list makes each complaint weigh more, not less. |
| skeptic | Send the test "from an ordinary mailbox in your real name, not through Resend" | Disagree | It moves the terms problem rather than solving it. Workspace's AUP bans "unsolicited mass email… or other solicitations" (V58), and a personal Gmail account puts the user's whole Google account at risk. The only version I accept is the narrow one in Q1. |
| ops | Fail closed, bind approval to the digest, per-item error handling, save state after sending | Agree | Each one also prevents a duplicate or unwanted email, which is my complaint risk. T7 (one permanent error blocks the queue) is a deliverability defect too, because suppressed addresses produce exactly those errors. |
| ops | Automatic sending after a fault-injected dry run plus two clean weeks of E | Disagree | The dry run sends to sinks, so it tests reliability, not how recipients react. Two weeks of E at 30 sends or fewer cannot show a complaint rate under 0.08%, since one complaint is over 3%. Ops' gate is necessary but not sufficient. See Q4. |
| finance | Lead supply, not sending capacity, is the binding limit; count it first for free | Agree | It costs no sends, and it can record email sources and MX checks for my conditions (Q3). |
| finance | 0 sales and fewer than 2 positive replies after 30 pitches leads to A | Agree, with a condition | Only if the seed test showed inbox placement. Otherwise the null result measures the spam filter, not demand (my Round 1 point on E1). |
| finance | 1 sale or 3 positive replies leads to C (automatic launch after fixes) | Disagree on the automatic part | A sale is evidence of demand, not of deliverability safety. It says nothing about complaints from the 29 who did not buy. |
| owner | 8 seconds an email is not a review; the sender must be verifiable (full name, phone, real site) | Agree | I withdraw my "2 minutes a day". A verifiable sender and a real website on the sending domain also lower filtering and spam reports (estimate). The owner's in-person preview test is the cleanest route for my seat, which is why D is my fallback. |
| lawyer | Never launch on payment alone; payment link off the public preview | Agree | It fits my "no payment link in the first touch" condition. One link on the user's own domain removes the Stripe link from both the email and the preview. |
| lawyer | Harvested addresses from sites with a no-harvesting notice are an aggravated violation | Agree | It is why I require `email_source` per lead and make it part of the "sendable" definition in Q3. |
| competitor | Exclude restaurants that already have a POS or ordering-vendor site; take down unsold previews | Agree | Irrelevant pitches drive spam reports, and previews left up on `*.netlify.app` keep the outreach visible with no end date. I would host previews on the user's own domain and delete them 30 days after last contact. |

## 3. Corrections accepted or disputed

- **ADDENDUM-01A item 1 (Resend bans cold outreach): accepted.** I read the live page in Round 1, and the verifier confirmed it from search results and the saved copy (V28, V57). It remains the deciding fact for my seat.
- **Item 2 (Netlify credits): accepted, with an unverified input** (ADDENDUM-01B item 12, V68). For my seat the conclusion holds either way: previews belong on the user's own domain, not `*.netlify.app`. That also lowers phishing-pattern filtering risk (estimate) and makes the first-touch email's "free hosting" line false unless it is changed (Q2).
- **Item 3 (public repository): accepted.** A public suppression list and outbox expose recipients' addresses to harvesting. State must move to private storage before any real address is stored there.
- **Item 4 (calendar-date trial; approval not tied to the digest): accepted.** It matches my Round 1 finding and ops' T1 to T3.
- **Item 5 (false lines in the email): accepted in full,** including (d), no advertisement disclosure (V19 confirms that "clear and conspicuous" identification is required).
- **ADDENDUM-01B item 10: accepted.** Bounces never read, `lost` not suppressed, no complaint events from Gmail and Workspace: these are my findings, reproduced independently. Escalated leads still getting follow-ups (ops) is why I now put follow-ups under approval.
- **Item 11 (crash re-send, trigger conditional): accepted as qualified.** For my seat a duplicate cold email is a likely complaint, so the idempotency key and the save-after-send are required whether or not runs start from fresh clones.
- **Item 17 / V56 (Resend's 150 emails on day 1 unverified): accepted.** I withdraw it as a fact (section 1, point 4).
- **V54: noted.** Whether Resend auto-suppresses hard bounces was not checked. Until it is, the script must not assume it.
- **Nothing disputed.**

## 4. What would reverse this vote

- **To D:** no transmitting provider answers yes in writing within about 2 weeks of asking; **or** the supply count finds fewer than 20 sendable leads (Q3); **or** the seed test lands in spam even in the one-link, own-domain format.
- **To A:** finance's supply thresholds fail (under 15 local and under 60 reachable) and the user will not spend time on D; **or** any spam complaint or abuse report during the test, after which I support stopping whatever the replies show (this matches the skeptic's rule).
- **To C:** if the council decides the targeting and hosting-term changes must come before the test. I already require the parts of C that appear in the email (Q2), so the difference between B and C for my seat is small, and I would not block C.
- **Nothing in the 3-month horizon moves this seat to E** (automatic first-touch sending). See Q4.

## 5. Dissent to record

None on the vote as such: B was the closest fit for three seats in Round 1. Three points from this seat must be carried unweakened into the recommendation **whatever option wins**, and I record them as dissent against any recommendation that drops them:

1. **"Permitted" means a written yes from the party that transmits the mail, for this exact use.** A cold-email tool's permission does not cure the terms of the Workspace or Microsoft mailbox it sends through. "The user's own mailbox" is not a permitted channel by default, and a personal Gmail account must never be used: its suspension costs the user far more than the business can earn.
2. **At local volume the complaint rate cannot be measured, so no automation gate may be written as a rate.** One complaint in 30 sends is 3.3% against a 0.08% limit, and Gmail and Workspace report no complaints at all. Any gate that "earns" automatic first-touch sending through a dry run, two clean weeks or one sale is measuring something other than recipient harm. Within 3 months locally, automatic first-touch sending should not be allowed.
3. **A test without seed placement checks cannot support "do nothing".** If the emails go to spam, silence looks like no demand. The recommendation's stop rule must require that the seed test showed inbox placement before a null result is read as a market result.
