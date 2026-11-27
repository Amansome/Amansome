# ROUND 2: Competing local web designer / DIY builder (archetype) (competitor)

**Read:** ROUND1-TALLY.md, every ADDENDUM-01*, and all Round 1 reports.

**Vote:** C
**Changed from round 1:** no
**Confidence:** medium

*Seat interest, stated up front: this seat wins when SiteHustle's offer is weak. Option C makes SiteHustle a stronger rival to it than Option B would. I still vote C, because the council's job is the user's outcome.*

## 1. Vote and reason

**C: count supply, change the offer, then run the hand-approved test.** This is the same position as in Round 1. Then I wrote it as "D then E". The tally maps it to C. Every fix listed under Option B is also part of my vote. C adds three things to B, and none of them costs a single send:

1. **Leads can be pitched once, and there are few of them, so a test of a known-weak offer wastes them.** Each local restaurant can be pitched only once (skeptic §1.6; assumption, widely held, not measured). Finance estimates 8 to 48 pitchable local leads, central about 22 (estimate, finance §3). Finance's binomial math shows that with 25 pitches, P(zero replies) is about 60% at a 2% reply rate (estimate, finance §3; recomputed by the verifier, ADDENDUM-01B "disagreements"). So B's test will most likely return nothing. With the offer unchanged, nobody will know whether the cause was deliverability, demand, or an offer the council already judged weak. Changing the offer afterwards needs fresh leads, and the town will already be used up. Fixing the offer first is a text change to `config.yaml` `offer.includes` and to the terms page. B already requires that terms page. Sending a known-weak offer to all the leads that exist is the expensive order.
2. **The offer has three known weaknesses against the free and DIY options, and B fixes only part of one.**
   - *Hosting with no end date.* B's "stated hosting term" covers this.
   - *Updates.* Static HTML that only the agent can change, at $75 a round after two (fact: `templates/site/index.html.j2`; RUNBOOK §1; ADDENDUM-01A item 7). B does not touch this. Square Online's free plan lets the owner edit the menu for $0 a month (fact, V76 CONFIRMED).
   - *Google Business Profile.* The offer ignores it (owner seat; fact: grep finds no "Google Business" in the templates, runbook or config). Customers find hours there.

   The lawyer's own terms list also requires that "the restaurant is responsible for the accuracy of its menu and prices after launch" (lawyer §6.6). Under the as-is offer the restaurant has no means to change its own menu. B with those terms would sell the owner a responsibility the owner cannot carry out. A menu-update path closes that gap.
3. **The niche is unmeasured, and my Round 1 claim about it rests on an unverified report.** "Many top-scored leads already have Square/Slice/Toast sites" came from the dossier's discovery test. The verifier could not reach that test (V26 UNVERIFIED, no artifact). I accept that. The free count is exactly what settles it, and it can come out against the whole email test. Finance confirms it needs no sends: `discover`, `upsert` and `build` run without Resend (fact, finance §3). An hour of agent time can save the user the entire test.

**The changed offer I would accept** is finance's version, extended with my care plan or handover. Finance's version keeps the user's involvement lowest:
- $500 one-time.
- 12 months of hosting and routine menu, price and hours updates included, turned around in 2 business days with a human check.
- Setting up or correcting the Google Business Profile hours, phone and website link at launch.
- After 12 months, either an optional yearly renewal at a stated price, or a free handover of the files to the restaurant's own account.
- No "preview-" address on a paid site. No $400 or $75 prices unless they can be charged.

**Targeting:** places with no own site and no POS or ordering-vendor site. A vendor-linked place is pitched only if the pitch openly says the site complements its existing ordering page. The template already links out to `order_url` (fact: `templates/site/index.html.j2`).

**The vote is conditional.** If the supply count fails the gate in §G3 below, my vote becomes A, or D for no-email leads. It does not become B.

## 2. Response to other members

| Member | Point | Agree / disagree | Why |
|---|---|---|---|
| owner | The offer ignores the Google Business Profile; $75 per price change is unworkable; the paid site keeps a "preview-" address | Agree | These are the complaints my clients bring me after another designer's build. GBP is free and is where diners see hours (fact that it is free; share of discovery is an assumption). Including GBP in the offer is cheap. It is something POS site builders don't do for the owner, so it is a real advantage over the free options. |
| owner | Cheapest first test: show a preview on a phone to 5 owners in person and ask "$500 one-time, or lower plus monthly with updates?" | Agree, as an optional step inside C | It answers my offer question (handover or care plan) directly, with no email and no provider problem. Caveat from my own card: I overrate the relationship channel, so five conversations are a signal, not a measurement. |
| owner | An opener may cite "a Google reviewer called your rigatoni the best in the county" | Partly disagree | It is honest, but in a crowded inbox a review quote reads as a mail merge (assumption, market experience). The preview itself is the hook. Lead with what was built and why, and drop the compliment slot entirely. |
| skeptic | The whole local list can be sent by hand in an afternoon, so automation adds little | Agree | Same conclusion as finance's supply math. It is also why the offer matters more than the pipeline: with a tiny list, conversion per lead is the only lever. |
| skeptic | Send the test from the user's ordinary mailbox in their real name | Disagree as the default | Deliverability found that Google Workspace's AUP forbids "unsolicited mass email… or other solicitations" (fact, deliverability §3). Whether a handful of one-to-one emails counts as "mass" is ambiguous. A personal consumer mailbox selling a business service has the same ambiguity (assumption; I have not read those terms). If the channel is in doubt, in-person first (D) is cleaner than a grey-area mailbox. |
| skeptic | (Silent on the offer) | Disagree by omission | A hand-sent test of a weak offer still measures the weak offer. Sending by hand fixes risk, not fit. |
| deliverability | One link per first email, on the user's own domain; no payment link and no `prefilled_email` until the owner replies | Agree | This also removes my "preview-" objection. It cuts unsold previews out of the public Netlify account. It makes the pitch look less like the phishing pattern that I, as a competitor, would point at. |
| deliverability | Fixes only before the test; no new pricing model required | Disagree | See §1 point 1: the unchanged offer goes to all the single-use leads, and a null result can't be read. Changing the offer needs no new pricing *model*. It needs a stated term, an update path and a renewal-or-handover line in text. |
| lawyer | Never launch on payment alone; terms must state the hosting term, file handover and who keeps the menu accurate | Agree, and it supports C | The lawyer's terms list is most of my offer change written as a contract. Its "restaurant responsible for menu accuracy" clause is the point where B without an update path contradicts itself (§1 point 2). |
| ops | Previews as screenshots or one shared preview site, not one Netlify site per lead | Agree | It removes most of the Netlify credit exposure, whatever the outcome of V68. It also removes unsold previews that never come down (V71 CONFIRMED), which a rival could point to. |
| finance | Lead supply is the binding limit; cap hosting at 12 months with optional renewal or handover | Agree | This is the best form of my care-plan-or-handover condition, with the least user involvement. |
| finance | Pitchable local leads 8 / 22 / 48 | Likely optimistic for this offer | Finance counts weak site plus published email. My niche also excludes places with an existing vendor site, so the count that matters is smaller (assumption, resting partly on the unverified V26). The count settles it either way. |

## 3. Corrections accepted or disputed

- **ADDENDUM-01B item 15 (Slice's $1,000 implementation fee): accepted.** I left the fee out in Round 1. It cuts both ways. For a restaurant not on Slice, a Slice site costs $1,000 setup + $39/month + $3 per card order (fact, V77). SiteHustle's $500 compares well against that. For a pizzeria already on Slice, the fee is sunk, and a $500 front page competes with something it already paid for. So the vendor-site exclusion stands. Also accepted: the verifier did not see "website included" on Slice's pricing page (V77). That claim rests on slice.com/websites marketing via search and is downgraded to unverified.
- **ADDENDUM-01A item 2 and 01B item 12 (Netlify credits): accepted, with the V68 qualifier.** My estimate of about 4,700 credits a month (V69, arithmetic reproduced) depends on API zip deploys being billed as production deploys, which is unverified (V68). My offer objection does not depend on that number. "Free hosting, no end date" on a free tier is an open-ended obligation either way. Netlify's terms on charging clients for hosting on Free are not reached (V30), and pause-on-exhaustion is confirmed (V29).
- **ADDENDUM-01A item 7 (menu changes are specified: two rounds, then $75): accepted.** This is what I said in Round 1. The gap is not that the path is unspecified. The gap is that it is the worst path a restaurant could be offered.
- **V26 (discovery test unverified): accepted against my own Round 1 claim.** "Many top-scored leads already have vendor sites" is downgraded from reported fact to assumption until the count is run.
- **V76, V78, V79 confirmed my pricing of Square (free plan, no custom domain), Toast (90-day trial, then quoted) and Wix/Squarespace.** One correction: Squarespace's 2026 entry tier is Basic at about $19, not $16 (V79). The conclusion is unchanged: $500 one-time with 12 months included sits below a freelance build and around 1 to 2 years of a DIY builder plan.
- **V80 (freelance $1,500 to $6,000, care plans $30 to $300/month): remains an estimate from vendor blogs with an interest in the figures. Not disputed, not relied on for the vote.**

## 4. What would reverse this vote

- **To A:** the supply count finds that **2 or fewer of 30** nearby places fall in the niche (no own decent site, no POS or vendor site, a published business email). Or no hosting arrangement exists that keeps paid sites up for the stated term at under about $10 a month in total.
- **To D (in-person or phone first):** no email provider confirms in writing that this outreach is permitted. Or the count finds the niche exists but mostly has **no published email** (3 or more of 30 in the niche without an email, against 2 or fewer with one). Then email can't reach the market and only a human channel can.
- **To B (test the offer as is, after fixes):** evidence that owners prefer the as-is shape, for example 4 or 5 of the owner's 5 in-person conversations choosing "$500 one-time, no updates, no ongoing anything". That would show my care-plan premise is wrong for this town. That premise is an assumption from this seat's market experience.
- **Nothing in this round moves me to E** (automatic sending after a batch-count trial). See §G4.

## 5. Dissent to record

On the action, all seven seats agree: no launch as built, no date switch, at most a small hand-approved test. If the council chooses B, the closest-fit option of three seats, this seat dissents on the order of steps. Its strongest form:

> **Testing the unchanged offer spends the town's only leads on an offer the council already knows is weak, and the result cannot be read.** Local leads can be pitched once, and the council's own estimate is a few dozen at most (finance 8 to 48; skeptic 25 to 70 before excluding vendor sites). With 25 pitches, the most likely outcome is zero replies whatever the offer (finance: 60% at a 2% reply rate). The offer as written has no way for the owner to update the menu except paying $75 a round to an AI. It has no end date on hosting, and it ignores the Google Business Profile. Square gives restaurants a free, owner-editable site with ordering (V76). If B's test returns nothing, the user will not know whether the market, the spam folder or the offer failed. The leads needed to try a better offer will already have been used. Fixing the offer first costs no sends, only text, and B's own required terms page already has to say most of it. The lawyer's required clause "the restaurant is responsible for menu accuracy after launch" is unworkable without an update path. A free supply count first may show the email test should not run at all. **Count first, fix the offer, then send.**

## Answers to the tally's Round 2 questions (section G)

**G1. Channel.** If no email provider confirms in writing, choose **D (in-person or phone first, email only after the owner says "send it")**, not the user's own mailbox, and A if the user won't spend that time. The mailbox route rests on an ambiguous reading of Workspace's terms (deliverability §3), and a grey-area channel in the user's own town is a bad trade. From the market side, a preview shown on a phone is how this kind of local work is usually sold. My card warns that I overrate that channel, so I claim it as the cleaner channel, not the higher-converting one. A written "yes" from a provider **does** resolve the channel question for this seat. Channel was never my main objection. It does **not** resolve the offer objection.

**G2. Offer.** It must change **before** the test (§1 point 1, §5). Minimum change before sending:
- a stated term (12 months);
- included routine menu, price and hours updates during that term, or self-edit;
- an optional renewal at a stated price, or a free file handover, after the term;
- GBP hours and link checked at launch;
- no "preview-" address on a paid site;
- vendor-site leads excluded, or pitched explicitly as a complement.

Whether to run a monthly care plan or the renewal-or-handover version can be decided *after* the test, from what owners ask. Finance is right that a monthly plan adds involvement. The 12-month version is the default.

**G3. Supply count as a gate.** Yes, before any outreach. It is free and needs no sends. Method: 30 to 50 places within 9 km, by web search and Google listing, each sorted into (a) own decent site, (b) POS or vendor site, (c) no or broken site, no vendor site, published business email, and (d) as (c) but no email. Thresholds, set now:
- **(c) at 6 or more of 30 (20% or more)** → run the test on the changed offer.
- **(c) at 3 to 5 of 30** → run the test only with the area widened enough to reach about 25 niche pitches. Otherwise D.
- **(c) at 2 or fewer of 30** → A. If (d) is large instead, D.

These are compatible with finance's gate (under 15 local and under 60 reachable → A or D) and skeptic's (under 10 of 30 → by hand only). Mine is stricter because it excludes vendor sites.

**G4. Automation.** This seat has no principled objection to automation. Its objection is economic: automation has nothing to work on. Evidence that would make automatic first-touch sending worth having, all of it required:
1. A supply count showing roughly **150 or more** niche leads across areas the user will serve (estimate: enough to need more than about 10 weeks of hand-approved sending at 15 a week).
2. The hand-approved test meeting finance's bar (at least 1 sale or at least 3 positive replies), with zero factual errors in previews and zero complaints.
3. Ops's fault-injected dry run passed.

Even then I would tell the user plainly that the edge a small local seller has over Square and Wix is being a real, accountable person. Unreviewed AI first touches spend that edge. The safety side belongs to deliverability, lawyer and ops, and I defer to them on it.

**G5. The user's goal: honest minimum involvement under C.**
- Supply count: about 15 minutes to read the result. The agent does the work.
- Offer and terms decisions, plus the attorney and tax questions the lawyer lists: about 1 to 2 hours once, plus registration paperwork if a studio name is used.
- The test: about 2.5 to 4 hours over 2 to 3 weeks, checking every preview and approving every email (finance's estimate, which I accept).
- Per sale: 1 to 2 hours (finance's estimate), mostly DNS and launch checks.
- **Per customer per year: about 1 to 1.5 hours** checking menu and hours updates. This is an estimate: 3 to 6 change requests a year × 10 to 15 minutes each, with the change-frequency input an assumption.
- Incidents as they come.

This is a small service business with a light workload, not passive income. Any version that promises "receive payment only" will, within a year, hand this seat a client whose menu prices went stale on a site with "Site by <studio>" in the footer.
