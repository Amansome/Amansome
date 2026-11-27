# ROUND 1: Operations engineer (unattended reliability) (ops)

**Dossier:** DOSSIER-01-launch-sitehustle-as-built-after-fixes-c.md. **Addenda read:** none (no ADDENDUM-01* file existed when this was written).
**Round 1, independent:** no other member's report was read before this one was written.

**Position:** Do not launch as built (B), and never use the date-based switch to automatic sending. Support only a capped, hand-approved test (E) after a short list of must-fix defects. Automatic sending (C) only after the dry-run pass criteria in §5 are met and two clean weeks of E follow.
**Confidence:** high that the system as built is not safe to run unattended (I reproduced ten defects in an offline simulation). Medium on the overall recommendation, because it also depends on platform limits I could not check live (Netlify credits, Resend terms).

## 1. Position and why

1. **The system has no reliable stop. It fails open, not closed.** I checked these in the code and reproduced each one in an offline simulation (§3):
   - The switch from trial to automatic sending depends only on the date (`cmd_send`, `hustle.py` L443-446). On 2026-12-07, every queued email the owner never approved is sent, even if the owner never approved a single batch. The trial is measured in calendar days, not in runs that were checked. Setup has not happened yet (F17), so the trial could be anywhere from five weekdays to zero.
   - Any `outreach.mode` value other than the exact string `trial` means "send without review" (L458). If the user sets `mode: paused`, `off` or `manual` to stop the system, it sends everything instead.
   - There is no documented way to stop the system. README and RUNBOOK do not say how to stop it short of deleting the scheduled task.
2. **The duplicate-send defenses are thin. Several paths send the same restaurant a second cold email.** The dossier says one duplicate bug was "found and fixed" (F15). I found more:
   - **Re-upsert regresses status (L207).** RUNBOOK §1 tells the agent to "make the requested edits to the lead JSON" after a reply. If it re-upserts its original file, `existing.update(...)` overwrites the status with `researched`. Then build, deploy and queue produce a second "A new website for..." email to someone who is already talking to us. `cmd_send` (L464-470) never checks whether an outreach email was already sent to that lead.
   - **Sample id collision (L202).** The sample file carries `"id": "L9999"`, and the runbook says "save it as JSON matching `examples/sample-lead.json`". If the agent keeps that id, the second restaurant silently overwrites the first.
   - **Slug collision (L213, L183, L279).** Two restaurants with the same name get the same slug, so they share `sites/<slug>/`. One restaurant's preview can be deployed with the other's phone number and menu.
   - **State is durable only at the very end of the run (RUNBOOK §6).** If the run dies after the send step but before `git push` (container recycled, usage limit, push conflict, agent error), the next run starts from the last pushed `leads.json` and `outbox/`. It then re-sends that day's batch. No idempotency key is sent to Resend (`send_email`, L338-349).
3. **Escalation does not pause automation.** RUNBOOK says that for an angry reply, legal threat or refund request the agent should "email the owner... and leave the lead alone". Leaving the lead alone keeps it in `contacted`, so `cmd_followups` (L478-498) queues the follow-up five days later anyway. In automatic mode it goes out with no review. Of all the failures I found, this is the one most likely to embarrass the user in their own town.
4. **The unsubscribe path depends on a chain of six links, with no health check.** The chain is: business inbox → forwarding → Gmail filter and label → connector → agent judgment → `mark ... unsubscribed` → git push. If forwarding or the label breaks, the agent sees no replies. Follow-ups keep going to people who said stop, and nothing alerts anyone. There is no handling for bounces or spam complaints at all: no Resend webhook and no polling. Hard bounces get a follow-up, and a provider suspension surfaces only as a 403 with the misleading message "add a Resend API key" (L346-347).
5. **Silence means three different things, and the user is told it means one.** README says "You get an email only when someone pays, or if something needs a human." There is no heartbeat email. When the run stops (trigger disabled, plan limit hit, connector expired), nothing happens: replies go unanswered and paid customers go unlaunched. The owner's silence looks the same as "no sales yet".
6. **Customer data would go to a public repository. This is a red line for this seat.** I checked it: `gh api repos/Amansome/Amansome` returns `"visibility":"public"`, and the branch holding `sitehustle/` is already pushed to origin (`git ls-remote` shows `refs/heads/claude/friendly-pascal-r0rno3`). The runbook commits `data/leads.json` (restaurant emails, phones, notes, payment status), `outbox/` and `config.yaml` (the user's personal email and postal address) on every run. Today `leads.json` is `[]`, so nothing has leaked yet. Moving the state is cheap now and impossible to undo later.

What this seat gains or loses: it is judged on silent failures avoided. The user hopes for "zero involvement after a week". That conflicts directly with what this seat needs, and I will not soften it: with this code, the minimum honest involvement is approving every outbound batch, reading a daily status line, and being the person who responds when something breaks.

## 2. Where the dossier is wrong, incomplete or mis-posed

- **F4 is incomplete in a dangerous way.** It says that in trial mode "emails are sent only after the owner replies APPROVE". In fact:
  - On `trial_ends`, already-queued unapproved emails are sent too (simulation T2).
  - Any mode other than `trial` sends without approval (T1).
  - `cmd_approve` (L424-430) approves everything in `outbox/`, not the items in the digest the owner actually read (T3).
  - RUNBOOK §1 searches `newer_than:2d`, so yesterday's APPROVE is seen again the next day. Combined with the unscoped `approve`, that can approve a batch the owner never saw.
  - Nothing records which Gmail messages have already been acted on.
- **F11 can now be settled.** The repository is **public** (GitHub REST API `visibility: public`; an anonymous raw.githubusercontent fetch of the README returned 200). The SiteHustle branch is already on the remote. This is no longer "not checked".
- **F5 and F13 overstate safety.** "Unsubscribes are handled" and "risky situations are emailed to the owner" are true only while the whole forwarding chain works. Escalation does not stop follow-ups (T8), and bounces and complaints are not handled at all.
- **F15 overstates testing.** The offline simulation covered the happy path. It did not cover crash-and-resume, API errors, duplicate ids or slugs, or status regression. All of those fail (§3).
- **F8 and F10 conflict, and the code accepts any amount.** The agent may offer $400, but there is only one $500 Payment Link and `claim_url` always uses it. The agent's Stripe key is read-only (README step 4), so the $400 deal cannot be carried out without improvising. `cmd_payments` (L511-521) marks a lead paid for any `amount_total`, even $1 (T10).
- **F9 rests on an unverified assumption: "Free hosting (no monthly fee)", forever, on the user's free Netlify account.** As I understand it (training knowledge, **not verified in this session**), Netlify moved new accounts to credit-based plans in 2025. On that model the free plan has about 300 credits a month, a production deploy costs about 15 credits (roughly 20 deploys a month), and sites on the free plan are paused when credits run out. The design needs one deploy per lead, plus more for each edit and for launch. At 15 leads a weekday that is far more than 20 deploys a month. When credits run out, **paid customers' live sites go dark** along with the previews. Nothing in the code checks plan usage. Dossier §6 lists Netlify terms as "not checked". That item should be at the top of the list, not buried.
- **Option B's cost line is mis-posed.** "2 min/day for one week" leaves out incident response (stuck payments, broken forwarding, a full Netlify quota, unanswered replies). Under B, someone still has to do that work, and nobody is assigned.
- **Missing from §6, "What is not known":** what happens when the scheduled run does not run; where state lives between runs and when it is saved; how a paid but unlaunched customer is noticed; what tears down previews for lost or unsubscribed leads (no command exists, so preview sites build up publicly forever); and that the agent reading untrusted restaurant replies has the power to send email, edit sites and push to git (a prompt-injection surface).
- **Missing option:** "Hand-approved permanently: the system researches, builds and drafts, and a human presses send on every batch." It sits between C and D, and it is the only form I can support for the 3-month horizon without the §5 evidence.

## 3. Evidence

How I tested: I copied `scripts/`, `templates/`, `config.yaml`, `data/` and `examples/` to the scratchpad (`ops-copy/`). I replaced the TODO values with dummy ones in the copy, stubbed `requests.post/get/request` (no network calls to Netlify, Resend or Stripe), froze the clock, and ran the real `hustle.py` functions. The harness is `/tmp/claude-0/-home-user-Amansome/c705ec05-971c-5fbf-aeea-395a71965e0d/scratchpad/sim.py`.

| Claim | Type | Source or method |
|---|---|---|
| T1: setting `mode: paused` sends unapproved emails | fact | Simulation; `cmd_send` L458 checks only `== "trial"` |
| T2: on `trial_ends`, a never-approved queue is sent and the config flips to `auto` | fact | Simulation at 2026-12-07 10:00 ET; L443-446 |
| T3: `approve` marks items approved that were queued after the digest | fact | Simulation; `cmd_approve` L424-430 has no digest id |
| T4: re-upserting the original research JSON after a reply leads to a second cold outreach email | fact (code path); assumption (that the agent would do it) | Simulation; `cmd_upsert` L207 overwrites `status`; `cmd_send` has no "already sent outreach" check |
| T5: the sample id `L9999` reused makes restaurant B overwrite restaurant A | fact (code); assumption (agent behavior) | Simulation; `examples/sample-lead.json` id; `cmd_upsert` L202 |
| T6: same-name restaurants share `sites/<slug>/`, so one lead's folder contains the other's phone number | fact | Simulation; `slugify` without a uniqueness check (L183, L213); build path L279 |
| T7: one permanent 4xx from Resend stops every later send, every day (head-of-line blocking) | fact | Simulation; `raise_for_status` L348 is uncaught in the `cmd_send` loop; `outbox_items` is sorted, so the failing item stays first |
| T8: a lead escalated and "left alone" still gets the follow-up | fact | Simulation; `cmd_followups` keys only on `status == "contacted"` |
| T9: if launch fails once after payment, `payments` never surfaces the lead again, and the owner was already told "Claude is launching their sites now. Nothing for you to do." | fact | Simulation; `paid_at` guard L514; owner email L525-528; no sweep for `paid` and not launched |
| T10: a $1 payment marks a lead paid | fact | Simulation; no amount check, L516-519 |
| State is saved remotely only at the end of the run, so a crash after sending re-sends next run | fact (runbook) + reasoning | RUNBOOK §6; no idempotency key in `send_email` |
| The state repository is public and the SiteHustle branch is pushed | fact | `gh api repos/Amansome/Amansome` returned `visibility: public`; `git ls-remote origin` |
| `data/leads.json` is empty today | fact | File contents `[]` |
| No bounce or complaint handling; a 403 tells the user to "add a Resend API key" whatever the cause | fact | `send_email` L346-347; grep finds no webhook or polling code |
| No heartbeat or dead-man alert; the owner hears only about payments and escalations | fact | README "Day to day"; RUNBOOK §6 alerts only "if something blocked the run", which assumes the run happened |
| No teardown of previews for lost or unsubscribed leads | fact | Command table L603-611 |
| Netlify free plan is about 300 credits a month and about 15 credits per production deploy; sites pause when credits run out | assumption (training knowledge, unverified) | Verifier should check netlify.com/pricing and the credit docs |
| Resend accepts an `Idempotency-Key` header and exposes delivery events (bounced, complained) per email via its API | assumption (unverified) | Check resend.com/docs |
| Over about 60 weekday runs in 3 months, at least one run will die between sending and pushing, if the per-run chance is around 2% | estimate | 60 × 2% ≈ 1.2 expected events. The 2% is a guess for a long agent run (research, build, deploy, push) in an ephemeral container; not measured |
| Menu accuracy cannot be assumed: restaurant sites could not be fetched in this session (F16), so content would come from search snippets or third-party pages | assumption | F16; RUNBOOK §4.5 requires published menus; no code checks content against a source |

## 4. Risks from this seat

- **A (do nothing):** no operational risk. The only loss is the option's upside.
- **B (as built):** the worst quiet failures, roughly in order of likelihood × harm:
  1. Follow-ups to people who complained or unsubscribed, when escalation or forwarding fails (T8 and the forwarding chain). This is an opt-out failure under CAN-SPAM, in the user's own town.
  2. Duplicate cold emails from a crash before push or from status regression (T4).
  3. Netlify credits run out, so every site pauses, including sites customers paid for.
  4. Paid but never launched (T9), while the owner has been told everything is fine.
  5. Data in a public repo: restaurant contacts and the user's personal address.
  6. A wrong menu or price shown under the restaurant's name, with no human looking at it after the trial.
  7. The run stops and nobody knows.

  All of these are **quiet**. The only loud failures are missing credentials, which `sys.exit` with a message.
- **C (after fixes):** this is safe only if the fixes include failing closed and the heartbeat. Otherwise C turns into B a week later.
- **D (human in the sales step):** lowest operational risk. A human looks at every outbound message, and pipeline errors get caught. The cost is the user's time.
- **E (hand-approved test):** low risk *if* approval is bound to what the human actually saw, and state is moved to a private repo first. The residual risks are duplicates on crash and wrong content. Twenty to thirty sends make both survivable.

## 5. The cheapest decisive step

There are two steps, the first much cheaper.

1. **10 minutes of reading, before anything else:** current Netlify free-plan limits (credits, deploy cost, what happens when credits run out, commercial-use terms), plus Resend's idempotency and email-events API.
   - **Decided now:** if the free plan allows fewer than about 100 production deploys a month, or pauses sites when credits run out, the "one live site per lead, free hosting forever" design fails whatever else we fix. I would then oppose B and C on the current architecture. Instead I would require previews as screenshots or a single shared preview site, and hosting priced as a paid plan or monthly fee.
2. **A one-week dry run with injected faults, after the must-fixes:** the real scheduled agent and runbook against real local restaurants, with research and builds real but all email sent to the owner's own addresses (or a sink), and Stripe in test mode. I would inject five faults: a reply, an unsubscribe, an angry message, a crash between send and push, and a paid session whose launch fails.
   - **Pass, decided now:**
     - zero duplicate sends;
     - zero sends to suppressed or escalated leads;
     - every injected fault produces an owner alert within one run;
     - the heartbeat arrives every weekday;
     - in a spot-check of 10 built sites against their sources, zero invented menu items, prices or hours;
     - Netlify usage projects within plan.
   - **If it passes:** I move to supporting E now, and C with automatic sending after two clean weeks of E.
   - **If any menu item or price is invented in the spot-check:** I oppose automated content entirely and support D (a human builds or checks each site).
   - **If any duplicate or post-unsubscribe send occurs:** I stay at "no automatic sending".

## 6. Conditions and red lines

**Must be fixed before any real email, even under E:**
1. Move `data/`, `outbox/`, `sites/` and `config.yaml` to a **private** repository or private storage. The current repository is public.
2. **Fail closed.** Use an allowlist of modes `{paused, trial, auto}`, and treat anything else as send nothing. Delete the date-based switch (L443-446): `auto` should require an explicit command from the owner, not a calendar date. Document a one-line kill switch in README.
3. **Bind approval to the digest.** The digest carries an id or hash of its items; `approve <digest-id>` approves only those items. Keep a ledger of processed Gmail message ids so each message is acted on once.
4. **Duplicate guards:**
   - `cmd_send` refuses an outreach email to any lead that already has one in `emails`, and refuses any address sent to in the last 30 days.
   - `cmd_upsert` never moves an existing lead's status backwards and rejects ids it did not assign (including `L9999`).
   - Slugs are unique.
5. **Save state right after sending:** commit and push immediately after `send` and after `payments`, and send an idempotency key (lead id plus kind) to Resend, if Resend supports it.
6. **Per-item error handling in `cmd_send`.** A 4xx error moves that item to a failed list and the loop continues. Every failure is reported to the owner.
7. **Escalation pauses the lead.** Add a `hold` status that stops follow-ups and sends. The runbook's "leave it alone" must set it.

**Must be true before any automatic sending (C):**
- A daily heartbeat email to the owner listing sent, queued, replies waiting, paid but not launched, and errors. A missing heartbeat is the alarm.
- A sweep for leads in `paid` that were never launched.
- A check that the payment amount matches the agreed price, and a real $400 link or no $400 rule.
- Bounce and complaint checks before each follow-up, with automatic suppression.
- Teardown of previews for lost or unsubscribed leads.
- Netlify quota checked against the plan.
- The §5 dry run passed.

**Will not accept:**
- Irreversible outbound email with no human review and no alerting. That is B after 2026-12-07.
- Customer data in a public repository.
- Telling the user "zero involvement" while they are, in fact, the unmonitored incident responder.

## 7. One line

As built, SiteHustle fails open and fails quietly: it has a date-triggered switch to automatic sending, several ways to email the same restaurant twice, escalations that don't stop follow-ups, no heartbeat, and its state is headed to a public repository. Fix those, then run only a small hand-approved test; automatic sending has to be earned with a clean dry run.
