# ROUND 2: Skeptic (argues for not doing it, or doing less) (skeptic)

**Read:** ROUND1-TALLY.md, every ADDENDUM-01* (01A, 01B), and all Round 1 reports (owner, skeptic, deliverability, lawyer, competitor, ops, finance). Consulted VERIFICATION.md (V28, V29, V30, V57, V58, V68, V86, V90). No ROUND2-* file of another member was read.

**Vote:** D
**Changed from round 1:** yes: ROUND1-deliverability.md §3 and §6 (Google Workspace's acceptable-use policy forbids using it to "generate, distribute ... unsolicited mass email, promotions, advertisements, or other solicitations", confirmed as V58), read together with ADDENDUM-01A item 1 (Resend bans cold outreach). In Round 1 my test was "send by hand from an ordinary mailbox in your real name". The deliverability report shows that the ordinary mailbox is not a clean channel either. That leaves first contact in person as the only route whose terms I can vouch for. I also take the lead filter from ROUND1-competitor.md §5 (no site and no vendor site).
**Confidence:** high that the tally's E (the user's preference) and anything that schedules automatic first-touch email must not run. Medium on D versus A. Low that D produces a sale.

## 1. Vote and reason

**What I vote for:** D, human first, in its smallest form. It has four steps:
1. **Free desk count.** The agent sorts 30 nearby places into: own decent site / POS or ordering-vendor site / no site and no vendor site. No outreach, about an hour of agent time.
2. **Build the previews privately.** The agent builds previews for 5 places from the third group. They are not deployed to a public `preview-*` URL and not committed to the public repo; a local file or an unguessable, unindexed link shown on a phone is enough.
3. **Check and visit.** The user checks each preview against the real menu, then walks into those 5 places between 2 and 4 pm and shows the preview on a phone. The user asks one question: "Would you pay $500 one-time for this, or would you rather pay less plus a monthly fee that covers menu changes?"
4. **Email only on request.** Email goes out only when an owner says "send it to me". That email is then solicited.

If the count fails, or the 5 visits produce nothing, the answer is A. If the user will not give about 3 to 4 hours, the answer is also A, and the user should hear that plainly rather than be offered a machine that pretends otherwise.

**Why D and not the tally's B (fix, then a hand-approved email test):**

1. **The fix list for B costs more than the test it enables.** These are estimates from counting. B needs every shared fix in tally §C: a new permitted provider with a written answer, private state, fail-closed modes, approval tied to the digest, duplicate guards, saving state right after sending, per-item error handling, a hold status, terms, a stated hosting term, no launch on payment alone, chargeable prices, and an honest template. That is ops' 7 must-fixes, the lawyer's 9 conditions and the deliverability seat's 8 conditions. Ten defects were reproduced independently (ADDENDUM-01B item 10, fact). All of that work buys **20 to 30 emails**, a number the user could write by hand in an afternoon (my Round 1 point, unchanged). D needs none of the sending, deploy or payment machinery until a real owner has said yes. Most of the ten defects drop out of the critical path because the code that has them is not run.
2. **No email channel is clean.**
   - Resend forbids this use outright (ADDENDUM-01A item 1, fact; I read the live page in Round 1).
   - Google Workspace forbids "unsolicited ... solicitations" (V58, fact). Whether one-to-one emails count as "mass" is unsettled, which the deliverability seat says honestly.
   - Personal Gmail's program policies also prohibit spam and unsolicited commercial mail (assumption: from memory, not checked this session).
   - Cold-outreach tools usually send through the user's own Gmail or Workspace mailbox (assumption, not checked for any vendor), so the mailbox terms come back.

   B's main risk is in the tally itself: "no permitted provider may exist." In D that question never arises, because the first touch is not email.
3. **At this volume, an email test cannot tell the user much. A conversation can.**
   - Finance's own binomial table: with 25 pitches at a 2% reply rate, P(zero replies) = 60% (fact that the arithmetic holds, per ADDENDUM-01B; inputs are estimates).
   - Deliverability: complaints from Gmail and Workspace recipients are invisible (V55, fact), and spam-folder placement makes silence look like no demand. Low replies would be ambiguous.
   - Five face-to-face answers to a direct price question tell the user why owners say no, not just that they did (estimate: qualitative, not a rate).
   - The owner seat, weighted 2 and the party being pitched, named this as the cheapest first test (ROUND1-owner.md §5).
4. **The user's own town is the asset at risk, and in person is the only channel where the user controls every word.**
   - There is no "I live nearby" template, no compliment invented from strangers' reviews, and no "one-time note" followed by a follow-up (ADDENDUM-01A item 5, fact).
   - A local person standing at the counter is the verifiable sender the owner card asks for.
   - The downside of a bad visit is one awkward conversation, not a spam report, a closed account or a forwarded screenshot.
5. **D is the only option that does not keep the false premise alive.**
   - The user's goal is "zero involvement besides receiving payment". All 7 seats agree it is not achievable as built (tally §C, 7 of 7).
   - B keeps "decide automation after the results" open, which tells the user the hands-off business is still on offer. With 8 to 48 pitchable local leads against about 945 send slots (finance, estimate), automation solves a problem this business does not have.
   - D says out loud what the business actually is: a local person selling websites. If the user does not want that business, the honest answer is A, and A costs $0 and nothing is irreversible.

**Conditions on my vote:**
- Previews stay out of the public repo, and nothing restaurant-specific sits at a guessable public URL.
- No money is taken before a one-page terms and refund page exists, with a stated hosting term or a handover.
- The user decides between trading under their own legal name and registering a fictitious name, and sees a tax professional before the first payment (lawyer's §6.9).
- The system's automatic first-touch sending is switched off, not merely postponed by date.

## 2. Response to other members

| Member | Point | Agree / disagree | Why |
|---|---|---|---|
| owner | Show one preview on a phone to 5 local owners in person, 2 to 4 pm; ask $500 one-time versus lower plus monthly (ROUND1-owner.md §5) | Agree. This is my vote | It is the cheapest test that settles the biggest unknown (will an owner pay at all, once the deception is gone). It needs no provider, and it gives the verifiable-sender condition for free. |
| owner | Revisit automatic sending only after 50+ hand-approved sends with zero errors and zero complaints | Agree with the bar; disagree that it is a live path | Finance estimates 8 to 48 pitchable local leads (estimate). The bar can likely never be reached locally inside 3 months, so the condition really means "never, here". The recommendation should say so rather than leave it looking like a step on a roadmap. |
| owner | "15 emails in 2 minutes a day is about 8 seconds an email, which is not checking" | Agree | It matches my Round 1 estimate of 15 to 30 minutes a day for a real review. Any option that relies on hand approval has to budget real minutes, or it is B with a rubber stamp. |
| deliverability | Google Workspace's AUP forbids unsolicited solicitations, so a Workspace mailbox is not a clean alternative | Agree. This changed my vote | It is confirmed (V58). My Round 1 "ordinary mailbox" channel rested on an unexamined assumption that a normal mailbox's terms allow cold pitching. They do not clearly allow it. |
| deliverability | A written "yes" from a provider resolves the channel objection and moves the seat to C with human approval | Disagree that it is sufficient | Terms are necessary, not sufficient. The seat's own finding is that complaints cannot be measured at this volume (Gmail and Workspace send no complaint events, V55). So even a permitted channel leaves the user unable to see reputation damage in their own town. Also (estimate): a written yes for "cold outreach to scraped addresses" from a mainstream transactional provider is unlikely, given Resend's explicit wording. |
| deliverability | Fallback if no provider permits it: email only after first contact in person, by phone or by postcard | Agree | This is D. I think it should be the starting point, not the fallback, for the reasons in §1. |
| ops | Ten reproduced defects; the system fails open and quietly | Agree | Reproduced by the verifier (ADDENDUM-01B item 10, fact). This is why D's "don't run that code until someone says yes" is safer than "fix it all first". |
| ops | Automatic sending after a fault-injected dry run plus two clean weeks of E | Disagree | Two weeks of E at 20 to 30 total sends is too few events to show reliability. The ops seat's own estimate puts the crash-before-push chance at about 2% per run (estimate). Clean weeks at this volume prove little, and once the town is used up, automation has nothing left to send. |
| finance | Lead supply (8 to 48) is the binding limit; P(zero sales) is about 72% locally; expected net about -$55 to +$25 over 3 months | Agree | It is consistent with my own wider estimate (25 to 70, V86, estimate with population from memory). I defer to finance's lower range for the email channel, because discovery collected no published emails. |
| finance | Finance's own §2.9: the published-email requirement is the likely bottleneck, and walk-in reaches restaurants with no published email | Agree; it supports D | In D the email filter disappears. The pool becomes "no site and no vendor site", which is larger than "weak site and published email" (estimate, from finance's own share assumptions). |
| finance | After 1 sale or 3 positive replies, support C (widen the area, then automate) | Disagree on the automation part | One sale means one owner liked it, not that a machine can sell it. Widening the area also breaks "I live nearby" and the local-trust advantage the test relied on. |
| competitor | The real niche is no site and no vendor site; many top-scored leads already have Square, Slice or Toast | Agree | It sharpens the desk count, and it decides which 5 places to visit. |
| competitor | A $25 to $50 a month care plan with menu updates | Disagree for this user | A care plan keeps the user on call for every price change for as long as the customer pays, the opposite of the user's goal. A **handover** (files and hosting moved to the restaurant's own account at launch) ends the user's liability, so my seat prefers it. The 5 visits can test which one owners want. |
| lawyer | Never launch on payment alone; terms at checkout; counsel and a tax professional before taking money | Agree | It is cheap, and it prevents the stranger-pays-and-publishes failure. D defers payment until after a conversation, which meets it naturally. |
| lawyer | Missing option: the user sends a handful of pitches personally from an ordinary mailbox, which "removes the provider-terms problem" | Disagree, as of the addenda | V58 shows Workspace's terms forbid solicitations, and personal Gmail's policies likely do too (assumption). The ordinary-mailbox route does not cleanly remove the terms problem. I held the same view in Round 1, and I now drop it. |

## 3. Corrections accepted or disputed

- **01A item 1 (Resend bans cold outreach):** accepted. I found and read it in Round 1. It rules out first-touch email through Resend under every option.
- **01A item 2 and 01B item 12 (Netlify credits; whether API deploys are billed as production is unverified):** accepted with the qualification. The free-plan rule (300 credits, pause on exhaustion) stands (V29). The per-deploy billing is open (V68). This does not affect D, which deploys nothing per lead before a yes. It also confirms my Round 1 point: "free hosting, no end date" on a shared, capped account cannot honestly be sold even once.
- **01A item 3 (repo public; branch pushed; `leads.json` empty):** accepted. I found it in Round 1. It means nothing about real restaurants should be written to that repository under any option.
- **01A item 4 (date-based trial; approval not tied to the digest):** accepted. It is the strongest single argument that "auto after a trial week" was never a trial.
- **01A items 5 and 6 (untrue email text; invented copy and third-party material in previews):** accepted. For D, the user checks each of the 5 previews against the real menu, and default marketing copy and review quotes are removed before showing.
- **01A item 7 ($400 and $75 cannot be charged; amounts not checked):** accepted. Under D there is one price per conversation, set by the user, not by an agent.
- **01A items 8 and 9 (Option B cost understated; the builder's "only setup remains" withdrawn):** accepted.
- **01B item 10 (ten defects reproduced):** accepted. 01B item 11 (crash re-send is conditional on a fresh clone): accepted as qualified. 01B item 13 (`config.yaml` not on the runbook's commit list): accepted. My Round 1 did not make that claim, and the substance (tracked, so exposed by a broad `git add`) stands.
- **V86 (my supply estimate uses population from memory):** accepted as an estimate. I do not rely on it. The desk count in §1 replaces it with a measurement.
- **Nothing disputed.**

## 4. What would reverse this vote

**Move to A (do nothing):**
- The user will not spend about 3 to 4 hours in total on the test. That covers about 15 minutes checking 5 previews, about 2 hours for 5 visits including driving, and replies and follow-up.
- Or the desk count finds **2 or fewer of 30** places in the no-site, no-vendor group (the competitor's threshold).
- Or the 5 visits produce **no owner** who asks for the price in writing, asks for the preview to be sent, or agrees to pay.
- Or any visit produces a complaint about how the preview used the restaurant's name or menu.

The stop rule is deliberately lopsided, and I say so openly. Five visits cannot tell a 10% interest rate from zero: at 10%, P(0 of 5) ≈ 59% (arithmetic). That is acceptable here because finance's estimate of the whole local upside is under about $300 over 3 months. A false "stop" costs little, and a false "go" costs the user's time and local name.

**Move to the tally's B (hand-approved email test), as a second channel after D, never instead of it:**
- A provider confirms **in writing** that one-to-one cold B2B pitches to published business addresses are permitted on the account used.
- And the user explicitly prefers email to visits.
- And the tally's shared fixes are done, with every first-touch email written or read in full by the user (15 to 30 minutes a day, not 2).

**Continue D beyond 5 visits (up to about 20 places):**
- At least 1 paid sale, or at least 2 of 5 owners asking for written terms or a price.
- Still human-first, with no automatic first-touch sending.

**Nothing on the table moves me to the tally's E.** No result does.

## 5. Dissent to record

I expect to be in the minority. The tally's B has the most closest-fit backers (deliverability, lawyer, ops). Stated in its strongest form, so the recommendation can carry it unweakened:

> The council is close to recommending that the user pay for a long list of fixes to a machine whose purpose is to remove the user, then use it to send 20 to 30 emails that could be written by hand in an afternoon, through a channel that may not legally or contractually exist. That puts the risk in the wrong place. The danger in this plan was never the volume; it was the machinery. It writes first-person claims in the user's name, publishes restaurants' names and menus at public addresses, takes money with no terms, and fails quietly. "Fix it, then test" keeps all of that on the critical path. It also keeps alive the idea that a hands-off business is waiting at the end, when every seat agrees that "zero involvement" is not achievable. Finance's numbers say the local market cannot support automation anyway: 8 to 48 leads against 945 send slots.
>
> The honest version of SiteHustle is a person who lives in Mechanicsburg walking into five restaurants with a preview on a phone. If the user will do that, it is the cheapest, safest and most informative test available. It needs no email provider, no public deploys, no payment machinery, and no fixes to code that has ten reproduced defects. If the user will not do that, the right answer is A. Do nothing; it costs $0 and nothing is irreversible. The user should not be offered a fixed-up machine as a way to avoid deciding whether they want to run this business at all.
>
> Specifically, the recommendation should not:
> - describe automatic first-touch sending as a later phase;
> - describe the user's involvement as minutes a day;
> - allow a single sale of "free hosting, no end date".

## G. Answers to the Round 2 questions

1. **Channel.**
   - If no provider confirms in writing, I choose **D**, and **A** if the user will not do D.
   - Not the user's own mailbox: V58 (Workspace) and, by assumption, personal Gmail's policies make it unclean, and I withdraw my Round 1 suggestion.
   - A written "yes" resolves only the *terms* part of my objection. It does not resolve the honesty part (fixable in the template), the reputation-blindness part (complaints from Gmail and Workspace recipients cannot be seen, V55), or the automation part. With a written yes, I accept email as a second channel after D, with every first-touch email read in full by the user.
2. **Offer.**
   - **The liability must change before any money is taken:** a stated hosting term, or (my preference) a handover to the restaurant's own account; a written terms and refund page; no "preview" in the live address; one price, set by the user. This is not optional, because a single sale of "free hosting, no end date" creates an open-ended obligation on a capped free account (01A item 2) for $500 once.
   - **The pricing model (one-time versus care plan) does not need redesigning before the test.** The 5 conversations are the test of it: ask both prices and record the answers.
   - Niche targeting (no site, no vendor site) applies before the test, because it picks who to visit.
3. **Supply count as a gate.**
   - **Yes,** a free desk count of 30 nearby places comes before any outreach. It costs agent time only and sends nothing.
   - **2 or fewer** of 30 in the no-site, no-vendor group: **A**.
   - **3 to 5:** D only, visit all of them, no email channel.
   - **6 or more:** D, with email as a later second channel only under the conditions in G1.
   - For any email route, fewer than 10 of 30 with a published business email (my Round 1 threshold, consistent with finance's "under 15 local") means email is not worth building for.
4. **Automation.**
   - My seat's honest answer: at this market size, **no evidence makes automatic first-touch sending worth it**, because the constraint is supply, not sending capacity (finance, estimate).
   - The evidence that would reopen it, all of it together:
     - a measured supply of **150+** reachable leads across areas the user can honestly describe themselves as local to;
     - a provider's written permission;
     - **50+** first-touch emails written or read in full by the user, with zero complaints and zero factual errors in previews (the owner's bar);
     - the ops seat's fault-injected dry run passed.
   - Even then, no first-person claims and no "I live nearby" outside the user's real town. My preference remains never within the 3-month horizon.
5. **The user's goal: honest minimum involvement under D.**
   - **Before the test:** about 15 minutes reviewing the desk count and choosing 5 places, and about 15 minutes checking 5 previews against real menus.
   - **The test:** about 2 hours for 5 visits including driving, plus about 15 minutes per owner who asks for the preview by email.
   - **Before the first payment:** a one-page terms page (1 to 2 hours with a template, or a lawyer's review), the trading-name decision and any fictitious-name filing, and a tax-professional consult (about 1 hour).
   - **Per sale:** 1 to 2 hours (DNS or handover, edits, payment) (estimate).
   - **Afterwards:** 1 to 3 hours a month while any customer is inside a hosting or support term, plus incidents (estimate).
   - **Total for the test:** about 3 to 4 hours over 2 weeks, plus about 3 to 5 hours of one-off setup if anyone pays.
   - This is a small part-time business, not passive income. The user should hear that in those words before anything is set up.
