import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { calculate } from "../calculate.ts";
import { calculateValuation } from "../valuation.ts";
import type { ModelInput } from "../types.ts";

const fixture = new URL("../../tests/fixtures/saas-tiny/assumptions.base.json", import.meta.url);
const load = async () => JSON.parse(await readFile(fixture, "utf8")) as ModelInput;

test("v3 valuation uses engine output and flags stage-default multiples", async () => {
  const input = await load();
  const valuation = calculateValuation(input, calculate(input), { stage: "seed" });
  assert.equal(valuation.revenue_multiple.source, "stage_default");
  assert.deepEqual([valuation.revenue_multiple.multiple_low, valuation.revenue_multiple.multiple_high], [10, 15]);
  assert.ok(valuation.revenue_multiple.warnings[0].includes("No sourced comparables"));
  assert.ok(valuation.valuation_range.low <= valuation.valuation_range.high);
  assert.equal(valuation.saas_health.verdict, "WATCH");
});

test("v3 valuation uses supplied comparable range", async () => {
  const input = await load();
  const valuation = calculateValuation(input, calculate(input), { comparables: [
    { name: "Low Co", ev_revenue_multiple: 7 }, { name: "High Co", ev_revenue_multiple: 11 },
  ] });
  assert.equal(valuation.revenue_multiple.source, "comparables");
  assert.deepEqual([valuation.revenue_multiple.multiple_low, valuation.revenue_multiple.multiple_high], [7, 11]);
  assert.deepEqual(valuation.revenue_multiple.warnings, []);
});

test("v3 verdict follows the documented critical-metric rule", async () => {
  const input = await load();
  input.revenue.monthly_logo_churn_pct.override = 0.1;
  const valuation = calculateValuation(input, calculate(input));
  assert.equal(valuation.saas_health.metrics.nrr_pct.health, "CRITICAL");
  assert.ok(["WATCH", "CRITICAL"].includes(valuation.saas_health.verdict));
});

test("v3 valuation rejects an invalid Gordon-growth spread", async () => {
  const input = await load();
  assert.throws(() => calculateValuation(input, calculate(input), { discount_rate: 0.03, terminal_growth_rate: 0.03 }), /must exceed/);
});
