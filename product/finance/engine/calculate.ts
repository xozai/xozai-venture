import { valueOf, type AggregatePeriod, type Assumption, type CostItem, type ModelInput, type ModelOutput, type OverrideProvenance, type Period, type Sensitivity } from "./types.ts";
import { validateInput } from "./validate.ts";

const money = (n: number) => Math.round(n * 100) / 100;
const active = (month: number, start: number, end: number) => month >= start && (end === 0 || month <= end);

export function calculate(input: ModelInput, withSensitivities = true): ModelOutput {
  validateInput(input);
  const horizon = valueOf(input.meta.horizon_months);
  const start = new Date(`${valueOf(input.meta.start_month)}-01T00:00:00Z`);
  let logos = valueOf(input.revenue.starting_logos);
  let cash = valueOf(input.meta.opening_cash);
  const revenueStart = input.revenue.start_month ? valueOf(input.revenue.start_month) : 1;
  const introDiscount = input.revenue.intro_discount_pct ? valueOf(input.revenue.intro_discount_pct) : 0;
  const introMonths = input.revenue.intro_discount_months ? valueOf(input.revenue.intro_discount_months) : 0;
  const cohorts: { logos: number; acquired: number }[] = valueOf(input.revenue.starting_logos) ? [{ logos: valueOf(input.revenue.starting_logos), acquired: 1 }] : [];
  const monthly: Period[] = [];
  let firstFundingMonth: number | null = null;
  for (const event of input.financing.events) if (valueOf(event.amount) > 0) firstFundingMonth = Math.min(firstFundingMonth ?? Infinity, valueOf(event.month));

  for (let month = 1; month <= horizon; month++) {
    const newLogos = month >= revenueStart ? valueOf(input.revenue.new_logos_monthly) * Math.pow(1 + valueOf(input.revenue.new_logo_growth_monthly_pct), month - revenueStart) : 0;
    cohorts.forEach(c => c.logos *= 1 - valueOf(input.revenue.monthly_logo_churn_pct));
    if (newLogos) cohorts.push({ logos: newLogos, acquired: month });
    logos = cohorts.reduce((sum, c) => sum + c.logos, 0);
    const expansion = Math.pow(1 + valueOf(input.revenue.annual_expansion_pct), (month - 1) / 12);
    const revenue = month < revenueStart ? 0 : cohorts.reduce((sum, c) => sum + c.logos * valueOf(input.revenue.acv) * expansion / 12 * (month - c.acquired < introMonths ? 1 - introDiscount : 1), 0);
    const cogs = revenue * valueOf(input.cogs.revenue_pct) + logos * valueOf(input.cogs.per_active_logo_monthly);
    let headcount = 0, personnel = 0, deferredComp = 0;
    for (const person of input.personnel.roster) {
      if (!active(month, valueOf(person.start_month), valueOf(person.end_month))) continue;
      const count = valueOf(person.headcount);
      const variable = person.variable_annual && person.attainment_pct ? valueOf(person.variable_annual) * valueOf(person.attainment_pct) : 0;
      const monthlyLoaded = (valueOf(person.annual_base) + variable) * (1 + valueOf(person.employer_tax_pct) + valueOf(person.benefits_pct)) / 12;
      const equipment = month === valueOf(person.start_month) ? valueOf(person.equipment) : 0;
      const due = count * (monthlyLoaded + equipment);
      headcount += count;
      const deferred = valueOf(person.founder) && valueOf(person.defer_until_funding) && (firstFundingMonth === null || month < firstFundingMonth);
      if (deferred) deferredComp += due; else personnel += due;
    }
    const formationLegal = sectionCost(input.formation_legal.items, month, headcount, revenue);
    const gaOps = sectionCost(input.ga_ops.items, month, headcount, revenue);
    const rnd = sectionCost(input.rnd.items, month, headcount, revenue);
    const salesMarketing = sectionCost(input.sales_marketing.items, month, headcount, revenue);
    const opex = personnel + formationLegal + gaOps + rnd + salesMarketing;
    const operatingIncome = revenue - cogs - opex;
    const financing = input.financing.events.filter(e => valueOf(e.month) === month).reduce((sum, e) => sum + valueOf(e.amount), 0);
    const cashBeginning = cash;
    const netCashFlow = operatingIncome + financing;
    cash += netCashFlow;
    const burn = Math.max(0, -operatingIncome);
    const runwayMonths = burn > 0 ? Math.max(0, cash / burn) : null;
    const d = new Date(Date.UTC(start.getUTCFullYear(), start.getUTCMonth() + month - 1, 1));
    monthly.push(roundPeriod({ month, label: d.toISOString().slice(0, 7), activeLogos: logos, newLogos, revenue, cogs, grossProfit: revenue - cogs, headcount, personnel, deferredComp, formationLegal, gaOps, rnd, salesMarketing, opex, operatingIncome, financing, cashBeginning, netCashFlow, cashEnding: cash, burn, runwayMonths }));
  }
  const annual = aggregate(monthly, 12, "Y");
  const quarterly = aggregate(monthly.slice(24), 3, "Q", 24);
  const metrics = deriveMetrics(input, monthly);
  assertChecks(input, monthly);
  const output: ModelOutput = { schema_version: "1.0.0", venture: valueOf(input.meta.venture), scenario: valueOf(input.meta.scenario), ventureType: input.meta.venture_type ? valueOf(input.meta.venture_type) : "saas", currency: valueOf(input.meta.currency), monthly: monthly.slice(0, 24), quarterly, annual, metrics, sensitivities: [], overrides: collectOverrides(input), checks: ["cash_reconciles", "personnel_reconciles", "material_assumptions_present"], disclaimer: "Estimates for planning; not legal, tax, or investment advice. Review with an accountant before external use." };
  if (withSensitivities) output.sensitivities = sensitivityCases(input);
  return output;
}

function sectionCost(items: CostItem[], month: number, headcount: number, revenue: number): number {
  return items.reduce((sum, item) => {
    if (!active(month, valueOf(item.start_month), valueOf(item.end_month))) return sum;
    const cadence = valueOf(item.cadence);
    if (!["monthly", "annual", "one_time"].includes(cadence)) throw new Error(`Unsupported cadence '${cadence}' for ${valueOf(item.name)}`);
    const occurs = cadence === "monthly" || (cadence === "annual" && (month - valueOf(item.start_month)) % 12 === 0) || (cadence === "one_time" && month === valueOf(item.start_month));
    if (!occurs) return sum;
    const basis = item.basis ? valueOf(item.basis) : "fixed";
    const rate = item.rate ? valueOf(item.rate) : valueOf(item.amount);
    return sum + (basis === "per_head" ? rate * headcount : basis === "pct_revenue" ? rate * revenue : valueOf(item.amount));
  }, 0);
}

function roundPeriod(p: Period): Period { return Object.fromEntries(Object.entries(p).map(([k, v]) => [k, typeof v === "number" ? money(v) : v])) as unknown as Period; }

function aggregate(periods: Period[], size: number, prefix: string, offset = 0): AggregatePeriod[] {
  const result: AggregatePeriod[] = [];
  for (let i = 0; i < periods.length; i += size) {
    const rows = periods.slice(i, i + size); if (!rows.length) continue;
    const sum = (key: keyof Period) => money(rows.reduce((n, row) => n + Number(row[key] ?? 0), 0));
    result.push({ label: `${prefix}${Math.floor((i + offset) / size) + 1}`, startMonth: rows[0].month, endMonth: rows.at(-1)!.month, revenue: sum("revenue"), cogs: sum("cogs"), grossProfit: sum("grossProfit"), personnel: sum("personnel"), deferredComp: sum("deferredComp"), formationLegal: sum("formationLegal"), gaOps: sum("gaOps"), rnd: sum("rnd"), salesMarketing: sum("salesMarketing"), opex: sum("opex"), operatingIncome: sum("operatingIncome"), financing: sum("financing"), netCashFlow: sum("netCashFlow"), cashEnding: rows.at(-1)!.cashEnding, headcountEnding: rows.at(-1)!.headcount, activeLogosEnding: rows.at(-1)!.activeLogos });
  }
  return result;
}

function deriveMetrics(input: ModelInput, rows: Period[]): Record<string, number | null> {
  const totalRevenue = rows.reduce((s, r) => s + r.revenue, 0), totalCogs = rows.reduce((s, r) => s + r.cogs, 0), totalSm = rows.reduce((s, r) => s + r.salesMarketing, 0), newLogos = rows.reduce((s, r) => s + r.newLogos, 0);
  const gm = totalRevenue ? (totalRevenue - totalCogs) / totalRevenue : 0;
  const isSaas = !input.meta.venture_type || valueOf(input.meta.venture_type) === "saas";
  const cac = isSaas && newLogos ? totalSm / newLogos : null;
  const monthlyChurn = valueOf(input.revenue.monthly_logo_churn_pct);
  const arpaMonthly = valueOf(input.revenue.acv) / 12;
  const ltv = monthlyChurn > 0 ? arpaMonthly * gm / monthlyChurn : null;
  const cashOut = rows.find(r => r.cashEnding < 0)?.month ?? null;
  const breakEven = rows.find(r => r.operatingIncome >= 0)?.month ?? null;
  const minCash = Math.min(valueOf(input.meta.opening_cash), ...rows.map(r => r.cashEnding));
  return { total_revenue: money(totalRevenue), gross_margin_pct: money(gm), acv: isSaas ? valueOf(input.revenue.acv) : null, cac: cac === null ? null : money(cac), cac_payback_months: cac === null || arpaMonthly * gm <= 0 ? null : money(cac / (arpaMonthly * gm)), nrr_annual_pct: isSaas ? money(Math.pow(1 - monthlyChurn, 12) * (1 + valueOf(input.revenue.annual_expansion_pct))) : null, ltv: isSaas && ltv !== null ? money(ltv) : null, ltv_cac: isSaas && ltv !== null && cac ? money(ltv / cac) : null, cash_out_month: cashOut, break_even_month: breakEven, capital_need_to_break_even: money(Math.max(0, -minCash)), ending_cash: rows.at(-1)?.cashEnding ?? valueOf(input.meta.opening_cash) };
}

export function assertChecks(input: ModelInput, rows: Period[]): void {
  let previous = valueOf(input.meta.opening_cash);
  for (const row of rows) {
    if (Math.abs(row.cashBeginning - previous) > 0.02 || Math.abs(row.cashEnding - (row.cashBeginning + row.netCashFlow)) > 0.02) throw new Error(`Cash reconciliation failed in month ${row.month}`);
    let expected = 0;
    for (const p of input.personnel.roster) if (active(row.month, valueOf(p.start_month), valueOf(p.end_month))) {
      const variable = p.variable_annual && p.attainment_pct ? valueOf(p.variable_annual) * valueOf(p.attainment_pct) : 0;
      const due = valueOf(p.headcount) * ((valueOf(p.annual_base) + variable) * (1 + valueOf(p.employer_tax_pct) + valueOf(p.benefits_pct)) / 12 + (row.month === valueOf(p.start_month) ? valueOf(p.equipment) : 0));
      const fundingMonth = input.financing.events.filter(e => valueOf(e.amount) > 0).reduce<number | null>((n, e) => Math.min(n ?? Infinity, valueOf(e.month)), null);
      if (!(valueOf(p.founder) && valueOf(p.defer_until_funding) && (fundingMonth === null || row.month < fundingMonth))) expected += due;
    }
    if (Math.abs(row.personnel - expected) > 0.02) throw new Error(`Personnel reconciliation failed in month ${row.month}`);
    previous = row.cashEnding;
  }
}

function collectOverrides(input: ModelInput): OverrideProvenance[] {
  const found: OverrideProvenance[] = [];
  const walk = (node: unknown, path: string) => {
    if (Array.isArray(node)) return node.forEach((v, i) => walk(v, `${path}[${i}]`));
    if (!node || typeof node !== "object") return;
    if ("value" in node && "override" in node) {
      const a = node as Assumption;
      if (a.override !== null) found.push({ path, sourcedValue: a.value, override: a.override, source: a.source, date: a.date });
      return;
    }
    Object.entries(node).forEach(([k, v]) => k !== "schema_version" && walk(v, path ? `${path}.${k}` : k));
  };
  walk(input, "");
  return found;
}

function sensitivityCases(input: ModelInput): Sensitivity[] {
  const cases: [string, string, (x: ModelInput) => void][] = [
    ["price", "+10%", x => { x.revenue.acv.override = valueOf(x.revenue.acv) * 1.1; }],
    ["win_rate", "+10%", x => { x.revenue.new_logos_monthly.override = valueOf(x.revenue.new_logos_monthly) * 1.1; }],
    ["churn", "+10%", x => { x.revenue.monthly_logo_churn_pct.override = valueOf(x.revenue.monthly_logo_churn_pct) * 1.1; }],
    ["hiring_pace", "+3 months", x => { for (const p of x.personnel.roster) if (!valueOf(p.founder)) p.start_month.override = valueOf(p.start_month) + 3; }]
  ];
  return cases.map(([variable, change, mutate]) => { const clone = structuredClone(input); mutate(clone); const result = calculate(clone, false); return { variable, change, revenue: Number(result.metrics.total_revenue), cashEnding: Number(result.metrics.ending_cash), capitalNeed: Number(result.metrics.capital_need_to_break_even) }; });
}
