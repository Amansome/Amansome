# ROUND 1: Unit-economics and finance (finance)

**Dossier:** DOSSIER-01-launch-sitehustle-as-built-after-fixes-c.md. **Addenda read:** none (I listed `council/` for `ADDENDUM-01*` when I wrote this, and there were none).
**Round 1, independent:** no other member's report was read before this one was written.

**Position:** Choose E (a capped, hand-approved test of 25 to 30 pitches) after a free supply count, and only once the offer's open-ended costs are capped. Reject B as built. The cash downside is small, but the expected profit is close to zero, and the offer carries obligations with no end date.
**Confidence:** medium

## 1. Position and why

1. **Cash risk is not the problem. Expected value is.** My estimate puts the cash at risk over 3 months at about $45 to $250 (table in §3), and one sale covers it. But in the local market the expected net over 3 months is about **-$55 to +$25** (low and mid-local scenarios). The chance of **zero sales is about 72%** in the mid-local case. A real profit (about $260 expected over 3 months, mid case) only appears if the user widens the area to reach about 70 pitches. Even then, P(zero sales) is still about 35%.
2. **The binding constraint is lead supply, not sending capacity.** At 15 emails per weekday the system can send about 945 emails in 3 months. My estimate of pitchable leads within 9 km (a weak site *and* a published business email) is **8 to 48, central about 22**. Automatic sending therefore adds almost nothing. It would use up the town in about 2 weeks, and the daily AI runs would then keep consuming plan usage on an empty pipeline. "Auto after a trial week" solves a problem the business does not have.
3. **The offer swaps a one-time payment for open-ended obligations.** Revenue is $500 once. Against it: "Free hosting (no monthly fee)" with no end date (F9), two edit rounds, DNS help, menu changes that must go through the agent forever (dossier §6), and no terms or refund policy (F8). The hosting's cash cost per site is tiny (about $0.20 a month in Netlify credits, §3). The real costs are the obligation to keep an account, a repository and an agent alive for every buyer indefinitely, and a hard credit cap on the free tier that can pause *every* site at once (§2, point 2).
4. **"Zero involvement" is not true on the money side.** Refunds, disputes, the $400 floor and the $75 edit rounds all need the user in the Stripe dashboard. The integration uses one fixed-price $500 Payment Link and a read-only key (F8, `claim_url`, README step 4), so the agent cannot issue refunds, discount or invoice. I estimate 1 to 2 user hours per sale plus 1 hour per dispute. In the mid-local case that is about 6 hours for about $25 of expected net, roughly $4 an hour before tax.
5. **My seat gains from a cheap, decisive measurement, not from a launch.** The test that matters costs under $100 in cash and about 3 hours of the user's time, and it yields the one number missing from the model (reply and close rate). Launching blind risks the domain, the user's local reputation and an open-ended support tail, for an expected profit near zero.
6. **On price:** keep a one-time build fee, but **cap the hosting and support term** (for example, 12 months of hosting plus small menu updates, then an optional yearly renewal, or a handover of the files). A pure monthly plan ($29 to $39) has a higher modelled lifetime value (about $490 to $780 at 5 to 8% monthly churn) but needs ongoing service and handling of failed card payments. That contradicts the user's goal, and the restaurant's free alternatives (Square Online's $0 plan, §3) put a ceiling on any monthly price. With scarce leads, revenue per lead matters more than volume, so an optional renewal adds yield without adding sends.

## 2. Where the dossier is wrong, incomplete or mis-posed

1. **The cost line for B ("about $20 + about $7/month") is incomplete.** It leaves out:
   - **The postal address.** The README says the law requires one. A USPS PO box costs about $31 to $170 per 6-month term depending on the post office's fee group (secondary sources, see §3), and 6 months is the minimum purchase. A virtual mailbox is an alternative (cost assumed, not checked).
   - **The Claude plan.** E4 is unmeasured, and AI run cost is a red line on my card. If the user already pays for a plan, the marginal cash cost is $0 but the runs share its usage limits. If the plan is bought for this, its monthly price counts in full. I did not check plan prices; I assume an entry plan on the order of $20 a month.
   - **Netlify beyond the free tier** (point 2), **Stripe fees** (W4 is listed but never netted against revenue), **refund and dispute losses**, and **who pays for a restaurant's domain** under "or help getting one" (F9).
2. **"Free hosting" rests on a capped free tier. I checked this against Netlify's public pricing and docs via web search.**
   - Netlify accounts created after Sep 4, 2025 are on credit-based plans. The Free plan gives 300 credits a month, and a production deploy costs 15 credits. That allows **20 production deploys a month** for the whole account, before bandwidth (20 credits per GB).
   - Third-party guides say the cap is hard: sites pause until the next month. Netlify's own documents did not confirm this in my search, so verify it.
   - I read the code: `cmd_deploy` POSTs a zip to `/sites/{id}/deploys`, which is a production deploy, not a draft. Every preview, every edit rebuild and every launch costs 15 credits.
   - At the configured pace (15 previews a day, about 315 a month) deploys alone would need about 4,700 to 7,100 credits a month, well beyond Pro's base 3,000. Even about 25 pitches a month needs about 560 credits, which means the $9 Personal plan.
   - On the free plan, preview churn could pause **paying customers' sites**.
   - Commercial use on the Free plan: Netlify's older launch post says it is allowed; the current terms were not read. The dossier marks this "not checked", and it is now partly checked.
3. **F10 cannot be carried out as built.** The only payment path is one fixed $500 Payment Link (F8, `claim_url`). The script has no way to charge $400 or $75. The agent would have to send a $500 link after agreeing to $400, or ask the user to make new links or enable promotion codes. `cmd_payments` also ignores refunds and disputes: a refunded lead stays `paid`, and its site stays live on the user's account.
4. **The capacity framing is mis-posed.** The options table and F3/F4 present the 15/day limit and auto mode as the main levers. E2 (supply) should be the headline question, because it caps revenue no matter how good conversion is.
5. **E1 and E3 have no numbers, and only the favourable claim (E3, "build-first converts better") is stated.** A null result is entirely possible with small samples (§3, reply-detection math), and the dossier should say so.
6. **Option E's time ("about 1 hour") looks low.** Properly checking 25 to 30 previews for wrong menus and prices at 2 to 3 minutes each, plus 45 minutes of setup and handling replies, comes to about 2.5 to 4 hours (estimate).
7. **No revenue target or hurdle rate is defined, so "worth it" cannot be judged.** I propose a hurdle: expected net of at least $25 per hour of the user's time, and at least 1 sale per 50 pitches.
8. **Tax:** the README's own line ("set aside about 25-30%") is advice written into the system, not a checked fact. Self-employment tax, federal and Pennsylvania income tax, any local earned-income tax, and whether PA sales tax applies to website design or hosting all need **a tax professional**. W5 (fictitious name registration) belongs to the lawyer's seat, but the fee is another uncounted setup cost.
9. **Missing option detail:** since the published-email requirement is the likely bottleneck (the discovery test collected no emails, dossier §2), D's phone or walk-in channel deserves a costed comparison. It reaches restaurants with no published email, at the price of the user's time.

## 3. Evidence

| Claim | Type | Source or method |
|---|---|---|
| Stripe US online card fee is 2.9% + $0.30; $500 sale nets $485.20 | fact | stripe.com/pricing (via web search, 2026-11-27); arithmetic |
| Stripe charges $15 per dispute received, plus $15 if countered manually (returned if won) | fact | Stripe pricing pages via web search; search results were mixed across regions, so confirm on the live page |
| Stripe keeps its processing fee on refunded charges | assumption (to verify) | My understanding of Stripe's refund policy; not checked this session |
| Netlify Free plan has 300 credits a month; production deploy costs 15 credits; bandwidth 20 credits/GB; Personal plan $9/mo for 1,000 credits; Pro $20/mo for 3,000 credits | fact | netlify.com/pricing and docs.netlify.com "how credits work" (via web search) |
| Free plan sites pause when credits run out | fact (secondary source; verify) | Third-party pricing guides found by web search; not confirmed on a Netlify page |
| Accounts created before Sep 4, 2025 stay on legacy plans | fact | Netlify docs (via web search) |
| Each preview, edit and launch is a production deploy (15 credits) | fact (code) + estimate | `scripts/hustle.py` `cmd_deploy` posts a zip to `/sites/{id}/deploys`; `cmd_launch` calls build and deploy again |
| One fixed $500 link; no path for $400 or $75; refunds and disputes not tracked | fact (code) | `hustle.py` `claim_url`, `cmd_payments` (no refund or dispute handling; grep for "refund", "dispute", "delete" finds nothing); `config.yaml` `offer`; README step 4 (read-only restricted key) |
| Square Online has a $0/month US plan (fees only on sales; no custom domain on the free plan) | fact | square.com US online-store plans page (via web search) |
| USPS PO box, size 1, costs about $31 to $170 per 6 months depending on fee group | fact (secondary sources) | thepricer.org and 2026 cost guides (via web search); check the Mechanicsburg post office's actual price |
| Pitchable local leads: 8 / 22 / 48 (low/mid/high) | estimate | Dossier E2's 100 to 200 independents × weak site 40 to 60% × published email 20 to 40% (shares assumed; discovery test found mostly no own site and no emails) |
| Send capacity is 945 in 3 months | estimate | 15/day × about 63 weekdays (`config.yaml`) |
| Close rate per pitched email: 0.5% / 1.5% / 4% | assumption | Bracketed from dossier E1 ("low single-digit" reply rates, fewer sales) |
| Effective net per sale is about $409 | estimate | 70% at $500 and 30% at $400 → $470 average; less Stripe fee → $456.07; less 10% refunded (fee not returned) and 2% disputed ($15) |
| 3-month expected net: low (10 pitches, 0.5%) -$55; mid-local (22, 1.5%) +$25; mid-expanded (70, 1.5%) +$259; high-expanded (150, 4%) +$2,203 | estimate | Expected sales × $409 minus cash cost ($75 / $110 / $170 / $250: domain $12 + PO box $31 to $60 + optional inbox $0 to $21 + Claude plan $0 to $60 + Netlify $0 to $60); script at `/tmp/claude-0/-home-user-Amansome/c705ec05-971c-5fbf-aeea-395a71965e0d/scratchpad/funnel.py` |
| P(zero sales) is 95% / 72% / 35% / about 0% in those scenarios | estimate | (1 - close rate)^pitches |
| With 25 pitches, P(zero replies) is 60% at a 2% reply rate, 28% at 5%, 7% at 10%; P(3 or more replies) is 1% / 13% / 46% | estimate | Binomial; same script |
| Monthly plan lifetime value: $29 at 5% churn ≈ $580; $39 at 5% ≈ $780; $39 at 8% ≈ $488 | estimate | Price / monthly churn; churn assumed |
| Hosting one launched site costs about 20 credits a month (≈ $0.20) | estimate | 2,000 visits × 0.5 MB ≈ 1 GB × 20 credits; $5 per 500-credit pack |
| User time per sale is 1 to 2 hours; per dispute 1 hour; trial review 2 to 3 minutes per pitch | assumption | DNS help (F9 needs the restaurant to change records), Stripe-dashboard actions only the user can take |
| Supply can be counted with no sends | fact (code) | `discover`, `upsert` and `build` work without Resend; only `send` needs it (`hustle.py`) |

## 4. Risks from this seat

- **A. Do nothing:** loses a small option value (my estimate: under about $300 expected over 3 months locally). This is a quiet loss, but a small one.
- **B. Launch as built:**
  - *Quiet risks:* (1) after about 2 weeks the AI runs keep consuming plan usage with no leads left. (2) Netlify credits run out mid-month and pause customers' sites, so the first sign is an angry buyer. (3) Refunded leads stay `paid` and their sites stay live. (4) Obligations build up with every sale and have no end date: hosting, edits and menu changes through an agent the user must keep paying for.
  - *Obvious risks:* disputes ($15 fee, plus the $500 if lost), which are more likely to be lost with no written terms (F8); and a promised $400 price the system cannot charge.
- **C. Launch after fixes:** the same supply ceiling applies. Fixes cut the tail risk but do not create leads, so expected value still depends on the area being widened.
- **D. Change the model:** a monthly plan means recurring revenue but also churn, failed-payment handling and ongoing service, which contradicts "zero involvement". A phone or walk-in channel means more of the user's time, but it may be the only way to reach the restaurants with no published email.
- **E. Small test:** the main risk is reading noise as signal. 25 pitches cannot tell a 1% close rate from a 3% one, so the decision rule must use replies as well as sales (§5).
- **Tax quiet risk:** income without estimated payments or a registered name. Refer to a professional.

## 5. The cheapest decisive step

**Step 1 (no sends, about $0 cash, no user time beyond what the AI usage costs):** run discovery and research on about 50 places within 9 km, plus one nearby expansion area. Count the leads that are both weak (score of 5 or less) and have a published business email. Record the AI usage for one full run, which settles E4.
- **Decided now:** if the count is **under 15 locally and under about 60 across all areas reachable in 3 months**, my position moves to **A, or D with a phone/walk-in channel**. The email channel cannot clear the hurdle at any plausible close rate (70 pitches × 1.5% ≈ 1 sale). If **40 or more locally** (or 120+ across areas), E as below.
- **Also decided now:** if one run uses enough plan usage that a dedicated plan would be needed, add its full monthly price to cost. If that pushes the mid-expanded case below $25 per user hour, I move to A or D.

**Step 2 (the test, E):** send 25 to 30 hand-approved pitches with a fixed offer: $500, with no $400 path unless a second link exists, and hosting capped at 12 months. Measure the reply rate, positive replies (asks about price or changes) and sales.
- **Decided now:**
  - At least 1 paid sale, **or** at least 3 positive replies → support **C**, with the area widened and the offer fixes in §6.
  - 0 sales and fewer than 2 positive replies after 30 pitches → **A**. Even if the true reply rate were about 2%, the close rate would be about 1% or less, and expected net stays under about $150 per 3 months even with expansion.

## 6. Conditions and red lines

**Must be true before I support any option that sends email:**
1. Hosting and support have an end date or a renewal price stated in the offer. No "free hosting" with no end date.
2. A one-page terms and refund policy is linked at checkout (it reduces dispute losses; the wording is for the lawyer's seat).
3. Every price the agent can quote has a payment path. Either drop the $400 floor and $75 rounds, or create the links or promotion codes in setup.
4. Netlify is sized to the plan: either a paid tier, or unconverted previews are deleted. Paying customers' sites must not share a capped free pool with previews.
5. All costs are counted in the decision: the Claude plan or its usage, the PO box, Netlify, Stripe fees and an allowance for refunds.
6. Daily runs stop or slow down once the lead pool is empty.
7. A tax professional is consulted on registration, self-employment tax, local taxes and any PA sales tax on services.

**Red lines (from my card):**
- A model whose costs, including the AI run costs, exceed its expected revenue. The mid-local case is already at about break-even.
- Auto mode switched on before any measured reply or close rate exists.

## 7. One line

Count the leads for free, then run a 25 to 30 pitch hand-approved test. The money at risk is small, but in this town expected profit is near zero, and as built the offer sells a $500 one-off with open-ended hosting and support.
