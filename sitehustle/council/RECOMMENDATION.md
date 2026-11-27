# RECOMMENDATION: Launch SiteHustle as built, after fixes, changed, or not at all

**Recommendation:** Do not switch SiteHustle on as built, or with automatic sending at any point in the next 3 months. Every seat accepts the same free first steps: count the local leads without contacting anyone, remove the false lines and the date-based auto-send switch, move the system to private storage, and ask an email provider for written permission. The next step then depends on the user's choice and the results. If the user will spend about 3 to 4 hours in person, show previews to 5 owners face to face. If not, run a hand-approved test of 20 to 30 emails on a corrected offer, and only if a provider says yes in writing. Otherwise do nothing.

**Council vote:** no option has a majority.
- B (fix, then a hand-approved email test): 3 of 7 seats, weighted 3 of 8.
- D (human first; email only after contact): 2 of 7, weighted 3 of 8.
- C (count supply, change the offer, then test): 2 of 7, weighted 2 of 8.
- A (do nothing) and E (the user's preference: launch after fixes, then automatic sending): 0 seats each.

**Dissent:** owner and skeptic (for D, against any email-first test); competitor and finance (for C, against testing the current offer); and three standing dissents carried whatever is chosen (deliverability, lawyer, ops; section 3).

**Confidence:** high that the system must not run as built (7 of 7 in both rounds, backed by reproduced defects and confirmed policy facts). Medium on which test comes next, because that depends on results nobody has yet: the supply count and a provider's written answer.

**Decision owner:** the user. The council is a simulation that advises; it does not decide.

## 1. What to do

**Step 1: the shared first steps.** Every seat's conditions allow these, and none sends anything or publishes a restaurant's details.
1. **Count the leads for free.** The agent researches 30 to 50 independent places within 9 km by web search and Google listing, with no contact. It sorts each into four groups:
   - own decent site;
   - POS or ordering-vendor site (Square, Toast, Slice, order.online);
   - no site or a broken one, no vendor site, and a published business email;
   - the same, but no published email.

   It records the source of every email address and any no-harvesting notice. Nothing is deployed and nothing goes into a public repository.
2. **Make the system safe to hold real data.**
   - Move SiteHustle and its state (`data/`, `outbox/`, `sites/`, `config.yaml`) out of the public profile repository into a private one.
   - Delete the date-based switch. Allow only `paused` and `trial`, with `paused` as the default.
   - Remove "I live nearby", first-person compliments, "one-time note" and "I was looking at your website" (for leads with no site), and the invented default copy.
3. **Ask for written permission.** Ask one email provider that would actually transmit the mail whether this exact use is permitted: about 5 individually written emails a day to restaurants' published business addresses, one email plus one follow-up, with an opt-out. Keep the answer.

**Step 2: choose the branch from the results.**

| Supply count (sample of 30) | User will spend about 3 to 4 hours in person | User will not |
|---|---|---|
| 2 or fewer in the "no site, no vendor site, published email" group (finance: 4 or fewer in 50) | D only if the "no email" group is large, otherwise A | A |
| 3 to 9 | D: show 5 previews in person | Email test (B/C) only with a written provider yes and a widened area; otherwise A |
| 10 or more | D first; email as a second channel only with a written yes | Email test on the corrected offer (C's order), with a written provider yes; otherwise A |

**Step 3: before any money changes hands, under any branch.**
- One-page terms and refund policy at checkout.
- A stated hosting term (12 months) with a renewal price or a file handover.
- No "preview" in a paid site's address.
- One chargeable price; remove the $400 floor and $75 rounds unless they can be charged.
- No launch on payment alone: the restaurant confirms from its published address.
- Paid sites kept off the free credit pool that previews use.
- The trading-name decision (and any PA fictitious-name filing), plus a tax professional's answer.

## 2. Why

1. **The system as built breaks its own sending provider's terms and is not free to host.**
   - Resend's acceptable-use policy prohibits "unsolicited messages of any kind, including cold outreach" (ADDENDUM-01A item 1).
   - Google Workspace's policy forbids unsolicited solicitations, so the user's own mailbox is not a clean substitute (V58; ROUND2-deliverability §1, ROUND2-lawyer §4).
   - Netlify's free plan allows about 20 production deploys a month and pauses every site on the account when credits run out. Paid customers' sites would share that pool (01A item 2; 01B item 12 notes one input is unverified).
2. **The system fails open and says untrue things in the user's name.**
   - Ten defects were reproduced independently (01B item 10). Among them: any mode other than `trial` sends, re-upserting a lead re-pitches it, escalated leads still get follow-ups, and any payer can trigger a launch.
   - The email templates hard-code a false "I live nearby", turn strangers' reviews into "my family loves…", and tell places with no website that someone looked at their website (01A item 5).
   - The repository that would hold the leads is public (01A item 3).
   - These are why all seven seats reject launching as built (ROUND1-TALLY §C).
3. **The market is small, so automation buys little and a mistake costs a lot.**
   - Finance estimates 8 to 48 pitchable local leads, against about 945 send slots in 3 months.
   - It estimates about a 72% chance of zero sales locally, and an expected net of about −$125 to +$25 over 3 months once a paid sending tool is counted (ROUND1-finance §1, ROUND2-finance §1; arithmetic verified, inputs are assumptions).
   - Each restaurant can be pitched once (skeptic, competitor).
   - Every seat concludes that "zero involvement besides receiving payment" is not achievable under any option. Their estimates of the honest minimum range from about 3 to 8 hours over 3 months for the test, plus 1 to 2 hours per sale and an ongoing obligation per customer (ROUND2 reports, question G5).

## 3. Dissent

| Seat | Dissent in its strongest form | What would prove it right |
|---|---|---|
| owner (weight 2), skeptic | The council agrees the business cannot be hands-off, yet B and C still choose the channel built for hands-off selling, which is the worst one for the customer. A cold email from a new domain with a free-hosting link and a payment link looks like phishing. With 25 sends, the chance of zero replies is about 60% at a 2% reply rate, and Gmail hides complaints, so silence can't be read. The best niche (no site, no vendor site) mostly publishes no email. Five face-to-face conversations cost the same 2 to 4 hours, need no provider permission, and always return five answers with reasons. If the user won't do that, the honest answer is A, not a fixed-up machine that keeps a false passive-income hope alive (ROUND2-owner §5, ROUND2-skeptic §5). | An email test with seed-verified inbox placement gets zero replies while in-person visits get interest. Or the count shows most niche leads have no published email. |
| competitor, finance | The local lead list is a fixed stock of perhaps 8 to 48 businesses, each pitchable once. A 20 to 30 pitch test is most of the market, not a sample of it. Testing before counting, and before fixing an offer the council already expects to change (open-ended hosting, uncollectable prices, no menu-update path, no Google Business Profile), spends the whole asset on the wrong offer. The lawyer's own required clause, "the restaurant is responsible for menu accuracy", can't be met without an update path. Count first, fix the offer, then send (ROUND2-competitor §5, ROUND2-finance §5). | The count shows few qualifying leads. Or test replies mostly ask "can I change it myself?" or "what does it cost later?" |
| deliverability (standing) | "Permitted" means a written yes from the party that actually transmits the mail, for this exact use. A tool's permission does not cure the terms of the mailbox it sends through, and a personal Gmail account must never be used. At local volume no automation gate can be written as a complaint rate (one in 30 is 41× Resend's limit, and Gmail reports none). A null email result supports "do nothing" only if seed tests first showed inbox placement (ROUND2-deliverability §5). | A seed test lands in spam, or a provider refuses. |
| lawyer (standing) | Do not pre-commit to automatic first-touch sending or AI negotiation as a later stage, however clean the test. Every automated message is a statement and an offer in the user's own legal name, and that liability can't be contracted away. Four kinds of false statement were written into this system by design and caught only by review. Price, refund and timeline replies stay human-approved permanently (ROUND2-lawyer §5). | Counsel reviews the templates and finds problems; or a factual error reaches a recipient. |
| ops (standing) | "Hand-approved" must mean bound and informed. Approval names specific item ids from a specific digest, shows each preview beside the source of every price, and acts on each message once; otherwise it is false assurance. Delete the date switch from the code: "we agreed not to use it" fails silently, a missing code path fails safely (ROUND2-ops §5). | A batch goes out that the user never saw. |

## 4. Risks and mitigations

| Risk | Who raised it | Likelihood / impact | Mitigation or early warning |
|---|---|---|---|
| Lead data, previews or the user's address published on the public GitHub profile | owner, skeptic, deliverability, lawyer, ops, verifier | High if nothing changes (the runbook commits daily) / high, irreversible | Move to a private repo before any real lead is stored (Step 1.2); `leads.json` is still empty today |
| Email provider account closed for cold outreach, also cutting customer and alert email | deliverability, skeptic, lawyer | High on Resend as configured / high | No first-touch email without a written yes; owner alerts on a separate solicited channel (ops G1) |
| A false or invented statement reaches a restaurant owner in the user's own town | owner, lawyer, skeptic | High as built / high, reputational | Template fixes; every first-touch email and preview reviewed beside its source; no AI free-text compliments |
| A stranger's payment launches a public site in a restaurant's name | lawyer | Low to medium / high | No payment link on previews; restaurant confirms before launch; amount checked |
| Free hosting pauses all sites, including paid ones | competitor, finance, ops, verifier | High at the configured volume / high for buyers | One shared preview site or screenshots; paid sites on a handover or separate paid account; stated hosting term |
| The test returns nothing that can be read (silence, spam folder) | finance, owner, deliverability | High: about 60% chance of zero replies from 25 sends at a 2% reply rate / wastes leads | Seed placement test before sending; in-person branch where possible; count before testing |
| The user's time far exceeds "zero involvement" | all seven | Certain / medium | State the honest minimum in writing before setup (section 2, point 3) |

## 5. Open questions

- **Channel (the deciding split).** In-person first (owner, skeptic) or a permitted email channel (deliverability, lawyer, ops)? Three of the email seats fall back to D if no provider confirms in writing, and none falls back to the user's own mailbox. It turns on the user's willingness to spend face-to-face time and on a provider's answer, neither of which the council has.
- **Offer before or after the test.** Competitor and finance say before; lawyer and ops say only the terms, hosting term and chargeable-price parts must come before, and the rest (care plan, update mechanism) after. The common floor is in Step 3.
- **Will automatic first-touch sending ever be allowed?** The action doesn't depend on this. Every seat sets conditions (about 150+ reachable leads, 50+ clean hand-approved sends, written permission, counsel sign-off, a passed fault-injected dry run). Several say these cannot be met locally within 3 months. It should not be presented to the user as a planned phase.
- **Unverified facts.** Whether Netlify bills API zip deploys as production deploys (V68); the discovery test's findings (V26); Netlify's terms on client hosting (V30); PA sales tax on website work (V31, for a tax professional).
- **Can the agent fetch menus reliably?** In this session, fetching restaurant sites was blocked (F16). If content can't be checked automatically, ops' threshold sends the build step to a human (D) or to A.

## 6. Next steps

| Step | Owner | Cost / time | Result that would change the decision |
|---|---|---|---|
| 1. Tell the council's facilitator whether you will spend about 3 to 4 hours on in-person visits | user | 1 minute | "No" removes D; then the email branch or A |
| 2. Move SiteHustle to a private repository; remove it from the public profile repo | user creates the repo; agent moves the files | about 10 minutes | none; a precondition for everything |
| 3. Free supply count of 30 to 50 nearby places, sorted into four groups with email sources | agent | about 1 to 2 hours of agent time, $0 | 2 or fewer of 30 in the target group → A (or D if many have no email); 10 or more → a test is worth running |
| 4. Code and template fixes: no date switch; fail closed; digest-bound approval; duplicate guards; hold status; honest copy; no payment link on previews; one shared preview site | agent | a few hours of agent work, $0 | any invented item in a 10-site spot-check against sources → content goes to a human (D) or A |
| 5. Ask one transmitting email provider in writing whether this exact use is allowed | user (the account holder) | about 30 minutes | No permitted provider → D or A; a yes allows the email branch |
| 6. Run the chosen test: 5 in-person visits (D), or 20 to 30 hand-approved emails after seed placement tests (B/C) | user, with the agent preparing everything | about 3 to 4 hours over 2 to 3 weeks | D: no owner asks for the price or the preview → A. Email: 0 sales and fewer than 2 positive replies after 30, with inbox placement shown → A. Any complaint → stop. At least 1 sale or 3 positive replies → continue, still human-approved |
| 7. Before the first payment: terms page, hosting term, chargeable price, trading-name decision, tax professional, optional one-hour attorney consult | user, with agent drafts | about 3 to 5 hours plus fees | an attorney or the tax answer advising against → A |

## 7. What changed during the session

**Corrections that mattered:**
- Resend's policy bans cold outreach (01A item 1; the dossier said "not checked").
- Netlify's free plan cannot carry the volume (01A item 2).
- The repository is public (01A item 3).
- The trial is a calendar date with unbound approval (01A item 4).
- The email text contains untrue statements (01A item 5).
- The builder's own position, that only account setup remained, was withdrawn (01A item 9).
- Ten code defects were reproduced independently (01B item 10).

**Votes that moved:**
- **skeptic: from E-by-hand to D.** Its Round 1 test, "send from an ordinary mailbox in your real name", was undercut by the deliverability seat's finding that Google Workspace's terms forbid unsolicited solicitations (V58), on top of Resend's ban.
- **lawyer:** withdrew the same mailbox fallback (V58). Its vote is unchanged.
- **deliverability:** withdrew "about 2 minutes a day" of review as too short to be real review, and made follow-ups hand-approved too (ops T8, V53).

No other vote moved.

## 8. Limits of this council

- **Simulated perspectives, not real stakeholders.** The owner seat's view is a hypothesis about restaurant owners, not evidence; 5 real conversations would test it. The legal points are issues flagged for a Pennsylvania attorney, not legal advice. Tax points go to a tax professional.
- **Conflict of interest.** The facilitator that wrote the dossier and ran the council is the same AI that built SiteHustle. The dossier labelled the builder's view as a position to test, and the verifier withdrew it, but readers should weigh that.
- **Parallel mode.** Each member was a separate subagent. All were the same underlying model, so their independence is limited even though Round 1 was isolated.
- **Unverified facts.** Some primary pages (Resend, Netlify, Google Workspace) could not be fetched by the verifier; the policy wording rests on search results plus one seat's saved copy, which match. One seat read the live Resend page. See section 5 for the remaining unverified items.
- **Missing seats.** No tax professional; no platform-policy seat for Netlify, Stripe or email providers; no diner or end-customer seat.
- **Real-world checks that should follow:**
  - the supply count (data);
  - a provider's written answer;
  - 5 owner conversations (customer interviews);
  - a one-hour attorney consult on templates and terms;
  - a tax professional on registration and sales tax.
