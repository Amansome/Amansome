# ROUND 2: Small-business lawyer (flags issues only) (lawyer)

**Read:** ROUND1-TALLY.md, every ADDENDUM-01*, and all Round 1 reports.

**Vote:** B
**Changed from round 1:** no. My Round 1 position (a small hand-approved test after fixes; dossier letter "E") is the option the tally now letters B. ADDENDUM-01B and VERIFICATION V58 (Google Workspace's acceptable-use wording) do refine one point: I withdraw my Round 1 suggestion that "an ordinary mailbox under the user's real name" is a clean channel. That changes my fallback, not my vote.
**Confidence:** high that B is the most this seat can support now, and that automatic first-touch sending stays off. Medium on whether B can actually run, because that depends on a written answer from an email provider that nobody has asked for yet.

*This seat flags issues and does not give legal advice. Every item below is a question for a Pennsylvania-licensed attorney and, for tax, a tax professional.*

## 1. Vote and reason

**B: fix, then send a hand-approved email test of 20 to 30 pitches. Two conditions: the channel is confirmed in writing, and a fixed list of legal pre-conditions is met before the first email and before the first dollar.**

1. **Every one of my Round 1 blockers is now a confirmed fact, not a lead.**
   - The provider's terms forbid this use. Fact: ADDENDUM-01A item 1 (V28, V57). Sending through Resend breaches the user's contract with Resend from the first email.
   - The repository is public. Fact: ADDENDUM-01A item 3.
   - Any payer can mark a lead paid, and the runbook then launches it. Fact: ADDENDUM-01B item 10; V42, reproduced with a stranger's payer email.
   - The email makes false first-person statements: "I live nearby", "my family loves…", "one-time note", and "your website" sent to places that have none. Fact: ADDENDUM-01A item 5; V40, V41.
   - The previews publish invented marketing copy in the restaurant's name ("Fresh, made-from-scratch food…") and a "© {restaurant}" footer. Fact: ADDENDUM-01A item 6.

   The Round 1 checks moved none of these toward "fine". So nothing supports moving this seat toward E (automatic sending after a trial).

2. **B is the only lettered option that pairs sending with my pre-conditions.** Its fix list covers four of my five Round 1 must-haves:
   - a permitted channel;
   - honest copy with an ad disclosure;
   - private state;
   - terms at checkout and no launch on payment alone.

   It also leaves the automation question closed until results exist. That is the right order for exposure that sits with one named person. Under CAN-SPAM the promoted business is liable and "can't contract away" the duty (fact: V61). Here the user is both sender and promoted business.

3. **Why B over A.** A handful of carefully reviewed, permitted, honest emails, with written terms, carries low legal exposure. That is an estimate: complaints and claims scale with the number of unreviewed statements, and B caps both. On those facts I cannot justify A on legal grounds alone. If the channel condition fails, A or D becomes right (section 4).

4. **Why B over C.** I do not object to C. A supply count publishes nothing and sends nothing, and I would accept C as a close second. I vote B because nothing in C's offer redesign is a legal pre-condition, beyond the terms and hosting-term fixes that B already contains. Care plans and niche targeting are market questions, and I defer to competitor and finance on them.

5. **What B must include from this seat.** These are additions or sharpenings of the tally's fix list. Without them my vote does not hold.
   - **Channel.**
     - Get a written answer from the provider that describes this exact use, and keep it on file.
     - A support email is evidence of good faith. It probably does not amend the published policy (assumption; ask counsel). If the provider's written policy says no, a friendly support reply does not cure it.
   - **No launch on payment alone.**
     - Take the payment link out of the public preview and out of the first email.
     - Send it only after the owner replies from the restaurant's published address.
     - Before `launch`, record the restaurant's written confirmation, from that address, of the content and terms.
   - **Terms at checkout, linked and accepted.** They cover:
     - what is delivered;
     - who owns the site and files;
     - the hosting term and what happens at its end, including handover of files;
     - edit rounds;
     - that the restaurant is responsible for the accuracy of its menu and prices after launch;
     - refund conditions;
     - no guarantee of business results;
     - a liability cap.
   - **The offer in the email must match the terms.** The first email is the offer. It says "it's yours", lists "Free hosting (no monthly fee)" and links to payment (fact: `templates/email/outreach.txt.j2`, `config.yaml` `offer.includes`). Whatever hosting term the terms page states must appear in the email too.
   - **Previews carry nothing the restaurant didn't publish.**
     - No invented default copy (ADDENDUM-01A item 6).
     - No "© {restaurant}" footer.
     - No JSON-LD naming the preview URL as the restaurant's URL. V75 says this appears only on rebuilds after deploy, but rebuilds happen.
     - No hot-linked photos without permission (V66: hot-linking is not a safe harbour outside the 9th Circuit; Third Circuit not checked).
     - No quoted Google or Yelp reviews.
     - A takedown date for unsold previews.
   - **Email sources recorded.** Record where each address came from, and skip sites that carry a no-harvesting or no-solicitation notice. Harvesting from such sites is an aggravating practice that compounds damages (fact: V62, 15 U.S.C. § 7704(b)(1)).
   - **Every reply that states a price, promise, timeline or refund is approved by the user before it goes.** Drop the $400 and $75 rules unless a real link exists (ADDENDUM-01A item 7).
   - **Before taking money:**
     - decide whether to trade under the user's legal name or a studio name;
     - if a studio name, file the fictitious-name registration, including the § 311(g) advertisement for an individual (V23, V64);
     - get a tax professional's answer on PA sales tax (V31).
   - **Opt-outs.** They must be honoured within 10 business days even if the agent run stops. Ops' heartbeat, or a manual weekly inbox check by the user during the test, covers this.

## 2. Response to other members

| Member | Point | Agree / disagree | Why |
|---|---|---|---|
| skeptic | Send by hand from the user's own ordinary mailbox, in their real name; that sidesteps the provider problem | **Disagree on the channel; agree on by-hand** | I made the same suggestion in Round 1 and I withdraw it. Google Workspace's policy forbids using it to "distribute… unsolicited mass email, promotions, advertisements, or other solicitations" (fact: V58). Whether 20 to 30 one-to-one emails are "mass" is not settled by the text (V58). Consumer Gmail's own program policies I have not checked (unknown). The user's personal account is also the one the agent reads, so a suspension would take down the user's personal email, a worse single point of failure than Resend (assumption about suspension scope). Separately, sending by hand does not switch off CAN-SPAM. Each commercial email still needs the ad disclosure, a postal address and a working opt-out, whatever the volume (fact: W1). |
| skeptic | "Zero involvement" as written is itself the red line | **Agree** | From this seat it is also a liability point. The user cannot hand the legal duty to the agent (V61), so the README line "your only job is getting paid" misdescribes who carries the risk. |
| deliverability | A written provider answer is the deciding step; first-touch email stays human-approved permanently | **Agree** | This is the same deciding step as my Round 1 §5. A "yes" settles the contract question only (section G1 below). |
| deliverability | One link on the user's own domain; no payment link and no `prefilled_email` in first touch | **Agree, strongly** | This also cures most of my third-party-payment and data-exposure points (V42; V8 `prefilled_email`). A payment link that reaches a restaurant only after its owner replies cannot be used by a diner or prankster to launch a site. |
| deliverability | Follow-ups may be automatic once the first email was approved | **Partly agree** | Acceptable to this seat on four conditions: the follow-up is a fixed template with no new AI-written claims; it is suppressed by any reply, unsubscribe, bounce or escalation; ops' `hold` status exists, since today an escalated lead still gets its follow-up (fact: ADDENDUM-01B item 10, T8); and the "one-time note" line is gone. Without the `hold` fix, an automatic follow-up to someone who sent a legal threat or a refund demand is the worst single message this system can send. |
| ops | Automatic sending can be earned by a fault-injected dry run plus two clean weeks of the test | **Disagree in part** | A dry run tests reliability, not legality. It can show no duplicates and alerts on faults. It cannot show that unreviewed AI-written statements in the user's name are true or non-deceptive. Ops' own pass criterion found that menus can't be checked without fetching sources (F16). I need different evidence (section G4). I agree fully with ops' must-fix list (private state, fail-closed modes, digest-bound approval, `hold`). |
| owner | The sender must be verifiable: full name, phone, real presence | **Agree** | It also matters legally. Header and "from" information must not mislead (W1), and a studio name means a fictitious-name filing that ties the studio to the person (V23). A full name in every email is the cheapest way to meet both. |
| owner | Open with a named public review ("a Google reviewer called your rigatoni…") instead of a first-person claim | **Agree, with a limit** | In an email, a short, accurate, attributed paraphrase is low risk. Republishing review text on the preview site is a different act. Google's and Yelp's terms on reusing review content I have not checked (unknown). Keep reviews out of the preview. |
| competitor | Change the offer to a handover, or a disclosed care plan | **Agree it is cleaner; flag a tax consequence** | A handover ends the open-ended hosting obligation, which is my Round 1 §1.5 concern. But PA Revenue guidance, as summarised by secondary sources, treats website development as taxable when the site is transferred to the customer and not taxable when the developer keeps control; separately stated hosting is not taxable (fact that the guidance reads this way: V31, V65; application to this offer is unresolved). So "handover" versus "we host for 12 months" may decide whether 6% sales tax applies. That is for the tax professional before the offer is fixed. |
| competitor | Take down unsold previews after a set period | **Agree** | A page in a restaurant's name that the restaurant never agreed to should have a short, stated life. Today none of them is ever removed (fact: competitor's code check, ADDENDUM-01A item 6 context). |
| finance | Cap hosting at 12 months with an optional renewal | **Agree, with one flag** | A stated term is what my terms page needs. Make renewal opt-in, not automatic: some states regulate automatic renewals. Whether Pennsylvania does for a B2B sale like this, I did not check (unknown; ask counsel). |

## 3. Corrections accepted or disputed

| Item | This seat's Round 1 claim | Correction | Accepted? |
|---|---|---|---|
| ADDENDUM-01A item 1 (V28, V57) | Resend's AUP bans cold outreach (I had only a search result) | Confirmed from the live page and a saved copy | **Accepted.** My contract-breach point now rests on a fact. |
| ADDENDUM-01A item 3, 01B item 13 | Repo public; runbook pushes data daily | Confirmed. `config.yaml` is tracked but not on the runbook's commit list | **Accepted.** Exposure of the user's own address is conditional, but one broad `git add` triggers it. Fix stands. |
| ADDENDUM-01A item 6 | Previews publish material the restaurant never authorised | Adds invented default copy, and robots.txt stops Google seeing `noindex`, so a linked URL can be indexed | **Accepted, and it makes my point stronger.** Invented claims about a restaurant's food are published in its name. The "noindex = private" premise is weaker than I said. |
| ADDENDUM-01B item 10 (V42) | Any payer triggers a launch | Confirmed. Qualifier: launch is an agent step per RUNBOOK §2, not automatic in the script | **Accepted.** The qualifier does not help: the runbook tells the agent to launch "each newly paid lead". |
| ADDENDUM-01B item 14 (V75) | JSON-LD names the preview URL as the restaurant's URL | `url` is `null` on first build; preview URL appears on rebuilds after deploy and on the final build | **Accepted as a correction of detail.** The fix (no JSON-LD on previews) still applies. |
| V63 | § 7707(b) leaves state deception law un-preempted | Confirmed, but *Omega World Travel* reads the carve-out narrowly (material misrepresentation or tort-like claims) | **Accepted. My legal hook was stated too broadly.** Whether a fabricated "my family loves…" is material enough for a state claim is for counsel, and it may not be. My recommendation does not depend on it. The fix costs nothing, and the practical risk (caught out in town, a complaint, a public post) is unchanged. |
| V64 | Unregistered fictitious name: no PA court to enforce contracts; possible $500 penalty | The contract stays valid and defence is not barred. The $500 applies on late registration when suing. A good-faith exception exists | **Accepted.** The consequence is narrower than I implied. Registration (or trading under the legal name) is still a pre-condition, because the filing is a legal duty in itself (V23). |
| V65 / ADDENDUM-01B item 16 | PA Revenue guidance dated December 2024 | Dated October 2024; substance unchanged | **Accepted.** Not load-bearing. |
| V66 | Hot-linking is not a safe harbour outside the 9th Circuit (labelled assumption) | Confirmed for S.D.N.Y.; Third Circuit not checked | **Accepted.** Still a question for counsel; the fix is to leave photos out. |
| ADDENDUM-01A item 2 / 01B item 12 | (finance, ops, competitor) Netlify free credits run out; all sites pause | Rule confirmed; whether API zip deploys count as production deploys is unverified | **Accepted as it bears on this seat.** If a pause can take down a paying customer's site, "free hosting, no end date" is a promise the user may break through no act of their own. That makes a stated hosting term a legal pre-condition, not a pricing preference. |

No correction is disputed.

## 4. What would reverse this vote

- **To D (human-first contact, email only after a reply).** No email provider confirms in writing that one-to-one cold B2B email to published business addresses is permitted. Then I would not support first-touch email at all, the user's own Gmail or Workspace included (V58). D's in-person or phone first contact, followed by email the owner asked for, removes the provider-terms problem and most of the misrepresentation risk.
- **To A (do nothing).** Any one of these:
  1. no permitted channel exists and the user will not spend D's time;
  2. the user will not put written terms at checkout, or will not give up launch-on-payment;
  3. a Pennsylvania attorney, shown the fixed templates and terms, advises against the structure;
  4. the tax professional's answer adds a sales-tax licence and collection duty that makes the venture not worth it (I defer to finance on "worth it").
- **To C.** No legal fact would force this. If the council settles on C, my conditions carry over unchanged, and I would support it.
- **Toward any automatic first-touch sending.** Only the evidence in G4 below. Nothing in the current record meets it.

## 5. Dissent to record

**On the vote: none.** B is backed by deliverability, ops and this seat, and every seat's next step is a hand-approved test.

**Standing dissent, to carry into the recommendation whatever option wins.** The council should not pre-commit the user to automatic first-touch sending, or to AI negotiation, as a later stage, however clean the test is. The strongest form of the argument:

> Every automated message is a statement of fact and an offer made in the user's own legal name, to a business in the user's own town. The user carries that liability personally and cannot contract it away (V61). A reliability dry run (ops) or a sales result (finance) shows that the system works and that people buy. Neither shows that the next unreviewed sentence is true. The record already holds four kinds of false statement written by this system's templates and runbook, all found before a single email was sent:
> - a fabricated customer experience;
> - a hard-coded "I live nearby";
> - "your website" sent to places with no website;
> - invented "made-from-scratch" copy published in a restaurant's name.
>
> These were written by design. They are not edge cases. Automation removes the only check that caught them. The volume automation buys is not needed: lead supply is about 8 to 48 locally (finance estimate). So the legal downside of automation is real and the business upside is close to nil. Price promises, refund answers and timelines in replies must always be approved by a human, because each one forms or varies a contract.

## Answers to the tally's Round 2 questions (section G)

**G1. Channel.**
- *If no provider confirms in writing:* **D**, then A if the user will not do D. Not the user's own mailbox. Workspace's policy forbids "unsolicited… solicitations" (V58). Consumer Gmail's policy is unchecked. A suspension of the user's personal account would cut off the inbox the agent reads and the user's own mail (assumption on scope).
- *Does a written "yes" resolve my channel objection?* **It resolves the contract objection only.** It does not touch:
  - CAN-SPAM content duties (ad disclosure, postal address, opt-out; W1);
  - the deception points (ADDENDUM-01A item 5);
  - terms at checkout;
  - launch on payment alone;
  - registration and tax.

  Also, a support reply that conflicts with the published policy may not protect the user (assumption; ask counsel). The yes should describe the use exactly, be in writing, and be kept.

**G2. Offer.**
- **Before the test**, because the first email is the offer and the payment link is in it today:
  - a stated hosting term and what happens at its end;
  - ownership and handover terms;
  - refund terms;
  - every quoted price chargeable.
- **After the test** (market questions; I defer to competitor and finance): the care-plan price, the menu-update mechanism beyond "included edits for N months", and niche targeting.
- One flag before choosing handover versus hosted: ask the tax professional whether a transfer makes the $500 taxable (V31).

**G3. Supply count as a gate.**
- **No legal objection, and no legal threshold from this seat.** Two conditions:
  1. the count publishes nothing: no Netlify deploys, nothing in a public repository;
  2. it records each address's source and any no-harvesting notice (V62), so the count also tells us which leads are lawful to email.
- I defer to finance (under 15 local and under 60 reachable → A or D) and competitor (6 or more of 30 in the niche) on where the line sits.

**G4. Automation. Evidence that would ever make automatic first-touch sending acceptable to this seat. All of these:**
1. A provider's written permission covering automated sending of this kind.
2. Counsel's written sign-off on the exact templates and the terms page.
3. First-touch content limited to a fixed, counsel-reviewed template whose only variable fields are verifiable facts (business name, address, a preview link). No AI-written free text: no compliments, no "problems" sentence.
4. At least 50 hand-approved sends (the owner seat's figure) with zero factual errors found in emails or previews, and zero complaints or abuse reports.
5. Ops' fail-closed, `hold`, digest-bound-approval and heartbeat fixes in place and passed.

Even then, replies that state prices, promises, timelines or refunds stay human-approved permanently. I do not expect items 2 to 4 to be met inside the 3-month horizon (estimate: 50 sends exceeds the likely local supply of 8 to 48).

**G5. The user's goal: the honest minimum involvement under B.**
- **One-time, before any email:**
  - choose legal name or studio name; file the fictitious name if needed;
  - approve the terms page;
  - get a written provider answer;
  - book a one-hour attorney consult (bring the templates and terms) and a tax-professional answer.

  Estimate: 3 to 5 hours plus fees, method: count of steps at about 30 to 60 minutes each. Filing fee about $70 plus an advertisement cost (V23); consult fees unknown.
- **During the test:**
  - read and approve every first-touch email and its preview: 20 to 30 at 1 to 2 minutes each, about 30 to 60 minutes in total (estimate);
  - approve every reply that states a price, promise or timeline;
  - confirm each buyer in writing before launch;
  - check the inbox for opt-outs at least weekly if the agent stops (assumption that this covers the 10-business-day duty with margin).
- **Per sale:** 1 to 2 hours (finance's estimate, which I accept), plus any refund or dispute handled personally in Stripe.
- **Always:** the user is the legally responsible sender and seller. That cannot be delegated to the agent, and the user should be told so in writing before setup.
