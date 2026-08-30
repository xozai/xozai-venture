import assert from "node:assert/strict";
import { mkdtemp, readFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";
import ExcelJS from "exceljs";
import { assertChecks, calculate } from "../calculate.ts";
import { validateInput } from "../validate.ts";
import { writeWorkbook } from "../xlsx.ts";
import type { ModelInput } from "../types.ts";

// These tests assert the engine reproduces the exact figures documented in
// product/finance/tests/TEST_PLAN.md and each fixture's EXPECTED.md. If a
// number here stops matching, the engine (or the plan) has a regression —
// re-verify both together, per TEST_PLAN.md's own instructions.

const fixtures = new URL("../../tests/fixtures/", import.meta.url);
const ucmDir = new URL("../../ucm/", import.meta.url);
const load = async (base: URL, path: string) => JSON.parse(await readFile(new URL(path, base), "utf8")) as ModelInput;

const saasBase = () => load(fixtures, "saas-tiny/assumptions.base.json");
const saasUpside = () => load(fixtures, "saas-tiny/assumptions.upside.json");
const saasDownside = () => load(fixtures, "saas-tiny/assumptions.downside.json");
const servicesBase = () => load(fixtures, "services-tiny/assumptions.base.json");

// TC-01 — cash roll-forward reconciles, including the m24->Q9 boundary
test("TC-01: saas-tiny base cash reconciles across the full horizon and the m24->Q9 boundary", async () => {
  const output = calculate(await saasBase());
  for (const row of output.monthly) assert.ok(Math.abs(row.cashEnding - (row.cashBeginning + row.netCashFlow)) < 0.02);
  assert.equal(output.annual[1].cashEnding, -78900); // Y2 (months 13-24)
  assert.equal(output.monthly.at(-1)!.cashEnding, output.annual[1].cashEnding); // month 24 === Y2 end
  assert.deepEqual(
    { startMonth: output.quarterly[0].startMonth, endMonth: output.quarterly[0].endMonth, revenue: output.quarterly[0].revenue, opex: output.quarterly[0].opex, cashEnding: output.quarterly[0].cashEnding },
    { startMonth: 25, endMonth: 27, revenue: 78000, opex: 45450, cashEnding: -61950 },
  );
});

test("TC-01: saas-tiny base key monthly figures match EXPECTED.md", async () => {
  const output = calculate(await saasBase());
  const expected: Record<number, [number, number, number, number, number]> = {
    1: [1000, 200, 19650, -18850, 31150],
    4: [4000, 800, 15150, -11950, -7100],
    12: [12000, 2400, 15550, -5950, -74300],
    18: [18000, 3600, 15150, -750, -90800],
    19: [19000, 3800, 15150, 50, -90750],
    24: [24000, 4800, 15550, 3650, -78900],
  };
  for (const [month, [revenue, cogs, opex, operatingIncome, cashEnding]] of Object.entries(expected)) {
    const row = output.monthly[Number(month) - 1];
    assert.deepEqual([row.revenue, row.cogs, row.opex, row.operatingIncome, row.cashEnding], [revenue, cogs, opex, operatingIncome, cashEnding], `month ${month}`);
  }
  assert.equal(output.metrics.ending_cash, 31700); // month 36, outside the 24-month monthly slice
});

// TC-02 — personnel cost == roster x loaded rate, incl. deferred comp and no day-level proration
test("TC-02: saas-tiny personnel/deferredComp reconcile against the roster every month", async () => {
  const input = await saasBase();
  const output = calculate(input);
  assertChecks(input, output.monthly); // throws on mismatch; also exercised directly below
  assert.equal(output.monthly[0].personnel, 12000 + 2000); // Engineer 1 cash + one-time equipment
  assert.equal(output.monthly[1].personnel, 12000);
  for (const row of output.monthly) {
    assert.equal(row.deferredComp, 12500); // founder fully deferred, no financing event ever fires
  }
});

test("TC-02: a mid-month hire jumps personnel by the full loaded rate (no proration)", async () => {
  const input = await saasBase();
  const leaf = <T>(value: T, unit: string) => ({ value, unit, source: "test", date: "2026-08-30", confidence: "H" as const, override: null, kind: "input" as const });
  input.personnel.roster.push({
    role: leaf("Engineer 2", "text"), headcount: leaf(1, "FTE"), start_month: leaf(10, "month"), end_month: leaf(0, "month"),
    annual_base: leaf(120000, "USD/year"), employer_tax_pct: leaf(0.1, "decimal"), benefits_pct: leaf(0.1, "decimal"),
    equipment: leaf(0, "USD/FTE"), founder: leaf(false, "boolean"), defer_until_funding: leaf(false, "boolean"),
  });
  const output = calculate(input);
  const jump = output.monthly[9].personnel - output.monthly[8].personnel; // month 10 vs month 9
  assert.equal(jump, (120000 * 1.2) / 12); // full loaded month, not a fraction of it
});

// TC-03 — run fails on any material assumption with null value or missing source; explicit sourced zero is accepted
test("TC-03: null material assumption value fails validation with the offending path", async () => {
  const input = await saasBase();
  (input.sales_marketing.items[0].amount as unknown as { value: null }).value = null;
  assert.throws(() => validateInput(input), /Material assumption has null\/empty value at \$\.sales_marketing\.items\[0\]\.amount/);
});

test("TC-03: missing source on a material assumption fails validation with the offending path", async () => {
  const input = await saasBase();
  input.personnel.roster[0].annual_base.source = "";
  assert.throws(() => validateInput(input), /Missing source at \$\.personnel\.roster\[0\]\.annual_base/);
});

test("TC-03: services-tiny's explicit sourced zero cogs is accepted, not treated as missing", async () => {
  const input = await servicesBase();
  const output = calculate(input);
  assert.equal(output.metrics.gross_margin_pct, 1);
});

// TC-04 — three scenarios from one schema produce internally consistent outputs
test("TC-04: saas-tiny base/upside/downside are internally consistent", async () => {
  const [base, upside, downside] = await Promise.all([calculate(await saasBase()), calculate(await saasUpside()), calculate(await saasDownside())]);
  assert.equal(base.monthly.length, upside.monthly.length);
  assert.equal(base.monthly.length, downside.monthly.length);
  let violations = 0;
  for (let i = 0; i < 24; i++) {
    if (!(downside.monthly[i].cashEnding <= base.monthly[i].cashEnding + 1e-9 && base.monthly[i].cashEnding <= upside.monthly[i].cashEnding + 1e-9)) violations++;
  }
  assert.equal(violations, 0);
  assert.equal(downside.metrics.break_even_month, null); // never breaks even within the horizon
  assert.equal(downside.monthly[23].activeLogos, 10.81); // converges toward churn steady-state, not linear growth
  assert.equal(base.monthly[23].activeLogos, 24);
  // TC-04 point 5: ltv/cac are divide-by-zero guards, not a business-type distinction
  assert.equal(base.metrics.ltv, null);
  assert.equal(base.metrics.ltv_cac, null);
});

test("TC-04: services-tiny runs standalone with only a base scenario file", async () => {
  const output = calculate(await servicesBase());
  assert.equal(output.metrics.cac, null); // new_logos_monthly = 0, same divide-by-zero guard as saas-tiny's ltv
  assert.equal(output.metrics.cac_payback_months, null);
});

// TC-05 — override changes results and is reported in provenance
test("TC-05: overriding sales_marketing amount raises capital_need_to_break_even without moving cash_out_month", async () => {
  const input = await saasBase();
  const before = calculate(input);
  assert.equal(before.metrics.capital_need_to_break_even, 90800);
  input.sales_marketing.items[0].amount.override = 1500;
  const after = calculate(input);
  assert.equal(after.metrics.capital_need_to_break_even, 100250);
  assert.equal(after.metrics.cash_out_month, 4); // shortfall already established before the extra spend compounds
  assert.deepEqual(after.overrides[0], { path: "sales_marketing.items[0].amount", sourcedValue: 1000, override: 1500, source: input.sales_marketing.items[0].amount.source, date: input.sales_marketing.items[0].amount.date });
});

// TC-06 — bootstrapped case with empty financing reports cash-out month and capital need from revenue timing alone
test("TC-06: saas-tiny and services-tiny derive opposite bootstrapped outcomes from the same formula", async () => {
  const saas = calculate(await saasBase());
  const services = calculate(await servicesBase());
  assert.equal(saas.metrics.cash_out_month, 4);
  assert.equal(saas.metrics.capital_need_to_break_even, 90800);
  assert.equal(services.metrics.cash_out_month, null);
  assert.equal(services.metrics.capital_need_to_break_even, 0);
});

// TC-08 — revenue.start_month + intro_discount_pct/intro_discount_months apply per cohort
test("TC-08: revenue.start_month delays revenue and intro_discount_pct applies per cohort for its first N months", async () => {
  const input = await saasBase();
  const leaf = <T>(value: T, unit: string) => ({ value, unit, source: "test", date: "2026-08-30", confidence: "H" as const, override: null, kind: "input" as const });
  input.revenue.start_month = leaf(3, "month");
  input.revenue.intro_discount_pct = leaf(0.5, "decimal");
  input.revenue.intro_discount_months = leaf(2, "months");
  const output = calculate(input);
  assert.equal(output.monthly[0].revenue, 0); // before start_month
  assert.equal(output.monthly[1].revenue, 0);
  assert.equal(output.monthly[2].newLogos, 1);
  assert.equal(output.monthly[2].revenue, 500); // cohort's first month: full $1,000 halved
  assert.equal(output.monthly[3].revenue, 1000); // two cohorts, both still inside their 2-month discount window
  assert.equal(output.monthly[4].revenue, 2000); // month-3 cohort ages out of the discount (full $1,000); two discounted cohorts remain
});

// TC-09 — the xlsx workbook's Checks tab passes and Statements totals equal the engine JSON (TC-07's workbook half)
test("TC-09: UCM workbook Checks tab passes and Statements totals equal the engine JSON", async (t) => {
  const dir = await mkdtemp(join(tmpdir(), "xozai-finance-xlsx-"));
  t.after(() => rm(dir, { recursive: true, force: true }));
  const [baseInput, upsideInput, downsideInput] = await Promise.all([load(ucmDir, "assumptions.base.json"), load(ucmDir, "assumptions.upside.json"), load(ucmDir, "assumptions.downside.json")]);
  const outputs = [baseInput, upsideInput, downsideInput].map((input) => calculate(input));
  const path = join(dir, "model.xlsx");
  await writeWorkbook(path, [baseInput, upsideInput, downsideInput], outputs);

  const workbook = new ExcelJS.Workbook();
  await workbook.xlsx.readFile(path);

  const cellNumber = (value: ExcelJS.CellValue): number => (value && typeof value === "object" ? Number((value as { result?: unknown }).result ?? 0) : Number(value ?? 0));

  const checks = workbook.getWorksheet("Checks")!;
  const passes: unknown[] = [];
  checks.eachRow((row, i) => { if (i > 1) passes.push((row.getCell(2).value as { result?: unknown } | null)?.result); });
  assert.equal(passes.length, 3);
  assert.ok(passes.every((p) => p === true));

  const statements = workbook.getWorksheet("Statements")!;
  let sumRevenue = 0, sumOperatingIncome = 0, rows = 0;
  statements.eachRow((row, i) => { if (i === 1) return; rows++; sumRevenue += cellNumber(row.getCell(2).value); sumOperatingIncome += cellNumber(row.getCell(7).value); });
  assert.equal(rows, outputs[0].monthly.length);
  const round2 = (n: number) => Math.round(n * 100) / 100;
  assert.equal(round2(sumRevenue), round2(outputs[0].monthly.reduce((s, r) => s + r.revenue, 0)));
  assert.equal(round2(sumOperatingIncome), round2(outputs[0].monthly.reduce((s, r) => s + r.operatingIncome, 0)));
});
