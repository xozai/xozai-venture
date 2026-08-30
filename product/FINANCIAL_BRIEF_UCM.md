# Financial brief — Utility Conflict Matrix (UCM) automation (CIVIL lead)

Venture: Xozai. Space: `research/spaces/CIVIL_ENGINEERING.md`. Drafted by Claude 2026-08-30 from
`research/OPPORTUNITY_SCAN_2026-08-30.md` (candidate #2, marketability 80 / band 5).
Parameters set by joseleos in-channel 2026-08-30 (thread `3c541c66…`).

## Parameters (joseleos)
| Parameter | Value |
|---|---|
| Horizon | 3 years, monthly m1–24, quarterly m25–36 |
| Founder salaries | Deferred until funding; model shows accrued/deferred comp as a memo line, $0 cash |
| Funding | Bootstrapped — no SAFE or round in base case; model reports cash need to reach break-even; upside/downside vary revenue not financing |
| First worked example | This venture (UCM), CIVIL space |

## Problem and product (from discovery evidence)
- Engineers on transportation / land-development corridor projects maintain a utility conflict
  matrix (ASCE 38-22, FHWA SHRP2 UCM) as a living document through design milestones.
- Workaround today: FHWA's spreadsheet "UCM lite"; consulting services (T2, SAM, Rios) — no
  software product found. Competitive intensity: Low.
- v1 (to be confirmed in Skill 2 Stage A): ingest utility records + plan overlay, generate and
  track the conflict matrix across milestones, export agency-ready UCM. Not a stamped deliverable
  (liability drag inverse = 5).
- Open evidence gap: no verbatim unprompted pain quote yet; job postings prove budgeted recurring
  EIT time. Revenue assumptions get `confidence: L` until 5–10 interviews close this.

## Buyer and pricing intent
- Buyer = user: individual PE / small private design-firm principal; card purchase, no procurement.
- Pricing intent (to validate via Researcher comparables): per-seat SaaS, ~$100–300/seat/month or
  ~$2–6k/firm/year; usage add-on per project possible. Annual upfront preferred for cash.
- Channels (zero-budget organic first, per `docs/DECISIONS.md`): ASCE UESI, state DOT utility-
  coordination training (PDH-native), APWA; tutorial SEO.

## Scenarios
| | Base | Upside | Downside |
|---|---|---|---|
| Win rate / logos | benchmark median (Researcher) | +50% | −50% |
| ACV | midpoint of pricing range | top of range | bottom of range |
| Churn | vertical-SaaS benchmark | −30% | +50% |
| Hiring | bootstrapped pace, hire only after gross-margin cash covers loaded cost | same | slower by one quarter |
| Financing | none | none | none (report cash-out month) |

## Required inputs (owners)
- `research/FINANCIAL_BENCHMARKS.md` — Researcher (comparables, cost + revenue benchmarks).
- `marketing/GTM_COST_MODEL.md` — HermesX (sales/channel) + Scribe (content/brand), three scenarios.
- Build effort — Codex estimate for the UCM product itself (distinct from the skill LOE already
  posted); refined in Skill 2 Stage A.

## Outputs
`product/finance/ucm/assumptions.{base,upside,downside}.json`, `MODEL.md`, `model.xlsx`.
Memo must answer: cost to reach v1, months to first revenue, cash need to break-even under
bootstrapping, and the five assumptions that move the answer most.

Estimates for planning; not legal, tax, or investment advice.
