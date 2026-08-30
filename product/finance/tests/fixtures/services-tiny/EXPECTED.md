# Expected values — fixture-services-tiny

Verified by running `product/finance/engine/calculate.ts` directly against
`assumptions.base.json` on 2026-08-30 (this fixture is a single scenario; see TC-04 point 4 for
why that's a valid, separately-tested case).
Re-verified 2026-08-30 against the committed engine on main (PR #16, commit `c131489`) via
`product/finance/engine/test/fixtures.test.ts`: every figure below is unchanged by the
cohort-based churn rewrite (this fixture has zero `new_logos_monthly`, so cohort tracking is a
no-op here regardless).

## Why this fixture is modeled the way it is
The engine's revenue module has exactly one shape: `activeLogos × acv`, with logo count driven
by `starting_logos`, `new_logos_monthly` (compounding), and churn (see `saas-tiny/EXPECTED.md`
finding #2). There is no billable-hours × rate primitive. This fixture represents a one-person
services practice as **one always-on "logo"** (the founder's own client base) with
`acv = 144,000` (= $12,000/mo × 12, standing in for 80 billable hrs/mo × $150/hr) and
`new_logos_monthly = 0` (no additional logo growth — this is deliberately a single-operator
business, distinct from `saas-tiny`'s growing customer count). `cogs` is explicitly `revenue_pct:
0, per_active_logo_monthly: 0` with `confidence: H` — a services engagement has no third-party
per-unit cost, since labor is already inside `personnel` (TC-03's negative control: an explicit,
sourced zero is accepted, not treated as a missing material assumption).

## Fixed monthly recurring cost
`ga_ops` $1,200 + `rnd` $100 + `sales_marketing` $500 = **$1,800/mo** cash, every month.
`personnel` cash = **$0** every month (`founder: true`, `defer_until_funding: true`, no financing
event ever fires, so deferral never lifts — same mechanic as `saas-tiny`, proving it isn't
SaaS-specific). `deferredComp` memo = $10,000/mo every month, tracked but never in cash `opex`.

## Engine output
| Month | revenue | cogs | opex | operatingIncome | cashEnding |
|---:|---:|---:|---:|---:|---:|
| 1 | 12,000 | 0 | 4,300 (incl. $2,500 one-time formation) | 7,700 | 17,700 |
| 2 | 12,000 | 0 | 1,800 | 10,200 | 27,900 |
| 3 | 12,000 | 0 | 1,800 | 10,200 | 38,100 |
| 4 | 12,000 | 0 | 1,800 | 10,200 | 48,300 |

`metrics`: `cash_out_month: null` (balance never goes negative — even month 1, with the $2,500
one-time formation cost, ends positive at $17,700 against the $10,000 starting cash plus
month-1 revenue), `break_even_month: 1` (operating income is positive from the very first month —
there's no ramp to model, per the note above), `capital_need_to_break_even: 0`,
`total_revenue: 432000` (36 × 12,000), `gross_margin_pct: 1` (COGS is $0 by construction),
`cac: null`, `cac_payback_months: null` (both null because `new_logos_monthly = 0` — zero new
logos this period makes CAC's denominator zero, so the engine returns `null` rather than
dividing by zero; this is the same guard pattern as `saas-tiny`'s `ltv`/`ltv_cac`, not a
business-type check — the engine has no concept of venture type at all, which is itself worth
flagging: nothing stops a services venture's `acv`/`cac`/`nrr_annual_pct` from being computed
and reported as if they were meaningful SaaS unit economics when `new_logos_monthly > 0`, e.g.
if this fixture instead modeled multiple growing client relationships).

## Contrast with `saas-tiny`
Same deferred-founder-comp mechanic and the same "no financing ⇒ deferral never lifts" behavior,
but the outcome is opposite: `saas-tiny` needs $90,800 of capital beyond its $50,000 starting
cash before it turns cash-generative at month 19; `services-tiny` is cash-generative from month 1
and needs nothing beyond its (much smaller) $10,000 starting cash. TC-06 checks the engine
derives both outcomes from the shared formula, not a hardcoded "bootstrapped ⇒ runs out of cash"
assumption.
