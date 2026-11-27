# ADDENDUM 01A: corrections to DOSSIER 01

**Wins over DOSSIER-01-launch-sitehustle-as-built-after-fixes-c.md and earlier addenda where they conflict.** Corrections and
measurements only. No member's position, vote or reasoning appears here.

Items are numbered on from the previous addendum so every correction has one stable number.
Verdict references (V…, O…) point to VERIFICATION.md.

## 1. The email provider (Resend) prohibits cold outreach

- **The dossier said:** Resend sends the outreach (F2); whether its acceptable-use policy permits cold outreach was "not checked" (§6).
- **Correct:** Resend's Acceptable Use Policy prohibits "unsolicited messages of any kind, including cold outreach, purchased lists,
  or scraped contact data", requires recipients to have explicitly opted in, sets complaint rate < 0.08% and bounce rate < 4%,
  and allows account shutdown without warning. The page is dated 13 Oct 2026. One seat fetched and read the live page; the verifier saw
  the same wording via search results.
- **Source:** resend.com/legal/acceptable-use (V28).
- **Found by:** skeptic, deliverability (read the live page), lawyer, verifier.
- **Matters because:** Options B and C as designed send through Resend; the same code path also sends the owner digest, payment
  alerts, replies and launch emails (F2), so a shutdown also cuts those.

## 2. Netlify hosting is not free at the configured volume

- **The dossier said:** hosting is free (F9; Option B cost); Netlify's free limits "not checked" (§6).
- **Correct:** Netlify accounts created since 4 Sep 2025 use credits. The Free plan has 300 credits a month; each production deploy
  costs 15 (at most about 20 deploys a month); bandwidth also costs credits. When credits run out on Free, all of the account's
  projects pause until the next cycle. `cmd_deploy` creates one site per lead and zip-deploys it, which reads as a production
  deploy (inferred from the code, not tested). At up to 15 previews per weekday, the free credits cover about 1 to 2 days a month.
  Paid customers' sites are on the same account, so a pause takes them down too. Netlify's terms on hosting client sites on Free
  were not found (forum statements conflict).
- **Source:** docs.netlify.com "How credits work", "Credit-based pricing plans"; netlify.com changelog (V29, V30).
- **Found by:** competitor, finance, ops, verifier.
- **Matters because:** the offer's "Free hosting (no monthly fee)" with no end date (F9), the cost of Option B, and Question 5.

## 3. The repository holding lead data is public

- **The dossier said:** visibility of `amansome/amansome` "was not checked directly" (F11).
- **Correct:** the GitHub API returns `visibility: public`, and the working branch is already pushed there. `data/leads.json` is still
  empty, so no lead data has been published yet. The runbook commits `data/`, `sites/` and `outbox/` every day. `config.yaml`,
  which will hold the user's personal email, postal address and Stripe link, is also tracked in the repo (O7). Publishing generated sites in a
  public repo also undoes the previews' `noindex`.
- **Source:** GitHub API `repos/Amansome/Amansome`; `git ls-files`; RUNBOOK §6.
- **Found by:** owner, skeptic, deliverability, lawyer, ops, verifier.
- **Matters because:** every option that stores real leads; Question 2.

## 4. The trial is a calendar date, and approval is not tied to what the owner saw

- **The dossier said:** trial mode until 2026-12-07, with emails sent only after the owner replies APPROVE (F4).
- **Correct:** the trial ends on a fixed date. As of 2026-11-27 nothing is set up, so at most 6 weekdays remain, and there is no trial
  at all if setup finishes on or after 7 Dec. When the mode flips, every queued item goes out unreviewed, including items never
  approved. `approve` approves every outbox file, not only those in the digest, and the runbook's 2-day inbox search can reuse one
  APPROVE across two runs. Any mode value other than exactly `trial` sends without review.
- **Source:** `config.yaml`; `hustle.py` `cmd_approve`, `cmd_send`; RUNBOOK §1, §5 (V4, O5).
- **Found by:** skeptic, deliverability, ops, verifier.
- **Matters because:** whether Option B really has a human review step; Question 3.

## 5. The email text contains statements that are not true as sent

- **The dossier said:** each email includes the business name, postal address and an unsubscribe line (F5). The opening is
  "I live nearby and {{compliment}}", with the compliment written "from real reviews or their story" (F6).
- **Correct:** in addition, (a) "I live nearby" is hard-coded for every lead, including future areas (O2). (b) The compliment is
  written in the first person, as the sender's own experience, from strangers' reviews. The sample says "my family loves your vodka
  rigatoni". (c) The footer says "one-time note" but a follow-up is sent 5 days later. (d) The email never says it is an advertisement
  (O1); CAN-SPAM requires clear and conspicuous identification (whether the content is enough is a legal question). (e) The email
  always says "I was looking at X's website", even for leads with no website (rubric score 2).
- **Source:** `templates/email/outreach.txt.j2`, `followup.txt.j2`; `examples/sample-lead.json`; FTC CAN-SPAM guide.
- **Found by:** owner, skeptic, deliverability, lawyer, competitor, verifier.
- **Matters because:** Question 2 (deceptive content) and compliance in every option that sends email.

## 6. Previews and launched sites contain invented copy and third-party material

- **The dossier said:** previews use the restaurant's own name, menu, hours, address and photos (F7).
- **Correct:** when the agent supplies none, the build inserts default marketing copy ("Fresh, made-from-scratch food in the heart of
  {city}.", "Made fresh, every day.", "Our story"). Previews also show quoted Google/Yelp reviews, hot-link the restaurant's photos
  from its server, and have a footer reading "© {year} {restaurant}. Site by {studio}". Google documents that a robots.txt block stops
  it reading `noindex`, so a linked preview URL can still be indexed (URL only). A launched site stays at
  `preview-<slug>.netlify.app` until the restaurant changes its DNS (O6).
- **Source:** `hustle.py` `cmd_build`; `templates/site/index.html.j2`; Google Search Central docs (V7, O3, O6, O8).
- **Found by:** verifier, lawyer, owner.
- **Matters because:** Question 2 and the lawyer seat's concerns about what is published before consent.

## 7. The $400 floor and $75 edit rounds cannot be collected, and payment amounts are not checked

- **The dossier said:** the agent may go to $400; extra edit rounds cost $75 (F10); payment is matched by `client_reference_id` (F8).
  §6 also said how a restaurant updates its menu after launch is "not specified".
- **Correct:** there is one fixed $500 Payment Link and the agent's Stripe key is read-only, so no $400 or $75 charge can be made by the
  system. `cmd_payments` does not check the amount, reads only the latest 100 sessions and does not paginate. Menu changes after
  launch are specified in RUNBOOK §1: they go through the agent, two rounds included, then $75 a round.
- **Source:** `hustle.py` `claim_url`, `cmd_payments`; README setup step 4; RUNBOOK §1 (O4).
- **Found by:** owner, skeptic, ops, finance, competitor, verifier.
- **Matters because:** Question 4 and the finance seat's revenue math.

## 8. Option B's cost is understated

- **The dossier said:** about $20 setup plus about $7 a month (§1, Option B).
- **Correct:** that figure counts Netlify as free (item 2). It also leaves out Claude plan usage, Stripe fees (2.9% + $0.30, about $14.80
  per $500 sale, confirmed), and Pennsylvania fictitious-name registration, which requires a filing fee and, for an individual, a published
  advertisement (54 Pa.C.S. § 311).
- **Source:** V22, V23, V24, O12.
- **Found by:** verifier, lawyer, finance.
- **Matters because:** Option B's cost row and Question 4.

## 9. The builder's stated position is withdrawn as a factual claim

- **The dossier said:** the builder believes "the main remaining blockers are the user's account setup" (§7, labelled a position to test).
- **Correct:** items 1, 2 and 5(d) are blockers other than account setup. The factual part of that position is withdrawn.
- **Source:** V38.
- **Found by:** verifier.
- **Matters because:** §7 and Question 2.

## Disagreements recorded, not adjudicated

None on facts so far. The verifier's second pass, on claims made in the Round 1 reports, will be published as ADDENDUM-01B if it
produces corrections.

## Standing instruction

Check this record too. Report anything further, and prefer checking a source or running the
analysis over arguing about it.
