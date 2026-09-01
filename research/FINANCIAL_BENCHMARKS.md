---
title: "Financial benchmarks and comparables — US C-Corp cost + revenue defaults"
author: Researcher
created: 2026-08-30
status: draft — feeds `product/finance/schema.json` defaults and the UCM base/upside/downside assumption files
---

# Financial benchmarks

Scope: general US C-Corp SaaS startup cost lines (schema sections `formation_legal`,
`ga_ops`, `personnel`, `rnd`, `sales_marketing`, `cogs`, `revenue`) plus UCM-specific
comparables for `product/FINANCIAL_BRIEF_UCM.md`. Every row below carries `value`,
`source`, `date`, `confidence` (H/M/L per the skill's convention) so Claude can drop
these straight into the assumptions JSON with `kind: benchmark` and `override: null`.
Confidence is capped at **M** anywhere the number is a general SaaS/startup benchmark
rather than a UCM-specific data point — flagged per row.

## 1. `formation_legal`

| Line | Value | Unit | Source | Date | Confidence |
|---|---|---|---|---|---|
| DE C-Corp formation (Stripe Atlas, all-in) | 500 | USD one-time | [Stripe Atlas pricing via startup-offers guide](https://guptadeepak.com/startup-offers/guides/stripe-atlas) | 2026 | M |
| DE C-Corp formation (Clerky, lifetime package) | 819 | USD one-time | [Clerky pricing 2026](https://sparklaun.ch/compare/clerky) | 2026 | M |
| Attorney-led formation (alternative, higher-touch) | 1,500–5,000 | USD one-time | [Rho: Delaware C-Corp setup, costs, requirements 2026](https://www.rho.co/blog/delaware-c-corp) | 2026 | M |
| Registered agent (year 2+) | ~100 | USD/yr | [Rho: Delaware C-Corp setup 2026](https://www.rho.co/blog/delaware-c-corp) | 2026 | M |
| Delaware franchise tax (assumed-par method, standard startup cap table) | 400–500 | USD/yr | [Rho: Delaware C-Corp setup 2026](https://www.rho.co/blog/delaware-c-corp) | 2026 | M |
| Delaware annual report fee | 50 | USD/yr | [Rho: Delaware C-Corp setup 2026](https://www.rho.co/blog/delaware-c-corp) | 2026 | M |
| **Total recurring formation/legal overhead, year 2+ (before counsel time)** | **700–900** | USD/yr | derived from rows above | 2026 | M |
| 83(b) election, IP assignment, founder stock docs | bundled in formation package above | — | same as formation row | 2026 | M |
| Ad hoc counsel (SAFE review, contract review, employment docs) — pre-financing | 3,000–8,000 | USD/yr, as-needed | Researcher estimate from formation-service ranges; no direct benchmark found | 2026 | L |

## 2. `ga_ops`

| Line | Value | Unit | Source | Date | Confidence |
|---|---|---|---|---|---|
| G&A total (bootstrapped/lean peer set, % of revenue at scale) | ~15% | % of ARR | [Pegacorn Group: G&A budget at a startup](https://www.pegacorngroup.com/insights/ga-budget-startup/) | 2026 | M |
| G&A premium for equity-backed vs. bootstrapped (driven by reporting/audit staffing) | +64% | relative | [Pegacorn Group: G&A budget at a startup](https://www.pegacorngroup.com/insights/ga-budget-startup/) | 2026 | M — use lower end since UCM base case is bootstrapped |
| Insurance stack, full program (Tech E&O + Cyber + D&O + GL), scaling company | 15,000–75,000 | USD/yr | [Vouch: Startup Insurance Costs 2026](https://www.vouch.us/blog/startup-insurance-costs) | 2026 | M |
| Cyber liability, seed-stage-appropriate | 500–3,000 | USD/yr | [Hotaling / Vouch cyber insurance ranges, SaaS startup insurance 2026](https://hotalinginsurance.com/hotaling-insurance-blog/saas-insurance-in-2025-costs-coverage-vc-essentials) | 2026 | M |
| Tech E&O, seed-stage-appropriate floor | ~5,000 | USD/yr | [Vouch: Startup Insurance Costs 2026](https://www.vouch.us/blog/startup-insurance-costs) | 2026 | L — floor of a range built for a scaling company, not pre-revenue |
| Bookkeeping/payroll compliance (basic, pre-Series A) | not skimped but no dollar figure found; budget as fractional bookkeeper/month | — | [indinero: Finance as a Service by Stage](https://www.indinero.com/blog/finance-as-a-service-by-stage) | 2026 | L |
| Payroll provider, Gusto Simple (base + per-employee), 2–5 person team | 49 base + 6/employee → 61–79/mo total | USD/mo | [Gusto pricing 2026, via Workstream](https://www.workstream.us/blog/gusto-pricing) | 2026 | H — direct vendor pricing page, matches UCM's team size |
| Payroll provider, Rippling (core platform + payroll module), alternative | 35 base + ~8/employee for payroll, ~20–35/employee all-in once HR/benefits modules added | USD/mo | [Pin: Rippling Pricing 2026](https://www.pin.com/blog/rippling-pricing/) | 2026 | M — modular/quote-based, less transparent than Gusto for a lean team; use Gusto as base case |
| Software/tooling per head, engineering-specific (tools + infra) | 150–400 | USD/engineer/mo | [Sasanova: SaaS Spending Benchmarks 2026](https://www.sasanova.com/guides/saas-spending-benchmarks-2026) | 2026 | M |
| Software/tooling per head, seed/Series A companies <50 employees (whole-stack, all functions) | 117–200 (1,400–2,400/yr) | USD/employee/mo | [Cledara: Average SaaS Spend Per Employee 2026](https://www.cledara.com/blog/average-saas-spend-per-employee-2026) | 2026 | M |

**Applied to UCM:** for a 2–5 person team, base case **Gusto Simple (~$61–79/mo total, not per-head)** for payroll, and **~$150–200/head/mo** for software/tooling — nearer the engineering-specific band than the broader $400–600/mo band, since that higher figure reflects 10–50-person companies past the lean pre-revenue stage UCM starts in.

## 3. `personnel`

| Line | Value | Unit | Source | Date | Confidence |
|---|---|---|---|---|---|
| Fully-loaded multiplier over base salary (US employee: payroll tax + benefits + equipment) | 1.25×–1.34× | multiplier | [Ravio: Startup salaries 2026](https://ravio.com/blog/startup-salaries) (1.34× worked example); corroborated 1.25–1.4× range, industry-general | 2026 | M |
| Employer payroll tax component | ~10% | % of base | [Ravio: Startup salaries 2026](https://ravio.com/blog/startup-salaries) | 2026 | M |
| Benefits load (health/dental/401k match) | 25–30% | % of base | [Ravio: Startup salaries 2026](https://ravio.com/blog/startup-salaries) | 2026 | M |
| Avg. employer health-insurance cost per employee | ~17,500 (2025) → ~18,500 (2026 projected) | USD/employee/yr | Mercer, via [Ravio: Startup salaries 2026](https://ravio.com/blog/startup-salaries) | 2026 | M |
| Mid-level engineer base, seed-stage, non-Bay-Area | 90,000–130,000 | USD/yr | [underdog.io: Early Stage Startup Salary Guide 2026](https://underdog.io/blog/early-stage-startup-salary) | 2026 | M |
| Mid-level engineer base, seed-stage, Bay Area | 100,000–145,000 | USD/yr | [underdog.io: Early Stage Startup Salary Guide 2026](https://underdog.io/blog/early-stage-startup-salary) | 2026 | M |
| Recruiter fee (if external, first-year hires) | 18–22% | % of first-year base | [Ravio: Startup salaries 2026](https://ravio.com/blog/startup-salaries) | 2026 | L — only relevant if UCM hires beyond founders pre-revenue, which base case avoids |

**Applied to UCM:** with founder salaries deferred per the brief, personnel cost only activates once non-founder hires start (Codex's build estimate: 2 FTE to M3). Recommend base case: 1 engineer at $110k base × 1.30 loaded ≈ **$143k/yr fully loaded**, starting the month Codex's build plan calls for a second FTE.

## 4. `rnd`

| Line | Value | Unit | Source | Date | Confidence |
|---|---|---|---|---|---|
| Build effort, UCM v1 | 11 eng-months base (8 upside / 18 downside) | eng-months | `product/finance/ucm/BUILD_ESTIMATE.md` (Codex, 2026-08-30) | 2026-08-30 | H — already project-specific |
| LLM API cost | $3–9 | USD/active user/mo | `product/finance/ucm/BUILD_ESTIMATE.md` (Codex, 2026-08-30) | 2026-08-30 | H — already project-specific |
| Cloud/hosting for a small B2B SaaS pre-scale | no fresh benchmark pulled this pass; do not silently assume — flag for a follow-up pass or a direct AWS/Vercel/Supabase calculator estimate | USD/mo | — | — | L |

## 5. `sales_marketing`

| Line | Value | Unit | Source | Date | Confidence |
|---|---|---|---|---|---|
| S&M + R&D + G&A combined opex, >$50M ARR (reference ceiling, not applicable to UCM stage) | 78% | % of revenue | [SaaSRise: 2026 SaaS Benchmarks Report](https://www.saasrise.com/blog/saas-benchmark-report-2026) | 2026 | L — wrong stage, included only as an upper anchor |
| Self-serve/PLG CAC, low-touch deals <$5k ACV | 150–400 | USD/customer | [Aleph: CAC payback period benchmarks SaaS 2026](https://www.getaleph.com/answers/cac-payback-period-saas-2026) | 2026 | M |
| Self-serve/PLG CAC payback | 6–12 (median 7–11) | months | [Aleph: CAC payback benchmarks 2026](https://www.getaleph.com/answers/cac-payback-period-saas-2026); [Artisan Strategies: SaaS payback period benchmarks 2026](https://www.artisangrowthstrategies.com/blog/saas-payback-period-benchmarks-cac-turns-positive-by-industry) | 2026 | M |
| Vertical SaaS CAC payback (median, vs. 14mo horizontal) | 18 | months | [Artisan Strategies: SaaS payback period benchmarks 2026](https://www.artisangrowthstrategies.com/blog/saas-payback-period-benchmarks-cac-turns-positive-by-industry) | 2026 | M |
| Vertical SaaS LTV:CAC (vs. 4.1x horizontal) | 5.6 | ratio | [Artisan Strategies: SaaS payback period benchmarks 2026](https://www.artisangrowthstrategies.com/blog/saas-payback-period-benchmarks-cac-turns-positive-by-industry) | 2026 | M |

**Applied to UCM:** buyer is an individual PE/small-firm principal on a card, zero-budget organic channels per `docs/DECISIONS.md` — this is the low-touch/self-serve profile, not the vertical-SaaS sales-led profile. Recommend **CAC $150–400, payback target ≤12mo** for base case, not the 18mo vertical-SaaS median, since there is no sales headcount in the bootstrapped plan. Still owed: HermesX/Scribe's `marketing/GTM_COST_MODEL.md` for the channel-specific cost (ASCE UESI, DOT training, APWA, SEO) — this table gives CAC/payback targets to check that plan against, not a substitute for it.

## 6. `cogs`

| Line | Value | Unit | Source | Date | Confidence |
|---|---|---|---|---|---|
| SaaS gross margin, software-only floor | 75% | % of revenue | [Livmo: SaaS Gross Margin Benchmarks 2026](https://livmo.com/blog/saas-gross-margin-benchmarks/) | 2026 | M |
| SaaS gross margin, best-in-class | 85% | % of revenue | [Livmo: SaaS Gross Margin Benchmarks 2026](https://livmo.com/blog/saas-gross-margin-benchmarks/) | 2026 | M |
| SaaS gross margin, median incl. services | 77% | % of revenue | Benchmarkit 2025, via [SaaSRise 2026 SaaS Benchmarks Report](https://www.saasrise.com/blog/saas-benchmark-report-2026) | 2025 | M |
| AI-native scaling company gross margin (compute-heavy reference, not the base case) | 25% | % of revenue | Bessemer Venture Partners, via [SaaSRise 2026 SaaS Benchmarks Report](https://www.saasrise.com/blog/saas-benchmark-report-2026) | 2026 | L — reflects consumer-scale inference load, not a document-generation workflow tool; UCM's own $3–9/user LLM cost (row above) is the better direct input |

**Applied to UCM:** use the classic SaaS gross-margin band (75–85%) with LLM API cost as an explicit COGS line item (Codex's $3–9/active user/mo, already project-specific) rather than the AI-native 25% figure, which describes a different usage pattern.

## 7. `revenue` — pricing comparables and churn/win-rate benchmarks

**Direct competitor pricing:** none — `product/FINANCIAL_BRIEF_UCM.md` already confirms no dedicated UCM software product exists (workaround is FHWA's spreadsheet + consulting). Comparables below are adjacent tools sold to the same buyer (civil/AEC firms, individual-PE-and-up).

| Comparable | Price | Unit | Source | Date | Confidence |
|---|---|---|---|---|---|
| Autodesk Civil 3D (single-seat annual) | 2,870 | USD/yr (≈ $239/mo) | [Autodesk Civil 3D Subscription FAQ](https://www.autodesk.com/solutions/aec/civil-3d-subscription-faq) | 2026 | H — direct, current vendor pricing, same buyer persona |
| Bluebeam Revu (per seat) | 22–49 | USD/mo | [Drawboard: Bluebeam pricing 2026](https://www.drawboard.com/blog/bluebeam-pricing) | 2026 | M — adjacent tool (markup/docs, not modeling), lower value density than UCM's workflow |
| PlanGrid (per seat) | 39–49 | USD/mo | search aggregation, multiple pricing pages 2026 | 2026 | L — general construction-docs tool, weak analog |
| Procore | 375+ | USD/mo base (not strictly per-seat, up to 10 users) | search aggregation 2026 | 2026 | L — different pricing model, platform not per-seat |

**Reading:** Civil 3D at ~$239/mo/seat is the strongest direct anchor — same buyer, same discipline, comparable "can't do the job without it" value. It sits inside and near the top of the brief's proposed $100–300/seat/mo range, supporting that range rather than the lower general-construction-tool comps (Bluebeam/PlanGrid $22–49), which serve a broader, more commoditized documents workflow. **Recommend base case ACV toward the upper-middle of the $100–300 range (~$200–250/seat/mo, ~$2,400–3,000/seat/yr)**, i.e. pricing UCM close to Civil 3D rather than to generic markup tools.

| Metric | Value | Unit | Source | Date | Confidence |
|---|---|---|---|---|---|
| Vertical SaaS churn (mid-market ACV band, which UCM's per-firm annual spend resembles) | 5–10% | annual | [Optifai: B2B SaaS churn rate benchmark](https://optif.ai/learn/questions/b2b-saas-churn-rate-benchmark/) | 2026 | L — UCM's buyer is individual/small-firm, closer to SMB churn band below, despite mid-market-like per-seat price |
| SMB-band churn (<$15K ACV) | 10–15% | annual | web search aggregation, multiple 2026 SaaS churn benchmark reports | 2026 | M |
| SMB customer-loss concentration | 43% of losses in first 90 days | — | web search aggregation, 2026 SaaS churn benchmark reports | 2026 | L |

**No win-rate benchmark found this pass** for low-touch/card-purchase individual-buyer SaaS specifically — flagged as an open gap, same as the brief's own "no verbatim pain quote yet" caveat. Recommend the engine take win-rate as a pure `confidence: L`, `source: "assumption"` input until Skill 3 (go-to-market) produces real funnel data, rather than borrowing an unrelated vertical's win rate.

## 7b. Valuation comparables (EV/ARR, EV/Revenue) — for v3 triangulation

Added 2026-09-01 per `financial-model` SKILL.md v3 step 5's requirement that
the revenue-multiple triangulation leg use a sourced comparable before
falling back to the generic stage-default bands (Seed 10–15×, Series A
8–12×, Series B 5–8×). PR #27's first triangulation run flagged this gap
explicitly. Three comparables below, ranked by relevance to UCM's actual
stage (bootstrapped, pre/early-revenue, individual-buyer B2B), not by size.

| Comparable | Multiple | Basis | Source | Date | Confidence |
|---|---|---|---|---|---|
| SaaS Capital 2025 bootstrapped SaaS M&A multiple, $100K–1M ARR tier | 3–5× (4.8× median across all bootstrapped tiers) | EV/ARR | [SaaS Capital 2025 index, via L40° SaaS Multiples 2026](https://www.l40.com/insights/saas-multiples) and [saasvaluationmultiple.com stage breakdown](https://saasvaluationmultiple.com/by-stage) | 2025 data, cited 2026-05-02 | **H — the only comp matching UCM's actual stage** (bootstrapped, no round, sub-$1M ARR base case) rather than a public-market or funded-round proxy |
| Bentley Systems (BSY), public — civil/infrastructure design software | 6.3× | EV/Revenue (TTM) | [TradingView BSY EV/Sales fwd](https://www.tradingview.com/symbols/BIVA-BSY/financials-statistics-and-ratios/enterprise-value-sales-fwd/); market cap ~$9B, EV ~$10–11B, TTM revenue ~$1.56B, as of 2026-07-01 | 2026-07-01 | M — same buyer ecosystem (civil engineers/AEC firms) and closest product analog by discipline, but a mature public company at massive scale; use as a ceiling anchor, not the base-case multiple |
| Procore Technologies (PCOR), public — construction/AEC project-management SaaS | 5.5× | EV/Revenue (TTM) | [stockanalysis.com PCOR statistics](https://stockanalysis.com/stocks/pcor/statistics/); market cap $8.5B, EV $7.9B, TTM revenue $1.371B, as of 2026-08-05 | 2026-08-05 | M — same buyer ecosystem (construction/AEC), same "vertical workflow SaaS, not horizontal" category, but public-scale; use as a ceiling anchor alongside Bentley, not the base-case multiple. (PCOR's own EV/Revenue was as low as 4.79× intraperiod, ~50% below its 10-yr median of 9.63× — flagging the spread since the two data points three months apart moved the multiple materially) |

**Applied to UCM:** base-case triangulation should use the **SaaS Capital
bootstrapped tier (3–5×)** as the stage-appropriate multiple — it is the only
comp that matches UCM's actual financing profile (bootstrapped, small ARR),
not just its buyer/discipline. Bentley and Procore confirm the *category*
supports premium multiples once a company reaches scale (6.3× and 5.5× at
$1.3–1.5B revenue) — useful as an upper-bound sanity check on the
"what could this become" question, but using either as UCM's near-term
multiple would overstate the value of a pre-revenue/early-revenue company by
conflating public-market scale economics with a two-person bootstrapped
start. Do not blend all three into one number; if the engine wants a single
comps-leg figure, use 3–5× and cite Bentley/Procore only in the memo's
qualitative "market ceiling" note.

## 8. `financing`

Not applicable to UCM base case (bootstrapped, no round). No benchmark pulled this pass — not needed unless joseleos changes the funding parameter.

## Confidence summary for Claude's assembly step

- **H (UCM-specific, use directly):** Codex's build estimate, API cost, and cloud/hosting run-rate rows (`product/finance/ucm/BUILD_ESTIMATE.md`, $300–600/mo at 10 users); Civil 3D pricing anchor; Gusto payroll pricing (direct vendor page, matches team size).
- **M (general SaaS/startup benchmark, reasonable default):** formation/legal costs, loaded-personnel multiplier and engineer salary bands, SaaS gross margin, self-serve CAC/payback, SMB churn band, software/tooling per head.
- **L (weak analog or gap, needs a follow-up pass or joseleos override before the model is presented as decision-grade):** ad hoc counsel budget, win rate, PlanGrid/Procore comparables, AI-native 25% gross margin (excluded from the UCM recommendation), Rippling pricing (quote-based, kept only as an alternative reference to Gusto).

## Open follow-ups (next Researcher pass)

1. ~~Cloud/hosting monthly cost~~ — resolved: already covered by Codex's `BUILD_ESTIMATE.md` run-rate table ($300–600/mo at 10 users), confirmed with Claude 2026-08-30, no separate benchmark needed.
2. ~~Payroll-provider and per-head software-tooling monthly fees~~ — resolved this pass: Gusto Simple ($61–79/mo for a 2–5 person team) and engineering-tooling ($150–200/head/mo) rows added to `ga_ops` above.
3. Win-rate benchmark for low-touch, card-purchase, individual-professional-buyer SaaS — none found; current recommendation is to leave as an unvalidated assumption rather than force-fit an unrelated vertical's number.
4. SPM-track benchmarks (enterprise incentive-comp space) are out of scope for this pass — this file covers CIVIL/UCM only, per the critical-path request in-thread. A separate SPM benchmarks pass is needed before any SPM candidate reaches financial-model stage.
5. ~~EV/ARR comparables for v3 triangulation~~ — resolved this pass: §7b adds 3 sourced comparables (SaaS Capital bootstrapped tier, Bentley Systems, Procore Technologies), requested after PR #27's triangulation run fell back to the generic stage-default band.
