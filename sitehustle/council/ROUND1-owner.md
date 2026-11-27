# ROUND 1: Independent restaurant owner (the customer pitched) (owner)

**Dossier:** DOSSIER-01-launch-sitehustle-as-built-after-fixes-c.md. **Addenda read:** none (no ADDENDUM-01*.md file existed when this was written).
**Round 1, independent:** no other member's report was read before this one was written.

**Position:** No to B, and no to automatic sending at any point in the first 3 months. The most I would accept is E folded into D: a small test where a real, named local person approves every email by hand, and only after the fixes in section 6. If that test produces no serious replies, do nothing (A).
**Confidence:** high that the system as built would cost my trust and should not be launched. Medium on whether any version of this offer sells to owners like me.

## 1. Position and why

1. **The email opens with a personal claim a machine made up, and that is the first thing I would catch.** The template opens "I live nearby and {{compliment}}". The runbook tells the agent to write the compliment from other people's reviews, and the sample lead says "my family loves your vodka rigatoni" (fact: `templates/email/outreach.txt.j2`, `RUNBOOK.md` §4.6, `examples/sample-lead.json`). That makes the sender claim to be a customer, which the runbook's own ground rule forbids ("Never claim to be the restaurant, a customer...", `RUNBOOK.md` ground rules). In a small town I know my regulars. If I write back "which night did you come in?", the deal is dead, and so is the sender's name with every owner I talk to. That one line is enough for me to call it a scam.
2. **For most of the targets the email would say something false about our website.** The template always says "I was looking at {{name}}'s website and noticed {{problems}}". If the agent wrote no problems, the default is "it's hard to read on a phone" (fact: `outreach.txt.j2`; `hustle.py` `render_email`). The dossier itself says most candidates had no website of their own, and "no website" counts as a strong lead with a score of 2 (fact: dossier §2; `RUNBOOK.md` §4.3). A place that only has a Facebook page would be told someone looked at its website, or told it doesn't have one in a sentence that starts by saying someone looked at it. To me that reads as a mail merge.
3. **What I'd be paying for isn't really mine.**
   - The "live" site stays on the seller's Netlify account, at the same `preview-<slug>.netlify.app` address. Sites are created with the `preview-` prefix and `cmd_launch` sets `live_url` to that same subdomain (fact: `hustle.py` `cmd_deploy`, `cmd_launch`; `config.yaml` `hosting.site_name_prefix`). If I have no domain, my paid site's address has "preview" in it.
   - Hosting is "free" with no end date, on a free tier the provider can turn off without notice. Netlify's free tier may disable sites without notice, and Netlify staff have said reselling client hosting is expected to be on a paid plan (estimate from a web search summary of Netlify's terms and forum answers; not read from the primary page).
   - The email says "it's yours", but nothing gives me the files, the account, or what happens if the seller quits.
4. **Changing my menu would cost me, and I change my menu.** Two edit rounds are included, then $75 a round (fact: `RUNBOOK.md` §1; `config.yaml` `offer.includes`). A pizzeria changes prices a few times a year (assumption). Compare Square Online's free plan: no monthly fee, the owner edits the menu, and only card processing fees are charged; a custom domain needs a paid plan (estimate from a web search summary of square.com plan pages; not verified on the primary page). The offer also says nothing about my Google Business Profile, which is where my customers really find my hours (I searched the offer, templates and runbook for "Google Business" and found nothing).
5. **I would be told one price and the system can't charge it.** The runbook lets the agent offer $400. But there is a single fixed $500 Stripe Payment Link in config, and the Stripe key is read-only "Checkout Sessions: Read" (fact: `config.yaml` `offer.stripe_payment_link`; `hustle.py` `claim_url`; `README.md` setup step 4). No code makes a $400 link. If I'm promised $400 and the link charges $500, that is a pricing complaint waiting to happen. There are also no terms and no refund policy (fact: dossier F8, confirmed by grep).
6. **What my seat gains or loses.** A good, correct, phone-friendly site with my real menu would help me (assumption; I underrate this per my card). What I lose under B:
   - $500 for something I don't control.
   - My name, menu and photos posted publicly before I agreed.
   - Wrong prices or hours shown to anyone who has the link.
   - My restaurant's details and payment status in a public GitHub repository (section 2).

   Pitches already crowd my inbox. A bad one doesn't cost me much, but one that reads like a scam turns every owner in town against the next honest person who pitches.

## 2. Where the dossier is wrong, incomplete or mis-posed

- **F11 is now settled: the repository is public.** I ran `gh api repos/Amansome/Amansome --jq '{private,visibility}'` and got `{"private":false,"visibility":"public"}`. Its branches are `claude/friendly-pascal-r0rno3` and `main`, so the SiteHustle code, runbook and templates are already publicly readable.
  - `RUNBOOK.md` §6 tells the daily run to commit and push `data/`, `sites/` and `outbox/`. Every restaurant's name, email, phone, notes, preview HTML and payment status would therefore be published on GitHub.
  - GitHub pages can be indexed by search engines, so this goes around the `noindex` on the previews.
  - The repository's profile README carries the user's real name. Any owner who searches the studio can find the code, and with it the runbook line "The owner wants to do nothing except get paid".
  - For me this is the biggest factual gap in the dossier.
- **F6 is presented neutrally, but it is a deception problem.** The sample compliment breaks the runbook's own rule against claiming to be a customer. The dossier should flag that the two disagree.
- **F7 is incomplete.** Launched sites keep the `preview-` subdomain as their live address (`hustle.py` `cmd_launch` sets `live_url` from `netlify_subdomain`, which `cmd_deploy` created with the `preview-` prefix).
- **The $400 price isn't covered.** F10 lists the $400 floor but not that the payment setup cannot charge $400 (point 5 above).
- **§6 says how a restaurant updates its menu is "not specified". That is wrong.** The runbook specifies it: two rounds included, then $75 per round (`RUNBOOK.md` §1). The real gap is that the owner has no way to edit anything themselves.
- **The no-website case is missing.** The dossier says most candidates have no site of their own but does not connect that to the email template, which assumes a website exists (point 2 above).
- **§4b is missing the free alternatives.** It leaves "prices and features" open. Square Online's free plan is an obvious one (search summary above). Toast and similar POS online-ordering pages also exist (assumption on their pricing, not checked).
- **The trial is short, and it ends by date, not by results.** The script switches to automatic sending on the calendar date, whatever happened in the trial (`hustle.py` `cmd_send`, lines 443 to 446). If setup lands this weekend, that is about 5 business days (estimate: Mon 30 Nov to Fri 4 Dec 2026). Nothing checks reply quality or complaints before the switch.
- **Question 4 is mis-posed.** It asks whether $500 is the right price. My question is what I get that I can't get free, and who keeps my hours and prices right. Price comes second to ownership and upkeep.
- **The sender can't be checked.** The From line is first name only, then a studio name and a PO box; `business.website` is optional and empty (fact: `hustle.py` `send_email`; `config.yaml`). The emails give no phone number and no last name. Nothing lets me check that this is a real local person, which is the first condition on my card.

## 3. Evidence

| Claim | Type | Source or method |
|---|---|---|
| The repository is public, and the SiteHustle branch is pushed to it | fact | `gh api repos/Amansome/Amansome` returned `visibility: public`; the branches list includes `claude/friendly-pascal-r0rno3` |
| The daily run commits and pushes lead data, sites and outbox | fact | `RUNBOOK.md` intro and §6 |
| The email opens with "I live nearby and {{compliment}}"; the sample compliment is "my family loves your vodka rigatoni" | fact | `templates/email/outreach.txt.j2`; `examples/sample-lead.json` |
| The runbook forbids claiming to be a customer | fact | `RUNBOOK.md` ground rules |
| The email always says "I was looking at X's website"; the default problem is "hard to read on a phone" | fact | `outreach.txt.j2`; `hustle.py` `render_email` |
| Most discovered candidates had no confirmed website of their own | fact (as reported, not independently verified) | Dossier §2 |
| The live site address keeps the `preview-` prefix | fact | `hustle.py` `cmd_deploy` (site name = prefix + slug), `cmd_launch` (`live_url` from `netlify_subdomain`) |
| No code supports charging $400; the Stripe key is read-only | fact | `hustle.py` `claim_url`; `README.md` step 4; grep found no discount code |
| Edits after two rounds cost $75 each | fact | `RUNBOOK.md` §1 |
| No terms, refund policy or Google Business Profile service in the offer | fact (searched templates, runbook, README, config; found nothing) | grep for "terms", "refund", "Google Business" |
| The switch to automatic sending is by date only | fact | `hustle.py` lines 443 to 446 |
| Square Online has a free plan (no monthly fee, owner-editable, custom domain needs a paid plan) | estimate | Web search summary of square.com plan and restaurant pages; primary page not opened |
| Netlify's free tier can remove sites without notice, and reselling client hosting is expected to be on a paid plan | estimate | Web search summary of Netlify terms and forum staff answers; primary pages not opened; the answers may be dated |
| Owners change menu prices several times a year | assumption | My card's knowledge; not measured |
| A first-person claim found to be fake ends the deal and spreads among local owners | assumption | My card's red lines and priorities; not measured |
| The trial covers about 5 business days | estimate | Calendar count from a setup on 28 to 29 Nov 2026 to `trial_ends` 2026-12-07 |

## 4. Risks from this seat

- **A (do nothing):** I lose nothing. A few owners who would have liked an honest, cheap site don't get one. That cost is small and nobody notices it.
- **B (as built):**
  - I get an email that claims to be from a customer and describes a website I don't have. My menu, prices, hours and photos sit on a public URL, and in a public GitHub repo, before I agree.
  - If I pay, I own nothing, my "live" address says "preview", my hosting rests on someone else's free account, and changing prices costs me $75.
  - **The quiet failure:** no complaint is filed, but owners mention "that fake website guy" to each other and to their suppliers. The user's name in their own town is damaged, and no metric records it.
  - **The obvious failure:** the AI copies a price or the hours wrong from a PDF menu, and I see my restaurant misrepresented.
- **C (after fixes, then automatic):** this is better, but automatic sending still means nobody checks each pitch, and the AI can still invent the friendly line or misread a menu with no human looking. I object to the automatic part, not the fixes.
- **D/E (human approves every email, small capped test):** the risk is limited to 20 to 30 owners. My remaining worry is that a person approving 15 emails in 2 minutes a day is not really checking them (estimate: that is about 8 seconds an email, from the README's "about 2 minutes a day").

## 5. The cheapest decisive step

**Biggest open question for my seat: would an owner like me pay for this at all, once the deception is removed and the ownership terms are clear?**

**Step:** after the fixes in section 6, the user sends 20 to 25 pitches by hand-approval only, signed with their real full name, a phone number, and an honest opener ("I'm a local web designer; I built this from your public menu"). The previews are not committed to a public repo. The cheaper first move, if the user will accept about 2 hours of involvement, is to show one preview on a phone to 5 local owners in person between 2 and 4 pm and ask whether they would pay $500 one time, or a lower price plus a monthly fee that includes menu updates.

**Decided now, for the 20 to 25 email test:**
- **I move to A (do nothing)** if it gets 0 replies asking about price or changes, or any complaint or angry reply.
- **I stay at "human-approved D, never automatic"** if it gets at least 1 paid sale or at least 3 serious replies, with no complaint and every preview's menu, prices and hours confirmed correct by the owners who replied.
- **I would revisit automatic sending only** after at least 50 hand-approved sends with zero factual errors found in previews and zero complaints. That cannot happen inside the trial week as configured.

## 6. Conditions and red lines

**Must be true before any email goes to an owner like me:**
1. No fabricated first-person claims. Remove "I live nearby and {{compliment}}" as written. An opener can cite a named public review ("a Google reviewer called your rigatoni the best in the county") but never "my family loves". There is a separate opener for places with no website.
2. Restaurant data, previews and outbox are not in a public repository. Either make the repository private or keep `data/`, `sites/` and `outbox/` out of git.
3. The sender is verifiable: full name, a phone number, and a real website or local presence in every email.
4. Previews are not on a guessable public URL before consent. At minimum use an unguessable link, and photos are used only with permission.
5. Clear written terms at checkout (one page): what I get, a refund if I'm not happy at launch, how long hosting lasts and what it costs after that, and that I can have the files and move the site.
6. The live site does not carry "preview" in its address.
7. Menu and hours updates are workable: either I can edit them myself, or routine menu and price updates are included. A $75 fee per price change is not workable.
8. The price promised is the price charged. Remove the $400 negotiation, or build a real way to charge it.
9. Every email is approved by a human. Remove the date-based automatic switch.

**Red lines I will not accept:** a fake personal claim of being a customer; my menu or prices shown wrong in public; my name, photos or payment status published without my agreement; ongoing costs or a hosting end that weren't disclosed; pressure or repeated chasing beyond the one follow-up.

## 7. One line

As built, this reads like a scam to the owner it pitches (a made-up "my family loves your food", a website we may not have, our data on public GitHub, a "preview" address after paying, and $75 to change a price). Fix those, keep a named human approving every email, and test it on 20 to 25 owners. If nobody bites, don't launch.
