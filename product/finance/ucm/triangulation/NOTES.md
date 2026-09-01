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

## Result
- Valuation range **$6.5M–$13.1M** (DCF $8.8M inside it). Terminal value is 69%
  of DCF total — inside the skill's 40–70% sanity band, barely.
- **Multiples are stage-default seed fallbacks (10×/14×/20× ARR)** —
  `research/FINANCIAL_BENCHMARKS.md` has no sourced EV/ARR comparables yet.
  The range is not defensible externally until Researcher adds 2–3 sourced comps.
- Health verdict: **WATCH.** The one genuine flag is **NRR 93% → CRITICAL**
  (benchmark >100%), consistent with MODEL.md's "retention, not price, is the
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
