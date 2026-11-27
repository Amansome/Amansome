# ROUND 2: Unit-economics and finance (finance)

**Read:** ROUND1-TALLY.md, every ADDENDUM-01*, and all Round 1 reports.

**Vote:** C
**Changed from round 1:** no. ADDENDUM-01A items 1, 2 and 8 and ADDENDUM-01B item 12 changed my cost lines and my fallback if no sending channel is permitted (section 3). They did not change the option. My Round 1 position (count supply first, cap the offer's open-ended costs, then a hand-approved test) is the tally's option C.
**Confidence:** medium. I am confident about the order of steps (count, fix the offer, then test). I am not confident the test will be worth running once its fixed costs are counted.

## 1. Vote and reason

My card asks one thing: is this worth it in money and time? The corrections made the answer worse for email, not better. That is why the order of steps in C matters more to me now than it did in Round 1.

1. **The local lead list is the scarce asset, and each lead can be pitched only once.** I estimated 8 to 48 pitchable local leads, central about 22 (estimate, Round 1 §3; the verifier reproduced the arithmetic, V85; the inputs are assumptions). The competitor's niche filter ("no site and no POS or ordering-vendor site") shrinks that further (assumption: the discovery test found many Slice, Toast and order.online pages, dossier §2). A 20 to 30 pitch test is therefore not a sample of the local market. It is most of it. If option B tests the current offer and the offer is changed afterwards, the leads that saw the first version are spent: they cannot be pitched the improved offer without a second cold email. So C's "change the offer before the test" is a finance condition, not a matter of taste.
2. **Counting supply is free and can make every other cost unnecessary.** `discover`, `upsert` and `build` run without Resend (fact, `hustle.py`; Round 1 §3). B asks for a permitted provider, code fixes, terms, private state and counsel before anyone knows whether there are 5 qualifying leads or 40. If the count comes back too low, all of that work is wasted. C puts the $0 step first.
3. **The email test now loses money in cash terms unless its fixed costs are kept small.** Recomputed (estimate; script `scratchpad/r2.py`; same $409 net per sale as Round 1, now backed by V22, V81, V82):
   - 25 pitches yield 0.13, 0.38 or 1.0 expected sales at 0.5%, 1.5% or 4% close: about **$51, $153 or $409** expected revenue. P(zero sales) is 88%, 69% or 36%.
   - Cash cost of the test path: about **$28** at the low end (domain $12, a 3-month PO box from about $16 per V83, an existing Claude plan, trading under the user's own legal name, one shared preview site). About **$330** at the high end (a paid cold-email sender at an assumed $50 a month for 3 months, Netlify Personal at $9 a month per V67, a Claude plan bought for this at an assumed $20 a month, a larger post-office fee group). That excludes counsel and a fictitious-name filing.
   - My Round 1 mid-local case (+$25 over 3 months) becomes **-$35** with a sending tool at an assumed $20 a month, and **-$125** at $50 a month. I did not check any vendor's price; these sender costs are assumptions.
   - The test is therefore worth buying only as **information**, and only if it is kept cheap. I propose a cap of about $150 cash and about 4 hours of the user's time before the first positive reply (estimate; section 2 G5).
4. **Automation has almost no financial value at this scale.** The most hand review can cost is about 3 minutes per pitch (estimate). For 8, 22 or 48 leads that is 0.4, 1.1 or 2.4 hours, worth about $10, $28 or $60 at my $25-an-hour hurdle (estimate). Ops' fault-injected dry run alone costs more than that. Every seat now agrees on a hand-approved first stage, and my seat agrees for a reason the others do not give: there is no money in removing the human.
5. **I do not vote B because of what it leaves out, not because of what it includes.** B carries every fix I asked for (terms, a stated hosting term, chargeable prices). It has no supply gate, and it tests the current offer, which burns scarce leads on a version we already expect to change. I do not vote D as the main path because it costs the most user time against the user's stated goal. D is my named fallback (section 4).

**Conditions on this vote (carried from Round 1 §6, updated):**
- **Hosting architecture.** Use one shared preview site, or screenshots, instead of one Netlify site per lead (ops). Or put the previews on the user's own domain (deliverability). Either way, previews and paid sites must not share a capped free credit pool (ADDENDUM-01A item 2; 01B item 12).
- **Prices.** Every quoted price must be chargeable. The $400 floor and $75 rounds go (01A item 7).
- **Costs.** Stage the fixed costs behind evidence of demand (section 2, lawyer row).
- **Stopping.** Runs stop once the lead pool is empty.

## 2. Response to other members

| Member | Point | Agree / disagree | Why |
|---|---|---|---|
| deliverability | A Resend ban also cuts the digest, payment alerts and launch emails to paying customers | Agree. It is a cost I did not price in Round 1 | After a sale, losing the channel to the customer turns into refunds, and Stripe keeps its processing fee on refunds (fact, V82) plus $15 per dispute (fact, V81). The ban is a tail cost on revenue already earned, not only on outreach. |
| deliverability | Replace rate thresholds with counts (0 complaints, at most 1 hard bounce in 20 to 30 sends) | Agree | My Round 1 binomial makes the same point about replies: 25 pitches cannot tell 1% from 3% (estimate, V85). A decision rule on small numbers has to use counts. |
| deliverability, lawyer, ops | Fix, then test (option B) | Disagree on the order | Their fixes are right, and I require most of them. But B spends build time, provider fees and possibly counsel fees before a $0 count shows whether a market exists. It also tests the offer we already expect to change, using up leads that can each be pitched once (section 1, points 1 and 2). |
| ops | Screenshots or one shared preview site instead of one Netlify site per lead | Agree, and I adopt it | It removes my Netlify cost line. Whether or not the API deploy is billed at 15 credits (01B item 12, unverified), one site means at most a few deploys a month. It also removes the risk that previews exhaust the credits and pause paying customers' sites (01A item 2). |
| ops | Automatic sending after a fault-injected dry run plus two clean weeks of E | Disagree, on value rather than safety | At 8 to 48 local leads, automation saves at most about 0.4 to 2.4 hours (estimate). The dry run and fixes needed to earn it cost more than they save, unless the area grows to 150+ qualified leads. |
| owner | $75 per price change is unworkable; menu updates must be workable | Agree | These charges cannot be collected anyway (fact, 01A item 7: one fixed $500 link and a read-only key). Two included rounds plus uncollectable $75 rounds is a liability with no matching revenue. Including small text updates for a stated 12-month term costs agent time, not cash. |
| owner | Showing a preview on a phone to 5 owners in person is the cheapest first test | Partly agree | In person removes the published-email requirement, which is my binding supply limit. Estimate: at about 2.5 visits an hour and an assumed 2%, 5% or 10% close rate in person, gross value is about $20, $51 or $102 per user hour, against about $15, $44 or $117 for email before email's higher fixed costs. Owner's 5-visits-in-2-hours figure is its own estimate; the close rates are my assumptions. But it is the most user time and contradicts the user's goal, so it is my fallback, not my first step. |
| competitor | Target only the no-site, no-vendor-site niche; many top-scored leads already have Square, Slice or Toast | Agree | Square Online's $0 plan is confirmed (V76). A restaurant already on a vendor site is a low-probability close, and a pitch to it uses up a scarce lead. Filtering raises the close rate per pitch, which matters more than volume here. |
| competitor | A $25 to $50 a month care plan as the offer | Disagree as the default before the test | A care plan at $25 a month with an assumed 5% monthly churn has a lifetime value of about $500 (estimate). That is the same as the one-off fee, but it brings ongoing service, failed-card handling and an obligation without end, which is what the user does not want. Use a one-time fee with a stated 12-month term and an optional yearly renewal or a file handover. Let the test's replies decide whether owners want a care plan, which is competitor's own decision rule (its §5). |
| skeptic | Automation adds little because the whole local list can be sent by hand in an afternoon | Agree | This matches my supply-versus-capacity estimate: 945 send slots against 8 to 48 leads (estimate, V85). The skeptic's 0 to 1 sales from the whole local list (V86) matches my 72% chance of zero sales (mid-local). |
| skeptic | Send from the user's own ordinary mailbox in their real name | Disagree on the mailbox, agree on the real name | Google Workspace's acceptable-use policy forbids "unsolicited mass email ... or other solicitations" (fact, deliverability, fetched). It also puts the most valuable account at risk: the mailbox the agent reads, where payment alerts land, would become the single point of failure. The real name is the right call and saves money: it avoids the fictitious-name filing and the published advertisement (fact, V23, 01A item 8). |
| lawyer | A stranger's payment can trigger a launch; no terms at checkout | Agree | Every unauthorised launch costs at least the Stripe fee the refund does not return (fact, V82), plus $15 if it becomes a dispute (fact, V81). Written terms are the cheapest way to cut dispute losses. |
| lawyer | Consult Pennsylvania counsel and a tax professional before taking money | Agree on the trigger, and propose staging the cost | One hour of counsel (assumption: a few hundred dollars, not checked) is larger than the test's expected revenue in the low and mid cases. So pay for it after a first positive reply and before the first payment, as the lawyer's own condition 9 says ("before taking money"), not before the count or before drafting. |

## 3. Corrections accepted or disputed

- **01A item 1 (Resend bans cold outreach): accepted.** For my seat it adds a cost (a permitted sender, price assumed at $0 to $50 a month and not checked) or a channel change. Either way the cost of reaching each lead goes up. It also adds a tail risk to revenue after a sale (section 2, deliverability row).
- **01A item 2 and 01B item 12 (Netlify credits): accepted, with the qualifier.** My Round 1 claim that each API zip deploy is a production deploy was labelled "fact (code)". The verifier rightly marks the billing as unverified (V68). The decision does not depend on it: with one shared preview site the deploy count falls to a handful a month, so the free plan covers it whichever way Netlify bills.
- **01A item 7 ($400 and $75 cannot be charged; amounts not checked): accepted.** It supports my Round 1 §2 point 3. My $409 net per sale assumed 30% of sales at $400. If the $400 path is removed, net per sale rises to about $435 ($500 less the $14.80 Stripe fee, then 10% refunded with the fee kept by Stripe and 2% disputed at $15, the same method as Round 1; estimate). That is a small improvement, and it does not change the vote.
- **01A item 8 (Option B's cost understated): accepted.** It is the same finding as my Round 1 §2 point 1, confirmed by the verifier (V24), with the PA fictitious-name filing fee and advertisement added (V23, O12). Trading under the user's legal name avoids that cost.
- **01B item 16 / V83 (PO box minimum term): accepted.** USPS offers a 3-month term, so the PO box line for a 3-month test falls to about $16 to $85 (estimate: half my Round 1 6-month range, assuming roughly pro-rata pricing).
- **01B "finance funnel recomputed and holds" (V85): noted.** The arithmetic holds; the inputs remain assumptions. Nothing in Round 1 measured a reply or close rate, and nothing in Round 2 can either. Only the test can.
- **Not disputed:** none of the corrections is contested by this seat.

## 4. What would reverse this vote

- **To A (do nothing):** the supply count finds **4 or fewer** niche-qualified leads in a sample of 50 nearby places. "Niche-qualified" means a weak or absent site, no POS or ordering-vendor site, and a published business email. Four in 50 implies under about 15 locally (estimate: scaled to 100 to 200 places), and the email channel cannot clear my hurdle at any plausible close rate. The vote also moves to A if the user will not accept the time in section 2, question 5.
- **To D (human-first, capped at 5 in-person visits):** the same low count, **and** the user accepts about 2 hours. D also wins if no sending provider confirms in writing that this use is permitted. In-person contact is the only channel that reaches the leads with no published email.
- **To B (fix then test, no count):** evidence that supply is large enough that one test cannot use up a meaningful share of it, for example 120+ qualified leads across reachable areas. Then burning 25 leads on an imperfect offer costs little, and the count step adds delay without changing the decision.
- **Stop after the test (A):** 0 sales and fewer than 2 positive replies after 30 pitches, as in Round 1 §5. Or any formal complaint, which I adopt from the skeptic and deliverability seats, because its cost to the user's local reputation cannot be priced and has no upper bound.
- **Widen to C with expansion:** at least 1 paid sale, or 3 or more positive replies, **and** a count in one nearby expansion area showing at least 40 more qualified leads.

## 5. Dissent to record

My seat may be in the minority against B (deliverability, lawyer, ops) and D (owner, weight 2). Strongest form:

**"The local lead list is a fixed, non-renewable stock of perhaps 8 to 48 businesses, and each can be cold-pitched once. A 20 to 30 pitch test is not a sample of that market. It is most of the market. Any option that tests before counting the supply and fixing the offer may spend the whole asset on an offer the council already expects to change. That offer has open-ended hosting, uncollectable prices and no menu-update path. The leads it reaches cannot be re-pitched the corrected version. Counting costs $0 and no user time, and a low count makes every other cost (provider, code fixes, counsel, registration) unnecessary. At local scale and on cash terms the email test has an expected value between about -$125 and +$25, and is worth buying only as information. Information about the wrong offer is worth nothing. Count first, fix the offer, then test. If the count is low, the answer is A or a capped in-person D, and no software spending is justified."**

Two further points to carry, even if C is not adopted:
1. **Automation should not be presented to the user as a future goal.** At this supply it would save at most a couple of hours (estimate), whatever its safety.
2. **Stage the fixed costs.** No counsel, registration or paid sending tool before the supply count and the first positive reply. Counsel and registration are still required before the first payment is taken.

## Answers to the tally's Round 2 questions (section G)

1. **Channel.**
   - **No provider confirms in writing:** I choose D, capped at 5 in-person visits, if the user accepts about 2 hours; otherwise A. Not the user's own mailbox: the Workspace policy forbids it (fact, deliverability), and it puts at risk the mailbox the agent and payment alerts depend on.
   - **A provider confirms in writing:** a written "yes" removes my objection about ban risk, but not my cost objection. Its monthly price must be counted, and above an assumed $20 a month it turns the mid-local case negative (section 1, point 3). A $0 permitted channel, or one the user already pays for, keeps the test inside my cap.
2. **Offer.** Change it **before** the test, because the test uses up the leads it measures (section 1, point 1). The minimum changes:
   - a stated 12-month hosting term with a renewal price or a file handover;
   - the $400 and $75 rules removed, or made chargeable;
   - small menu and hours updates included for the term;
   - targeting limited to the no-site, no-vendor-site niche;
   - one shared preview site.

   A full care-plan redesign is not needed first. Ask about it in the test.
3. **Supply count as a gate.** Yes, first, at $0, with the AI usage of one full run recorded to settle E4. Thresholds in a sample of 50 places:
   - **4 or fewer** niche-qualified: A, or D if the user accepts the time.
   - **5 to 9:** a local test only, hand-sent, with no automation ever.
   - **10 or more** (20% or more, which matches the competitor's threshold): run the test, and count one expansion area before any talk of scale.
   - If one run's AI usage would need a plan bought only for this, add its full price to cost before deciding.
4. **Automation.** My seat does not object to automation in principle. It sees no return from it. It would need all three of the following, on top of the other seats' safety conditions:
   - a measured close rate of at least about 1 sale per 50 hand-approved pitches, over at least 50 pitches;
   - at least about 150 qualified leads reachable, so that automation saves more than about 7 hours of review (estimate);
   - a measured daily run cost below the review time it replaces.

   None of these can be met locally within 3 months (estimate).
5. **The user's goal: honest minimum involvement under C.** Estimates, assuming 0 to 1 sales:
   - account setup: 45 minutes (dossier);
   - reading the supply count and deciding: about 30 minutes;
   - deciding the offer terms: about 30 minutes;
   - checking 25 to 30 previews and emails at 2 to 3 minutes each: about 1 to 1.5 hours;
   - handling replies: about 1 hour;
   - per sale: 1 to 2 hours (DNS, the Stripe dashboard); per dispute: about 1 hour;
   - before the first payment: 1 to 3 hours for registration or a decision to trade under the legal name, and a tax professional.

   Total: **about 4 to 8 hours over 3 months.** After any sale add an obligation for the stated hosting term, which I estimate at 15 to 30 minutes a month per customer, plus incidents. "Zero involvement besides receiving payment" is not available under any option this council has offered.
