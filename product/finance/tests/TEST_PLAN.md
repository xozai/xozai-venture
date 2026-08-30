# Test plan — financial-model deterministic engine

Owner: Honey0. Scope: `product/finance/engine/` (`calculate.ts`, `validate.ts`, `types.ts`,
`cli.ts`) against the behavior described in `.claude/skills/financial-model/SKILL.md` (merged to
main in PR #7) and `product/finance/schema.json`. Codex's engine and schema were already present
in this checkout when I started (uncommitted, not yet on any branch) — every test case and every
number in this plan and in the two fixtures' `EXPECTED.md` was verified by actually running
`calculate()` against the fixtures on 2026-08-30, not just hand-derived. Re-verify after any
engine change; if a number here stops matching, the engine (or this plan) has a regression.

**Wired into CI:** every case below runs as `product/finance/engine/test/fixtures.test.ts`
(`npm test`). Re-verified 2026-08-30 against the committed engine (main, Codex's PR #16 /
schema+xlsx retry commit `c131489`) — cohort-based churn produces byte-identical figures to the
ones below for both fixtures, since neither uses `revenue.start_month`/`intro_discount_pct`
(uniform per-month churn applied per cohort sums identically to the old aggregate formula when
every cohort ages at the same rate). No `EXPECTED.md` numbers changed.

Two hand-computable fixtures live in `product/finance/tests/fixtures/`:
- `saas-tiny/` — subscription revenue, one paid engineer, one deferred-comp founder, no
  financing. Needs real runway (capital need $90,800 beyond its $50,000 starting cash). Three
  scenarios (base/upside/downside). See its `EXPECTED.md` for the full verified table.
- `services-tiny/` — single-operator services practice, fully deferred-comp founder, no
  financing. Cash-generative from month 1 (capital need $0). Base scenario only. See its
  `EXPECTED.md`.

Both conform to `product/finance/schema.json` v1.0.0 and run cleanly through `cli.ts` /
`calculate()` as committed in this checkout.

## Test cases

### TC-01 — Cash roll-forward reconciles every period, including the m24→Q9 boundary
**Preconditions:** engine run on `fixtures/saas-tiny/assumptions.base.json`.
**Steps:** 1) Run the engine: monthly output m1–m24 (JSON `monthly` array), quarterly from
`Q9` (months 25–27) onward, annual Y1–Y3. 2) For every monthly and quarterly period, compute
`cashBeginning + netCashFlow − cashEnding` (quarterly aggregates omit `cashBeginning` — reconstruct
it as the prior period's `cashEnding`). 3) At the boundary: confirm annual `Y2`'s `cashEnding`
(months 13–24) equals month 24's `cashEnding` in the underlying (pre-slice) monthly series, and
that `Q9`'s reconstructed opening balance chains from it with no drift.
**Expected (verified 2026-08-30):** difference in step 2 is 0 for every period. `Y2.cashEnding =
-78,900`, which equals month 24's `cashEnding` exactly. `Q9`: `startMonth: 25, endMonth: 27,
revenue: 78,000, opex: 45,450, cashEnding: -61,950` — a $16,950 net inflow over the quarter,
consistent with month-24-onward trend (operating income already positive by month 19).

### TC-02 — Personnel cost == roster × loaded rate, incl. start/end-month edges and deferred comp
**Preconditions:** `fixtures/saas-tiny/assumptions.base.json`.
**Steps:**
1. Deferred comp: assert Engineer 1's `personnel` (cash) line = $12,000/mo every month 2–36
   ($14,000 in month 1, including the one-time $2,000 `equipment`), the Founder's `personnel`
   contribution = $0 every month, and the Founder's `deferredComp` = $12,500/mo every month —
   separately reported, never summed into cash `opex` and never dropped.
2. Assert `personnel + deferredComp` = `sum(roster: headcount × (annual_base × (1 + tax% +
   benefits%) / 12 + equipment-in-start-month-only))` computed directly off the roster, matching
   the engine's own `assertChecks` reconciliation (which the engine runs on every `calculate()`
   call and throws on mismatch — confirmed by the clean run against this fixture).
3. **No day-level granularity.** `Person.start_month`/`end_month` are whole-month integers (see
   `product/finance/engine/types.ts`); there is no start-day field. Add a synthetic second
   engineer with `start_month: 10` to a copy of the fixture and confirm month 10's `personnel`
   jumps by exactly that engineer's full `annual_base × 1.2 / 12` — not a fraction of it,
   regardless of which calendar day within month 10 they'd nominally start. If a future schema
   version adds day-level start dates, this test case must be rewritten as a real proration
   check; until then, it exists to catch an *accidental* introduction of undocumented proration.

### TC-03 — Run fails on any material assumption with null value or missing source
**Preconditions:** `fixtures/saas-tiny/assumptions.base.json`, three mutations: (a) null
`sales_marketing.items[0].amount.value`, (b) empty `personnel.roster[0].annual_base.source`,
(c) `services-tiny/assumptions.base.json`'s `cogs` block as-is (`revenue_pct: 0,
per_active_logo_monthly: 0`, both `confidence: "H"`, real source string) as the negative control.
**Steps:** run `calculate()` against each.
**Expected (verified 2026-08-30):** (a) throws `Material assumption has null/empty value at
$.sales_marketing.items[0].amount`. (b) throws `Missing source at
$.personnel.roster[0].annual_base`. Both name the exact offending path — not a generic failure.
(c) runs successfully and produces `gross_margin_pct: 1`; an explicit, sourced zero is accepted,
not treated as missing.

### TC-04 — Three scenarios from one schema produce internally consistent outputs
**Preconditions:** `fixtures/saas-tiny/assumptions.{base,upside,downside}.json` — same cost
assumptions; upside changes `new_logos_monthly: 2` and `acv: 14400`; downside adds
`monthly_logo_churn_pct: 0.08`.
**Steps:** run all three, compare period-by-period (verified 2026-08-30, see `saas-tiny/
EXPECTED.md` for the full table).
**Expected:**
1. Same table shape across all three (same period count/labels) — confirmed.
2. Monotonicity: `cashEnding.downside(t) ≤ cashEnding.base(t) ≤ cashEnding.upside(t)` for every
   month 1–24 — checked programmatically, **zero violations**.
3. Downside converges toward its churn steady-state (`new_logos_monthly ÷ churn ≈ 12.5` active
   logos) instead of growing linearly, and never reaches `break_even_month` within the 36-month
   horizon (`break_even_month: null`) — the engine must report `null`, not throw or wrap to a
   bogus number, when a scenario never breaks even.
4. `services-tiny` ships with only a `base` scenario file: confirmed `calculate()` takes a single
   `ModelInput` and has no dependency on sibling scenario files existing — only `cli.ts`'s
   argument parsing enforces "exactly three files," which is a CLI convenience, not an engine
   constraint. A venture with only one scenario authored so far must still be able to run it.
5. **Cross-cutting finding:** `ltv`/`ltv_cac` are `null` in `saas-tiny` base/upside (zero churn)
   and `cac`/`cac_payback_months` are `null` in `services-tiny` (zero new-logo growth) — both are
   the same divide-by-zero guard in `deriveMetrics`, not a business-type distinction. The engine
   has no `venture_type` concept at all: nothing stops a growing services venture (`new_logos_monthly
   > 0`) from getting a `cac`/`acv` that's computed correctly but semantically meaningless (ACV
   of a "logo" that's actually a billable-hours client relationship). Not a bug in what's built —
   there's no schema hook to flag it as one — but worth Claude/Codex deciding whether `MODEL.md`'s
   narrative should suppress or caveat these metrics based on how `revenue` is populated.

### TC-05 — Override field changes results and is reported in Sources
**Preconditions:** `fixtures/saas-tiny/assumptions.base.json`, `sales_marketing.items[0].amount
.override` set to `1500` (vs. sourced `value: 1000`) per `valueOf()`'s `override ?? value`
semantics in `types.ts`.
**Steps:** run once with `override: null`, once with `override: 1500` (verified 2026-08-30).
**Expected:** `capital_need_to_break_even` rises from **$90,800 to $100,250**; `cash_out_month`
stays at 4 (the shortfall is already established before the extra spend compounds). The engine
itself doesn't emit a "Sources" table (that's `MODEL.md`'s job per SKILL.md step 6, owned by
Claude at assembly time) — this test case's remaining assertion is for that assembly step, not
`calculate()`: confirm the memo lists both the original sourced value and the override (value,
by, date, reason) for any line where `override !== null`, per SKILL.md step 7's "never edited in
place." Flagging this as a gap to close before the first real `MODEL.md` is written: nothing in
`ModelOutput` currently threads override provenance through to the output for the memo to read
back — Claude will need to walk the input assumptions again at write time, not just the
`ModelOutput`.

### TC-06 — Bootstrapped case with empty financing reports cash-out month and capital need
**Preconditions:** both fixtures, `financing.events: []` in both.
**Steps:** run each; read `cash_out_month` and `capital_need_to_break_even`.
**Expected (verified 2026-08-30):** `saas-tiny`: `cash_out_month: 4`,
`capital_need_to_break_even: 90800` — computed as `max(0, -min(opening_cash, all monthly
cashEnding))`, i.e. the capital needed *in addition to* `opening_cash` to keep the balance
non-negative through the trough at month 18, not a total-capital figure. `services-tiny`:
`cash_out_month: null`, `capital_need_to_break_even: 0`. Same formula, same empty-financing,
same deferred-founder-comp shape — opposite outcomes, purely from each fixture's own revenue
timing. Confirms the engine doesn't hardcode "bootstrapped ⇒ runs out of cash."

### TC-07 — Narrative totals match table totals
**Preconditions:** any completed run.
**Steps:** once `MODEL.md`'s narrative-writing step exists (Claude, SKILL.md step 6), extract
every dollar figure the memo prose states and compare each to the corresponding `metrics` /
`monthly` / `annual` cell.
**Expected:** exact match; a rounded prose figure (e.g. "~$91k") must round-trip to its
unrounded source cell. **Not yet testable** — `calculate()` and `cli.ts` produce tables and
Markdown tables (`toMarkdown()`) but no prose memo; that's Claude's assembly step, still pending.
This test case is written now so it's ready the first time a real `MODEL.md` (e.g. for UCM)
exists to check.

### TC-08 — `revenue.start_month` and `intro_discount_pct`/`intro_discount_months` apply per cohort
**Preconditions:** `fixtures/saas-tiny/assumptions.base.json`, with `revenue.start_month: 3`,
`intro_discount_pct: 0.5`, `intro_discount_months: 2` set on a copy of the input (the checked-in
fixture files don't use these fields; UCM's real assumptions do — see `product/finance/ucm/
assumptions.base.json`'s `revenue.start_month: 8`).
**Steps:** run `calculate()`, inspect `monthly[].revenue` and `.newLogos` month by month.
**Expected (verified 2026-08-30):** months 1–2 revenue = 0 (before `start_month`). Month 3 (first
paid month): 1 new logo, revenue = $500 (its own first month, discounted 50%). Month 4: two
cohorts (acquired month 3 and 4), both still inside their 2-month discount window, revenue =
$1,000. Month 5: the month-3 cohort ages out of the discount (full $1,000/mo), the month-4 and
month-5 cohorts are still discounted ($500 each) = $2,000. Confirms the discount is per-cohort
(tracked from each cohort's own acquisition month), not a global ramp applied to total revenue.

### TC-09 — xlsx workbook Checks tab passes and Statements totals equal the engine JSON
**Preconditions:** `product/finance/ucm/assumptions.{base,upside,downside}.json` (the real UCM
assumptions, not a synthetic fixture — chosen because it's the first venture to exercise
`revenue.start_month`).
**Steps:** run `calculate()` on all three, `writeWorkbook()` to a temp directory (not committed —
keeps CI hermetic and avoids a stale binary artifact), reopen with ExcelJS, read back the
`Checks` tab's three formula cells' cached results and sum the `Statements` tab's `Revenue` and
`Operating income` columns (cached formula results; a `result` of exactly `0` is dropped by
ExcelJS on write/read and must be treated as `0`, not `NaN`).
**Expected (verified 2026-08-30):** all three `Checks` rows cache `true`. Summed `Statements`
`Revenue` and `Operating income` columns equal the sum of the engine JSON's own `monthly[].revenue`
/ `.operatingIncome` (24-month slice) to the cent. This is TC-07's workbook half — the narrative
(`MODEL.md` prose-vs-cell) half remains **not yet testable** until a UCM `MODEL.md` exists.

## Out of scope for this plan
- Exact scenario-by-scenario hand-computed tables for `upside`/`downside` beyond the
  monotonicity property — the base case already proves the arithmetic; programmatic comparison
  covers the rest with less transcription risk than a second and third full 36-month table.
- Exports (`model.xlsx`/`.csv`) — Fizz0's scope per SKILL.md. Fizz0's export tests should assert
  export totals match these same `metrics`/table totals (ties into TC-07's principle).
- The real UCM model (`product/finance/ucm/`) — these are synthetic fixtures chosen for
  hand-computability and schema coverage, not the venture's actual numbers. TC-04 point 5's
  revenue-shape finding is directly relevant when UCM's assumptions are assembled, since UCM's
  brief describes per-seat SaaS pricing, which maps cleanly onto this engine's logo model — but
  its evidence-gap ramp period does not, per `saas-tiny/EXPECTED.md` finding #2.
