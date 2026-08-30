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
| Software/tooling per head | not directly sourced this pass; carry forward `SKILL.md` placeholder | USD/head/mo | — | — | L |

**Gap flagged:** no dollar-specific bookkeeping/payroll-provider (e.g. Gusto, Rippling) monthly fee or software-per-head figure was pulled this pass — both need a follow-up search or a direct vendor-pricing check before the base-case JSON is finalized.

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

## 8. `financing`

Not applicable to UCM base case (bootstrapped, no round). No benchmark pulled this pass — not needed unless joseleos changes the funding parameter.

## Confidence summary for Claude's assembly step

- **H (UCM-specific, use directly):** Codex's build estimate and API cost rows; Civil 3D pricing anchor.
- **M (general SaaS/startup benchmark, reasonable default):** formation/legal costs, loaded-personnel multiplier and engineer salary bands, SaaS gross margin, self-serve CAC/payback, SMB churn band.
- **L (weak analog or gap, needs a follow-up pass or joseleos override before the model is presented as decision-grade):** software-per-head and bookkeeping/payroll-provider dollar figures, cloud/hosting cost, ad hoc counsel budget, win rate, PlanGrid/Procore comparables, AI-native 25% gross margin (excluded from the UCM recommendation).

## Open follow-ups (next Researcher pass)

1. Cloud/hosting monthly cost for a pre-scale B2B SaaS (no benchmark pulled this pass).
2. Payroll-provider (Gusto/Rippling-class) and per-head software-tooling monthly fees — currently unsourced placeholders in `ga_ops`.
3. Win-rate benchmark for low-touch, card-purchase, individual-professional-buyer SaaS — none found; current recommendation is to leave as an unvalidated assumption rather than force-fit an unrelated vertical's number.
4. SPM-track benchmarks (enterprise incentive-comp space) are out of scope for this pass — this file covers CIVIL/UCM only, per the critical-path request in-thread. A separate SPM benchmarks pass is needed before any SPM candidate reaches financial-model stage.
