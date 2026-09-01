# UCM valuation triangulation — first run (2026-09-01)

First real run of the optional v3 triangulation step (vendored in PR #25), per that
PR's own test plan. Supplementary sanity check only — `MODEL.md` + `model.xlsx`
(accepted v1) remain the source of truth and are untouched by this run.

## Snapshot basis
Inputs are the **modeled m36 base-case state** from
`output/assumptions.base.model.json` (engine run of 2026-08-30), *not* today's
actuals — UCM is pre-revenue until m8. Derivations:

| Input | Value | From |
|---|---|---|
| MRR | $54,583 | Q12 revenue 163,749 / 3 (quarter average) |
| MRR growth | 7.1%/mo | Q11→Q12 revenue (+22.8%/qtr) |
| NRR | 93% | engine `metrics.nrr_annual_pct` |
| Gross margin | 94% | engine `metrics.gross_margin_pct` |
| CAC | $104.30 | engine metric — organic-GTM artefact, see caveats |
| ARPU | $450/firm/mo | 2 seats × $225 |
| Churn | 1.06%/mo | 12%/yr base |
| Burn | −$23,473/mo (cash-generating) | Q12 netCashFlow 70,420 / 3 |
| Cash | $132,679 | funded-to-plan view: m36 ending cash −250,147 + 382,826 capital need |

## Result (updated 2026-09-01 — sourced comparables now in config)
- **Comps leg: $2.0M–$3.3M** on the SaaS Capital 2025 bootstrapped M&A tier
  (3–5× EV/ARR, confidence H — the only comp matching UCM's actual stage; see
  `research/FINANCIAL_BENCHMARKS.md` §7b, PR #34). Bentley (6.3×) and Procore
  (5.5×) are ceiling anchors for the memo's qualitative note only — never
  blended in, per §7b's explicit instruction.
- The two layers now agree on the comps leg and differ only on DCF horizon,
  which is expected and documented:
  - this script's 5-year extrapolated DCF: $8.8M → its range $2.0M–$8.8M
  - the engine's 3-year deterministic DCF (`../valuation.json`): $0.19M → its
    range $0.19M–$3.3M. The engine is the authoritative layer.
- First run (stage-default fallback, before #34's comps existed) showed
  $6.5M–$13.1M; superseded. Terminal value remains 69% of this script's DCF —
  inside the skill's 40–70% band, barely.
- Health verdict: **WATCH.** The one genuine flag is **NRR 93% → CRITICAL**
  (benchmark <100%), consistent with MODEL.md's "retention, not price, is the
  revenue-quality risk." Burn multiple is healthy (cash-generating by m36 in the
  funded view).

## Caveats
- LTV:CAC 383× and 0.2-month payback are **artefacts of the organic-GTM CAC
  assumption** (MODEL.md already flags this); ignore those two HEALTHY flags.
- The script's 5-year DCF projection compounds the m36 growth rate forward
  ($1.5M → $17.8M revenue), far above the deterministic engine's build — treat
  as order-of-magnitude only, as the script itself is labeled.
- Run on the funded-to-plan view; the unfunded base has negative cash at m36
  and the $383k base capital need (joseleos's open lever decision) still stands.

## 2026-09-01 update (Honey0, PR #28)
`financial_calc.py` previously emitted per-metric HEALTHY/WATCH/CRITICAL flags
but never rolled them into the single verdict SKILL.md step 5 requires
("engine computes ... never prose"). Added `overall_verdict()` (pure function,
not from the upstream vendor) and a top-level `verdict` field to
`model_output.json`. Re-ran against the inputs above: **`verdict: "WATCH"`**,
`concerning_metrics: ["nrr"]` — matches this file's hand-written verdict above
exactly. Every other field in `model_output.json` is byte-identical to the
first run; this was a pure addition, not a recompute.

## 2026-09-01 update (Pollen0, spec-conformance pass)
`financial_calc.py`'s seed-stage revenue multiple was 10×/14×/20× — inconsistent
with SKILL.md's published "Seed 10–15×" band and the TS engine's own
`STAGE_MULTIPLES` (`[10, 15]`). Corrected to 10×/12×/15× (mid = rounded-down
average, matching the convention of the other stage bands in the same table).
Re-ran the script against the unchanged inputs above:
- **Valuation range narrows to $6.5M–$9.8M** (was $6.5M–$13.1M) — only the
  revenue-multiple high end moves (20× → 15×); DCF ($8.8M) is untouched.
- Health verdict unchanged: **WATCH**, still driven solely by NRR 93% →
  CRITICAL. Burn multiple stays HEALTHY under the also-tightened burn-multiple
  bands (doc's `<1x`/`<2x`/`>2x`, was `<1.5x`/`<2.5x`/`>2.5x`) — UCM is
  cash-generating (burn multiple −6.06), nowhere near either cutoff.
- NRR bands also tightened to the doc's best-in-class `>120%` (was `>110%`,
  which collapsed best-in-class and good into one HEALTHY band per PR #30's
  flag); does not change UCM's 93% CRITICAL classification.
