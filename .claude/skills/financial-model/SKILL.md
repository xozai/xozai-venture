---
name: financial-model
description: >
  Produce a sourced, scenario-based 3–5 year financial model (revenue,
  personnel, COGS, OpEx by function, cash, burn/runway, capital need) for a
  venture in any space, as a US C-Corp, plus a triangulated valuation range
  and a SaaS-health verdict against named benchmarks. Researcher supplies
  benchmarks and comparables, Codex the build effort, HermesX and Scribe the
  GTM cost; Claude assembles assumptions and runs the deterministic engine.
version: 3
---

# Skill 4 — Financial model

v3 adds valuation triangulation and SaaS-health benchmarking (below) as an
engine addition — not a replacement of v2's 3-statement build. Benchmark
thresholds and the DCF/comps/health-check triangulation pattern are adapted
from [davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude/blob/main/plugins/venture-capital-intelligence/skills/financial-model/SKILL.md)
and the `unit-economics`/`comps-analysis` skills in
[w95/awesome-claude-corporate-skills](https://github.com/w95/awesome-claude-corporate-skills)
(both MIT). Those repos' own engines are not vendored — the existing
deterministic `product/finance/engine/` stays the source of truth; this is a
new computed section layered on its output, per the decision recorded in
`research/SKILL_SOURCES.md` §4.

## When to run
After `venture-discovery` has a lead candidate (a `pick:` is not required —
the model is an input to the pick). Re-run after `product-build` Stage A
(real build estimate) and after `go-to-market` sign-off (real S&M budget).

## Inputs
- Venture brief: `product/FINANCIAL_BRIEF_<VENTURE>.md` — problem, buyer,
  pricing intent, horizon (3–5 y), funding plan, scenario definitions.
- Space profile `research/spaces/<SPACE>.md` — buyer archetype, sales
  motion, pricing norms, liability analog (drives insurance/legal lines).
- `research/FINANCIAL_BENCHMARKS.md` — Researcher's comparables and cost /
  revenue benchmarks, each with source, date, confidence.
- `marketing/GTM_COST_MODEL.md` — HermesX (sales/channel cost) and Scribe
  (content/brand cost), three scenarios.
- Build effort: `product/ARCHITECTURE.md` milestones if Skill 2 has run;
  otherwise Codex's estimate posted in-channel.
- Schema: `product/finance/schema.json`. Engine + xlsx export: `product/finance/engine/`.
- Fixtures and test plan: `product/finance/tests/` (Honey0).
- `research/FINANCIAL_BENCHMARKS.md` must also carry 2–3 comparables' revenue
  multiples (EV/ARR or EV/Revenue, sourced) when triangulation runs — see
  "Valuation & SaaS-health benchmarks" below.

## Roles
| Who | Does |
|---|---|
| Claude | Owns assumptions assembly, runs engine, writes memo, reviews |
| Researcher | Benchmarks + comparables with sources |
| Codex | Build-effort estimate |
| HermesX | GTM plan cost (headcount ramp, channels, events, pilots) |
| Scribe | Content/brand/paid-media cost |
| Codex | Builds/maintains the engine and the .xlsx export |
| Honey0 | Fixtures, reconciliation tests, warnings |
| joseleos | Brief, funding plan, scenario intent; accepts the model |

## Steps
1. **Brief.** Claude drafts `product/FINANCIAL_BRIEF_<VENTURE>.md` from the
   discovery evidence and asks joseleos the batched questions (horizon,
   founder pay, funding, scenarios). No model until the brief is answered.
2. **Collect.** Dispatch Researcher, HermesX + Scribe, and Codex in one
   channel message each, pointing at the exact files above. Each returns a
   PR. Claude reviews for: every number sourced/dated/confidence-tagged;
   ranges where sources disagree; three scenarios present.
3. **Assemble assumptions.** Claude writes
   `product/finance/<VENTURE>/assumptions.{base,upside,downside}.json`
   against `schema.json`. Rules:
   - Every material assumption has `value`, `unit`, `source`, `date`,
     `confidence`, `override` (null unless joseleos changed it).
   - Benchmarks, derived values, and user inputs are tagged separately.
   - Never invent a material number silently; if no source, tag
     `confidence: L`, `source: "assumption"`, and list it in the memo's
     "assumptions to validate".
4. **Run.** `engine` reads the three files and emits monthly (m1–24),
   quarterly (to horizon), and annual tables: revenue build, headcount and
   payroll burden, COGS and gross margin, OpEx by function (G&A/ops,
   legal, S&M, R&D), P&L, cash roll-forward, burn, runway, cash-out month,
   capital need to milestone, unit metrics (ACV, CAC, payback, NRR,
   LTV/CAC), break-even, and one-variable sensitivities (price, win rate,
   churn, hiring pace).
5. **Triangulate (v3).** Once base-case revenue exists, the engine computes
   three independent valuation views and reconciles them — never prose math:
   - **DCF intrinsic value**: base-case unlevered FCF from step 4, discounted
     at a stage-appropriate rate (default WACC 20% pre-seed/seed, step down
     for later stages — never below the risk-free rate), terminal value by
     perpetuity growth (2–3%), sanity-checked that terminal value is 40–70%
     of the total (flag if outside that band).
   - **Revenue-multiple (comps)**: ARR × the stage-appropriate multiple from
     `FINANCIAL_BENCHMARKS.md`'s sourced comparables (fall back to
     stage-default ranges — Seed 10–15×, Series A 8–12×, Series B 5–8× — only
     if no comparable is sourced, and flag the fallback).
   - **SaaS-health check**: LTV:CAC, CAC payback, gross/net retention, Rule
     of 40 (growth % + margin %), burn multiple, against the benchmark table
     below → a single **HEALTHY / WATCH / CRITICAL** verdict with the
     specific ratios that drove it.
   Engine writes all three plus the reconciled range to
   `product/finance/<VENTURE>/valuation.json`; Claude never picks a single
   number without showing the spread and why.
6. **Check.** Engine fails if cash does not reconcile period to period, if
   headcount cost ≠ roster × loaded rate, or if any material assumption is
   missing. Honey0's fixtures run in CI, including v3 triangulation fixtures
   (known-input → known-verdict cases per benchmark band).
7. **Write.** The primary deliverable is `product/finance/<VENTURE>/model.xlsx`
   (joseleos, 2026-08-30), produced by the engine: tabs Assumptions, Revenue,
   Headcount, OpEx, Statements, Cash, Metrics, Scenarios, Checks, Sources,
   and (v3) Valuation. Workbook conventions (pattern sources, Apache-2.0:
   anthropics/skills `skills/xlsx`; anthropics/financial-services
   `xlsx-author` and `3-statement-model`): real formulas in calc cells,
   inputs only on the Assumptions tab (blue), formulas black, cross-sheet
   links green, named ranges for externally referenced cells, a Checks tab
   of TRUE/FALSE reconciliation cells, and a scenario selector that switches
   all tabs. Alongside it, `MODEL.md`: one-page memo (what it costs, when it
   pays back, capital needed, the five assumptions that move the answer
   most, the triangulated valuation range and health verdict) + the tables.
   Narrative totals must match workbook totals (Honey0 TC-07).
8. **Review.** Claude posts the memo in-channel and @mentions joseleos.
   Overrides go into the `override` field, never edited in place; re-run.

## US C-Corp default cost lines (schema sections)
formation_legal (formation, registered agent, franchise tax, foreign
qualification, IP/trademark, financing counsel) · ga_ops (accounting, tax
prep, payroll provider, insurance D&O/E&O/cyber/GL, banking, office or
remote stipend, software per head, recruiting %) · personnel (role,
start month, base, employer tax %, benefits %, equipment) · rnd (cloud,
LLM API usage-driven, tooling, contractors) · sales_marketing (from GTM
cost model) · cogs (per-customer hosting/inference/support/data) ·
revenue (pipeline → logos → ACV, tiers, expansion, churn, billing terms) ·
financing (instrument, month, amount).

## Valuation & SaaS-health benchmarks (v3)
Thresholds below are industry-standard bands, not this venture's targets —
the verdict step compares actuals against them and shows the gap. Source:
w95/awesome-claude-corporate-skills `unit-economics` skill (MIT); re-verify
against `FINANCIAL_BENCHMARKS.md` comparables when they disagree with the
generic band.

| Metric | Best-in-class | Good | Concerning |
|---|---|---|---|
| Net dollar retention (NDR) | >120% | >110% | <100% |
| Gross retention | >95% | >90% | <85% |
| LTV:CAC | >5x | >3x | <2x |
| CAC payback | <12 mo | <18 mo | >24 mo |
| Rule of 40 (growth % + margin %) | — | ≥40 | <40 and not accelerating |
| Burn multiple (net burn / net new ARR) | <1x | <2x | >2x ("default dead" zone) |
| Revenue multiple (ARR ×), by stage | — | Seed 10–15×, Series A 8–12×, Series B 5–8× | outside range without a sourced comp justifying it |

**Verdict rule:** HEALTHY needs no metric in "Concerning"; CRITICAL if two or
more are in "Concerning" or burn multiple implies <6 months of runway at
current burn; otherwise WATCH. Always show which specific ratios drove the
verdict — never emit the label alone.

## Exit
joseleos accepts `MODEL.md` in-channel. Record the accepted scenario and
any overrides in `docs/DECISIONS.md`. The model becomes an input to
`product-build` (budget), `go-to-market` (S&M budget), and `pitch-deck`
(financials slide + the ask, which must trace to the triangulated range).

## Rules
- Arithmetic lives in the engine, never in prose.
- Outputs carry: "Estimates for planning; not legal, tax, or investment
  advice." Review with an accountant before external use.
- Space-specific content stays in `research/spaces/<SPACE>.md`.
- Branch + PR for every artifact; Claude or Codex reviews.
- v3 triangulation is additive: if `FINANCIAL_BENCHMARKS.md` has no sourced
  comparable, the revenue-multiple leg falls back to the generic stage band
  and is flagged low-confidence in the memo — it never blocks the DCF/3-
  statement build, which remains the primary deliverable.
