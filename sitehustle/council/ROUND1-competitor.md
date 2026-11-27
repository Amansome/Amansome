# ROUND 1: Competing local web designer / DIY builder (archetype) (competitor)

**Dossier:** DOSSIER-01-launch-sitehustle-as-built-after-fixes-c.md. **Addenda read:** none (no ADDENDUM-01*.md existed when this was written).
**Round 1, independent:** no other member's report was read before this one was written.

**Position:** Do not launch as built. Change the offer first (option D), then run a small hand-approved test (option E) on that changed offer, aimed only at places that have no site and no POS or ordering-vendor site. As built, it is the kind of competitor I would be glad to face.
**Confidence:** medium

## 1. Position and why

1. **As built, SiteHustle helps me.** I win when a rival's offer is weak, carries hidden costs or loses trust. The offer as written has all three. "Free hosting (no monthly fee)" has no end date and sits on the user's own Netlify account (F9). The menu is fixed in static HTML that only the agent can change, and changes cost $75 a round after two rounds (F10; `templates/site/index.html.j2`). The pitch opens with a first-person compliment that the agent writes ("my family loves your vodka rigatoni", F6). In a town the size of Mechanicsburg, one owner who finds out that line was made up becomes my best referral source. Every restaurant whose menu prices go stale on a SiteHustle site, with "Site by <studio>" in the footer, is a site-rescue job for me in year two. Honestly, my seat gains most from option B. I still advise against it, because the council's job is the user's outcome.
2. **$500 is not the problem. What it buys is.** By public pricing, $500 sits between DIY (about $0 to $350 a year) and a freelance build (vendor blogs put it at about $1,500 to $6,000 plus $30 to $300 a month; see §3). That is a real gap in the market. But my clients don't keep paying me for the build. They keep paying for someone who changes the specials, prices and holiday hours within a day. SiteHustle offers neither self-editing (what Square, Wix and Slice give) nor a cheap human for updates (what a care plan gives). It offers a one-off build and then the agent at $75 a round. Restaurants raise prices often, so this is the main weakness.
3. **Against the free POS options, it loses for many of the best-scored leads.** The rubric rates "no website, only Facebook or a delivery app" as a 2, the strongest lead (F12; `RUNBOOK.md` §4.3). The discovery test found that many candidates already have Slice, Toast or order.online pages (Dossier §2). These are the restaurants that already have a vendor relationship which includes or upsells a website with menus that sync to the POS. Slice says its branded website comes with its ordering service. Square Online's free plan includes a site with online ordering (§3). The template only links out to the existing `order_url`, so the restaurant would be paying $500 for a nicer front page to an ordering system it already has. Some will want that, but many will not.
4. **Where it does beat the free options.** These are places with no site, or a broken one, and no POS website. Also places on Square's free plan that want their own domain, which that plan does not allow (§3). The template is good work: mobile call/directions bar, JSON-LD, map, tabbed menu (`templates/site/index.html.j2`). For a one-time $500, a restaurant gets something a DIY builder would charge about $200 to $350 a year for, with no labour. That niche is real. It is just narrower than the dossier implies (E2).
5. **The "free hosting forever" promise may already be broken on the current plan.** This is a cost the dossier missed (see §2): on Netlify's credit-based free plan, the preview pipeline alone likely uses up the monthly allowance. If the account is paused, paying customers' sites are on the same account. When "free forever" hosting goes down for a paying customer, a competitor gets the call.
6. **What would make it a strong competitor to me:** a small honest recurring fee (or a clean handover to the restaurant's own account), a way for the owner to update the menu, a true sender line, and targeting of only the no-site / no-POS-site niche. With those changes, I would expect a low-cost rival in the under-$1,000 segment that I would have to price against.

## 2. Where the dossier is wrong, incomplete or mis-posed

- **The hosting cost is missing, and "about $7 a month" is likely understated.** Netlify's current credit-based plans give the Free plan 300 credits a month, and each successful production deploy costs 15 credits (Netlify docs and changelog, §3). `cmd_deploy` creates one Netlify site per lead and POSTs a production deploy (`scripts/hustle.py` lines 300-334). Edits and `launch` redeploy. *Estimate:* at the configured 15 new previews per weekday, that is about 21 × 15 ≈ 315 production deploys a month, or ≈ 4,700 credits, about 15 times the free allowance. Even at 5 a day it is ≈ 1,600 credits. Netlify's own pricing page lists the Free plan's audience as "Individual". Community forum reports (user posts, not official policy) describe Free-plan teams whose production deploys were paused, and some whose sites went offline, after credits ran out. I did not find Netlify's terms on reselling hosting to clients; that is "searched, not found", not "does not exist". It needs checking. This also changes Q4/Q5: the hosting promise has a monthly cost that grows with every preview sent, not only with every sale.
- **Old previews are never removed.** I searched `hustle.py` for any delete or teardown of Netlify sites and found none. Every unsold restaurant's preview, with its name, menu and photos, stays live at `preview-<slug>.netlify.app` with no end date. That keeps adding to the account's site count and to the IP exposure the lawyer will care about. F7 states the preview's contents but not how long it stays up.
- **F5 is incomplete.** The first email's footer says "You got this one-time note…" (`templates/email/outreach.txt.j2`), but a follow-up is sent 5 days later (`followup.txt.j2`; F3). The footer is wrong in every case that gets a follow-up.
- **F6 is understated.** The runbook says the compliment should come "from real reviews or their story". The template, however, frames it as the sender's own experience ("I live nearby and {{compliment}}"), and the sample shows first-person family experience. Unless the user really ate there, that is a made-up personal claim. The dossier records the line but does not mark it as a truthfulness issue.
- **§2 leaves alternatives unpriced.** That framing hides the competitive question. I have filled it in from public sources (§3). The headline: a site plus online ordering is available for $0 a month on Square's free plan (no custom domain). Slice includes a website with its ordering plan. Toast Websites is free only for a 90-day trial. Wix and Squarespace run about $16 to $29 a month at the entry tiers. Freelance builds run in the low thousands.
- **The question is mis-posed.** Q4 ("Is $500 one-time, with free hosting and no end date, the right offer?") bundles a price with an open-ended liability. Those should be judged separately. The option list also lacks two clear model changes: (i) **handover**, where the site is deployed to the restaurant's own free account or exported, with no ongoing obligation; and (ii) **care plan**, a small monthly fee covering hosting plus menu and hours updates. These are the two ways competitors in my segment actually sell.
- **E2 and the rubric overrate "no website" leads** that have an ordering vendor (see §1.3). A no-site place with a Slice or Toast page should count as weaker, not stronger.
- **What the dossier does not say about the restaurant's domain.** Many restaurants with a "bad site" have their domain bundled with an old Wix, GoDaddy or Squarespace plan, or held by "the nephew". The launch email asks the owner to edit DNS themselves (`launched.txt.j2`). That is where many of my own projects stall. It is a hidden support load that the "zero involvement" goal does not account for.

## 3. Evidence

| Claim | Type | Source or method |
|---|---|---|
| Square Online's free plan lets a restaurant build a site with online ordering for no monthly fee. It charges 2.9% + 30¢ per online transaction in the US, with no custom domain on the free plan | fact (vendor page, via search summary; page not fetched directly) | square.com/us/en/online-store/plans; squareup.com/us/en/website-templates/restaurants |
| Toast Websites is free for a 90-day trial, then a paid subscription. Toast's ordering pricing is quote-based | fact (vendor terms) / third-party | pos.toasttab.com/websites-trial-terms-of-service; nerdwallet.com/article/small-business/toast-online-ordering |
| Slice says its pizzeria websites are free or customised and sync menus with Slice POS. Its pricing text lists $39 a month + $3 per card order for online ordering, which includes the custom website | fact (vendor marketing, via search summary) | slice.com/websites; slice.com/online-ordering |
| Wix Light is about $17 a month annually ($24 monthly) and Core $29. Squarespace entry tiers are about $16 to $29+ a month; sources conflict, and one reports a 2026 increase | fact (third-party compilations; official pages not fetched) | hostadvice.com Wix vs Squarespace 2026; tech.co/website-builders/wix-pricing |
| Freelance restaurant builds cost about $1,500 to $6,000, with care plans of about $30 to $300 a month | estimate (vendor blogs with an interest in the figures) | owner.com/blog/how-much-does-a-restaurant-website-cost; ambrite.ca maintenance plans |
| All-in restaurant platforms cost about $179 to $499 a month | estimate (vendor blog summary) | same search; not verified |
| Netlify Free = 300 credits a month; a production deploy = 15 credits; deploy previews are free; the Free plan's audience is listed as "Individual" | fact (Netlify docs and changelog, via search summary) | docs.netlify.com …/credit-based-pricing-plans; netlify.com/changelog/netlify-pricing-update-introducing-credit-based-plans |
| SiteHustle at 15 previews a day ≈ 4,700 credits a month | estimate (21 weekdays × 15 leads × 15 credits; ignores redeploys and bandwidth, so likely low) | arithmetic on `config.yaml` + `hustle.py` `cmd_deploy` |
| Free-plan teams have reported deploys paused, and sites at risk of going offline, after running out of credits | fact that such reports exist; not official policy | answers.netlify.com threads (e.g. "Free plan credits not renewed… site paused") |
| `cmd_deploy` creates one site per lead and does a production deploy; no teardown of unsold previews exists | fact | `scripts/hustle.py` lines 290-334; grep for delete found none |
| The outreach footer says "one-time note" while a follow-up is sent | fact | `templates/email/outreach.txt.j2`, `followup.txt.j2`, `config.yaml` `max_followups: 1` |
| The menu is static HTML; owners cannot self-edit; edits go through the agent; $75 a round after two | fact | `templates/site/index.html.j2`; `RUNBOOK.md` §1 |
| The site links out to an existing `order_url` and does not provide ordering | fact | `templates/site/index.html.j2` |
| Owners value ongoing menu and price updates more than the initial build | assumption (this seat's market experience; not measured) | none; testable in owner interviews |
| Lead supply in the true niche (no site, no POS site, public email) is a small fraction of the ~100 to 200 places | assumption | Dossier §2 discovery notes; not measured |
| Google Business Profile is free and is where most local diners find hours and phone numbers | fact (free: Google) / assumption (share of discovery) | google.com/business; share not measured |

## 4. Risks from this seat

- **B (launch as built):** My best case. The quiet failure is not a bounced email but stale menus. A restaurant raises prices, doesn't want to pay $75 or email an agent, and its site shows old prices with the user's studio name in the footer. Nobody alerts anyone. Customers complain at the counter, and the owner tells other owners. A second quiet failure is that Netlify credits run out and paying customers' sites stop updating or go offline. A third is the made-up first-person compliment found out in a small town where owners talk.
- **C (fixes only, same offer):** This removes the compliance and truthfulness problems, but the offer stays weak against POS options for vendor-linked leads, and the "free hosting forever" cost remains.
- **D/E (changed offer, small test):** This is the version that would compete with me. The risk to the user is small and capped. The risk to my seat is a cheap, honest rival in the under-$1,000 segment.
- **A (do nothing):** No harm to anyone. Restaurants keep their current options. The open niche (no-site places) stays with DIY builders and with people like me.

## 5. The cheapest decisive step

**Step:** Before any email is sent, take 30 real restaurants within the 9 km radius and, by web search and Google listing only (no outreach), sort each into: (a) has its own decent site; (b) has a POS or ordering-vendor site (Square, Toast, Slice, order.online); (c) no site or a broken one, no vendor site, **and** a published business email. Separately, read Netlify's current Terms of Service and Free-plan limits for client hosting. Total cost: about 1 to 2 hours of agent time, $0.

**Result decided now that changes my position:**
- If **(c) is 6 or more of 30 (≥ 20%)** and Netlify's terms allow client hosting on a plan that costs under about $10 a month in total, I move to supporting **E on a changed offer** with more confidence, and C becomes acceptable if hosting is handed over to each restaurant.
- If **(c) is 2 or fewer of 30**, the market this system is built for barely exists locally. My position becomes **A (do nothing)** or a manual, relationship-led model (D with a human seller), because automation has nothing to work on.
- For the owner-side question (do they value updates over the build), the deciding test is the first 20 to 30 approved pitches in E. If replies mostly ask "can I change it myself?" or "what does it cost later?", the care-plan or handover offer is confirmed.

## 6. Conditions and red lines

This seat supports a launch only if all of the following are true:
1. The offer states what happens after year one. Either hosting moves to the restaurant's own account (handover), or there is a disclosed recurring fee (e.g. $25 to $50 a month including menu and hours updates; an estimate in line with the low end of care-plan pricing). "Free hosting, no end date" on the user's account is not acceptable.
2. There is a stated menu-update path that is faster and cheaper than "email the agent, $75 after two rounds", or the price includes updates for a stated period.
3. Targeting excludes restaurants that already have a POS or ordering-vendor website, unless the pitch openly says it complements that site.
4. The pitch makes no first-person claims the user can't back up. The "one-time note" footer is corrected.
5. Unsold previews are taken down after a set period (e.g. 30 days after the last contact).
6. Netlify (or the chosen host) terms and costs are checked and costed into the price.

This seat has no red lines of its own; it argues from market reality. But it will not call the as-built offer competitive with the free and DIY options, because for vendor-linked restaurants it is not.

## 7. One line

Don't switch it on as built: change the offer to a handover or a small disclosed care plan with a real way to update the menu, aim it only at the no-site, no-POS-site niche, and test 20 to 30 hand-approved pitches before automating anything.
