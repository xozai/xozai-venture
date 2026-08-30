# Expected values — fixture-saas-tiny

Hand-computed, then verified by running `product/finance/engine/calculate.ts` directly against
`assumptions.base.json` / `.upside.json` / `.downside.json` on 2026-08-30. Every figure below is
the engine's actual output, not a projection — re-verify after any engine change.

## Fixed monthly recurring cost (base)
personnel cash (Engineer 1 only; founder is 100% deferred) $12,000 + ga_ops $2,000 + rnd $150 +
sales_marketing $1,000 = **$15,150/mo**, every month from month 2 on (month 1 additionally carries
$2,000 one-time equipment). Founder memo cost (`deferredComp`, non-cash) = $12,500/mo, every
month 1–36, since `financing.events` is empty so `defer_until_funding` never lifts.

## Revenue and COGS (base: no churn, 1 new logo/mo from month 1)
`activeLogos(N) = N` (schema has no per-item start delay for revenue — logos accrue from month 1
unconditionally; see "Findings" below). `revenue(N) = 1,000 × N`. `cogs(N) = 200 × N`
(`per_active_logo_monthly`, `revenue_pct = 0`). Gross margin = 80% every month with revenue.

## Engine output, base scenario (`calculate()` on `assumptions.base.json`)
| Month | revenue | cogs | opex | operatingIncome | cashEnding |
|---:|---:|---:|---:|---:|---:|
| 1 | 1,000 | 200 | 19,650 | −18,850 | 31,150 |
| 4 | 4,000 | 800 | 15,150 | −11,950 | **−7,100** ← first negative balance |
| 12 | 12,000 | 2,400 | 15,550 | −5,950 | −74,300 (= annual Y1 `cashEnding`) |
| 18 | 18,000 | 3,600 | 15,150 | −750 | **−90,800 ← trough (minimum cash)** |
| 19 | 19,000 | 3,800 | 15,150 | **+50 ← first month operating income ≥ 0** | −90,750 |
| 24 | 24,000 | 4,800 | 15,550 | 3,650 | −78,900 (= annual Y2 `cashEnding`) |
| 36 | — | — | — | — | 31,700 (= `metrics.ending_cash`, = annual Y3 `cashEnding`) |

`metrics`: `cash_out_month: 4`, `break_even_month: 19`,
`capital_need_to_break_even: 90800` (= `max(0, -min(opening_cash, all cashEnding))`; here the min
is month 18's −90,800 — this is the number to raise/self-fund *in addition to* the $50,000
`opening_cash` already in the trajectory, not a total), `total_revenue: 666000`,
`gross_margin_pct: 0.8`, `acv: 12000`, `cac: 1000` (S&M ÷ new logos), `cac_payback_months: 1.25`,
`nrr_annual_pct: 1`, `ltv: null`, `ltv_cac: null` (both null because `monthly_logo_churn_pct = 0`
makes lifetime undefined — a divide-by-zero guard, not a business-type branch; see TEST_PLAN TC-04).

## Quarterly boundary (TC-01)
`quarterly[0]` (label `Q9`) covers `startMonth: 25, endMonth: 27`: revenue 78,000, opex 45,450,
`cashEnding: -61,950`. `annual[1]` (Y2, months 13–24) `cashEnding: -78,900` — this must equal
month 24's `cashEnding` in the full (pre-slice) monthly series, and `Q9`'s `cashBeginning`
(reconstructed as `cashEnding(24) + first-item netCashFlow` since `AggregatePeriod` doesn't carry
`cashBeginning` directly) must chain from it with no drift.

## Override (TC-05)
Overriding `sales_marketing.items[0].amount.override = 1500` (vs. sourced value 1,000): the run
still cash-out's in month 4 (unchanged — the shortfall was already established before the extra
$500/mo compounds), but `capital_need_to_break_even` rises from **90,800 to 100,250**
(+9,450 over the 18-month pre-breakeven window at approximately +$500/mo, consistent with
break-even also shifting later).

## Upside / downside metrics (engine-verified, not hand-derived)
| | base | upside (2 adds/mo, $1,200 price) | downside (8%/mo churn) |
|---|---:|---:|---:|
| `cash_out_month` | 4 | 5 | 4 |
| `break_even_month` | 19 | 8 | **null (never, within 36mo)** |
| `capital_need_to_break_even` | 90,800 | 4,550 | 250,384.43 |
| `ending_cash` (month 36) | 31,700 | 830,900 | −250,384.43 |
| `nrr_annual_pct` | 1.0 | 1.0 | 0.37 |

Monotonicity (TC-04): `cashEnding.downside(t) ≤ cashEnding.base(t) ≤ cashEnding.upside(t)` holds
for every month 1–24 in the JSON output — verified by direct comparison, zero violations.
Downside logo count converges toward the churn steady-state (`new_logos_monthly / churn ≈ 12.5`)
rather than growing linearly — by month 24 it's 10.81 active logos vs. base's 24.

## Findings from building this fixture against the real engine
1. **No day-level granularity for hires.** `Person.start_month`/`end_month` are whole-month
   integers; there is no day field. A new hire "starting mid-month" is charged the full monthly
   loaded rate for that month, or none at all — there is no proration. TC-02's mid-month-start
   sub-case tests this (the *absence* of proration), not a proration formula.
2. **No per-item start delay for revenue.** Cost sections (`formation_legal`, `ga_ops`, `rnd`,
   `sales_marketing`) each have `start_month`/`end_month` per item, but `revenue` is one global
   block with no equivalent — logo accrual begins month 1 unconditionally. A venture with a
   pre-revenue ramp (e.g., UCM's likely sales-cycle lag) can only approximate a delay via a low
   or negative `new_logo_growth_monthly_pct`, which distorts the whole curve rather than cleanly
   zeroing early months. Worth raising with Codex/Claude before the UCM model is assembled.
