# UCM financial model — inputs

- `build_assumptions.py` regenerates `assumptions.{base,upside,downside}.json`. Edit the generator, not the JSON.
- Sources bound: `research/FINANCIAL_BENCHMARKS.md` (#11, #13), `marketing/GTM_COST_MODEL.md` (#12, #15, #21;
  §B priced from published UESI sources — exhibit-at-all and B4 purchasability still await HermesX,
  neither touches the base case), `BUILD_ESTIMATE.md` (Codex), `docs/DECISIONS.md` defaults
  (3-year, founder comp deferred, bootstrapped, opening cash $50k = **assumption L, joseleos to confirm**).
- `revenue.start_month = 8` needs schema ≥ 1.1.0 (Codex engine PR). Until then the file fails
  `additionalProperties`; strip the key to run on 1.0.0 — but year-1 revenue will then be overstated.
- Sanity run on schema 1.0.0 (start_month stripped, 2026-08-30): all three scenarios pass
  `cash_reconciles` / `personnel_reconciles` / `material_assumptions_present`. Headline numbers are
  **not** reported here because they predate the revenue-ramp fix.
- Metrics caveat: base/downside S&M cash is near zero (organic), so CAC/payback/LTV:CAC are not
  meaningful — pending `venture_type`/caveat support in the engine.
