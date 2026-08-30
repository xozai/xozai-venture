# Deterministic financial-model engine

Requires Node.js 22.18+ (native TypeScript type stripping). Calculation makes no network or LLM calls; ExcelJS is used only for `.xlsx` serialization.

```bash
npm test
npm run model -- --out product/finance/ucm/output \
  product/finance/ucm/assumptions.base.json \
  product/finance/ucm/assumptions.upside.json \
  product/finance/ucm/assumptions.downside.json
```

The command validates all three files, then writes deterministic JSON and Markdown for each scenario plus `model.xlsx`. Months 1–24 remain monthly in JSON; quarters begin at month 25; annual totals cover the complete horizon. The workbook includes Assumptions, Revenue, Headcount, OpEx, Statements, Cash, Metrics, Scenarios, Checks, and Sources tabs, with a Base/Upside/Downside selector and visible formula checks. The engine exits non-zero for missing material assumptions, cash reconciliation failures, or personnel/loaded-rate reconciliation failures.

Supported recurring-cost cadences are `monthly`, `annual`, and `one_time`. Percentages are decimals (`0.15`, not `15`). An assumption's `override`, when non-null, is used without changing its sourced `value`.

Optional v1 fields preserve compatibility with earlier fixtures: `meta.venture_type`; `revenue.start_month`, `intro_discount_pct`, and `intro_discount_months`; `personnel.roster[].variable_annual` and `attainment_pct`; and cost-item `basis`, `rate`, and `notes`. Missing optional fields use the original behavior.
