---
name: financial-model
description: >
  Produce a sourced, scenario-based 3–5 year financial model (revenue,
  personnel, COGS, OpEx by function, cash, burn/runway, capital need) for a
  venture in any space, as a US C-Corp. Researcher supplies benchmarks and
  comparables, Codex the build effort, HermesX and Scribe the GTM cost;
  Claude assembles assumptions and runs the deterministic engine. Optional
  v3 step: valuation triangulation (DCF + revenue-multiple + SaaS-health)
  as a fast sanity check alongside the engine, not a replacement for it.
version: 3
---

# Skill 4 — Financial model

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
5. **Check.** Engine fails if cash does not reconcile period to period, if
   headcount cost ≠ roster × loaded rate, or if any material assumption is
   missing. Honey0's fixtures run in CI.
6. **Write.** The primary deliverable is `product/finance/<VENTURE>/model.xlsx`
   (joseleos, 2026-08-30), produced by the engine: tabs Assumptions, Revenue,
   Headcount, OpEx, Statements, Cash, Metrics, Scenarios, Checks, Sources.
   Workbook conventions (pattern sources, Apache-2.0: anthropics/skills
   `skills/xlsx`; anthropics/financial-services `xlsx-author` and
   `3-statement-model`): real formulas in calc cells, inputs only on the
   Assumptions tab (blue), formulas black, cross-sheet links green, named
   ranges for externally referenced cells, a Checks tab of TRUE/FALSE
   reconciliation cells, and a scenario selector that switches all tabs.
   Alongside it, `MODEL.md`: one-page memo (what it costs, when it pays
   back, capital needed, the five assumptions that move the answer most) +
   the tables. Narrative totals must match workbook totals (Honey0 TC-07).
7. **Review.** Claude posts the memo in-channel and @mentions joseleos.
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

## Optional — Valuation triangulation (v3, supplementary)
A fast, independent sanity check that can run alongside the engine (never
instead of it) once a venture has ARR/MRR-scale traction — DCF intrinsic
value, revenue-multiple/comps, and SaaS health metrics (LTV:CAC, CAC
payback, burn multiple, Rule of 40) with a HEALTHY/WATCH/CRITICAL verdict
against stage benchmarks. Vendored + adapted (MIT) from
[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude/blob/main/plugins/venture-capital-intelligence/skills/financial-model)
— see `THIRD_PARTY_LICENSE` and `research/SKILL_SOURCES.md` for the
vendoring decision record.

1. Copy `scripts/valuation_triangulation/model_inputs.example.json` to
   `product/finance/<VENTURE>/triangulation/model_inputs.json` and fill in
   top-line numbers (MRR/ARR, growth, NRR, CAC, ARPU, churn, burn, cash,
   comparables). These are simplified inputs, not the full schema — no
   `source`/`confidence` tagging required here.
2. Run:
   ```
   python3 .claude/skills/financial-model/scripts/valuation_triangulation/financial_calc.py <VENTURE>
   python3 .claude/skills/financial-model/scripts/valuation_triangulation/report_formatter.py <VENTURE>
   ```
3. Treat the output (`product/finance/<VENTURE>/triangulation/model_output.json`)
   as a second opinion: if it diverges sharply from `MODEL.md`, investigate
   why (usually an assumption mismatch) before trusting either number more.
   Never paste triangulation output into `MODEL.md` or the memo — it is not
   sourced/dated/confidence-tagged like the engine's assumptions and is not
   fit for that bar.
4. This step is opt-in per venture; skip it entirely if the engine's model
   already answers the question at hand.

## Exit
joseleos accepts `MODEL.md` in-channel. Record the accepted scenario and
any overrides in `docs/DECISIONS.md`. The model becomes an input to
`product-build` (budget) and `go-to-market` (S&M budget).

## Rules
- Arithmetic lives in the engine, never in prose.
- Outputs carry: "Estimates for planning; not legal, tax, or investment
  advice." Review with an accountant before external use.
- Space-specific content stays in `research/spaces/<SPACE>.md`.
- Branch + PR for every artifact; Claude or Codex reviews.
