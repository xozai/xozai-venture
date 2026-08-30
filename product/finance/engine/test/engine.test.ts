import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { assertChecks, calculate } from "../calculate.ts";
import { validateInput } from "../validate.ts";
import type { ModelInput } from "../types.ts";

const fixtureUrl = new URL("./fixtures/saas-placeholder.json", import.meta.url);
const load = async () => JSON.parse(await readFile(fixtureUrl, "utf8")) as ModelInput;

test("SaaS fixture emits required grains and reconciles", async () => {
  const output = calculate(await load());
  assert.equal(output.monthly.length, 24);
  assert.equal(output.quarterly.length, 4);
  assert.equal(output.annual.length, 3);
  assert.deepEqual(output.checks, ["cash_reconciles", "personnel_reconciles", "material_assumptions_present"]);
  for (const row of output.monthly) assert.ok(Math.abs(row.cashEnding - row.cashBeginning - row.netCashFlow) < 0.02);
});

test("bootstrapped founder compensation is memo-only cash", async () => {
  const output = calculate(await load());
  assert.equal(output.monthly[0].personnel, 0);
  assert.equal(output.monthly[0].deferredComp, 12500 + 2000);
  assert.equal(output.monthly[1].deferredComp, 12500);
});

test("personnel equals roster loaded rate after funding", async () => {
  const input = await load();
  const leaf = <T>(value: T, unit: string) => ({ value, unit, source: "test", date: "2026-08-30", confidence: "H" as const, override: null, kind: "input" as const });
  input.financing.events.push({ instrument: leaf("SAFE", "text"), month: leaf(2, "month"), amount: leaf(100000, "USD") });
  const output = calculate(input);
  assert.equal(output.monthly[0].personnel, 0);
  assert.equal(output.monthly[1].personnel, 12500);
});

test("missing material value fails before calculation", async () => {
  const input = await load();
  (input.revenue.acv as unknown as { value: null }).value = null;
  assert.throws(() => validateInput(input), /null\/empty value/);
});

test("cash check detects tampering", async () => {
  const input = await load();
  const output = calculate(input);
  output.monthly[2].cashEnding += 1;
  assert.throws(() => assertChecks(input, output.monthly), /Cash reconciliation failed/);
});

test("revenue start month and introductory discount apply by cohort", async () => {
  const input = await load();
  const leaf = <T>(value: T, unit: string) => ({ value, unit, source: "test", date: "2026-08-30", confidence: "H" as const, override: null, kind: "input" as const });
  input.revenue.start_month = leaf(3, "month");
  input.revenue.intro_discount_pct = leaf(0.5, "decimal");
  input.revenue.intro_discount_months = leaf(2, "months");
  input.revenue.starting_logos.override = 0; input.revenue.acv.override = 12000;
  input.revenue.new_logo_growth_monthly_pct.override = 0; input.revenue.monthly_logo_churn_pct.override = 0; input.revenue.annual_expansion_pct.override = 0;
  const output = calculate(input);
  assert.equal(output.monthly[0].revenue, 0);
  assert.equal(output.monthly[1].revenue, 0);
  assert.equal(output.monthly[2].newLogos, 1);
  assert.equal(output.monthly[2].revenue, 500);
  assert.equal(output.monthly[4].revenue, 2000);
});

test("variable compensation and override provenance are deterministic", async () => {
  const input = await load();
  const leaf = <T>(value: T, unit: string) => ({ value, unit, source: "test", date: "2026-08-30", confidence: "H" as const, override: null, kind: "input" as const });
  const founder = input.personnel.roster[0];
  founder.defer_until_funding.override = false;
  founder.variable_annual = leaf(12000, "USD/year"); founder.attainment_pct = leaf(0.5, "decimal");
  const output = calculate(input);
  assert.equal(output.monthly[0].personnel, 13125 + 2000);
  assert.deepEqual(output.overrides[0], { path: "personnel.roster[0].defer_until_funding", sourcedValue: true, override: false, source: founder.defer_until_funding.source, date: founder.defer_until_funding.date });
});

test("services venture suppresses SaaS unit metrics", async () => {
  const input = await load();
  input.meta.venture_type = { ...input.meta.venture, value: "services", override: null };
  const output = calculate(input);
  assert.equal(output.metrics.acv, null); assert.equal(output.metrics.nrr_annual_pct, null); assert.equal(output.metrics.ltv, null);
});
