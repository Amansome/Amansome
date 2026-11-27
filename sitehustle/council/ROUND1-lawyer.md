# ROUND 1: Small-business lawyer (flags issues only) (lawyer)

**Dossier:** DOSSIER-01-launch-sitehustle-as-built-after-fixes-c.md. **Addenda read:** none (no ADDENDUM-01*.md existed when this was written).
**Round 1, independent:** no other member's report was read before this one was written.

**Position:** Do not launch as built (B). The most I would support is a small, hand-approved test (E). Before any email goes out it needs a sending provider whose terms allow cold outreach, written terms at checkout, a fix so a payment from anyone other than the restaurant cannot trigger a launch, a pitch with no false first-person claims, and lead data kept out of the public repository. Automatic sending, and an AI negotiating on the user's behalf with no review, I oppose under every option.
**Confidence:** high that B as built should not run; medium on the exact list of fixes, because several points need qualified counsel.

*This seat flags issues and does not give legal advice. Each item below is a question for a Pennsylvania-licensed attorney and, for tax, a tax professional.*

## 1. Position and why

1. **The sending channel appears to break its own contract before any law comes into it.** A search of Resend's published Acceptable Use Policy returned wording that bans "unsolicited messages of any kind, including cold outreach, purchased lists, or scraped contact data" and requires that "all mail must be sent to recipients who have explicitly opted in" (WebSearch result citing resend.com/legal/acceptable-use; a direct fetch was blocked by this session's network, so I have not read the page myself). SiteHustle's whole outreach is exactly that: cold email to addresses scraped from public listings. If the search result is accurate, launching through Resend breaches the user's contract with Resend from email one, and the account can be closed with no refund. CAN-SPAM compliance does not cure a breach of contract. The dossier lists this as "not checked" (§6). It is the most checkable blocker on the table.
2. **The user carries full legal responsibility for what the agent says, and "zero involvement" does not reduce it.** Under CAN-SPAM, the business whose product is promoted is liable, and the FTC guide says you cannot contract that duty away. The agent writes the pitches, answers replies, offers discounts down to $400 (RUNBOOK §1), promises go-live "within 2 business days" (outreach template), and quotes paid edits. Each of those is a statement or promise made in the user's name. Automatic mode (F4) removes the only human check on irreversible outbound statements. My seat gains nothing from automation and is exposed by every unreviewed message.
3. **The pitch contains first-person claims the system cannot know are true.** The template opens "I live nearby and {{compliment}}". The runbook tells the agent to build the compliment from other people's reviews, and the sample is "my family loves your vodka rigatoni" (F6). A sentence built from a stranger's review and sent as the sender's own family's experience is a false statement of fact in a commercial message. CAN-SPAM itself polices headers and subject lines. But 15 U.S.C. §7707(b) leaves state laws against falsity or deception in commercial email un-preempted, and FTC Act §5 and Pennsylvania's consumer-protection statute reach deceptive practices generally. Whether a B2B pitch is covered is a question for counsel. In practical terms, in the user's own town, it is the line most likely to be caught out ("you've never eaten here") and to turn a pitch into a complaint.
4. **Money changes hands with no terms, and a stranger can trigger a launch.** F8 is correct that no terms or refund policy are shown. Worse, I checked the code: the "Make it yours" link sits in the public preview bar (`templates/site/index.html.j2`), and `cmd_payments` treats any completed Stripe session carrying that lead's `client_reference_id` as the restaurant paying (`scripts/hustle.py`, `cmd_payments`). It never checks who paid. The runbook then says to `launch` every paid lead. Launch removes the preview bar and `noindex`, sets robots.txt to `Allow`, and emails the restaurant "Thank you for your payment!" (`cmd_build`, `cmd_launch`, `launched.txt.j2`). So a diner, an employee without authority, a prankster or a competitor who reaches the preview can, by paying, publish an indexable site in the restaurant's name that the restaurant never agreed to. Then the user owes a refund and an explanation. No contract with the actual business exists.
5. **The offer makes open-ended promises the user can't keep with zero involvement.** "Free hosting (no monthly fee)" has no end date and runs on the user's own Netlify account (F9). The site is "yours", yet there is no transfer of the files, the Netlify site or any rights. Two edit rounds and the 2-business-day promise depend on a daily agent run that can stop. Once the user loses interest, cancels, or Netlify removes a free-tier site, every buyer has a breach-of-promise grievance against a named local person.
6. **The "previews are private" premise is weaker than the dossier says.** I checked the repository with the GitHub API: `Amansome/Amansome` is **public**, and the working branch `claude/friendly-pascal-r0rno3` is on that public remote. The runbook tells the agent to commit and push `data/`, `sites/` and `outbox/` every day. So restaurant names, owner email addresses, phone numbers, negotiation notes, reply contents, payment status and the full preview HTML, payment link included, would be readable and indexable on GitHub. That holds whatever `noindex` says on Netlify.

## 2. Where the dossier is wrong, incomplete or mis-posed

- **F11 is now settled:** the repository is public, and so is the working branch. Method: `gh api repos/Amansome/Amansome` returned `"visibility":"public"`, an unauthenticated `curl` of the API returned HTTP 200, and `gh api .../branches` lists `claude/friendly-pascal-r0rno3`. `data/leads.json` is currently `[]`, so nothing is exposed **yet**.
- **F7 overstates privacy.** `noindex` and robots.txt protect only the Netlify copy. The same HTML is committed to a public GitHub repository (RUNBOOK §6). F7 also leaves out three things the template publishes: (a) a footer reading "© {year} {restaurant}. Site by {studio}", which claims copyright in the restaurant's name on a page it never authorised; (b) schema.org `Restaurant` JSON-LD naming the preview URL as the restaurant's `url`; (c) a "What guests say" section quoting Google/Yelp review text (`templates/site/index.html.j2`).
- **F8 is incomplete.** It misses the third-party-payment problem in §1 point 4, and that the claim link carries `prefilled_email=<restaurant email>`, putting the owner's address in a public link (`claim_url` in `hustle.py`).
- **F5 is incomplete.** The first email says "You got this one-time note", but the system sends a follow-up five days later (F3). A small self-contradiction, but it is a false statement in the message. The template also never labels the email as an advertisement. CAN-SPAM requires that disclosure to be "clear and conspicuous" (FTC guide, W1). An offer with a price may be enough, but counsel should confirm. The opt-out depends on the agent reading Gmail. If the run stops for more than 10 business days, or the forwarding breaks, opt-outs go unhonoured, a CAN-SPAM violation no one would notice (W1).
- **W1 leaves out two duties that matter here.** First, the liability of the business whose product is promoted, even when someone else sends. Second, the "aggravated violation" for addresses harvested from sites that say they don't give out addresses. Runbook §4.4 scrapes footers and contact pages with no check for such a notice.
- **W2:** the FTC's 2025 adjustment puts the CAN-SPAM maximum at **$53,088 per email**, and a 2026 Federal Register notice says the 2025 levels continue (WebSearch: Federal Register 2025-01361 and the 2026 notice; secondary sources give the exact figure). "Can exceed $50,000" is right. Realistic exposure for a careful small sender is far below the maximum, so the figure should not be used to scare.
- **W5 is right but incomplete.** The PA Department of State says individuals and sole proprietors using a fictitious name must register. The consequence of not registering: no Pennsylvania court can be used to enforce a contract made under that name until registration, plus a possible $500 civil penalty (54 Pa.C.S. §331; 19 Pa. Code §17.211; via WebSearch, primary text not opened). `config.yaml` plans a studio name ("TODO Studio Name"), so this applies unless the user trades under their own legal name. Also from memory, not verified here: PA has a newspaper-advertising step for fictitious names, and a filing fee. Check with the Department.
- **§6 "sales tax: not researched" can be narrowed.** Secondary summaries of Pennsylvania Department of Revenue guidance (December 2024) say website development is **taxable when the site is transferred to the customer** and non-taxable when the developer keeps possession and control; separately stated hosting is non-taxable (WebSearch: summaries citing pa.gov "Canned Computer Software & Digital Goods"; older sources disagree). SiteHustle's offer ("it's yours", but hosted on the user's account) sits right on that line. A tax professional should decide whether the user needs a PA sales-tax licence and whether $500 must carry 6% tax.
- **Netlify terms (§6):** Netlify staff answers on its forum conflict. Some say commercial and client sites on the free tier are fine as long as hosting isn't resold. Others say client or reseller hosting expects a paid plan. The free tier can reportedly be removed without notice (WebSearch: answers.netlify.com threads; binding terms not read). "Free hosting, no end date" bundled into a $500 sale could count as resale. Unresolved.
- **Mis-posed question:** §8 Q2 asks what is "wrong, risky or deceptive". The dossier's own §7 records the builder's belief that the main blockers are account setup. From this seat the main blockers are contract (provider terms), deception (the compliment) and contract formation (who is buying, on what terms). None of them is setup.
- **Missing option:** a version of D where the user sends a handful of pitches personally from an ordinary mailbox under their real name, with written terms. That removes the provider-terms problem and most of the misrepresentation risk. It is not "zero involvement", and the dossier should say so plainly.
- **Not found after searching:** I searched the code and templates for any terms-of-service text, refund policy, IP or ownership transfer clause, or check of the payer's identity, and found none (`grep` over `scripts/`, `templates/`, `config.yaml`, `RUNBOOK.md`). That means none exists in this repository, not that the user hasn't drafted one elsewhere.

## 3. Evidence

| Claim | Type | Source or method |
|---|---|---|
| Resend's AUP forbids cold outreach and requires explicit opt-in | fact (secondary; primary page not opened) | WebSearch result quoting resend.com/legal/acceptable-use; WebFetch blocked by session network |
| Repository `Amansome/Amansome` is public; working branch is on the public remote | fact | `gh api repos/Amansome/Amansome` → `visibility: public`; unauthenticated curl → 200; `gh api .../branches` |
| Runbook pushes `data/`, `sites/`, `outbox/` daily | fact | RUNBOOK.md header and §6 |
| Any completed Stripe session with the lead's `client_reference_id` marks it paid, with no payer check | fact | `scripts/hustle.py` `cmd_payments` |
| Claim link is in the public preview bar and carries `prefilled_email` | fact | `templates/site/index.html.j2`; `hustle.py` `claim_url` |
| Launch removes noindex and allows robots, and sends a "Thank you for your payment!" email | fact | `hustle.py` `cmd_build(final=True)`, `cmd_launch`; `templates/email/launched.txt.j2` |
| Preview footer claims "© {year} {restaurant}"; JSON-LD names the preview as the restaurant's URL; Google/Yelp reviews are quoted | fact | `templates/site/index.html.j2`; `hustle.py` `cmd_build` |
| Outreach says "one-time note", but a follow-up is sent | fact | `templates/email/outreach.txt.j2`; `config.yaml` `max_followups: 1` |
| Compliment is built from third-party reviews and phrased as the sender's own experience | fact | RUNBOOK §4.6; `examples/sample-lead.json`; outreach template |
| Agent may discount to $400 and quote $75 edit rounds with no human review | fact | RUNBOOK §1 |
| No terms, refund policy, IP transfer or hosting term exists in the repo | fact (searched repo only) | grep over `scripts/`, `templates/`, `config.yaml`, `RUNBOOK.md`, `README.md` |
| CAN-SPAM maximum $53,088 per email, unchanged in 2026 | fact (secondary for the exact figure) | WebSearch: Federal Register 2025-01361; 2026 FR notice; FTC press release |
| CAN-SPAM does not pre-empt state laws against falsity or deception in commercial email | fact (secondary) | WebSearch: Cornell LII on 15 U.S.C. §7707(b); Omega World Travel (4th Cir.) |
| PA fictitious-name registration covers individuals; unregistered businesses can't enforce contracts in PA courts; possible $500 penalty | fact (secondary) | WebSearch: PA Dept of State fictitious-names page; 19 Pa. Code §17.211; 54 Pa.C.S. §331 |
| PA may tax website development when the site is transferred to the customer | estimate (secondary summaries; conflicting older sources) | WebSearch summaries of Dec 2024 PA DOR guidance |
| Netlify free tier for paid client sites: unclear, staff answers conflict | fact that the guidance is unclear | WebSearch: answers.netlify.com threads |
| Hotlinking a photo is not a safe harbour from copyright display claims outside the Ninth Circuit | assumption from general legal knowledge (e.g. a 2018 S.D.N.Y. decision rejected the "server test"); not checked this session | counsel to confirm for the Third Circuit |
| Photos on a restaurant's site are often licensed from a photographer, so the restaurant may not be able to permit reuse | assumption | general practice; not measured |
| The chance that a given recipient complains or contests is low per email but rises with automatic volume | estimate | reasoning: complaints scale with sends; no data |
| Pennsylvania-specific AI-disclosure duty for automated email | not checked | I did not search; flagged for counsel |

## 4. Risks from this seat

- **A. Do nothing:** no legal exposure. Nothing is lost except the opportunity.
- **B. Launch as built:**
  - *Obvious failures:* Resend closes the account (contract breach, if the AUP reads as found). A restaurant complains to the Pennsylvania Attorney General's consumer-protection bureau, or posts the email publicly. A chargeback lands with no terms to defend it.
  - *Quiet failures:*
    - Opt-outs go unhonoured during an agent outage.
    - Lead data and reply contents sit indexable on a public GitHub profile.
    - A third party pays and an unauthorised, indexable site goes live in a restaurant's name.
    - The agent makes a promise (price, timeline, feature) the user doesn't know about.
    - A photographer's copyright letter arrives for a hotlinked image.
    - Unregistered fictitious name and uncollected sales tax build up silently.
    - "Free hosting forever" becomes a liability the day the user stops.
- **C. After fixes:** most of the above is fixable in text and code. What remains: the user is still the legally responsible sender, and automatic mode still lets unreviewed statements out.
- **D. Change the model:** a human-sent, terms-first model removes most issues. A monthly fee plus a defined hosting term is legally cleaner than "free forever".
- **E. Small test:** low exposure *if* it uses a channel whose terms permit it, shows terms at checkout, and blocks third-party launches. Run through Resend as built, it still breaches the AUP. Small volume doesn't change that.

## 5. The cheapest decisive step

**Step:** open resend.com/legal/acceptable-use (and Resend's consent guidance) in a browser and read it in full. About five minutes. If it is ambiguous, email Resend support and ask in writing whether one-to-one cold B2B outreach to published business addresses is allowed.

**Decided now:**
- If the primary text **does** prohibit cold or unsolicited outreach, as the search result says, no option that sends through Resend gets this seat's support. B and C as specified are off the table until the channel changes.
- If the text permits it, or Resend confirms in writing, I move to supporting E, still only once the other conditions in §6 are met.

No result from this step moves me to B with automatic sending. That would need counsel's sign-off on the pitch wording and terms, plus the conditions below.

Second-cheapest step: a one-hour consult with a Pennsylvania small-business attorney. Bring the outreach template, the preview template and a draft one-page terms.

## 6. Conditions and red lines

**Must be true for this seat to support E (or a later C):**
1. A sending method whose terms permit one-to-one cold B2B email, confirmed from the primary text or in writing.
2. No false first-person statements: drop "I live nearby" unless it is literally true of the named sender, and drop compliments phrased as personal experience. The sender name must be the real person accountable for the message.
3. Fix "one-time note" so it matches the follow-up, and consider a plain line saying the email is a sales offer.
4. Previews: remove the "© {restaurant}" footer and the JSON-LD from previews. Leave out restaurant photos unless the restaurant permits them, and leave out third-party review quotes. Keep the preview bar and `noindex`.
5. Remove the payment link from the public preview page, or require a confirmation reply from the restaurant's published address before `launch`. Never launch on payment alone.
6. A one-page terms and refund policy linked and accepted at checkout. It should cover: what is delivered; who owns the site and files; the hosting term and what happens at its end (including handing over files); edit rounds; that the restaurant is responsible for the accuracy of its menu and prices after launch; refund conditions; no guarantee of business results; and a liability cap.
7. Lead data, outbox and site files kept out of the public repository: a private repository, or excluded from commits.
8. Every outbound message and every price or promise in a reply reviewed by the user for the duration of the test. The agent never negotiates on its own.
9. Before taking money: decide trading name versus legal name, register the fictitious name if one is used, and get a tax professional's answer on PA sales tax.

**Red lines (I will not support):**
- Sending through a provider whose terms forbid it.
- Taking payment with no terms describing what is delivered.
- Publishing an indexable site in a business's name without that business's confirmed agreement.
- Automatic sending or AI negotiation with no human review.
- Customer data in a public repository.

## 7. One line

As built, SiteHustle would breach its email provider's terms (per the published AUP as found), put false first-person claims in the user's name, take money with no terms, let any stranger trigger a public site in a restaurant's name, and push lead data to a public GitHub profile. Fix those and keep a human on every send, and a small test becomes defensible. Automatic launch does not.
