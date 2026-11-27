# ADDENDUM 01B: corrections to DOSSIER 01 and to claims in the Round 1 reports

**Wins over DOSSIER-01-launch-sitehustle-as-built-after-fixes-c.md and earlier addenda where they conflict.** Corrections and
measurements only. No member's position, vote or reasoning appears here.

Items are numbered on from the previous addendum so every correction has one stable number.
Verdict references (V…) point to VERIFICATION.md section 4 (the verifier's second pass: 52 Round 1 claims checked, 40 confirmed).

## 10. The code defects reported in Round 1 are reproduced independently

- **The dossier said:** one duplicate-follow-up bug was found and fixed (F15).
- **Correct:** the verifier reproduced each of the following with its own offline test against a copy, with all external calls stubbed.
  These are measurements, not opinions.
  - Any `outreach.mode` value other than exactly `trial` sends without approval.
  - Re-upserting a lead's research file resets its status, and a second cold email goes to the same restaurant.
  - A reused sample id `L9999` overwrites an earlier lead.
  - Restaurants with the same name share one site folder.
  - One permanent Resend error blocks every later send, every run.
  - An escalated lead that is "left alone" still gets its follow-up.
  - A launch that fails after payment is never surfaced again.
  - Any payer and any amount marks a lead paid. The fixed $500 link cannot itself produce a smaller amount, but another checkout on the same Stripe account carrying the lead id would.
  - `lost` addresses are not added to the suppression list.
  - Bounces are never read, and Resend sends no complaint events for Gmail or Google Workspace recipients.
- **Source:** `scripts/hustle.py`; verifier's offline test (V39 onward).
- **Found by:** ops (T1-T10), lawyer (third-party payment), deliverability (bounces, suppression, complaints); reproduced by the verifier.
- **Matters because:** Question 2, and any option relying on unattended operation.

## 11. Crash re-send: the mechanism is confirmed, the trigger is conditional

- **A Round 1 report said:** a crash after sending but before the end-of-run push re-sends that day's batch.
- **Correct:** no idempotency key is sent to Resend, although Resend supports one, and state is pushed only at the end of the run.
  Whether a re-send actually happens depends on each scheduled run starting from a fresh clone of the repo, which was not checked.
- **Source:** `hustle.py` `send_email`; RUNBOOK §6; Resend docs via search.
- **Found by:** ops; qualified by the verifier.

## 12. Netlify deploy cost: one input is unverified

- **ADDENDUM-01A item 2 said:** each script deploy reads as a production deploy costing 15 credits.
- **Correct:** whether Netlify bills the script's API zip deploy as a production deploy is **unverified** (V68). The free-plan rule
  itself (300 credits a month, 15 per production deploy, projects pause when credits run out) stands. If API deploys are billed the
  same way, item 2 holds as stated.
- **Source:** V29, V68.
- **Found by:** verifier.

## 13. `config.yaml` is tracked but not named in the runbook's commit list

- **A Round 1 report said:** the runbook commits `config.yaml` every run.
- **Correct:** RUNBOOK §6 names only `data/`, `sites/` and `outbox/`. `config.yaml` is tracked in git, so the user's personal email,
  postal address and Stripe link are exposed only if it is committed after being filled in (or by a broad `git add`).
- **Source:** RUNBOOK §6; `git ls-files` (V74).
- **Found by:** verifier.

## 14. Preview structured data

- **A Round 1 report said:** the preview's structured data names the preview URL as the restaurant's site.
- **Correct:** on the first preview build the `url` is `null`; it carries the preview URL only on rebuilds after deploy.
- **Source:** `hustle.py` `cmd_build` (V75).
- **Found by:** verifier.

## 15. Slice pricing omitted a fee

- **A Round 1 report said:** Slice costs $39 a month plus $3 per order and includes a website.
- **Correct:** slice.com/pricing also lists a $1,000 implementation fee.
- **Source:** slice.com/pricing via search (V77).
- **Found by:** verifier.

## 16. Minor date and term corrections

- PA Revenue's website-tax guidance is dated October 2024 by secondary sources, not December 2024. The substance is unchanged (V65).
- USPS offers 3-, 6- and 12-month PO box terms; 6 months is not the minimum. The price range quoted is consistent (V83).
- **Found by:** verifier.

## 17. Items that remain unverified

- Resend allowing 150 emails on day 1 of warm-up (V56).
- Netlify's Free-plan audience label "Individual" (V70).
- The primary pages for Resend, Google Workspace and Netlify could not be fetched by the verifier (permission policy).
  The policy wording rests on search results plus one seat's saved copy of the Resend and Workspace pages, which match.

## Disagreements recorded, not adjudicated

None on facts. The finance seat's funnel arithmetic was recomputed and holds; its inputs are assumptions, labelled as such (ESTIMATE).

## Standing instruction

Check this record too. Report anything further, and prefer checking a source or running the
analysis over arguing about it.
