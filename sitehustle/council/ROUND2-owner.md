# ROUND 2: Independent restaurant owner (the customer pitched) (owner)

**Read:** ROUND1-TALLY.md, every ADDENDUM-01*, and all Round 1 reports.

**Vote:** D
**Changed from round 1:** no
**Confidence:** medium (high that in-person first is the right first contact for an owner like me; medium because it costs the user time they said they do not want to spend)

## 1. Vote and reason

**D: human-first contact; email only after a reply or a meeting; automatic first-touch email never used. Start with 5 in-person conversations.** I was the closest fit for D in Round 1, and nothing in the addenda or the other reports moved me off it. Several of them made it stronger. My vote carries three conditions:

- **Before anything is shown to an owner,** the honesty and data fixes in tally section C (items 2, 3 and 4) apply to the preview itself. That means: no invented copy (ADDENDUM-01A item 6), no "© {restaurant}" footer, no quoted Google or Yelp reviews, no hot-linked photos without permission, nothing committed to the public repository (item 3), and no payment link on the preview (lawyer).
- **The offer shown is honest about its open ends.** It states a hosting term, hands over the files, puts no "preview" in the live address, includes a workable menu-update path, and charges the price it states (section G2 below).
- **If the user will not do any in-person or phone contact at all,** my vote falls back to C (count, change the offer, then a hand-approved email test through a permitted provider). If no provider confirms in writing, it falls back to A. It does not fall back to B, because B tests an offer whose open ends I have already said I would refuse.

Why D, from the seat of the person being pitched:

1. **It is the only option that meets all three of my card's "would change my mind" conditions at the first contact.** My card asks that I see my own real menu and hours correct on the preview, that the sender is a verifiable local person, and that nothing is due until I am happy. A neighbour standing at my counter at 3 pm with my menu on their phone meets all three in one minute. A cold email from a days-old domain meets none of them at first touch. The From line is a first name and a studio name, with no surname and no phone number (fact: V87). Its first email carries a `*.netlify.app` link and a `buy.stripe.com` link with my address prefilled (fact: deliverability §3; `claim_url`). The deliverability seat calls that combination a phishing pattern (estimate, their professional heuristic). From my side of the counter, that is exactly what it looks like.
2. **The email test in options B and C will most likely return nothing that can be read.** With 25 pitches and a 2% reply rate, the chance of zero replies is about 60% (estimate: binomial, finance §3; I recomputed 0.98^25 = 0.60). At a 5% reply rate it is still about 28%. Gmail and Google Workspace do not report complaints to the sender (fact: V55, ADDENDUM-01B item 10). So a silent result cannot tell "owners don't want it" apart from "it went to spam" or "owners flagged it quietly" (deliverability §4). Five conversations always return five answers. They also return the reason: price, ownership, menu updates, "my nephew does it", "I'm on Slice". No email test at this size can deliver that.
3. **The niche the competitor and finance seats want to target is mostly reachable only in person or by phone.** The competitor seat says the real niche is places with no site and no POS or vendor site. The skeptic seat and finance seat both say the published business email is the bottleneck, and that Facebook-only places rarely publish one (estimates). The discovery test collected no emails (fact: dossier §2, not independently verified). Option C's targeting and its email channel therefore pull against each other: the best leads are the ones email cannot reach. D reaches them.
4. **The channel problem goes away instead of waiting on a provider.** Resend bans cold outreach (fact: ADDENDUM-01A item 1). Workspace's policy forbids "unsolicited ... solicitations" (fact: V58; whether one-to-one counts as "mass" is open). Once I have said "send me the link", the email is solicited, and the deliverability seat judges that Resend's terms would plausibly allow it (estimate, deliverability §2). D needs no written answer from a provider before it starts.
5. **In my town, a mistake made face to face can be recovered; a mistake by email spreads.** If the preview gets a price wrong, I can tell the person standing in front of me, and they fix it, and I think better of them. If the same wrong price arrives in a cold email with a made-up compliment, I tell other owners about "that fake website guy" (assumption, from my card's red lines and priorities). The skeptic seat makes the same point from the other side: each lead can be pitched only once.
6. **The first test costs the user about the same time under D as under B.** The tally prices D at about 2 hours for 5 visits. It prices B at 1 to 3 hours. The finance seat estimates an honest B or E test at 2.5 to 4 hours once every preview is checked (estimate, finance §2 item 6). The real difference is not the first test. D does not pretend the business will become hands-off later, and the other options leave that hope alive. All 7 seats already agree that "zero involvement" is not achievable as built (tally C).
7. **D can start before most of the email-side fixes are built.** B needs a permitted provider, fail-closed modes, approval tied to the digest and duplicate guards before the first data point. Those are real fixes, and I support them for any later email stage. But showing 5 honest previews on a phone needs only the content and data fixes in my first condition, terms before money, and a person.

## 2. Response to other members

| Member | Point | Agree / disagree | Why |
|---|---|---|---|
| deliverability | Resend bans cold outreach; a ban also cuts customer email; Gmail and Workspace do not report complaints; one link on the user's own domain; no payment link in the first touch | Agree | All checked (ADDENDUM-01A item 1; V55). One link on the user's own domain with no payment link is the minimum before any email reaches me, even after contact. |
| deliverability | A written "yes" from a provider resolves the channel, and permanent human approval of first touch costs "about 2 minutes a day" | Disagree in part | A written yes settles the contract problem, not the trust problem: a cold email with a link to a site built from my data is still a stranger's pitch. And 2 minutes for 15 emails is about 8 seconds each (estimate: README's 2 minutes ÷ 15). That is clicking, not checking my prices. The skeptic seat's 15 to 30 minutes a day is the honest figure. |
| lawyer | Any stranger who pays can trigger a public, indexable site in my restaurant's name; the "© {restaurant}" footer; quoted reviews; no terms | Agree, strongly | Confirmed by the verifier (V42, ADDENDUM-01A item 6). A diner or competitor paying to put a site up in my name, followed by a "Thank you for your payment!" email to me, is the scariest item in the whole record from my seat. |
| lawyer | Supports B (the hand-approved email test) | Disagree on the channel, not the fixes | The lawyer's own Round 1 report names the missing option as "the user sends a handful of pitches personally ... under their real name" and says it "removes the provider-terms problem and most of the misrepresentation risk". In-person contact goes further than that. The lawyer's fixes 2, 4, 5, 6 and 9 still apply to D, and fix 1 is not needed for the first contact. |
| competitor | Owners pay for someone who changes the specials and prices, not for the build; exclude places that already have a POS or vendor site; take unsold previews down | Agree | This matches what I said about menu updates at $75 a round (fact: V88). Unsold previews of my menu staying up forever is a red line for me ("my name ... used publicly without permission"). |
| competitor | Target only the no-site, no-vendor niche, by email | Disagree on the channel | That niche mostly does not publish an email (skeptic and finance estimates; discovery found none). Aiming email at it measures supply, not demand. The niche is a walk-in or phone list. |
| finance | Lead supply is the binding limit; about a 72% chance of zero sales locally; automation solves a problem the business doesn't have | Agree | It is the strongest economic case against automation, and it supports D: if there are about 22 leads (finance's central estimate), the user can meet most of them. |
| finance | Model assumes 30% of sales close at $400 | Disagree | The $400 path cannot be charged (fact: ADDENDUM-01A item 7). From my seat, being promised $400 and charged $500 is a complaint. Remove the rule rather than model it. |
| ops | Fails open; escalated leads still get the follow-up; no heartbeat; ten defects reproduced | Agree | Reproduced independently (ADDENDUM-01B item 10). A follow-up arriving after I have sent an angry reply is the most embarrassing failure for the user in my town (ops §1 item 3). |
| ops | Automatic sending possible after a fault-injected dry run and two clean weeks of the test | Disagree | A clean pipeline is not the same as accurate content. A spot-check of 10 sites against their sources is too small, and the agent checking itself is not the check I need. My bar is owner-confirmed accuracy (section G4). |
| skeptic | The local list can be sent by hand in an afternoon; "zero involvement" written in the README is itself the red line | Agree | That is the honest framing. The user is choosing between a small local service with real involvement and doing nothing. |
| skeptic | First touch by email from the user's own ordinary mailbox | Disagree in part | It is better than a new domain, because it carries a real name. But it is still a cold email to me, and the Workspace terms are not a clean permission (V58). The user lives here: walking in or calling is more trustworthy and avoids the terms question. |

## 3. Corrections accepted or disputed

All addendum items are accepted. None is disputed. The ones that bear on my seat:

- **01A item 5 (email text not true as sent): accepted.** It confirms my Round 1 points: the "I live nearby" line, the first-person compliment built from strangers' reviews, "one-time note" followed by a follow-up, and "I was looking at your website" sent to places that have none (V39, V40).
- **01A item 6 (invented copy and third-party material): accepted, and it adds to my case.** "Fresh, made-from-scratch food in the heart of {city}", "Made fresh, every day" and "Our story" are statements about my restaurant that I never made (fact: V7, O3). That hits my red line "a site that misstates their menu". It also carries onto the launched site, not only the preview (O6).
- **01A item 2 and 01B item 12 (Netlify credits): accepted, including the qualification.** Whether the script's API deploy is billed as a production deploy is unverified (V68). The rule that a Free account's projects pause when credits run out is confirmed (V29). For me the point stands either way: a "free hosting" site I paid for can go dark because previews for other restaurants used up the shared allowance. That answers my card's question "who fixes it next year?" badly. Correction to my own Round 1 report: I wrote that Netlify staff say reselling client hosting needs a paid plan. The record shows forum statements conflict and the terms were not found (V30). I accept that.
- **01A item 3 and 01B item 13 (public repository; `config.yaml`): accepted.** Nothing about me has leaked yet (`leads.json` is empty), so fixing it now costs nothing.
- **01A item 7 ($400 and $75 cannot be charged; amount not checked): accepted.** It confirms my Round 1 point 5.
- **01B item 14 (structured data `url` is null on the first build): accepted.** It is minor. The "© {restaurant}" footer and the quoted reviews remain.
- **01B item 15 (Slice has a $1,000 implementation fee): accepted.** It makes a $500 one-time site more attractive to a pizzeria that is not already on Slice. It does not help with pizzerias already on Slice, which have paid that fee and have a website.
- **My Round 1 claims checked by the verifier:** the website line (V39), the runbook rule against claiming to be a customer (V40), no surname or phone number in the sender line (V87), the menu-update path being specified at $75 a round (V88), no mention of the Google Business Profile (V89), and Square Online's free plan having no custom domain (V76). All were confirmed.

### Answers to the tally's Round 2 questions (section G)

**G1. Channel.** If no provider confirms in writing, I choose **D**. If the user will not do D, I choose **A**. I do not choose the user's own mailbox for first contact, because it is still a cold email to me and the Workspace terms are not a clean permission (V58). It is fine for the follow-up once I have asked for the link. **Does a written "yes" resolve my objection?** It resolves the contract objection only. My trust objection is about who first contacts me and how. With a written yes, I would accept a hand-approved email stage as a **second** step, after the 5 conversations and only if they show interest. The section C content and data fixes, one link on the user's domain, no payment link, and a real surname and phone number would all still apply.

**G2. Offer.** **The open-ended and misleading parts must change before the test.** Testing a known-bad offer wastes the few leads in town. That means:
- a stated hosting term with handover of the files, and what it costs after the term;
- no "preview" in the live address;
- a menu-update path, either a way for me to edit it myself or small updates included for the hosting term, instead of $75 for each price change;
- the price promised is the price charged (no $400 rule unless a real $400 link exists);
- one page of terms at checkout;
- something about the Google Business Profile, because that is where my customers find my hours (fact that the offer omits it: V89; that customers mostly look there is an assumption, my card).

**The pricing model can be chosen during the test.** The 5 conversations are the cheapest way to choose it: ask "$500 one time with 12 months of hosting and updates, or a lower price plus $X a month with updates?" That question can be asked face to face. A 25-email test cannot answer it.

**G3. Supply count as a gate.** **Yes, run it first.** It is free, sends nothing to anyone, and produces the list of places to visit. My thresholds are for my channel; I defer to finance's email thresholds (under 15 local leads means no email channel).
- **Fewer than 5 places within 9 km that have no site, or a broken one, and no POS or vendor site:** go to **A**. There is no one to show.
- **5 or more:** run D on them, whether or not they publish an email.
- **Record separately which ones publish an email.** Those are the only ones a later email stage could reach.

**G4. Automation.** No automatic **first-touch** email to owners like me within the 3-month horizon, under any evidence. I would revisit it only if all of these hold:
- **(a)** at least 50 hand-approved first-touch sends;
- **(b)** zero factual errors in previews, confirmed by the owners who replied, not by the agent;
- **(c)** zero complaints or angry replies;
- **(d)** at least one sale showing owners trust it at all;
- **(e)** a provider that permits it in writing;
- **(f)** the automatic email is limited to fixed, factual template text with no AI-written personal claims or compliments.

At about 22 local leads (finance's central estimate), (a) cannot be reached locally in 3 months. That is the point: automation has nothing to do here. Automatic follow-ups after an approved first email, and automatic transactional email to people who have paid, are acceptable to me once the ops seat's duplicate and escalation guards are in.

**G5. Honest minimum involvement under D.** Tell the user plainly that this is a small local service business, not passive income:
- **Before the visits:** about 15 to 30 minutes per preview to check it against the real menu, prices and hours (estimate: finance's 2 to 3 minutes per pitch is for a light check; a real menu line-by-line takes longer).
- **The visits:** about 2 hours for 5 visits, weekdays roughly 2 to 4 pm, between lunch and dinner (estimate, from my Round 1 report and the tally). Ask, don't sell. Leave a card with a full name and phone number.
- **One-time paperwork before taking money:** terms page, fictitious-name decision and filing if a studio name is used, and a tax professional's answer on PA sales tax. A few hours, plus filing and advertising fees (fact that these apply: V23, ADDENDUM-01A item 8; hours are an estimate).
- **Per sale:** 1 to 2 hours (finance's estimate), mostly the domain/DNS step and confirming the menu with the owner.
- **For the whole hosting term:** being the named person an owner calls when a price is wrong or the site is down. That is the part "zero involvement" hides, and it lasts as long as the hosting term promised.

## 4. What would reverse this vote

- **To A:**
  - the supply count finds fewer than 5 qualifying places within 9 km;
  - of the 5 conversations, none would pay at any price offered;
  - any owner treats the approach as a scam or complains;
  - or the user declines D and no provider confirms email in writing.
- **To C (count, change the offer, then a hand-approved email test):**
  - the user firmly declines any in-person or phone contact, but a provider confirms in writing and all my section 1 conditions hold;
  - or at least 2 of the 5 owners say they would pay and that a plain email from a named local person would have been fine for them. The email stage then becomes step 2.
- **To B (the email test with the current offer):** nothing I can foresee. It tests the open-ended hosting and the $75 menu changes that I would refuse as an owner.
- **To E (the user's preference with fixes):** nothing. Unreviewed AI-written outreach to my neighbours in the user's own town is my red line.

## 5. Dissent to record

This seat is in the minority (D, against B and C as the closest fits for five seats). Its argument in its strongest form:

**The council agrees that the business cannot be hands-off. B and C nonetheless choose the channel built for hands-off selling, and it is the worst channel for the customer.** The person being pitched decides whether anyone pays. For that person, trust comes from three things: their own menu shown correctly, a verifiable local sender, and nothing due until they are happy. Only face-to-face contact delivers all three at the first touch. A cold email from a new domain delivers none of them, and with a free-hosting link and a payment link it looks like phishing (deliverability's own estimate).

The email test is also likely to teach nothing:
- with 25 sends there is about a 60% chance of zero replies at a 2% reply rate (finance's binomial);
- Gmail and Workspace hide complaints (V55);
- the niche everyone wants, places with no site and no vendor site, mostly publishes no email.

So B and C would spend part of a small and unrepeatable list of local leads (each can be pitched once) on a channel that cannot reach the best of them and cannot tell silence from spam. They would also need to build a permitted provider, fail-closed modes and approval tied to the digest before the first data point.

D costs the user about the same 2 to 4 hours as the honest email test. It needs no provider permission, returns five real answers including the reason, can choose between one-time and monthly pricing, and risks the user's name in their own town only in conversations where a mistake can be fixed on the spot.

If the user will not spend those 2 hours face to face, the honest advice to them is A, not a cold-email test that keeps a passive-income hope alive. Every seat has already concluded that hope is false.
