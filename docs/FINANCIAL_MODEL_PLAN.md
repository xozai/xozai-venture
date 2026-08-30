# Plan — Skill 4: `financial-model`

Owner: joseleos. Orchestrator: Claude. Created 2026-08-30. Status: **plan + skill scaffold; inputs in flight.**

## Goal

A reusable skill that, given a venture brief (any space) and a horizon of 3–5
years, produces a sourced, scenario-based financial model for a US C-Corp tech
startup: revenue build, personnel, COGS, OpEx by function (G&A/ops, legal,
S&M, R&D), cash flow, burn/runway, capital need, and a short narrative memo.

## Why a fourth skill

Skills 1–3 answer *what to build, build it, sell it*. None answers *what it
costs and when it pays back*, which joseleos needs before committing
engineering time or money. The model also closes a loop: axis 1 (effort) and
axis 2 (value) of discovery become dollars, and the GTM plan gets a budget
instead of a wish list.

```
 venture-discovery ──► financial-model ──► product-build ──► go-to-market
   (candidate + evidence)   (cost/revenue/runway)    (build budget)   (S&M budget)
```

It can be re-run after Skill 2 (actuals replace build estimates) and after
Skill 3 (real CAC replaces benchmark CAC).

## Inputs and who supplies them

| Input | Owner | Artifact | Status 2026-08-30 |
|---|---|---|---|
| Market size, comparables (stage, headcount, pricing, ARR/funding), cost + revenue benchmarks | Researcher | `research/FINANCIAL_BENCHMARKS.md` | requested in thread `3c541c66…` |
| Build effort (eng-days, team shape, infra) | Codex | thread reply 2026-08-30 06:06 (18–29 eng-days MVP for the *skill*; per-venture build effort comes from Skill 2 Stage A) | received; UCM product estimate in `product/finance/ucm/BUILD_ESTIMATE.md` |
| GTM plan cost (channels, sales headcount ramp, OTE, tooling, events, pilots) | HermesX | `marketing/GTM_COST_MODEL.md` | requested |
| Content/brand cost (site, SEO, paid, design, PR, collateral) | Scribe | `marketing/GTM_COST_MODEL.md` (same file, Scribe section) | requested |
| Venture brief, horizon, funding plan, pricing intent, scenario definitions | joseleos | `product/FINANCIAL_BRIEF_UCM.md` | answered 2026-08-30; brief drafted |

## Design decisions (Claude; joseleos may veto)

1. **Arithmetic outside the LLM.** Codex's recommendation, adopted. A small
   deterministic engine (TypeScript, matching the default stack) reads a
   typed JSON assumptions file and emits the tables. The LLM's job is to
   assemble and source assumptions and write the narrative, never to "do
   the math" in prose.
2. **Assumptions are the product.** Every number has `value`, `source`
   (URL or "assumption"), `date`, `confidence` (H/M/L), and `override`
   field. Unsourced material assumptions fail the build.
3. **Three scenarios, one schema.** Base / upside / downside are three
   assumption files that share a schema; the engine runs all three.
4. **Granularity.** Monthly for months 1–24, quarterly to the end of the
   horizon, annual rollup. Cash rolls forward and reconciles period to period.
5. **Space-agnostic.** The skill reads `research/spaces/<SPACE>.md` for
   buyer archetype, sales motion, and pricing norms; nothing space-specific
   in `SKILL.md`.
6. **Outputs.** `product/finance/<VENTURE>/` contains `assumptions.*.json`,
   `MODEL.md` (tables + memo), and `model.xlsx`/`.csv` exports with tabs:
   Assumptions, Revenue, Headcount, OpEx, Statements, Cash, Metrics,
   Scenarios, Sources.
7. **Not advice.** Outputs carry a fixed note that defaults are estimates,
   not legal or tax advice; joseleos reviews with an accountant before
   external use.

## Cost model content (US C-Corp defaults)

Defaults live in `research/FINANCIAL_BENCHMARKS.md` once Researcher delivers;
until then the schema lists them with `confidence: L` placeholders.

- **Formation & legal**: Delaware C-Corp formation + registered agent,
  83(b)/founder stock, IP assignment, SAFE/priced-round counsel, annual
  Delaware franchise tax + state foreign qualification, trademark.
- **G&A / operations**: accounting + bookkeeping, tax prep, payroll provider,
  D&O + E&O + cyber + general liability, banking/fees, office or remote
  stipend, software seats per head, recruiting (% of first-year salary).
- **Personnel**: role-based fully-loaded cost = base × (1 + employer payroll
  tax + benefits %) + equipment; hiring plan by month; founder salaries.
- **R&D / engineering**: headcount, cloud/hosting, LLM API spend (usage-
  driven, tied to revenue build), tooling, contractors.
- **Sales & marketing**: from HermesX/Scribe — headcount ramp with OTE,
  quota ramp, tooling, events, paid media (CPL → CAC), content, agencies.
- **COGS**: hosting + inference + support + third-party data per customer.
- **Revenue**: pipeline → logos → ACV; price tiers; expansion/churn; billing
  terms (annual upfront vs monthly) driving cash vs recognised revenue.
- **Financing**: SAFE/round timing and size; the model reports cash-out month
  and capital needed to reach a target milestone (e.g. $1M ARR).

## Build plan (Codex's estimate, sequenced)

| # | Step | Owner | Effort | Depends on |
|---|---|---|---|---|
| 1 | `SKILL.md` + typed schema (`product/finance/schema.json`) | Claude | 2–3 d | — |
| 2 | Deterministic engine + unit tests (`product/finance/engine/`) | Codex | 5–8 d | 1 |
| 3 | Benchmarks file + comparables | Researcher | in flight | — |
| 4 | GTM cost model | HermesX + Scribe | in flight | — |
| 5 | Skill orchestration: assemble assumptions from 3 + 4 + brief, run engine, write memo | Claude | 3–5 d | 1–4 |
| 6 | Exports (MD + CSV/XLSX) | Fizz0 | 3–5 d | 2 |
| 7 | Fixtures + QA: SaaS/services fixtures, cash reconciliation, warnings | Honey0 | 4–6 d | 2, 6 |
| 8 | First worked example: CIVIL lead (UCM) 3-year model | Claude | 1–2 d | 5, 7 |

MVP total ≈ 18–29 eng-days (Codex), ~4–6 calendar weeks for one engineer;
shorter with Codex/Fizz0 in parallel on 2 and 6. A prompt-only prototype
(no engine) is 5–8 days but not reproducible — not recommended.

## Gates

- **G1** (this PR): plan + skill scaffold reviewed by joseleos.
- **G2**: benchmark + GTM cost PRs merged; schema frozen.
- **G3**: engine passes Honey0's fixtures; cash reconciles every period.
- **G4**: first venture model reviewed by joseleos; then the skill is
  "done" and re-runnable per venture.

## Answers from joseleos (2026-08-30)

1. Horizon default: **3 years** (5 remains an option per brief).
2. Founder salaries: **deferred until funding** — shown as a memo line, $0 cash.
3. Funding: **bootstrapped** — no round in base case; model reports cash need to break-even.
4. First worked example: **CIVIL UCM** — brief in `product/FINANCIAL_BRIEF_UCM.md`.
