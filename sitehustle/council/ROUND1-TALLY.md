# ROUND 1: tally and options

Written after all 7 voting members reported. Raw reports sit beside this file and are
the record; this file does not replace them. The options below are offered as options, with **no
claim that any one of them satisfies every member's conditions.**

## A. Corrections since the dossier

See ADDENDUM-01A. The ones that changed the picture:
- Item 1: Resend's acceptable-use policy prohibits cold outreach.
- Item 2: Netlify's free plan covers only about 20 production deploys a month and pauses every site on the account when credits run out.
- Item 3: the repository is public; the branch is already pushed; `leads.json` is still empty.
- Item 4: the trial is a calendar date; approval is not tied to the digest.
- Item 5: the email text has a hard-coded "I live nearby", first-person compliments from strangers' reviews, "one-time note" despite a follow-up, no ad disclosure, and "I was looking at your website" for leads without one.
- Item 6: previews contain invented default copy and third-party material.
- Item 7: the $400 and $75 prices cannot be charged; payment amounts are not checked.
- Items 8 and 9: Option B's cost is understated; the builder's "only account setup remains" is withdrawn.

The verifier's second pass (ADDENDUM-01B) checked 52 claims made in the Round 1 reports: 40 confirmed. It reproduced the reported code defects independently (item 10). It qualified the crash re-send (item 11) and the Netlify deploy-cost input (item 12). It corrected minor details: `config.yaml` is not on the runbook's commit list (item 13), the preview's structured data (item 14), Slice's $1,000 implementation fee (item 15), and a guidance date and PO box terms (item 16).

## B. Positions

| Seat | Weight | Position (own words, shortened) | Main reason | Key condition |
|---|---:|---|---|---|
| owner | 2 | "No to B, and no to automatic sending at any point in the first 3 months. At most E folded into D: a named local person approves every email by hand, after the fixes." | The email reads like a scam to the person pitched (made-up first-person compliment, "your website" for places without one, "preview" address after paying, $75 to change a price) | No fabricated claims; verifiable sender; terms; menu updates workable; every email human-approved |
| skeptic | 1 | "Do not launch as built, and do not promise yourself a hands-off business. At most E, sent by hand in your own name through a setup whose terms allow it. If nothing, stop." | "Zero involvement" is not true; the provider bans the use; a small local list can be sent by hand, so automation adds little and risks a lot | Never sold as zero-involvement; no date-based auto; honest minimum involvement written down |
| deliverability | 1 | "Do not launch B or C as designed. Only E: 20 to 30 first-touch emails, each approved by hand, through a channel whose terms permit it. A human approves every first-touch email for good." | Resend bans cold outreach (read the live policy); complaint thresholds can't be measured at this volume; a ban also kills customer email | A permitted channel confirmed in writing; SPF/DKIM/DMARC; one link on own domain; honesty fixes; bounce and unsubscribe handling |
| lawyer | 1 | "Do not launch as built. At most a small, hand-approved E, after five fixes. Automatic sending and AI negotiation with no review: opposed under every option." | Contract breach with the provider; false first-person claims; money taken with no terms; any stranger's payment can trigger a public site in a restaurant's name; data in a public repo | Permitted channel; no false claims; terms at checkout; never launch on payment alone; private data; counsel and tax pro before taking money |
| competitor | 1 | "Do not launch as built. Change the offer first (D), then a hand-approved test (E) aimed only at places with no site and no POS or ordering-vendor site." | The offer has no menu-update path and open-ended hosting; many top-scored leads already have Square/Slice/Toast sites | Stated hosting term or handover; a real menu-update path; exclude POS-site restaurants; previews taken down |
| ops | 1 | "Do not launch as built, and never use the date-based switch. Only a capped, hand-approved E after must-fix defects. Automatic sending only after a fault-injected dry run and two clean weeks of E." | Fails open (date switch, any non-`trial` mode sends); several duplicate-send paths; escalations don't stop follow-ups; no heartbeat; ten defects reproduced offline | Private state; fail-closed modes; digest-bound approval; duplicate guards; save state after send; per-item errors; hold status |
| finance | 1 | "Choose E (25 to 30 hand-approved pitches) after a free supply count, and only once the offer's open-ended costs are capped. Reject B." | Cash at risk is small (~$45 to $250) but expected net is about −$55 to +$25 over 3 months locally, with about a 72% chance of zero sales; lead supply (about 8 to 48 leads) is the binding limit | Capped hosting term; terms; every quoted price chargeable; Netlify sized; all costs counted |

Headcount: 7 of 7 reported. All 7 reject Option B (launch as built). Weighted: 8 of 8 reject B.

## C. Where the council agrees

**On the action (7 of 7):**
- Do not launch as built.
- Do not use the calendar-date switch to automatic sending.
- The most any seat supports now is a small (20 to 30 pitch) test with every outbound email approved by a human, after fixes.
- If the test produces nothing, do nothing.

**On the fixes, before any real email.** Each of these is named by at least four seats:
1. Do not send first-touch email through Resend as configured. Use a channel whose terms permit it (deliverability, lawyer, skeptic, ops by reference).
2. Remove the false or unverifiable first-person lines ("I live nearby", "my family loves…") and fix "one-time note" (all seven).
3. Keep lead data, outbox, sites and config out of the public repository (owner, skeptic, deliverability, lawyer, ops).
4. Give the offer a stated hosting term (or a handover) and a written terms and refund page at checkout (owner, skeptic, lawyer, competitor, finance).
5. Make every price the agent can quote chargeable, or remove the $400 and $75 rules (owner, skeptic, lawyer, ops, finance).
6. Tie approval to what the owner actually saw, and make the system fail closed (deliverability, ops, lawyer).

**On the reasons.** The seats agree on the action for different reasons:
- terms of service (deliverability, lawyer);
- honesty and trust (owner, skeptic, lawyer);
- reliability (ops);
- economics, because lead supply is small, so automation buys little (finance, skeptic);
- market fit (competitor).

**On the user's goal (7 of 7):** "zero involvement besides receiving payment" is not achievable as built. Several seats estimate the honest minimum: about 2 minutes a day approving sends while sending, 1 to 3 hours a month, 1 to 2 hours per sale, plus incident handling, registration and tax.

## D. Where it splits

1. **Will automatic sending ever be acceptable?**
   - *Never, or not in the first 3 months:* owner (never within 3 months; revisit only after 50+ clean hand-approved sends), lawyer (opposed under every option), skeptic (preference never; at most after a measured test and a set count of reviewed sends), deliverability (first-touch emails permanently human-approved; follow-ups may be automatic).
   - *Possible if earned:* ops (after a fault-injected dry run plus two clean weeks of E), finance (C after at least 1 sale or 3 positive replies in the test).
   - **Does the next action depend on it?** No. Every seat's next step is the same hand-approved test. It matters for what the user is promised long-term.

2. **Which channel carries the first contact?**
   - *Email through a provider that permits it, confirmed in writing:* deliverability, lawyer, ops, finance.
   - *The user's own ordinary mailbox, in their real name:* skeptic. The deliverability seat notes that Google Workspace's terms forbid "unsolicited mass email… or other solicitations", so a Workspace mailbox is not a clean alternative.
   - *In person first:* owner prefers showing a preview on a phone to 5 owners as the cheapest first test; skeptic suggests some walk-ins. Deliverability's fallback if no provider permits it is email only after first contact in person, by phone or postcard.
   - **Does the next action depend on it?** Yes. It decides whether the test can run by email at all. Round 2 question 1.

3. **Change the offer before the test, or test the offer as is (after the honesty fixes)?**
   - *Change first:* competitor (handover or a $25 to $50/month care plan with menu updates; exclude POS-site restaurants), finance (cap hosting at 12 months with optional renewal), owner (menu updates workable; no "preview" in the live address).
   - *Fixes only:* deliverability, lawyer, ops and skeptic name honesty, terms and safety fixes, and stated hosting terms, but do not require a new pricing model before testing.
   - **Does the next action depend on it?** Partly. It changes what the 20 to 30 test emails offer. Round 2 question 2.

4. **Count the supply before testing?**
   - *Yes, as a gate:* finance (under 15 local and under 60 reachable leads → A or D), competitor (6+ of 30 in the no-site, no-vendor group, else A or a human-led model), skeptic (under 10 of 30 → by-hand only).
   - *Not named as a gate:* owner, lawyer, deliverability and ops do not name it; it is compatible with their steps.
   - **Does the next action depend on it?** It could replace or postpone the test. Round 2 question 3.

5. **Hosting architecture.** Ops proposes screenshots or one shared preview site instead of one Netlify site per lead. Deliverability proposes previews on the user's own domain, with one link and no payment link until the owner replies. Lawyer wants the payment link off the public preview, and no launch on payment alone. These do not conflict, but they are not yet combined into one design.

## E. What each seat added

| Seat | A point no other seat made |
|---|---|
| owner | The pitch says "I was looking at your website" to places that have none; the paid site keeps a "preview-" address; menu-price changes at $75 each are unworkable for a restaurant; the offer ignores the Google Business Profile, where customers actually find hours |
| skeptic | The whole local list can be sent by hand in an afternoon, so automation adds little and can spoil every lead for good; "zero involvement" written in the README is itself the red line |
| deliverability | A Resend ban also cuts the digest, payment alerts and customer emails (single point of failure); Gmail/Workspace don't report complaints, so the threshold can't be monitored; one link on the user's own domain, with no payment link in first touch; a written provider answer as the deciding step |
| lawyer | Any stranger who reaches a preview can pay and trigger a public, indexable site and a "thank you for your payment" email in the restaurant's name; state deception law is not preempted by CAN-SPAM; PA fictitious-name consequences; the "© restaurant" footer |
| competitor | Many top-scored leads already have Square/Slice/Toast sites, so the real niche is "no site and no vendor site"; recurring care or handover is what restaurants actually buy; unsold previews never come down |
| ops | Ten reproduced defects, including: any mode other than `trial` sends; re-upsert regresses status and re-pitches; slug and id collisions mix restaurants; a crash before push re-sends a batch; escalated leads still get follow-ups; no heartbeat, so silence is ambiguous |
| finance | Funnel math: about 72% chance of zero sales locally; expected net near zero; lead supply of about 8 to 48 versus about 945 send slots, so automation solves a problem the business doesn't have; the user's hours per sale |

Every seat added something distinct. No seat is flagged.

## F. Options for Round 2

"Other" is always allowed.

- **A. Do nothing.** Backed in Round 1 as the fallback by owner, skeptic, competitor and finance if their gates fail, and as an outcome by all seven if the test produces nothing.
  - Cost: $0.
  - Main risk: forgoing a small, uncertain upside; the built system goes unused.

- **B. Fix, then a hand-approved email test.** Apply the shared fixes (section C):
  - a permitted sending channel, confirmed in writing;
  - honest email copy with an ad disclosure;
  - private state;
  - fail-closed modes, digest-bound approval and duplicate guards;
  - terms at checkout and a stated hosting term;
  - no launch on payment alone, and every quoted price chargeable.

  Then send 20 to 30 first-touch emails, each approved by the user, with decision thresholds fixed in advance. Automatic sending is not part of this option; whether it is ever allowed is decided only after the results.
  - Backed (closest fit) by: deliverability, lawyer, ops.
  - Cost: setup plus fix work; about 1 to 3 hours of the user's time over 2 to 3 weeks.
  - Main risk: no permitted provider may exist; low supply may make the test too small to read.

- **C. Count supply, change the offer, then test.** First, a free count of 30 to 50 nearby places by type (own decent site / POS or vendor site / no site with a published email). Then change the offer: a stated hosting term with handover or an optional renewal or care plan, and a real menu-update path. Target only the no-site, no-vendor niche. Then run B's test. If the count falls below the pre-declared thresholds, go to A or D instead.
  - Backed (closest fit) by: competitor, finance; skeptic's Step 0.
  - Cost: as B, plus 1 to 2 hours of agent time and offer redesign.
  - Main risk: delays any test; the redesigned offer is itself untested.

- **D. Human-first channel; email only after contact.** The strongest minority view. First contact is in person (showing a preview on a phone), by phone, or by a hand-sent message from the user's own name. Email follows only after a reply or meeting. Automatic first-touch email is never used. Start with 5 in-person conversations, as the cheapest test.
  - Backed (closest fit) by: owner; skeptic in part; deliverability as its fallback if no permitted provider exists.
  - Cost: the most user time (about 2 hours for 5 visits, more to scale).
  - Main risk: contradicts the user's stated goal of near-zero involvement; may still not sell.

- **E. The user's stated preference, with fixes.** Launch after all of section C's fixes, with a trial measured by a count of reviewed batches rather than a date, then automatic sending. No seat backed this in Round 1. It is listed so it can be voted on explicitly.
  - Cost: as B.
  - Main risk: unreviewed AI-written outreach in the user's own town; the provider terms problem returns at higher volume.

## G. Questions for Round 2

1. **Channel.** If no email provider confirms in writing that this use is permitted, which do you choose: D (human-first), the user's own mailbox, or A? And does a written "yes" from a provider resolve your channel objection?
2. **Offer.** Must the offer change (hosting term or handover, care plan, menu-update path, niche targeting) before the test, or after it?
3. **Supply count as a gate.** Should a free count of local leads come before any outreach? If so, what threshold sends the user to A or D?
4. **Automation.** Name the evidence, if any, that would ever make automatic first-touch sending acceptable to your seat.
5. **The user's goal.** What is the honest minimum involvement you would tell the user to expect under your chosen option?
