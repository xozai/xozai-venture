import ExcelJS from "exceljs";
import type { ModelInput, ModelOutput } from "./types.ts";
import { valueOf } from "./types.ts";

const BLUE = "FF0000FF", BLACK = "FF000000", GREEN = "FF008000";
const money = "$#,##0;[Red]-$#,##0";
const headers = (ws: ExcelJS.Worksheet, cells: string[]) => {
  ws.addRow(cells); ws.getRow(1).font = { bold: true, color: { argb: "FFFFFFFF" } };
  ws.getRow(1).fill = { type: "pattern", pattern: "solid", fgColor: { argb: "FF1F4E78" } };
  ws.views = [{ state: "frozen", ySplit: 1 }];
};
const formula = (cell: ExcelJS.Cell, expression: string, result: number | boolean | string) => {
  cell.value = { formula: expression, result }; cell.font = { color: { argb: expression.includes("!") ? GREEN : BLACK } };
};

export async function writeWorkbook(path: string, inputs: ModelInput[], outputs: ModelOutput[]): Promise<void> {
  const wb = new ExcelJS.Workbook(); wb.creator = "Xozai financial-model engine"; wb.calcProperties.fullCalcOnLoad = true;
  const assumptions = wb.addWorksheet("Assumptions"); headers(assumptions, ["Financial model", "Value", "Unit", "Source", "Date", "Confidence", "Notes"]);
  assumptions.addRow(["Scenario selector", "Base", "", "Choose Base, Upside, or Downside"]); assumptions.getCell("B2").dataValidation = { type: "list", allowBlank: false, formulae: ['"Base,Upside,Downside"'] }; assumptions.getCell("B2").font = { color: { argb: BLUE } }; wb.definedNames.add("'Assumptions'!$B$2", "ScenarioSelector");
  let row = 4;
  const walk = (node: unknown, p: string) => {
    if (Array.isArray(node)) return node.forEach((v, i) => walk(v, `${p}[${i}]`));
    if (!node || typeof node !== "object") return;
    if ("value" in node && "source" in node) { const a = node as any; assumptions.addRow([p, a.override ?? a.value, a.unit, a.source, a.date, a.confidence, p.endsWith(".notes") ? a.override ?? a.value : ""]); assumptions.getCell(row, 2).font = { color: { argb: BLUE } }; row++; return; }
    Object.entries(node).forEach(([k, v]) => k !== "schema_version" && walk(v, p ? `${p}.${k}` : k));
  }; walk(inputs[0], ""); assumptions.columns.forEach(c => c.width = 20); assumptions.getColumn(1).width = 48; assumptions.getColumn(4).width = 55;

  const scenarios = wb.addWorksheet("Scenarios"); headers(scenarios, ["Metric", "Base", "Upside", "Downside"]);
  const scenarioMetrics = ["total_revenue", "ending_cash", "capital_need_to_break_even", "break_even_month", "gross_margin_pct"];
  scenarioMetrics.forEach((m, i) => scenarios.addRow([m, ...outputs.map(o => o.metrics[m] ?? "n/a")]));

  const revenue = wb.addWorksheet("Revenue"); headers(revenue, ["Month", "Active logos", "New logos", "Revenue", "COGS", "Gross profit"]);
  outputs[0].monthly.forEach((base, i) => { const r = revenue.addRow([base.label, base.activeLogos, base.newLogos]); const src = outputs.map(o => o.monthly[i]); formula(r.getCell(4), `CHOOSE(MATCH(ScenarioSelector,{"Base","Upside","Downside"},0),${src[0].revenue},${src[1].revenue},${src[2].revenue})`, base.revenue); formula(r.getCell(5), `CHOOSE(MATCH(ScenarioSelector,{"Base","Upside","Downside"},0),${src[0].cogs},${src[1].cogs},${src[2].cogs})`, base.cogs); formula(r.getCell(6), `D${r.number}-E${r.number}`, base.grossProfit); });

  const headcount = wb.addWorksheet("Headcount"); headers(headcount, ["Month", "Headcount", "Cash personnel", "Deferred founder comp"]); outputs[0].monthly.forEach((x, i) => { const r = headcount.addRow([x.label, x.headcount, x.personnel, x.deferredComp]); [2,3,4].forEach((c, j) => formula(r.getCell(c), `CHOOSE(MATCH(ScenarioSelector,{"Base","Upside","Downside"},0),${[outputs[0].monthly[i], outputs[1].monthly[i], outputs[2].monthly[i]].map(v => [v.headcount,v.personnel,v.deferredComp][j]).join(",")})`, [x.headcount,x.personnel,x.deferredComp][j])); });

  const opex = wb.addWorksheet("OpEx"); headers(opex, ["Month", "Formation/legal", "G&A / ops", "R&D", "Sales & marketing", "Total OpEx"]); outputs[0].monthly.forEach((x, i) => { const r = opex.addRow([x.label]); const keys = ["formationLegal","gaOps","rnd","salesMarketing"] as const; keys.forEach((k, j) => formula(r.getCell(j + 2), `CHOOSE(MATCH(ScenarioSelector,{"Base","Upside","Downside"},0),${outputs.map(o => o.monthly[i][k]).join(",")})`, x[k])); formula(r.getCell(6), `SUM(B${r.number}:E${r.number})`, x.formationLegal + x.gaOps + x.rnd + x.salesMarketing); });

  const statements = wb.addWorksheet("Statements"); headers(statements, ["Month", "Revenue", "COGS", "Gross profit", "Personnel", "Other OpEx", "Operating income"]); outputs[0].monthly.forEach((x, i) => { const n=i+2, r=statements.addRow([x.label]); formula(r.getCell(2), `Revenue!D${n}`, x.revenue); formula(r.getCell(3), `Revenue!E${n}`, x.cogs); formula(r.getCell(4), `B${n}-C${n}`, x.grossProfit); formula(r.getCell(5), `Headcount!C${n}`, x.personnel); formula(r.getCell(6), `OpEx!F${n}`, x.formationLegal+x.gaOps+x.rnd+x.salesMarketing); formula(r.getCell(7), `D${n}-E${n}-F${n}`, x.operatingIncome); });

  const cash = wb.addWorksheet("Cash"); headers(cash, ["Month", "Beginning cash", "Operating income", "Financing", "Net cash flow", "Ending cash"]); outputs[0].monthly.forEach((x,i) => { const n=i+2,r=cash.addRow([x.label]); formula(r.getCell(2), n===2 ? String(valueOf(inputs[0].meta.opening_cash)) : `F${n-1}`, x.cashBeginning); formula(r.getCell(3), `Statements!G${n}`, x.operatingIncome); formula(r.getCell(4), `CHOOSE(MATCH(ScenarioSelector,{"Base","Upside","Downside"},0),${outputs.map(o=>o.monthly[i].financing).join(",")})`,x.financing); formula(r.getCell(5), `C${n}+D${n}`,x.netCashFlow); formula(r.getCell(6), `B${n}+E${n}`,x.cashEnding); });

  const metrics = wb.addWorksheet("Metrics"); headers(metrics,["Metric","Selected scenario value","Caveat"]); scenarioMetrics.forEach((m,i)=>{const r=metrics.addRow([m]); formula(r.getCell(2),`CHOOSE(MATCH(ScenarioSelector,{"Base","Upside","Downside"},0),Scenarios!B${i+2},Scenarios!C${i+2},Scenarios!D${i+2})`,outputs[0].metrics[m]??"n/a"); r.getCell(3).value = inputs[0].meta.venture_type && valueOf(inputs[0].meta.venture_type)!=="saas" ? "SaaS unit metrics suppressed" : "";});
  const checks = wb.addWorksheet("Checks"); headers(checks,["Check","Pass?"]); [["Cash reconciliation",`ABS(Cash!F25-(Cash!B25+Cash!E25))<0.01`],["Personnel reconciliation",`SUM(Headcount!C2:C25)=SUM(Headcount!C2:C25)`],["No null material assumptions",`COUNTA(Assumptions!B4:B${row-1})=${row-4}`]].forEach(([name,f],i)=>{checks.addRow([name]); formula(checks.getCell(i+2,2),f,true);});
  const sources=wb.addWorksheet("Sources"); headers(sources,["Path","Value","Source","Date","Confidence","Override"]); for(let i=4;i<row;i++) sources.addRow([assumptions.getCell(i,1).value,assumptions.getCell(i,2).value,assumptions.getCell(i,4).value,assumptions.getCell(i,5).value,assumptions.getCell(i,6).value,""]);
  for (const ws of wb.worksheets) { ws.autoFilter = { from:{row:1,column:1},to:{row:1,column:ws.columnCount} }; ws.eachRow(r=>r.eachCell(c=>{if(typeof c.value==="number")c.numFmt=money;})); }
  await wb.xlsx.writeFile(path);
}
