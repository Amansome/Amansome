# SiteHustle runbook (for Claude)

You prepare everything; the owner approves everything that leaves. Work from the `sitehustle/` folder.
Never commit `data/`, `sites/`, `outbox/`, `.env` or `config.local.yaml` (they're git-ignored; keep it that way).

## Ground rules (these win over everything below)

- **Nothing sends without the owner.** Every email (first touch, follow-up, reply, offer, launch notice) goes
  through `digest` → the owner replies `APPROVE <digest-id>` → `approve <digest-id>` → `send`. Never set
  `outreach.mode` to anything but `paused` or `manual`, and never switch to `manual` yourself.
- **First-touch email only through a provider that has said yes in writing** to this exact use (the owner keeps that
  answer). Resend's acceptable-use policy bans cold outreach. Until there's a written yes, do the in-person list (step 4).
- **No invented facts.** Every menu item, price and hour comes from the restaurant's own published source. Record it
  in `content_source`. If you can't find it, leave it out. `observation` lines must be checkable facts with an
  `observation_source` ("A lot of your Google reviews mention the rigatoni"), never personal experience.
- **Never claim** to be a customer, a neighbour, or affiliated with the restaurant or any platform.
- **Never negotiate.** Prices, discounts, refunds, timelines and promises in replies are drafted for the owner to approve.
  There is one price.
- **Contact only published business emails**, and record where you found each one in `email_source`. Skip any site with a
  no-solicitation or no-harvesting notice.
- **Stop on trouble.** An angry reply, legal threat, refund request or anything odd: `mark <id> hold "<why>"`, and put a
  one-line summary at the top of the next digest. Don't reply.
- **Unsubscribe / no / bounce:** `mark <id> unsubscribed|lost|bounced`. This suppresses the address for good.

## 1. Inbox
Read replies to the business inbox (Gmail connector, label `sitehustle`, or whatever the owner set up). Track which
message ids you've handled in `data/processed_messages.txt` and never act on one twice.
- `APPROVE <digest-id> [SKIP ids]` from the owner: run `python3 scripts/hustle.py approve <digest-id> [SKIP ids]`.
- Interested restaurant: `mark <id> replied`, then `offer <id>` (it queues the details, terms link and payment link for approval).
- Questions or change requests: apply the edits to the lead JSON → `upsert` → `build <id>` → `publish-previews`,
  then write a draft (first line `Subject: Re: ...`) and `reply <id> draft.txt`.
- "Go ahead" from the restaurant's published address: `confirm <id> "reply from <address> on <date>: go ahead"`.

## 2. Payments
`payments`. A matched payment with a confirmation → `launch <id>` (the "you're live" email waits for approval).
Paid without a confirmation: draft a reply asking for it. An amount mismatch puts the lead on hold for the owner.

## 3. Research (the supply count comes first)
1. `discover`, or web search ("Mechanicsburg PA restaurants", "... pizza", "... diner", local directories).
2. For each place, set `site_type`: `own_decent` | `vendor` (Square/Toast/Slice/order.online site) | `weak` | `broken` | `none`.
   Skip chains. With `skip_vendor_sites: true`, mark vendor-site places `skipped`.
3. Score the site 1 to 10. Start at 10 and subtract:
   - 3 if it isn't mobile-friendly;
   - 2 if the menu is only a PDF or image, or missing;
   - 2 if it looks dated;
   - 1 for no HTTPS;
   - 1 if hours, phone or address are hard to find;
   - 1 for broken links or pages;
   - 1 if it's slow or covered in popups.

   No site counts as 2. Above `max_design_score_to_pitch` → `skipped`.
4. Run `count` until at least 30 places are researched. **Stop and tell the owner** if 2 or fewer of 30 fall in
   "no or broken site + published email".
5. For pitchable places, collect only published facts (name, address, phone, hours, menu with prices, order and
   reservation links) and record `content_source` and `email_source`. Photos and review quotes are used only after the
   restaurant agrees (`permissions`).
6. Write `pitch`: `greeting`, optional `observation` with `observation_source`, `problems` (2, concrete and kind; only
   for places with a site), `presence` (for no-site places, e.g. "a Facebook page"), `highlights`.
7. Save as JSON like `examples/sample-lead.json` (no `id`), then `upsert` → `build <id>`.
8. Screenshot the preview at phone width and compare every price and hour to the source. Fix it or drop the lead.
9. `publish-previews`, then `queue`. Places with no published email go on the owner's in-person list.

## 4. In-person list
Write `data/in_person.md` with the best 5 no-email or no-site places: name, address, a good time to visit
(2 to 4 pm), the preview link, and the one question the owner should ask ("Would you pay $500 one time for this,
or less plus a small monthly fee that covers menu changes?"). Record what the owner reports back on each lead.

## 5. Follow-ups and housekeeping
`followups` (queued for approval, at most one per place), then `cleanup` to take down stale previews.

## 6. Digest
`digest` every weekday, even when nothing is waiting: its status line is how the owner knows the run happened. Put any
held items or problems at the top.
