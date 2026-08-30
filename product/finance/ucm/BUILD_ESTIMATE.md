# UCM product build estimate (Codex, 2026-08-30)

Source: Codex reply in Xozai thread `3c541c66…`, event `694acd08…`, 2026-08-30 14:58 UTC.
Planning estimate; confidence **M** for app/platform work, **L** for ingestion/overlay until
20–30 representative utility-record and plan-set samples are tested. Feeds the `rnd` and
`cogs` sections of `assumptions.*.json`.

## Effort by milestone (base)

| Milestone | Scope | Incremental eng-months | Calendar |
|---|---|---:|---:|
| M1 — walking skeleton | Project/auth, upload PDF + CSV/XLSX, manual field mapping/georeference, plan-view overlay, editable conflict matrix, XLSX export | 3 | months 1–2 |
| M2 — feature complete | Repeatable ingestion, extraction/review queue, milestone versions + diffs, conflict lifecycle/assignment, agency-template export, billing/admin | 5 | months 3–5 |
| M3 — release candidate | Real-project QA, security/backups/audit trail, performance, observability, onboarding, accessibility, import/export hardening | 3 | months 6–7 |

Assumptions: web SaaS, managed Postgres/object storage, plan sheets primarily PDF plus CSV/XLSX
utility records, human-confirmed georeferencing, no native DWG authoring or automated
engineering judgment. Visual overlay included (the brief's strongest demo).

## Scenario envelope

| Scenario | Total eng-months | M1 / M2 / M3 cumulative calendar | Main assumption |
|---|---:|---|---|
| Upside | 7–8 (model: 8) | 1.5 / 3.5 / 5 mo | Clean standardized PDFs/tables; reuse mature GIS components; narrow export templates |
| Base | 11 | 2 / 5 / 7 mo | Mixed PDFs + spreadsheets; human-in-loop alignment and extraction |
| Downside | 16–20 (model: 18) | 3 / 8 / 11–13 mo | Scanned/as-built records, inconsistent coordinate systems, DWG/DGN pressure, many agency formats |

Post-v1 (excluded): +3–6 eng-months native DWG/DGN ingestion; +4–8 automatic spatial conflict
detection. One-time $2k–5k data/parser spike before locking the estimate. 15% contingency on
contractor/tooling spend. Capitalize nothing unless the accountant directs.

## Team shape
- M1: 1 senior full-stack/geospatial engineer + 0.5 product/domain founder + 0.25 design/QA.
- M2–M3: +1 full-stack/product engineer; senior geospatial lead retained; founder 0.25–0.5;
  design 0.2; QA 0.5 → 1.0 near release; fractional security/privacy review at M3.
- ≈ 2 FTE engineers, ~7 calendar months to M3 in base.

## Infrastructure + LLM/API run rate (monthly, base usage; excludes payroll, support, taxes, payment fees)

| Active users | Core hosting/data/monitoring | OCR + LLM/API | Total |
|---:|---:|---:|---:|
| 10 | $250–450 | $50–150 | $300–600 |
| 100 | $500–1,100 | $300–900 | $800–2,000 |
| 1,000 | $2,500–7,000 | $3,000–9,000 | $5,500–16,000 |

API cost per active user/month: **$3–9 base, $1–4 upside, $10–25 downside** — driven by pages
processed, OCR quality, retries, model choice, not seats. Minimum managed-service fees dominate
at 10 users; document processing + storage/egress dominate at 1,000.

First architecture spike should measure parse success, manual correction minutes, and cost per
processed plan set.
