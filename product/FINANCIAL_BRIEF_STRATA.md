# Financial brief — Strata Civic Solutions (municipal decision intelligence)

Venture: **Strata** (joseleos's own product; stratacivicsolutions.com). Space:
`research/spaces/GOVTECH_MUNICIPAL.md`. Drafted by Claude 2026-08-30 on joseleos's request
("run the /financial-model skill for Strata", Strata channel `9eb9ad35…`, event `a3b423ac…`).

Strata is not an Xozai discovery candidate; it is modeled in this repo because the skill and
engine live here (`docs/DECISIONS.md`, 2026-08-30). Everything Strata-specific lives under
`product/finance/strata/` and this brief; nothing about Strata is mixed into the CIVIL or SPM
tracks.

## Parameters
| Parameter | Value | Status |
|---|---|---|
| Horizon | 3 years (m1–24 monthly, m25–36 quarterly), start **2026-10** (launch "in 6–8 weeks" from 2026-08-30) | confirmed by joseleos 2026-08-30 15:23 |
| Founder salary | Deferred until funding; $150k memo line, $0 cash | confirmed 2026-08-30 15:23 |
| Funding | Bootstrapped; no round in any scenario; model reports cash need to break-even | joseleos 2026-08-30 04:47 and 15:23 |
| Opening cash | **$10,000** (joseleos: "assume under $10,000"; modeled at the ceiling) | override applied 2026-08-30 15:23 |
| Entity | **Public Benefit Corporation**; state assumed Delaware, foreign-qualified in Texas; taxed as a C-Corp | joseleos 2026-08-30 15:23; state still unconfirmed |
| Schertz | Live demo city, not committed to paying → 0 starting paying cities | joseleos 2026-08-30 15:23 |

## Problem and product (from research + GTM docs)
- Elected officials and appointed boards prepare for votes by Ctrl+F-ing 200–400-page packets
  and calling the clerk; Strata answers questions over the city's own published record with
  page citations (Ask Strata, Meeting Prep, City Snapshot). Live demo city: Schertz, TX.
- Product is **already built and live** (domain, Claude API, 4 council interviews done per
  HermesX's 2026-06-27 note). The build line in this model is hardening for paying cities, not
  greenfield — see `product/finance/strata/BUILD_ESTIMATE.md`.
- Closest competitor Ordinal AI ($1M seed, 7+ cities). Incumbent risk: CivicPlus / Granicus
  shipping "good enough" AI summarization into installed bases.
- Sources: `~/Documents/Strata_Market_Research.docx` (Researcher, 2026-08-29) and
  `~/Documents/Strata_GTM_Strategy.docx` (HermesX, 2026-08-29, draft pending sign-off).

## Buyer and pricing intent
- Buyer: city manager (budget); users: mayor, council, boards. Texas-only, cities 10k–50k
  (~230), founder-led demos via advisor intros, free 90-day pilot for the first 5 cities.
- Pricing (GTM §4): Starter $3,600 / **Core $9,600** / Growth $18,000 per year, onboarding fee
  $500–1,500 (waived for pilots), token usage bundled. Annual billing.
- Municipal specifics that matter to the model: sales-tax exempt buyer; most target cities can
  buy under the $50k competitive-bidding threshold; Texas city fiscal years start Oct 1, so
  budgets are set Aug–Sep (renewals and new deals cluster there); insurance certificate and a
  security questionnaire are common pre-conditions.

## Scenarios
| | Base | Upside | Downside |
|---|---|---|---|
| Paying cities (month-1 rate → monthly compounding) | 0.35/mo, +5%/mo → ≈34 cumulative by m36 | 0.5/mo, +7%/mo → ≈74 | 0.2/mo, +3%/mo → ≈13 |
| ACV | $9,600 (Core) | $11,000 (Core-heavy with some Growth) | $7,200 (discounting) |
| Logo churn | 0.6%/mo (≈93% annual retention) | 0.4%/mo | 1.2%/mo |
| Expansion | 5%/yr | 8%/yr | 2%/yr |
| COGS per city | $75/mo | $60/mo | $110/mo |
| Hiring | 0.5-FTE contractor m13–27, FTE engineer m28 | contractor m7–15, FTE m16, CS/sales m25 | founder only |
| Events | TML Nov 2026 + ~1 regional/mo y1; 3 conf/yr y2–3 | 4 conf/yr | 2 conf/yr |
| Financing | none | none | none |

Hiring rule: a hire starts only when the scenario's gross-margin cash covers the loaded cost
(FTE engineer ≈ $13.1k/mo ≈ 18 paying Core cities); contractors carry no payroll burden.

## Required inputs (owners)
| Input | Owner | Status |
|---|---|---|
| Market / pricing benchmarks | Researcher | delivered in `Strata_Market_Research.docx` §6; no `research/FINANCIAL_BENCHMARKS.md` yet — govtech retention and COGS per city still tagged L |
| GTM cost (events, channels, headcount) | HermesX + Scribe | derived from `Strata_GTM_Strategy.docx` §5–7; no `marketing/GTM_COST_MODEL.md` yet — HermesX asked to confirm the S&M lines in-channel |
| Build / run cost | Codex (not in Strata channel) | Claude's estimate in `product/finance/strata/BUILD_ESTIMATE.md`; Codex to refine if joseleos wants |
| Brief parameters, opening cash, entity | joseleos | questions above |

## Outputs
`product/finance/strata/assumptions.{base,upside,downside}.json`, `output/*.model.{json,md}`
(engine output), `MODEL.md` (memo + tables). Exports (`model.xlsx`) wait for Fizz0's exporter.

Estimates for planning; not legal, tax, or investment advice.
