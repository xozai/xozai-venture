import type { ModelInput, ModelOutput, ValuationConfig, ValuationOutput } from "./types.ts";

const money = (n: number) => Math.round(n * 100) / 100;
const STAGE_MULTIPLES: Record<string, [number, number]> = { seed: [10, 15], "series a": [8, 12], "series b": [5, 8] };

const health = (value: number | null, healthy: (n: number) => boolean, critical: (n: number) => boolean) =>
  value === null ? "N/A" as const : healthy(value) ? "HEALTHY" as const : critical(value) ? "CRITICAL" as const : "WATCH" as const;

export function calculateValuation(input: ModelInput, model: ModelOutput, config: ValuationConfig = {}): ValuationOutput {
  const stage = (config.stage ?? "seed").trim().toLowerCase();
  const discountRate = config.discount_rate ?? 0.2;
  const terminalGrowthRate = config.terminal_growth_rate ?? 0.03;
  if (discountRate <= terminalGrowthRate) throw new Error("Valuation discount_rate must exceed terminal_growth_rate");
  const projectedFcfs = model.annual.map(row => row.operatingIncome);
  const pvFcfs = projectedFcfs.reduce((sum, fcf, i) => sum + fcf / Math.pow(1 + discountRate, i + 1), 0);
  const finalFcf = projectedFcfs.at(-1) ?? 0;
  const terminalRaw = finalFcf > 0 ? finalFcf * (1 + terminalGrowthRate) / (discountRate - terminalGrowthRate) : 0;
  const terminalValue = terminalRaw / Math.pow(1 + discountRate, projectedFcfs.length);
  const dcfValue = Math.max(0, pvFcfs + terminalValue);
  const terminalPct = dcfValue > 0 ? terminalValue / dcfValue : null;
  const dcfWarnings = terminalPct !== null && (terminalPct < 0.4 || terminalPct > 0.7)
    ? [`Terminal value is ${(terminalPct * 100).toFixed(1)}% of DCF; expected 40–70%.`] : [];

  // Exit run-rate ARR as of the period ending `endMonth`: the quarter that ends there if one
  // exists (months 25+), else the exposed monthly row (months 1-24). Used for both the headline
  // `arr` and `previousArr` below so a year-over-year ARR delta compares like with like, instead
  // of a forward-looking exit rate against a backward-looking trailing-twelve-months total.
  const arrAtMonth = (endMonth: number): number => {
    const quarter = model.quarterly.find(q => q.endMonth === endMonth);
    if (quarter) return quarter.revenue / (quarter.endMonth - quarter.startMonth + 1) * 12;
    const monthRow = model.monthly.find(m => m.month === endMonth);
    return monthRow ? monthRow.revenue * 12 : 0;
  };
  const finalAnnual = model.annual.at(-1);
  const finalQuarter = model.quarterly.at(-1);
  const finalMonth = finalQuarter ? finalQuarter.endMonth : model.monthly.at(-1)?.month;
  const arr = finalMonth !== undefined ? arrAtMonth(finalMonth) : 0;
  const fiscalYearRevenue = finalAnnual?.revenue ?? Number(model.metrics.total_revenue ?? 0);
  const validComps = (config.comparables ?? []).filter(c => c.name && Number.isFinite(c.ev_revenue_multiple) && c.ev_revenue_multiple > 0);
  const fallback = STAGE_MULTIPLES[stage] ?? STAGE_MULTIPLES.seed;
  const compMultiples = validComps.map(c => c.ev_revenue_multiple).sort((a, b) => a - b);
  const [multipleLow, multipleHigh] = compMultiples.length ? [compMultiples[0], compMultiples.at(-1)!] : fallback;
  const compWarnings = validComps.length ? [] : [`No sourced comparables supplied; using ${stage} stage-default ${multipleLow}–${multipleHigh}x range.`];

  const previousAnnual = model.annual.at(-2);
  const growth = previousAnnual && previousAnnual.revenue > 0 ? finalAnnual!.revenue / previousAnnual.revenue - 1 : null;
  const margin = finalAnnual && finalAnnual.revenue > 0 ? finalAnnual.operatingIncome / finalAnnual.revenue : null;
  const rule40 = growth !== null && margin !== null ? (growth + margin) * 100 : null;
  // Compare exit run-rate to exit run-rate a year earlier, not to the prior year's trailing
  // total revenue (mixed units — that mismatch inflates netNewArr, and so understates burn
  // multiple, for any venture growing meaningfully within its fiscal year).
  const previousArr = previousAnnual ? arrAtMonth(previousAnnual.endMonth) : 0;
  const netNewArr = previousAnnual ? Math.max(0, arr - previousArr) : 0;
  const netBurn = finalAnnual ? Math.max(0, -finalAnnual.operatingIncome) : 0;
  const burnMultiple = netNewArr > 0 ? netBurn / netNewArr : null;
  const finalMonthlyBurn = finalAnnual ? Math.max(0, -finalAnnual.operatingIncome / 12) : 0;
  const runway = finalAnnual && finalMonthlyBurn > 0 ? Math.max(0, finalAnnual.cashEnding / finalMonthlyBurn) : null;
  const ltvCac = model.metrics.ltv_cac;
  const payback = model.metrics.cac_payback_months;
  const nrr = model.metrics.nrr_annual_pct;
  const metrics = {
    ltv_cac: { value: ltvCac, health: health(ltvCac, n => n > 3, n => n < 2) },
    cac_payback_months: { value: payback, health: health(payback, n => n < 18, n => n > 24) },
    // SKILL.md benchmark table: NDR best-in-class >120%, good >110%, concerning <100%.
    nrr_pct: { value: nrr === null ? null : nrr * 100, health: health(nrr, n => n > 1.2, n => n < 1) },
    // SKILL.md: Rule of 40 good >=40, concerning <40 "and not accelerating" — without a growth-
    // trend signal, treat a buffer below 40 as WATCH rather than jumping straight to CRITICAL.
    rule_of_40: { value: rule40 === null ? null : money(rule40), health: health(rule40, n => n >= 40, n => n < 30) },
    burn_multiple: { value: burnMultiple === null ? null : money(burnMultiple), health: health(burnMultiple, n => n < 2, n => n > 2) },
    runway_months: { value: runway, health: health(runway, n => n >= 12, n => n < 6) },
  };
  const critical = Object.entries(metrics).filter(([, metric]) => metric.health === "CRITICAL").map(([name]) => name);
  const watch = Object.values(metrics).some(metric => metric.health === "WATCH");
  const concerningRunway = runway !== null && runway < 6;
  const verdict = critical.length >= 2 || concerningRunway ? "CRITICAL" : critical.length || watch ? "WATCH" : "HEALTHY";
  const drivers = Object.entries(metrics).filter(([, metric]) => metric.health !== "HEALTHY" && metric.health !== "N/A").map(([name, metric]) => `${name}: ${metric.health}`);

  const impliedLow = arr * multipleLow, impliedHigh = arr * multipleHigh;
  const values = [dcfValue, impliedLow, impliedHigh].filter(value => value > 0);
  return {
    schema_version: "1.0.0", venture: model.venture, scenario: model.scenario, stage, arr: money(arr), fiscal_year_revenue: money(fiscalYearRevenue),
    valuation_range: { low: values.length ? money(Math.min(...values)) : 0, high: values.length ? money(Math.max(...values)) : 0 },
    dcf: { value: money(dcfValue), terminal_value: money(terminalValue), terminal_value_pct: terminalPct === null ? null : money(terminalPct), projected_fcfs: projectedFcfs, discount_rate: discountRate, terminal_growth_rate: terminalGrowthRate, warnings: dcfWarnings },
    revenue_multiple: { source: validComps.length ? "comparables" : "stage_default", multiple_low: multipleLow, multiple_high: multipleHigh, implied_value_low: money(impliedLow), implied_value_high: money(impliedHigh), comparables: validComps, warnings: compWarnings },
    saas_health: { verdict, drivers, metrics },
    disclaimer: "Estimates for planning; not legal, tax, or investment advice. Review with an accountant before external use.",
  };
}
