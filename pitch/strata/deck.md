---
marp: true
theme: strata
paginate: true
---

<!--
Phase 5 — Strata Civic Solutions pitch deck v1. Scribe, 2026-09-01.

This file is the canonical text of the deck. The shipped render is
`Strata_Pitch_Deck_v1.pptx` / `.pdf`, built by `build_deck.py` on the Strata deck design
system (`deckkit.py`) so this deck matches the GTM and research decks already delivered in
the Strata channel. The skill specifies Marp + `theme.css`; `theme.css` is vendored here and
this file carries the Marp front matter, but no `marp` binary exists on this machine, so the
PPTX/PDF built from `build_deck.py` is the artifact of record. Regenerate with:
  ~/.buzz/.scratch/pptx-venv/bin/python build_deck.py

Every number traces to product/finance/strata/MODEL.md. Every quoted line is verbatim from
stratacivicsolutions.com via the 30 Aug 2026 research brief. Nothing here is invented; the
three things nobody has told us are marked NEEDS JOSELEOS and rendered in red monospace so
they cannot be presented by accident.
-->

<!-- _class: lead invert -->

# Strata Civic Solutions

## Know the record before you vote.

Municipal decision intelligence: plain-language answers over a city's own published record —
budgets, ordinances, minutes, contracts — cited to the page.

Delaware Public Benefit Corporation, foreign-qualified in Texas · San Antonio, TX · 1 September 2026

`Draft for joseleos — three slides carry unresolved placeholders. Do not present externally as-is.`

---

# The packet is 300 pages. The vote is Tuesday.

A council member in a Texas city of 10,000–50,000 is a part-time official with a separate
full-time job and no staff of their own.

**200–400** pages in a typical agenda packet · delivered days before the vote, read on personal time
**0** staff reporting to an elected official · city staff serve the institution
**~5 : 1** board volunteers per elected official · the least-served users in govtech

**The cost of being under-prepared is not a bad quarter. It is being wrong on the record, in public, on video.**

<!-- Source: research/spaces/GOVTECH_MUNICIPAL.md; Strata market & competitive research, 30 Aug 2026, §3. -->

---

# They already tried the obvious fix.

**What they do now** — Ctrl+F the PDF for a word they hope appears · call the clerk, who has
their own job · ask the colleague who has been on council longest · vote, and find out afterwards.

**What it costs them** — hours per packet on unpaid time · precedent they never find because
they did not know the word for it · cost history three budgets back · deferring to staff on a
decision that is legally theirs.

**The competitor we actually have to beat is Ctrl+F.**

---

<!-- _class: quote -->

# Your city already published the answer.

> “Search returns documents and leaves the reading to you.
> Strata returns an answer, and the documents behind it.”

Strata creates no new data and asks the city to change nothing. Budgets, ordinances, minutes
and contracts are already published under the Public Information Act. The record is not
missing — it is unusable at meeting-prep speed.

---

# 2026 is the year cities wrote their AI policies.

1. **Incumbents shipped AI into installed bases.** CivicPlus, Granicus and OpenGov all
   released AI summarization in 2026 — built for the staff who prepare the meeting.
2. **Councils responded with governance, not enthusiasm.** 67% of municipal leaders report
   actively integrating AI; the agenda item is the use policy, and the objection is hallucination.
3. **So the adoptable form is citation-first.** A tool that shows the page the answer came
   from clears an AI-use policy. A tool that summarizes without one does not.

**The window is the gap between incumbents serving staff and someone serving the official.**

---

# Ask a question. See the page it came from.

**Ask Strata** — plain-language Q&A over the city's own budgets, ordinances, minutes and
contracts; every answer resolves to a specific page. *The question you had at 10pm, answered
before the meeting.*

**Meeting Prep** — each agenda item briefed with its own history and what it has cost the city
before. *Hours of packet reading become minutes of reading that matters.*

**City Snapshot** — one page: revenue, spending, tax rates, payroll by position. *A new board
volunteer is useful in their first month, not their first year.*

Setup is on us. The city does not change how it works, and nothing migrates.

---

<!-- _class: invert big-number -->

# “An answer you cannot check is an answer you cannot use.”

The citation is not a feature of the product. It is the product. The official verifies the page
and then speaks — so the vote, the discussion and the judgment stay exactly where the law puts them.

Strata assists; it does not draft the record or determine the vote. An error is an embarrassment
and a churn event — not statutory liability. That boundary is a design decision.

---

# One city manager can sign this.

Texas requires competitive bidding above **$50,000** (Tex. Loc. Gov't Code §252.021).
Our top tier is **$18,000**. That is a design decision, not an accident.

- **Economic buyer: the city manager.** Controls the software line, signs alone below the threshold.
- **Champion and user: mayors, council, boards.** They feel the pain; they do not hold the budget.
- **Gatekeepers: the clerk, and IT in 50k+ cities.** Ally or blocker — and a security questionnaire.
- **Demo to signature: 4–8 weeks.** Not a procurement season.
- **Buying window is Aug–Sep.** Texas fiscal years start Oct 1; budgets adopt just before.
- **No sales tax, no per-seat fees.** Municipalities are exempt (Tex. Tax Code §151.309).

---

# Our senior advisor was mayor of our reference city. Twice.

**Ralph Gutierrez — Senior Municipal Advisor.** Two-term mayor and council member of Schertz,
our demo city. ~50 years public service, USAF veteran, 20 years of federal judiciary leadership.

**Raquel Gutierrez — Municipal Outreach Advisor.** 30+ years of Central Texas civic engagement;
the warm-intro channel is hers.

**Holly Richard — Founder / CEO.** Doctor of Physical Therapy; previously built healthcare and
fitness businesses. An outsider to govtech — which is why the product is built for the official,
not the staff.

`[ NEEDS JOSELEOS ] Helena Carre, Founder/CTO — no published bio. A blank CTO on an investor`
`deck is a live objection. Also missing: Holly's own account of why municipal records.`

**A former mayor's recommendation is how you get into 230 city halls. It is not purchasable at any seed size.**

---

# Live product. One demo city. Zero paying customers.

| | Status | As of | Source |
|---|---|---|---|
| Product | Built and live — Ask Strata, Meeting Prep, City Snapshot in production | Aug 2026 | Company site |
| Reference city | Schertz, TX (~50k) — live demo city; has not committed to paying | Aug 2026 | Site + joseleos |
| Customer discovery | 4 council interviews completed | Jun 2026 | HermesX note — second-hand |
| Entity | Delaware PBC, foreign-qualified in Texas | Aug 2026 | joseleos |
| Revenue | $0. Zero paying cities is an explicit model input, not an oversight. | — | MODEL.md |
| **Pipeline** | **NOT DISCLOSED — no verified commitments, LOIs or pilots in flight** | — | **NEEDS JOSELEOS** |

No usage metric appears on this deck because no one has given us a verified one. A number we
cannot defend is worth less than the blank.

---

# Everyone else built AI for the people who prepare the meeting.

| Vendor | Primary buyer | Core job | Scale signal | Overlap |
|---|---|---|---|---|
| **Strata** | Elected & appointed officials | Prep before a vote, cited answers | 1 demo city, pre-revenue | — |
| Ordinal AI | Officials + staff, multi-dept | Research, live meeting Q&A, public chatbot | $1M seed; 7+ live cities | High |
| CivicSummary | Public + officials | Summaries + follow-through tracking | Early pilots (West Hollywood) | Medium |
| Aware | Public, press, residents | Post-meeting summaries, news digest | 3,800+ cities claimed; thin usage | Low–Med |
| CivicPlus | City staff | AI-assisted agenda & minutes drafting | Large installed base; AI as upsell | Med–High |
| Granicus | City staff, larger governments | Records & comms summarization | Entrenched enterprise incumbent | Medium |
| OpenGov | Finance & budget staff | Budgeting, ERP, performance reporting | Well-funded incumbent | Low |
| **Ctrl+F** | Everyone, today | Find the word, hope it is the right one | Free. Universally deployed. | **The one to beat** |

---

# $3,600 to $18,000 a year. 89% gross margin.

Starter **$3,600** · Core **$9,600** (the modeled ACV, our beachhead tier) · Growth **$18,000**.
COGS is ≈$75/city/month of inference and retrieval — it scales with packet volume, not seats.
Margin holds 79–91% across all three scenarios.

- **Annual invoice, ACH or check.** Onboarding $500–1,500, waived for pilots.
- **Usage bundled.** An official who uses it twice a week costs the same as one who uses it twice a year.
- **ACV is capped by design.** Everything stays under the $50k bid threshold — which is what makes the 4–8 week cycle possible.
- **Retention is budget-line retention.** Model uses 0.6%/mo logo churn ≈93%/yr; the 90–95% public-sector figure is vendor-reported and low-confidence.

---

# 230 Texas cities in our tier. We counted them one at a time.

- **230** Texas cities, 10k–50k population × $9,600 Core = **≈$2.2M SAM** — the beachhead
- **1,224** Texas municipalities, all sizes — the state expansion path, unmodeled
- **19,519** U.S. municipalities (+16,360 towns) — context only. We do not claim it.

**A $2.2M beachhead is a small number and we are not going to dress it up.** It is the number
we can defend, city by city, against a published population table. If a fund needs a national
TAM underwritten today, this is the wrong stage of this company.

---

# Thirty-one cities and break-even in month 19 — on founder effort alone.

| | Paying cities (end) | Revenue | Operating income | Ending cash |
|---|---|---|---|---|
| Year 1 (FY27) | 5.4 | $26,660 | −$13,104 | −$3,104 |
| Year 2 (FY28) | 14.8 | $103,894 | −$16,398 | −$19,502 |
| Year 3 (FY29) | 31.2 | $248,290 | +$51,103 | +$31,600 |

**Month 19** first month of positive operating income · **≈$325k** ARR run-rate exiting month 36 ·
**$1,225** CAC, paid back in 1.7 months

Five assumptions move this answer: opening cash ($10k) · new cities/mo (0.35, +5%) ·
ACV ($9,600 Core) · hire timing (contractor m13, engineer m28) · COGS ($75/city/mo).

---

<!-- _class: invert -->

# The risks, from the one you will ask about to the one that actually ends it.

**Outer — market.** *"Isn't this a feature CivicPlus ships next quarter?"* It already did — for
staff. Our user has no seat in those systems and no staff. An incumbent would have to build a
different product for a different person and sell it into a body that did not procure it.

**Middle — competition.** *Ordinal AI is funded and ahead.* $1M seed, 7+ live cities, broader
surface. Broad and shallow. We are narrow and deep on one buyer inside the same building.

**Inner — execution.** *One founder, 0.35 cities a month, and a $29,069 cash trough at month 18.*
This is the one that actually ends it, and it is why the ask is the size it is. Hire timing is
the most sensitive input; an earlier draft that hired an engineer at month 16 sank the base case to −$101k.

---

<!-- _class: invert lead -->

# We do not need a round. We need $40,000 and five pilot cities.

**Use of funds — traced to the model**
- **≈$29k** covers the cash trough — the base case bottoms at −$29,069 in month 18
- **$11.7k** year-1 sales and marketing: TML annual conference plus about one regional event a month
- **$6k** formation and Texas foreign qualification
- **$10.6k** G&A — the $1M GL + cyber certificate cities require before data access, accounting, software

**What it unlocks:** five pilot cities converting in months 4–9, the first paying cities by
month 6, and positive operating income from month 19 without a second raise.

`[ NEEDS JOSELEOS — THE ONE OPEN DECISION ] $40k is the only ask the accepted model supports:`
`bootstrapped, no financing in any scenario. An institutional round means saying the number and`
`re-running the model financed before this slide is true. If the deck is for pilots and partners`
`rather than capital, the ask becomes five pilot slots and the dollar figure comes off.`

---

# Appendix 1 — All three scenarios, side by side.

| Metric | Base | Upside | Downside |
|---|---|---|---|
| 3-year revenue | $378,843 | $922,560 | $107,511 |
| Paying cities at month 36 | 31.2 | 71.3 | 10.7 |
| Ending cash, month 36 | $31,600 | $309,645 | −$4,472 |
| Capital need to break-even | $29,069 | $32,738 | $31,557 |
| First month operating income ≥ 0 | 7 | 4 | 15 |
| Gross margin | 89.0% | 91.0% | 79.0% |
| ACV | $9,600 | $11,000 | $7,200 |
| CAC / payback | $1,225 / 1.7 mo | $592 / 0.7 mo | $3,009 / 6.3 mo |
| Net revenue retention | 98.0% | 103.0% | 88.0% |

---

# Appendix 2 — How a Texas city actually buys this.

- **Competitive bidding above $50,000.** Tex. Loc. Gov't Code §252.021. Many charters set lower internal thresholds — verify per city.
- **$3k–$50k needs two HUB quotes where practicable.** §252.0215 — a form, not a season.
- **Cooperative purchasing is the shortcut for larger cities.** BuyBoard, TIPS, DIR — later-stage.
- **TX-RAMP binds state agencies, not cities.** Tex. Gov't Code §2054.0593 — but cities borrow the questionnaire.
- **Everything is a public record.** Public Information Act, Tex. Gov't Code ch. 552.
- **$1M GL + cyber certificate before data access.** An early G&A line in the model, not a later one.
- **Buying and renewal cluster Aug–Sep.** Texas city fiscal years mostly begin Oct 1 (ch. 102).
- **Channels: TML, TCMA, ELGL.** TML annual conference 11–13 Nov 2026, San Antonio.

---

# Internal — six things this deck does not know.

**Pull this slide before any external meeting.**

1. **Founder story** — Holly's own account of why municipal records. *(joseleos)*
2. **CTO bio** — Helena Carre has no published bio. *(joseleos)*
3. **Traction specifics** — Schertz usage, verbal commitments, LOIs, pilots in flight. *(joseleos)*
4. **The ask** — $40k is the only figure the accepted model supports. *(joseleos)*
5. **Pricing contradiction** — model prices Core at $9,600; June/July meeting notes floated
   ~$50k/yr and a ~$20k 60-day pilot. Both cannot be true, and $50k breaks the no-bid design. *(joseleos + HermesX)*
6. **Missing GTM source** — `Strata_GTM_Strategy.docx` and `Strata_Market_Research.docx` are
   cited by the brief but are not on disk. Positioning here was rebuilt from the space profile
   and the BMC. *(HermesX)*
