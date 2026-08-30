import { mkdir, readFile, writeFile } from "node:fs/promises";
import { basename, join } from "node:path";
import { calculate } from "./calculate.ts";
import { toMarkdown } from "./markdown.ts";
import { writeWorkbook } from "./xlsx.ts";
import type { ModelInput } from "./types.ts";

const args = process.argv.slice(2);
if (args.length < 4 || args[0] !== "--out") {
  console.error("Usage: npm run model -- --out <directory> <base.json> <upside.json> <downside.json>"); process.exit(1);
}
const outDir = args[1], files = args.slice(2);
if (files.length !== 3) throw new Error("Exactly three scenario assumption files are required");
await mkdir(outDir, { recursive: true });
const inputs: ModelInput[] = [], outputs = [];
for (const file of files) {
  const input = JSON.parse(await readFile(file, "utf8")) as ModelInput;
  const output = calculate(input);
  inputs.push(input); outputs.push(output);
  const stem = basename(file, ".json");
  await writeFile(join(outDir, `${stem}.model.json`), `${JSON.stringify(output, null, 2)}\n`);
  await writeFile(join(outDir, `${stem}.model.md`), toMarkdown(output));
}
await writeWorkbook(join(outDir, "model.xlsx"), inputs, outputs);
