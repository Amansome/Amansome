# ROUND 2: Operations engineer (unattended reliability) (ops)

**Read:** ROUND1-TALLY.md, every ADDENDUM-01*, and all Round 1 reports.

**Vote:** B
**Changed from round 1:** no
**Confidence:** high that B is the right next step from this seat; medium that B's test will be large enough to read (finance's and competitor's supply point).

## 1. Vote and reason

**B: fix, then a hand-approved email test of 20 to 30 first-touch emails. Automatic sending is not part of the option.** This is the Round 1 position ("only a capped, hand-approved E after must-fix defects") restated against the tally's lettering. The vote has not changed. One sub-condition, the evidence needed before automation, is tightened in §4 and in answer to G4, citing owner and finance.

Why B, from a seat judged on silent failures avoided:

1. **The defects are now measurements, not my opinion.** ADDENDUM-01B item 10 reproduces, independently, every defect I reported (T1, T4 to T10), plus the third-party payment launch (lawyer) and the bounce and suppression gaps (deliverability) (fact: V43 to V54). As built, the system fails open: any `mode` other than `trial` sends (V44), the date switch sends never-approved items (01A item 4), and several paths send the same restaurant a second cold email (V45 to V47). B fixes these before anything leaves the building. No other option that sends email does.
2. **B keeps a human on every irreversible action.** Sending email and publishing a site in a restaurant's name cannot be undone. My card's red line is "irreversible outbound actions with no review and no alerting". B removes both. Option E (the user's preference with fixes) does not, because it ends in unreviewed sending, so I reject E. My reason is reliability: the alerting path (heartbeat, bounce intake, paid-not-launched sweep) does not exist yet (fact: V50, V54; README "Day to day").
3. **Why not A.** A carries zero operational risk. But the must-fixes are a few hours of work (estimate: about 10 small code changes, most under 20 lines, from reading `hustle.py`), and B's test is capped at 20 to 30 sends. At that size, every residual failure (one duplicate, one wrong menu item) can be survived and seen. Under B, the downside this seat cares about is small enough that A is not required. If B's own gates fail (no permitted channel, too little supply), I move to A or D (§4).
4. **Why not C as a separate option.** I adopt C's supply count, but as a step inside B's fix period, not as a gate that comes before the fixes (G3). Changing the offer's pricing model is outside this seat's mandate. The part of the offer that is operational (where paid sites live, for how long, and that previews come down) must be settled before any money is taken. B already includes "a stated hosting term". I add the architecture conditions in G2. C is an acceptable second choice for this seat: the difference between B and C hardly changes operational risk.
5. **Why not D as the first choice.** D has the lowest operational risk of any sending option (Round 1 §4), but it costs the most user time, and the system's research and build stages are useful under B too. D is my fallback if no permitted email channel exists (G1).

**Conditional on:** the must-fix list in G2 being done and checked offline before any real lead is stored or any email sent. If B is run on the code as it stands today, my vote is A.

## 2. Response to other members

| Member | Point | Agree / disagree | Why |
|---|---|---|---|
| deliverability | A Resend ban takes down the digest, payment alerts and customer email too (single point of failure) | Agree, and it is worse than stated | The same `send_email` also carries the owner alert. RUNBOOK §6 line 78 tells the agent to "email the owner" when a run is blocked, and that email goes through Resend too (fact: RUNBOOK; `hustle.py`). If Resend closes the account, the alarm and the approval channel go down with the outreach channel, at the moment they are needed. **Condition:** owner alerts and digests must not travel over the channel whose terms are at risk. |
| deliverability | Follow-ups may be automatic once the first email was approved | Disagree, for now | Follow-ups are exactly where T8 (an escalated lead still gets its follow-up, V49), the weekend gap in the `newer_than:2d` window (V53) and "sending while the inbox step failed" all bite. Deliverability names that last one as its own condition. Automatic follow-ups are acceptable only after the `hold` status, a send that is skipped when the inbox step failed, and a processed-message ledger all exist and pass the fault-injected dry run. Until then, follow-ups are approved by hand like first touches. At 20 to 30 leads that is at most about 30 more approvals (estimate). |
| owner | One person approving 15 emails in "about 2 minutes" is about 8 seconds an email, which is not a check | Agree; this is the strongest reliability point from another seat | An approval that does not show the preview next to its source menu is a rubber stamp. It looks like a human check and catches nothing, which is a quiet failure. **Condition:** the digest shows, for each item, the email text, the preview link and the source URL each menu and price came from, and approval names item ids. The time estimate goes up accordingly (G5). |
| owner | Revisit automatic sending only after 50+ hand-approved sends with zero factual errors and zero complaints | Agree; adopted into my automation bar (G4) | My Round 1 bar was "fault-injected dry run plus two clean weeks of E". At finance's supply estimate of 8 to 48 local leads, two weeks may be only about 10 sends, too few to see a 1-in-20 failure (estimate: P(zero failures in 10 sends at a 5% rate) ≈ 60%). A count of sends beats a count of days, the same flaw as the date-based trial (01A item 4). |
| skeptic | The whole local list can be sent by hand in an afternoon, so automation adds little and risks a lot | Agree | It matches the reliability view: every automated step is a failure mode, and here the automation buys about 945 send slots for 8 to 48 leads (finance estimate). Fewer automated steps means fewer silent failures. |
| skeptic | Send from an ordinary mailbox in your own name, not through Resend | Partly disagree | Operationally, hand-sending is the safest email path: no scheduled send, so T1, T2, T3, T7 and the crash re-send cannot happen. Two costs remain. (a) Google Workspace's AUP bans "unsolicited mass email… or other solicitations" (fact: V58), so it is not a clean channel; whether it applies is for deliverability and lawyer to settle, not me. (b) Hand-sent mail leaves the system's ledger. Suppression, "already contacted" and follow-up dates must then be recorded by hand, or `mark` must be run for each send. At 30 leads that is workable. At 100 it is how duplicates happen. |
| finance | Lead supply (about 8 to 48) is the binding limit; count it first, for free | Agree, and the count is also my dry run | The count runs discover, research, upsert and build with no sends (fact: only `send` needs Resend, finance §3). That exercises the stage this seat could not test: F16 says restaurant sites could not be fetched in this session. If the scheduled agent also cannot fetch menus, it writes menus from search snippets. The count would show that before any owner sees it. It also measures E4 (run cost). |
| finance | After at least 1 sale or 3 positive replies in the test, support C (wider area, automatic) | Disagree on what that evidence proves | A sale is evidence of demand, not of reliability. Neither a sale nor three replies tells us whether a crash re-sends a batch or whether escalations stop follow-ups. Automation needs its own evidence (G4). Demand evidence should decide whether to continue at all. |
| competitor | Unsold previews never come down; one Netlify site per lead breaks the free plan | Agree | Fact: no delete or teardown exists (`hustle.py`; competitor §2). Even B's test may exceed the free plan. 30 previews × 15 credits = 450 credits, above the 300 free (estimate, valid **if** API zip deploys are billed as production deploys, which is unverified, 01B item 12). On Free, running out pauses every project on the account, including paid sites (01A item 2). That is a quiet outage of a customer's site. |
| competitor | Handover (the site deployed to the restaurant's own account) or a care plan | Agree that handover is the cleanest answer for this seat | Handover removes three long-tail failure modes at once: paid sites sharing a capped pool with previews, the user's account as a single point of failure for every buyer, and an agent that must stay alive indefinitely to change menus. A care plan keeps all three. The pricing choice is outside my mandate. The architectural consequence is not. |
| lawyer | Any stranger who pays through the preview triggers a public, indexable site and a "thank you for your payment" email in the restaurant's name | Agree; this is my red line seen from another side | It is an irreversible public action with no human check (fact: V42). The verifier notes launch is an agent step, not a script step, but RUNBOOK §2 says "for each newly paid lead, run `launch`", so in practice it happens automatically. **Condition:** `launch` requires a human confirmation plus a reply from the restaurant's published address. Never launch on payment alone. |
| lawyer | Automatic sending and AI negotiation with no review: opposed under every option | Agree on negotiation; on sending, "opposed until earned" | Every price the agent quotes is an unmonitored commitment, and the $400 and $75 prices cannot even be charged (01A item 7). On sending, I keep a door open that the lawyer closes. The bar in G4 is high enough that it will very likely not be met inside 3 months, so in practice we agree on the horizon. |

## 3. Corrections accepted or disputed

- **01A item 1 (Resend bans cold outreach): accepted.** It also confirms the alert-path point above: alerts and outreach share one provider.
- **01A item 2 and 01B item 12 (Netlify credits; whether API deploys count as production deploys is unverified): accepted with the qualification.** The cheapest way to settle V68 is one real deploy of a test site, then reading the credit usage in the Netlify dashboard (about 5 minutes). My condition does not depend on the answer. Previews should not be one site per lead in any case, because of teardown, exposure and quota (G2, item 8).
- **01A item 3 (repository public, branch pushed, `leads.json` empty): accepted.** This was my red line in Round 1, and it is now a confirmed fact.
- **01A item 4 (calendar trial; approval not bound to the digest): accepted.** Same as my T2 and T3.
- **01A items 5 to 7: accepted.** Item 7 adds a point for this seat: `cmd_payments` reads only the latest 100 sessions with no pagination. That is a silent miss once the Stripe account is busy, which is unlikely at this volume (estimate) but costs one loop to fix.
- **01B item 10 (my defects reproduced): accepted.** Two verifier caveats are accepted as stated. On V45 and V46, *that the agent would* re-upsert or keep `L9999` is an assumption, which I labelled as such in Round 1. On V50, `status` still counts `paid` leads, so a run that reads it *could* notice a failed launch. Nothing in the runbook tells it to look, so the failure stays quiet in practice.
- **01B item 11 (crash re-send depends on each run starting from a fresh clone, unchecked): accepted.** It does not change the fix. Pushing right after `send`, plus an `Idempotency-Key` (Resend de-duplicates over 24 h, V51), costs a few lines and makes the question moot whichever way the scheduled run starts. Even without a fresh clone, an unpushed local commit lost on a recycled container gives the same re-send (assumption: containers are ephemeral, as the dossier's "cloud container" implies).
- **01B item 13 (`config.yaml` is tracked but not on the runbook's commit list): accepted. It corrects my Round 1 wording**, which said the runbook commits `config.yaml` on every run. It does not. The exposure is still real: the file is tracked, so one filled-in commit or a broad `git add` publishes the user's email, postal address and Stripe link. `.gitignore` does not exclude it (fact: `sitehustle/.gitignore`). The fix is unchanged: private storage.
- **01B item 14 (structured data `url` is `null` on the first build): accepted.** It matters little to this seat.
- **Nothing disputed.**

## 4. What would reverse this vote

- **To A:**
  - The supply count (done during the fix period) finds fewer than 10 pitchable leads in 30 researched places. I adopt the skeptic's threshold, which sits close to finance's. A test that small cannot show a failure rate, and the fix work is not worth it.
  - Or, in the no-send build pass, any preview contains a menu item, price or hour that is not in its cited source, and the cause is that the agent cannot fetch menus (F16). In that case content cannot be automated at all, and B's premise (agent builds, human approves) collapses into D, with a human building each site. If the user will not do that, A.
  - Or the user wants B run on the code as it stands, without the must-fixes.
- **To D:** no email channel whose terms permit this use can be confirmed in writing (G1).
- **To C:** a decision that money may be taken during the test with the current hosting design (paid sites on the same free-plan account as previews, no handover, no end date). Then the offer change becomes a precondition for this seat too, because the test would create obligations the system cannot reliably carry.
- **Toward allowing automation later (never to E now):** only the evidence in G4.

## 5. Dissent to record

I am with the plurality on B. Two points from this seat are not settled by the tally and should be carried into the recommendation without weakening:

1. **"Hand-approved" must mean bound and informed, or it is worse than no approval.** An APPROVE that releases everything in `outbox/` (VERIFICATION O5; 01A item 4), or a digest that shows email text without the preview and its source, gives the user and the council false assurance. The recommendation should define approval as follows: approval names specific item ids from a specific digest; each item shows the preview and the source of every price; and each Gmail message is acted on once (a processed-message ledger).
2. **The date-based switch should be deleted from the code, not just "not used".** As long as `trial_ends` and the auto-flip exist (`config.yaml` line 40; `cmd_send`), one setup on or after 7 Dec 2026, or one config edit, turns B into unreviewed sending with no warning (fact: 01A item 4; V44). "We agreed not to use it" fails silently. A missing code path fails safely.

## Answers to the tally's Round 2 questions (section G)

**G1. Channel.** If no provider confirms in writing, this seat chooses **D**, and A if the user will not do D. The user's own mailbox is operationally the safest email path, because nothing sends on a schedule. Whether its terms allow this use is for deliverability and lawyer (V58), and I will not override them. A written "yes" from a provider resolves the channel question for this seat, but the channel was never my main objection. A permitted provider does not fix fail-open modes, duplicate paths or missing alerts. Whatever the channel: **owner alerts and digests go over a separate, solicited channel** (for example, a transactional account used only to email the user), so an outreach ban cannot also silence the alarm.

**G2. Offer.** Pricing (care plan or one-off) can wait until after the test; that is not my mandate. **Before the test, and before any money is taken:**
- Paid sites must not share a capped free pool with previews. Either hand over (preferred by this seat) or use a separate paid account.
- The hosting term is stated.
- Unsold previews are removed after a set period (competitor's 30 days).

**Must-fix list before any real lead is stored or any email sent** (cut down from Round 1 to what a 20 to 30 send test needs; my card warns I may overengineer):
1. State (`data/`, `outbox/`, `sites/`, `config.yaml`) moves to private storage. Keep the profile repository public and move SiteHustle out of it.
2. Delete the date switch. Allow only the modes `{paused, trial}`; anything else sends nothing. Default `paused`.
3. Approval is bound to the digest (item ids), with a processed-message ledger.
4. `send` refuses a second outreach email to any lead or address already contacted. `upsert` never moves a status backwards and rejects ids it did not assign. Slugs are unique.
5. Escalation sets a `hold` status, which stops follow-ups and sends.
6. Commit and push right after `send` and after `payments`. Send an `Idempotency-Key`.
7. `launch` requires human confirmation and a reply from the restaurant. Payment amount is checked. Only chargeable prices are quoted.
8. Previews use one shared preview site on the user's own domain, at unguessable paths, with no payment link (this combines deliverability's one-link idea and lawyer's no-payment-link-on-preview). It also settles the credit question: one deploy per batch, not per lead (estimate).
9. Per-item error handling in `send`, so one bad address cannot block the queue (V48), and a failure is reported to the user.

**Deferred until before any automation:** heartbeat, bounce and complaint intake, paid-not-launched sweep, quota monitoring, and the fault-injected dry run.

**G3. Supply count as a gate.** Yes. Run it during the fix period: it costs no sends and doubles as the content-accuracy dry run. Thresholds:
- **Fewer than 10 of 30 researched places pitchable** (weak site and published email): stop the email test; go to A, or to D if the user accepts the time.
- **Any invented menu item, price or hour** in a 10-site spot-check against cited sources: automated content is off; go to D (a human builds or checks each site) or A.
- I defer to finance and competitor on the finer commercial thresholds (finance: under 15 local and under 60 reachable; competitor: 2 or fewer of 30 in the no-site, no-vendor group). Either one tripping is enough for me.

**G4. Automation.** Automatic **first-touch** sending becomes acceptable to this seat only when **all** of these hold:
- (a) the provider's permission is confirmed in writing;
- (b) the deferred list in G2 is built;
- (c) a one-week fault-injected dry run passes. Faults: reply, unsubscribe, angry message, crash between send and push, paid session with a failed launch. Pass means zero duplicates, zero sends to suppressed or held leads, an alert for every fault within one run, and a heartbeat every weekday;
- (d) **at least 50 hand-approved live sends** with zero duplicate sends, zero sends after an opt-out, zero factual errors in previews, and zero complaints. The count is adopted from owner; deliverability's caveat applies, because Gmail complaints are invisible (V55), so "zero complaints" is a weak signal and the other three counts carry the weight.

At finance's supply estimate, (d) very likely cannot be reached locally inside 3 months (estimate: 8 to 48 leads). For this seat, automatic first-touch is therefore off the table for the decision horizon. That is a conclusion from the numbers, not a softened "maybe later".

**G5. The user's goal: honest minimum involvement under B.**
- **Setup:** the 45 minutes stated, plus account, domain and channel checks. Registration and tax are referred to professionals (lawyer, finance).
- **During the test (2 to 3 weeks):** reviewing each pitch properly, with the preview next to its source menu, takes 2 to 3 minutes. 20 to 30 pitches and their follow-ups come to about 1.5 to 2.5 hours. With replies and setup, **about 2.5 to 4 hours in total** (estimate; I adopt finance's figure over the tally's 1 to 3 hours, because owner's point shows 8-second approvals are not review).
- **Every sending day:** read one status line, and act when it is missing or shows an error. Until a heartbeat exists, the user *is* the monitoring.
- **Per sale:** about 1 to 2 hours (DNS, confirmation, launch check; finance estimate).
- **Incidents:** when one happens, the user is the incident responder. No one else is.

"Zero involvement besides receiving payment" is not true under B, or under any option that sends email from this code.
