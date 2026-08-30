import type { Assumption, ModelInput } from "./types.ts";

const REQUIRED = ["schema_version", "meta", "formation_legal", "ga_ops", "personnel", "rnd", "sales_marketing", "cogs", "revenue", "financing"];
const leafKeys = ["value", "unit", "source", "date", "confidence", "override", "kind"];
const isLeaf = (x: unknown): x is Assumption => !!x && typeof x === "object" && "value" in x;

export function validateInput(input: unknown): asserts input is ModelInput {
  if (!input || typeof input !== "object") throw new Error("Input must be an object");
  const root = input as Record<string, unknown>;
  for (const key of REQUIRED) if (!(key in root)) throw new Error(`Missing required section: ${key}`);
  if (root.schema_version !== "1.0.0") throw new Error("Unsupported schema_version; expected 1.0.0");
  walk(root, "$");
  const model = input as ModelInput;
  const horizon = effectiveNumber(model.meta.horizon_months, "$.meta.horizon_months");
  if (!Number.isInteger(horizon) || horizon < 1 || horizon > 120) throw new Error("horizon_months must be an integer from 1 to 120");
  if (!/^\d{4}-\d{2}$/.test(String(model.meta.start_month.value))) throw new Error("start_month must be YYYY-MM");
  if (model.meta.currency.value !== "USD") throw new Error("v1 supports currency USD only");
}

function walk(node: unknown, path: string): void {
  if (Array.isArray(node)) return node.forEach((item, i) => walk(item, `${path}[${i}]`));
  if (!node || typeof node !== "object") throw new Error(`Material leaf at ${path} is not an assumption object`);
  if (isLeaf(node)) {
    const a = node as unknown as Record<string, unknown>;
    for (const key of leafKeys) if (!(key in a)) throw new Error(`Missing ${key} at ${path}`);
    if (a.value === null || a.value === undefined || a.value === "") throw new Error(`Material assumption has null/empty value at ${path}`);
    if (!String(a.source).trim()) throw new Error(`Missing source at ${path}`);
    if (!/^\d{4}-\d{2}-\d{2}$/.test(String(a.date))) throw new Error(`Invalid date at ${path}`);
    if (!["H", "M", "L"].includes(String(a.confidence))) throw new Error(`Invalid confidence at ${path}`);
    if (!["benchmark", "derived", "input"].includes(String(a.kind))) throw new Error(`Invalid kind at ${path}`);
    return;
  }
  for (const [key, value] of Object.entries(node)) {
    if (path === "$" && key === "schema_version") continue;
    walk(value, `${path}.${key}`);
  }
}

function effectiveNumber(a: Assumption<number>, path: string): number {
  const value = a.override === null ? a.value : a.override;
  if (typeof value !== "number" || !Number.isFinite(value)) throw new Error(`Expected finite number at ${path}`);
  return value;
}
