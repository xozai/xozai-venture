# Phase 1 — Foundation: Strata Civic Solutions

Skill: `.claude/skills/pitch-deck/SKILL.md`. Built by Scribe 2026-09-01 on joseleos's
instruction ("Generate a pitch deck for Strata using the pitch deck skill", Strata channel,
event `ef6afb97…`). Phase 0 (`interview.md`) had six questions open; joseleos asked for the
deck rather than answering them, so this foundation is built from **accepted artifacts only**
and every gap is carried forward as a marked flag rather than filled with invention
(anti-BS rule 11).

**Sources used, in order of authority**
1. `product/finance/strata/MODEL.md` — every number on the deck.
2. `research/spaces/GOVTECH_MUNICIPAL.md` — buyer, motion, procurement, channels.
3. `OUTBOX/Strata_Market_Competitive_Research.docx` (Researcher, 2026-08-30) — site copy
   verbatim, team bios, competitor set, national counts.
4. `OUTBOX/STRATA_BMC_2026-08-30.md` — business model canvas.
5. `product/FINANCIAL_BRIEF_STRATA.md`, `docs/DECISIONS.md` — accepted parameters.

**Not used, and why:** `~/Documents/Strata_GTM_Strategy.docx` and `Strata_Market_Research.docx`
are cited by the brief but **are not on this disk** (`find /Users/jleos -maxdepth 4 -iname
"*Strata*"` returns neither). The GTM positioning in this foundation therefore comes from the
space profile and the BMC, both of which were derived from those docs while they existed. Per
the skill, a deck should not be built on a GTM plan nobody can open — flagged at Gate 1.

---

## 1. Business audit

**The pain.** A mayor or council member in a Texas city of 10k–50k is a part-time official
with a separate full-time job and **no staff of their own**. The agenda packet is 200–400
pages and arrives days before the vote. The current workflow is Ctrl+F and a phone call to
the clerk. The cost of being under-prepared is not a bad quarter — it is being wrong on the
record, in public, on video. Appointed board and commission volunteers, who outnumber elected
officials roughly 5:1, are served even worse.
*Source: `GOVTECH_MUNICIPAL.md` buyer archetypes; research brief §3.3.*

**The inevitable future.** Every one of those packets is already a public document. The city
published it. Retrieval over a city's own record is now cheap and accurate enough to answer a
question in seconds with the page it came from. It is not a question of whether officials get
an answer layer over the record — every incumbent in the category shipped an AI feature in
2026 (CivicPlus Intelligence, Granicus, OpenGov). The question is whose, and whether it is
built for the person casting the vote or for the staff preparing the packet.

**What blocks it.** Three things, all trust-shaped, none technical:
- *Hallucination governance.* The most common AI-related item on a 2026 council agenda is
  passing an AI-use policy. An uncheckable answer is disqualifying in a public meeting.
- *Procurement.* Above $50,000 a Texas city must competitively bid (Tex. Loc. Gov't Code
  §252.021). Above that line a sale takes a season; below it a city manager signs.
- *Change cost.* A resource-constrained city will not migrate records or train staff for a
  research tool.

**The solution.** Strata answers plain-language questions over the city's own published
record — budgets, ordinances, minutes, contracts — and shows the page the answer came from.
Three surfaces: **Ask Strata** (Q&A), **Meeting Prep** (agenda-item briefs with history and
cost), **City Snapshot** (one-page financial picture). Nothing migrates; the city keeps
publishing exactly as it does today.

**Hard value.** Meeting prep goes from hours of packet reading to minutes of cited answers,
for every official and every board volunteer on one contract, at $3.6k–$18k/yr — inside the
signature authority of one city manager.
**Soft value.** Confidence at the dais. The official verifies the citation, so the judgment
and the accountability stay exactly where the law puts them. That is what makes it sellable
into a body that has just written itself an AI-use policy.

---

## 2. Investor psychology map

**Reasons to invest**
- **Sharpest wedge in a crowding category.** Of six reviewed players, Strata is the only one
  built exclusively for the individual elected or appointed official's moment before a vote.
  Ordinal sells across departments; Aware and CivicSummary sell to the public and the press;
  CivicPlus, Granicus and OpenGov sell to staff. Nobody else's primary user is the person
  voting. *(research brief §5.3)*
- **Distribution asset that money cannot buy quickly.** Senior Municipal Advisor **Ralph
  Gutierrez** is a two-term mayor and council member of Schertz — the live demo city — with
  ~50 years of public service. Elected officials take a former mayor's word over a vendor's.
  **Raquel Gutierrez** brings 30+ years of Central Texas civic engagement. This is the entire
  early channel and it is not purchasable at any seed size.
- **Capital efficiency that is unusual even for B2G.** The accepted model shows operating
  income positive from **month 19** and a **89% gross margin** with **zero** outside capital.
  The binding constraint across all three scenarios is ≈$40k of working capital, not a round.
- **Structurally sticky revenue.** Once a line is in a municipal budget it is re-adopted;
  public-sector SaaS gross retention is commonly reported at 90–95% (vendor-reported, tagged
  low-confidence in the model, which uses 0.6%/mo logo churn ≈ 93%/yr).

**Reasons not to invest — say them first, on the slide**
- **No paying customer.** Schertz is a live demo city that has **not** committed to paying.
  Zero starting paying cities is an explicit model input, not an oversight.
- **A funded direct competitor moving faster.** Ordinal AI raised $1M seed (Aug 2025, Plains
  Venture Partners) and is live in 7+ named cities across five states.
- **Incumbent good-enough AI.** A city already paying CivicPlus or Granicus can get
  summarization as an upsell with no new vendor, no new contract, no new procurement cycle.
- **Founder bandwidth is the growth rate.** The base case is 0.35 new paying cities per month
  because one founder is doing every demo. That is the model's real ceiling.
- **Small stated market.** Bottom-up, honestly counted, the Texas beachhead is ≈$2.2M SAM.
  A national number exists (19,519 municipalities) but is deliberately unmodeled.

**Moat analysis (Seven Moats, `references.md`)**
| Moat | Strata | Reading |
|---|---|---|
| Brand/trust | **Strong-forming** | Citation discipline is the brand; "an answer you cannot check is an answer you cannot use" |
| Distribution | **Strong** | Former-mayor advisor + TML/TCMA + peer referral among officials who all know each other |
| Switching costs | Medium | Per-city ingestion + budget-line inertia; low technical lock-in |
| Network effects | Weak | Per-city instance; no cross-city effect designed in yet |
| Economies of scale | Medium | COGS is per-city inference (~$75/mo), so margin is high but not increasing |
| Counter-positioning | **Strong** | Incumbents sell to staff; serving the official directly is a customer they are structured to under-serve |
| Cornered resource | Medium | Advisor relationships are real but personal, not contracted |

**Risk onion (outer = investor's first worry, inner = the one that actually kills it)**
1. *Outer — market:* "Isn't this a feature CivicPlus ships next quarter?" → Answer: it already
   did, for staff. The buyer here has no staff.
2. *Middle — competition:* "Ordinal is funded and ahead." → Answer: broader surface, shallower
   wedge; different buyer inside the same building.
3. *Inner — execution:* **one founder, 0.35 cities/month, and a $29k cash trough at month 18.**
   This is the real risk, and the ask is sized to exactly this.

---

## 3. Traction narrative

Honest position: **pre-revenue, one live demo city, product built and shipping.**

| Asset | Status | Source |
|---|---|---|
| Product | Built and live; Ask Strata / Meeting Prep / City Snapshot in production | stratacivicsolutions.com; `FINANCIAL_BRIEF_STRATA.md` |
| Reference city | Schertz, TX (~50k) — live demo city with cached example queries on-site; **not committed to paying** | research brief §2.4; joseleos 2026-08-30 |
| Customer discovery | 4 council interviews completed | HermesX note 2026-06-27 — **second-hand, unverified by Scribe** |
| Entity | Delaware Public Benefit Corporation, foreign-qualified in Texas | joseleos 2026-08-30 15:28 |
| Pipeline | **UNKNOWN — needs joseleos** | Phase 0 Q5 unanswered |

Anti-BS rule 4 applies: the deck states these as facts with dates, not as momentum. There is
no usage metric on the deck because nobody has given me one, and a fabricated one would be
the fastest way to lose the room.

---

## 4. Team assessment

Not a bio list — the question is *why this team wins this problem*.

- **Holly Richard, Founder/CEO.** Doctor of Physical Therapy; previously built healthcare and
  fitness businesses. An outsider to govtech. Read positively: no assumption that the
  incumbents' staff-facing frame is the right one — which is exactly the assumption Strata
  breaks. **The personal "why municipal records" is not documented anywhere I can read, and
  the team slide is weaker without it. Flagged for joseleos.**
- **Helena Carre, Founder/CTO.** Bio not published on the site. Researcher flagged this as a
  visible trust gap for a buyer being asked to trust an AI tool with governance decisions.
  It is a bigger gap on an investor deck than on the website. **Flagged.**
- **Ralph Gutierrez, Senior Municipal Advisor.** ~50 years public service; USAF veteran; 20
  years federal judiciary leadership; **two-term mayor and council member of Schertz** — the
  demo city. The single strongest credibility asset with the exact buyer.
- **Raquel Gutierrez, Municipal Outreach Advisor.** 30+ years Central Texas civic engagement;
  drives municipal partnerships and pilot development.

**Team placement decision (required by Phase 2): slide 8, mid-deck — product-led open,
team as the go-to-market moat.** Reasoning: the product is built, live and demoable, so the
strongest opening is the problem and the product, not the founders. But the team cannot go
last either, because in this category the *distribution* is the differentiated asset — a
former mayor of the reference city is the answer to "how will you ever reach 230 city
councils." Placing it immediately after the buyer/procurement slide makes it read as the
answer to the question the buyer slide raises. It is not placed first because the founder's
own domain story is currently undocumented; if joseleos supplies it, revisit and consider
slide 3.

---

## 5. Competitive positioning

Full disclosure, per anti-BS rule 3 — the deck names all six and the workaround.

| Vendor | Primary buyer | Core job | Scale signal | Overlap |
|---|---|---|---|---|
| **Strata** | Elected/appointed officials | Prep before a vote, cited answers | 1 demo city, pre-revenue | — |
| Ordinal AI | Officials + staff, multi-dept | Research, live meeting Q&A, public chatbot | $1M seed; 7+ live cities | **High** |
| CivicSummary | Public + officials | Summaries + follow-through tracking | Early pilots (West Hollywood) | Medium |
| Aware | Public / press / residents | Post-meeting summaries, news digest | 3,800+ cities claimed, "infancy" usage | Low-Med |
| CivicPlus | City staff | AI-assisted agenda/minutes drafting | Large installed base; AI as upsell | **Med-High** |
| Granicus | City staff, larger govs | Records/comms summarization | Entrenched enterprise incumbent | Medium |
| OpenGov | Finance/budget staff | Budgeting, ERP, performance reporting | Well-funded incumbent | Low (adjacent data layer) |

**The real incumbent is the manual workaround** — Ctrl+F through the packet and call the
clerk. It is free, universally deployed, and every prospect is currently satisfied enough with
it to have not bought anything. The deck says this out loud.

**Positioning line (carried into Phase 2):** *Everyone else built AI for the people who
prepare the meeting. Strata built it for the people who have to vote at it.*

---

## 6. Cross-check against MODEL.md and the GTM/BMC — contradictions found and resolved

| Claim in circulation | Status |
|---|---|
| "~34 paying cities base case" (early brief) | **Superseded.** Engine says **31.2**. Deck uses 31. |
| "~$20K/60-day pilot, ~$50K/yr" (HermesX BMC from June/July meeting notes) | **Contradicts** the accepted pricing (Starter $3.6k / Core $9.6k / Growth $18k, ACV held under the §252.021 $50k bid threshold) and the model's $9,600 ACV. Deck uses the accepted model. **Flagged — if $50k/yr is live in sales conversations, the model and the no-bid design constraint both break.** |
| "Founder salary $150k memo" (brief) vs `$184,000` (MODEL.md Y1 memo line) | Deck cites neither; both are memo, $0 cash. No deck impact. |
| GTM docx "draft pending sign-off" | Still unsigned, and now not on disk. Positioning above is sourced from the space profile + BMC instead. |

---

## 7. CoVe pass — four readers

- **Skeptical VC.** "Pre-revenue, $2.2M SAM, funded competitor ahead, one founder. Why is this
  venture-scale?" → It may not be, at this ask. The deck's honest answer is capital efficiency
  and a distribution asset, and it asks for working capital, not a venture round. Any investor
  looking for a $100M outcome should be told no on slide 2 rather than slide 20.
- **Domain expert (city manager).** "Who owns the answer if it's wrong?" → The official does;
  the citation is the mechanism. Covered on the trust slide and in objections.
- **Storyteller.** The arc holds: *the people who vote have no staff → the answer is already
  published → here is the machine that finds it and shows its work → here is why a former
  mayor can get us into 230 city halls → here is what it costs to prove it.*
- **First-time reader.** Biggest confusion risk is Strata vs. "AI meeting summaries," which
  everyone in this category sounds like. Fixed by leading every slide with the official's
  moment, not the technology.

---

## Gate 1 — open items for joseleos (deck ships with these marked, not invented)
1. **Founder story** — Holly's "why municipal records." Team slide is complete but flat without it.
2. **CTO bio** — Helena Carre. A blank CTO on an investor deck is a live objection.
3. **Traction specifics** — Schertz usage, any verbal commitments, pilots in flight.
4. **The ask** — deck currently asks for **$40k working capital + 5 pilot cities**, the only
   figure the accepted model supports. An institutional round requires a financed model re-run.
5. **Pricing contradiction** — $9.6k Core (model) vs the "~$50k/yr" floated in the June/July
   meeting notes. These cannot both be true.
6. **joseleos's own role** — the interview assumes joseleos is the founder; the published team
   page does not list him. The deck says nothing about him either way. Confirm.
