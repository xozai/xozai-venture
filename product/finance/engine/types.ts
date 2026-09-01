export type Confidence = "H" | "M" | "L";
export type Kind = "benchmark" | "derived" | "input";
export type Assumption<T = string | number | boolean> = { value: T; unit: string; source: string; date: string; confidence: Confidence; override: T | null; kind: Kind };
export const valueOf = <T>(a: Assumption<T>): T => a.override === null ? a.value : a.override;
export type CostItem = { name: Assumption<string>; amount: Assumption<number>; cadence: Assumption<string>; start_month: Assumption<number>; end_month: Assumption<number>; basis?: Assumption<"fixed" | "per_head" | "pct_revenue">; rate?: Assumption<number>; notes?: Assumption<string> };
export type CostSection = { items: CostItem[] };
export type Person = { role: Assumption<string>; headcount: Assumption<number>; start_month: Assumption<number>; end_month: Assumption<number>; annual_base: Assumption<number>; employer_tax_pct: Assumption<number>; benefits_pct: Assumption<number>; equipment: Assumption<number>; founder: Assumption<boolean>; defer_until_funding: Assumption<boolean>; variable_annual?: Assumption<number>; attainment_pct?: Assumption<number> };
export interface ModelInput {
  schema_version: "1.0.0";
  meta: { venture: Assumption<string>; scenario: Assumption<string>; venture_type?: Assumption<"saas" | "services" | "marketplace">; currency: Assumption<string>; start_month: Assumption<string>; horizon_months: Assumption<number>; opening_cash: Assumption<number> };
  formation_legal: CostSection; ga_ops: CostSection; personnel: { roster: Person[] }; rnd: CostSection; sales_marketing: CostSection;
  cogs: { revenue_pct: Assumption<number>; per_active_logo_monthly: Assumption<number> };
  revenue: { starting_logos: Assumption<number>; new_logos_monthly: Assumption<number>; new_logo_growth_monthly_pct: Assumption<number>; monthly_logo_churn_pct: Assumption<number>; acv: Assumption<number>; annual_expansion_pct: Assumption<number>; billing_terms_months: Assumption<number>; start_month?: Assumption<number>; intro_discount_pct?: Assumption<number>; intro_discount_months?: Assumption<number> };
  financing: { events: { instrument: Assumption<string>; month: Assumption<number>; amount: Assumption<number> }[] };
}
export interface Period { month: number; label: string; activeLogos: number; newLogos: number; revenue: number; cogs: number; grossProfit: number; headcount: number; personnel: number; deferredComp: number; formationLegal: number; gaOps: number; rnd: number; salesMarketing: number; opex: number; operatingIncome: number; financing: number; cashBeginning: number; netCashFlow: number; cashEnding: number; burn: number; runwayMonths: number | null }
export interface OverrideProvenance { path: string; sourcedValue: unknown; override: unknown; source: string; date: string }
export interface ModelOutput { schema_version: "1.0.0"; venture: string; scenario: string; ventureType: string; currency: string; monthly: Period[]; quarterly: AggregatePeriod[]; annual: AggregatePeriod[]; metrics: Record<string, number | null>; sensitivities: Sensitivity[]; overrides: OverrideProvenance[]; checks: string[]; disclaimer: string }
export interface AggregatePeriod { label: string; startMonth: number; endMonth: number; revenue: number; cogs: number; grossProfit: number; personnel: number; deferredComp: number; formationLegal: number; gaOps: number; rnd: number; salesMarketing: number; opex: number; operatingIncome: number; financing: number; netCashFlow: number; cashEnding: number; headcountEnding: number; activeLogosEnding: number }
export interface Sensitivity { variable: string; change: string; revenue: number; cashEnding: number; capitalNeed: number }
export interface ValuationComparable { name: string; ev_revenue_multiple: number }
export interface ValuationConfig { stage?: string; discount_rate?: number; terminal_growth_rate?: number; comparables?: ValuationComparable[] }
export type HealthBand = "HEALTHY" | "WATCH" | "CRITICAL" | "N/A";
export interface ValuationOutput {
  schema_version: "1.0.0"; venture: string; scenario: string; stage: string; arr: number; fiscal_year_revenue: number;
  valuation_range: { low: number; high: number };
  dcf: { value: number; terminal_value: number; terminal_value_pct: number | null; projected_fcfs: number[]; discount_rate: number; terminal_growth_rate: number; warnings: string[] };
  revenue_multiple: { source: "comparables" | "stage_default"; multiple_low: number; multiple_high: number; implied_value_low: number; implied_value_high: number; comparables: ValuationComparable[]; warnings: string[] };
  saas_health: { verdict: Exclude<HealthBand, "N/A">; drivers: string[]; metrics: Record<string, { value: number | null; health: HealthBand }> };
  disclaimer: string;
}
