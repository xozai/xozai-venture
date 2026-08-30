# Strata — 3-year financial model (v1, 2026-08-30)

Venture: Strata Civic Solutions. Brief: `product/FINANCIAL_BRIEF_STRATA.md`. Space:
`research/spaces/GOVTECH_MUNICIPAL.md`. Assumptions: `assumptions.{base,upside,downside}.json`
(every number carries source, date, confidence). Engine: `product/finance/engine/` (Codex,
deterministic; cash and personnel reconcile every period). Engine output: `output/`.
Prepared by Claude; not yet accepted by joseleos.

> Estimates for planning; not legal, tax, or investment advice. Review with an accountant
> before external use.

## Memo

**What it costs.** Bootstrapped and founder-only, Strata's cash cost is small: roughly
**$37k of opex in year 1** (formation and Texas qualification ≈ $5k, insurance/accounting/
software ≈ $12k, hosting and tooling ≈ $8k, TML booth and regional events ≈ $12k) against
≈ $27k of year-1 revenue in the base case. The real cost is the founder's deferred
compensation — **≈ $184k/yr memo, $0 cash** — which no scenario pays within the horizon.

**When it pays back.** Base case: operating income is positive every month from **month 19
(Apr 2028)** onward; year 3 is +$51k on $248k revenue with ≈ 31 paying cities and a run-rate
exiting month 36 of ≈ $325k ARR (Q12 revenue × 4). Upside (0.5 cities/mo compounding 7%, Core-heavy mix at
$11k): ≈ 71 cities, $651k year-3 revenue, +$301k year-3 operating income, and enough cash to
have hired an engineer (m16) and a CS/sales person (m25). Downside (0.2 cities/mo, $7.2k ACV,
1.2%/mo churn): ≈ 11 cities and $64k year-3 revenue — a lifestyle-scale business whose operating
income is positive from year 3 (first positive month: 15) only because it never hires.

**Capital needed.** With **$10k opening cash** (joseleos: "assume under $10,000", modeled at
the ceiling), cash goes negative in **month 2** — the TML booth, Texas qualification and
pilot-agreement counsel land before any revenue — and the base case bottoms at **−$29k in
month 18** (year-2 renewals plus the contractor start), ending month 36 at +$32k. So the
cash the founder must cover beyond the $10k is **≈ $29k (base), ≈ $33k (upside — the early
contractor), ≈ $32k (downside, which also ends month 36 at −$4k)**; about **$40k total from
launch** in every scenario. No round is needed; the gap is founder-funded or closed by the
levers below (slipping the contractor three months cuts the base need to ≈ $11k; +10% price
or win rate to ≈ $23k). Annual-upfront invoicing (not yet in the engine) would cover most of it.

**Engine conservatism worth knowing.** v1 recognizes revenue ratably and does not model
annual-upfront invoices, the $500–1,500 onboarding fee, or the free 90-day pilot window. Upfront
annual billing on 5–6 cities in year 1 would add ≈ $20–40k of early cash and likely erase the
month-14 trough; the pilot window pushes first cash out by ~3 months. Net effect is favorable
but unquantified until the engine grows a billing-terms cash line (ask for Codex).

**The five assumptions that move the answer most** (all confidence L unless noted):
1. **Opening cash** — $10k (joseleos, upper bound); every dollar moves the trough one-for-one.
2. **Paying-city acquisition rate** — 0.35/mo compounding 5%/mo in base (≈ 5–6 paid cities in
   year 1, matching the GTM's 5 pilots → 1 paid by day 90 with pilots converting in months 4–9).
   +10% on this rate cuts capital need by ~45%.
3. **ACV / tier mix** — $9,600 Core (confidence M, from the GTM pricing table). +10% price has
   the same effect as +10% win rate.
4. **Hire timing** — a 0.5-FTE contractor at m13 and an FTE engineer at m28 (base). Delaying
   three months takes capital need to $0; hiring the FTE at m16 (first draft) sank the base
   case to −$101k. Hiring is the only lever that can break a bootstrapped plan.
5. **COGS per city** — $75/mo base (inference + retrieval + re-ingestion). Gross margin
   stays 79–91% across scenarios, so this only matters if real usage is ≥ 3× the assumption.
   Churn (0.6%/mo) barely moves 3-year cash but dominates LTV.

**Assumptions to validate** (source = "assumption", confidence L): TML exhibitor fee
($3k assumed — TML has not quoted); insurance package ($3.6k/yr); pilot-agreement counsel
($2.5k); public-sector logo retention (90–95%/yr, vendor-reported); per-city COGS; contractor
and FTE rates. Researcher's `research/FINANCIAL_BENCHMARKS.md` and HermesX/Scribe's
`marketing/GTM_COST_MODEL.md` should replace these when delivered.

**Answers from joseleos (2026-08-30 15:23, event `7a9ad457`)** — applied as `override`
values, never edited in place:
1. Opening cash: under $10,000 → modeled at $10,000.
2. Xozai defaults kept: 3-year horizon, founder pay deferred, bootstrapped.
3. Entity: Delaware Public Benefit Corporation (confirmed 15:28), foreign-qualified in Texas; taxed as a C-Corp.
4. Schertz has not committed to paying → starting paying cities = 0 (unchanged).
5. No cash floor.

## Scenario summary (engine metrics)

| Metric | Base | Upside | Downside |
|---|---:|---:|---:|
| 3-year revenue | $378,843 | $922,560 | $107,511 |
| Ending cash (m36) | $31,600 | $309,645 | $-4,472 |
| Capital need to break-even (min cash below 0) | $29,069 | $32,738 | $31,557 |
| Cash-out month | 2 | 2 | 2 |
| First month with operating income ≥ 0 | 7 | 4 | 15 |
| Gross margin | 89.0% | 91.0% | 79.0% |
| ACV | $9,600 | $11,000 | $7,200 |
| CAC (S&M ÷ new logos) | $1,225 | $592 | $3,009 |
| CAC payback (months) | 1.7 | 0.7 | 6.3 |
| NRR | 98.0% | 103.0% | 88.0% |
| LTV:CAC | 96 | 354 | 13 |

## Base — annual

| Year | Paying cities (end) | Revenue | COGS | Gross profit | Personnel (cash) | Founder comp deferred (memo) | Formation/legal | G&A | R&D | S&M | Operating income | Ending cash | Headcount (end) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Y1 | 5.4 | $26,660 | $3,224 | $23,436 | $0 | $184,000 | $6,000 | $10,640 | $8,200 | $11,700 | $-13,104 | $-3,104 | 1.0 |
| Y2 | 14.8 | $103,894 | $12,153 | $91,742 | $72,000 | $181,500 | $600 | $10,640 | $10,200 | $14,700 | $-16,398 | $-19,502 | 2.0 |
| Y3 | 31.2 | $248,290 | $28,032 | $220,258 | $138,475 | $181,500 | $600 | $11,180 | $4,200 | $14,700 | $51,103 | $31,600 | 2.0 |

### Base — quarterly, months 25–36

| Quarter | Paying cities (end) | Revenue | Gross profit | Personnel | Opex total | Operating income | Ending cash |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q9 (m25–27) | 18.0 | $44,897 | $39,748 | $18,000 | $31,110 | $8,638 | $-10,864 |
| Q10 (m28–30) | 21.8 | $55,134 | $48,868 | $41,825 | $47,315 | $1,553 | $-9,311 |
| Q11 (m31–33) | 26.1 | $67,116 | $59,557 | $39,325 | $44,365 | $15,192 | $5,881 |
| Q12 (m34–36) | 31.2 | $81,142 | $72,084 | $39,325 | $46,365 | $25,719 | $31,600 |

### Base — monthly, months 1–24

| Month | New cities | Paying cities | Revenue | COGS | Opex | Operating income | Ending cash | Runway (mo) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 (2026-10) | 0.35 | 0.3 | $280 | $35 | $9,170 | $-8,925 | $1,075 | 0.1 |
| 2 (2026-11) | 0.37 | 0.7 | $575 | $71 | $9,870 | $-9,366 | $-8,291 | 0.0 |
| 3 (2026-12) | 0.39 | 1.1 | $885 | $109 | $1,370 | $-594 | $-8,885 | 0.0 |
| 4 (2027-01) | 0.41 | 1.5 | $1,211 | $148 | $1,370 | $-307 | $-9,192 | 0.0 |
| 5 (2027-02) | 0.43 | 1.9 | $1,555 | $190 | $1,370 | $-5 | $-9,198 | 0.0 |
| 6 (2027-03) | 0.45 | 2.4 | $1,916 | $234 | $3,170 | $-1,487 | $-10,685 | 0.0 |
| 7 (2027-04) | 0.47 | 2.8 | $2,297 | $279 | $1,370 | $648 | $-10,037 | — |
| 8 (2027-05) | 0.49 | 3.3 | $2,698 | $327 | $1,370 | $1,001 | $-9,036 | — |
| 9 (2027-06) | 0.52 | 3.8 | $3,120 | $377 | $1,370 | $1,373 | $-7,662 | — |
| 10 (2027-07) | 0.54 | 4.3 | $3,565 | $429 | $1,370 | $1,765 | $-5,897 | — |
| 11 (2027-08) | 0.57 | 4.8 | $4,033 | $484 | $1,370 | $2,179 | $-3,718 | — |
| 12 (2027-09) | 0.60 | 5.4 | $4,526 | $541 | $3,370 | $614 | $-3,104 | — |
| 13 (2027-10) | 0.63 | 6.0 | $5,045 | $602 | $11,370 | $-6,927 | $-10,031 | 0.0 |
| 14 (2027-11) | 0.66 | 6.6 | $5,592 | $665 | $18,120 | $-13,193 | $-23,224 | 0.0 |
| 15 (2027-12) | 0.69 | 7.3 | $6,167 | $731 | $7,620 | $-2,184 | $-25,408 | 0.0 |
| 16 (2028-01) | 0.73 | 8.0 | $6,774 | $801 | $7,620 | $-1,647 | $-27,055 | 0.0 |
| 17 (2028-02) | 0.76 | 8.7 | $7,413 | $874 | $7,620 | $-1,080 | $-28,135 | 0.0 |
| 18 (2028-03) | 0.80 | 9.4 | $8,086 | $950 | $8,070 | $-934 | $-29,069 | 0.0 |
| 19 (2028-04) | 0.84 | 10.2 | $8,796 | $1,030 | $7,620 | $145 | $-28,923 | — |
| 20 (2028-05) | 0.88 | 11.0 | $9,543 | $1,114 | $7,620 | $809 | $-28,115 | — |
| 21 (2028-06) | 0.93 | 11.9 | $10,330 | $1,203 | $7,620 | $1,507 | $-26,607 | — |
| 22 (2028-07) | 0.98 | 12.8 | $11,160 | $1,295 | $7,620 | $2,244 | $-24,363 | — |
| 23 (2028-08) | 1.02 | 13.8 | $12,034 | $1,393 | $7,620 | $3,021 | $-21,342 | — |
| 24 (2028-09) | 1.08 | 14.8 | $12,954 | $1,495 | $9,620 | $1,840 | $-19,502 | — |

### Base — one-variable sensitivities (engine)

| Variable | Change | 3-year revenue | Ending cash | Capital need |
|---|---:|---:|---:|---:|
| price | +10% | $416,728 | $68,348 | $22,692 |
| win_rate | +10% | $416,728 | $65,144 | $23,280 |
| churn | +10% | $376,703 | $29,704 | $29,247 |
| hiring_pace | +3 months | $378,843 | $88,925 | $11,224 |

## Upside — annual

| Year | Paying cities (end) | Revenue | COGS | Gross profit | Personnel (cash) | Founder comp deferred (memo) | Formation/legal | G&A | R&D | S&M | Operating income | Ending cash | Headcount (end) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Y1 | 8.8 | $48,451 | $4,473 | $43,978 | $36,000 | $184,000 | $6,000 | $10,640 | $8,200 | $11,700 | $-28,562 | $-18,562 | 2.0 |
| Y2 | 28.1 | $223,104 | $19,652 | $203,452 | $138,475 | $181,500 | $600 | $11,180 | $10,200 | $16,200 | $26,797 | $8,235 | 2.0 |
| Y3 | 71.3 | $651,005 | $54,585 | $596,421 | $262,650 | $181,500 | $600 | $11,360 | $4,200 | $16,200 | $301,411 | $309,645 | 3.0 |

### Upside — quarterly, months 25–36

| Quarter | Paying cities (end) | Revenue | Gross profit | Personnel | Opex total | Operating income | Ending cash |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q9 (m25–27) | 35.9 | $107,250 | $98,055 | $67,538 | $82,328 | $15,727 | $23,962 |
| Q10 (m28–30) | 45.4 | $138,687 | $126,943 | $65,038 | $70,528 | $56,416 | $80,378 |
| Q11 (m31–33) | 57.1 | $177,981 | $163,095 | $65,038 | $70,078 | $93,018 | $173,396 |
| Q12 (m34–36) | 71.3 | $227,087 | $208,327 | $65,038 | $72,078 | $136,249 | $309,645 |

### Upside — monthly, months 1–24

| Month | New cities | Paying cities | Revenue | COGS | Opex | Operating income | Ending cash | Runway (mo) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 (2026-10) | 0.50 | 0.5 | $458 | $44 | $9,170 | $-8,755 | $1,245 | 0.1 |
| 2 (2026-11) | 0.54 | 1.0 | $953 | $91 | $9,870 | $-9,008 | $-7,763 | 0.0 |
| 3 (2026-12) | 0.57 | 1.6 | $1,487 | $141 | $1,370 | $-24 | $-7,787 | 0.0 |
| 4 (2027-01) | 0.61 | 2.2 | $2,063 | $194 | $1,370 | $498 | $-7,288 | — |
| 5 (2027-02) | 0.66 | 2.9 | $2,684 | $252 | $1,370 | $1,062 | $-6,226 | — |
| 6 (2027-03) | 0.70 | 3.5 | $3,354 | $313 | $3,170 | $-129 | $-6,355 | 0.0 |
| 7 (2027-04) | 0.75 | 4.3 | $4,077 | $379 | $7,370 | $-3,672 | $-10,027 | 0.0 |
| 8 (2027-05) | 0.80 | 5.1 | $4,857 | $450 | $7,370 | $-2,963 | $-12,989 | 0.0 |
| 9 (2027-06) | 0.86 | 5.9 | $5,698 | $525 | $7,370 | $-2,198 | $-15,187 | 0.0 |
| 10 (2027-07) | 0.92 | 6.8 | $6,604 | $606 | $7,370 | $-1,372 | $-16,559 | 0.0 |
| 11 (2027-08) | 0.98 | 7.8 | $7,581 | $693 | $7,370 | $-482 | $-17,041 | 0.0 |
| 12 (2027-09) | 1.05 | 8.8 | $8,635 | $786 | $9,370 | $-1,521 | $-18,562 | 0.0 |
| 13 (2027-10) | 1.13 | 9.9 | $9,770 | $885 | $11,370 | $-2,485 | $-21,047 | 0.0 |
| 14 (2027-11) | 1.20 | 11.0 | $10,994 | $992 | $19,620 | $-9,617 | $-30,664 | 0.0 |
| 15 (2027-12) | 1.29 | 12.3 | $12,314 | $1,106 | $7,620 | $3,588 | $-27,077 | — |
| 16 (2028-01) | 1.38 | 13.6 | $13,736 | $1,229 | $17,288 | $-4,781 | $-31,858 | 0.0 |
| 17 (2028-02) | 1.48 | 15.0 | $15,268 | $1,360 | $14,788 | $-880 | $-32,738 | 0.0 |
| 18 (2028-03) | 1.58 | 16.6 | $16,919 | $1,501 | $15,238 | $180 | $-32,558 | — |
| 19 (2028-04) | 1.69 | 18.2 | $18,699 | $1,651 | $14,788 | $2,259 | $-30,299 | — |
| 20 (2028-05) | 1.81 | 19.9 | $20,616 | $1,813 | $14,788 | $4,015 | $-26,284 | — |
| 21 (2028-06) | 1.93 | 21.8 | $22,682 | $1,986 | $14,788 | $5,907 | $-20,377 | — |
| 22 (2028-07) | 2.07 | 23.8 | $24,908 | $2,172 | $14,788 | $7,948 | $-12,429 | — |
| 23 (2028-08) | 2.22 | 25.9 | $27,306 | $2,371 | $14,788 | $10,147 | $-2,282 | — |
| 24 (2028-09) | 2.37 | 28.1 | $29,890 | $2,585 | $16,788 | $10,517 | $8,235 | — |

### Upside — one-variable sensitivities (engine)

| Variable | Change | 3-year revenue | Ending cash | Capital need |
|---|---:|---:|---:|---:|
| price | +10% | $1,014,816 | $399,134 | $23,950 |
| win_rate | +10% | $1,014,816 | $394,031 | $24,378 |
| churn | +10% | $919,328 | $306,687 | $32,928 |
| hiring_pace | +3 months | $922,560 | $392,683 | $12,664 |

## Downside — annual

| Year | Paying cities (end) | Revenue | COGS | Gross profit | Personnel (cash) | Founder comp deferred (memo) | Formation/legal | G&A | R&D | S&M | Operating income | Ending cash | Headcount (end) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Y1 | 2.7 | $10,163 | $2,145 | $8,018 | $0 | $184,000 | $6,000 | $10,640 | $8,200 | $11,700 | $-28,522 | $-18,522 | 1.0 |
| Y2 | 6.1 | $33,083 | $6,878 | $26,206 | $0 | $181,500 | $600 | $10,640 | $10,200 | $13,200 | $-8,434 | $-26,956 | 1.0 |
| Y3 | 10.7 | $64,264 | $13,140 | $51,124 | $0 | $181,500 | $600 | $10,640 | $4,200 | $13,200 | $22,484 | $-4,472 | 1.0 |

### Downside — quarterly, months 25–36

| Quarter | Paying cities (end) | Revenue | Gross profit | Personnel | Opex total | Operating income | Ending cash |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q9 (m25–27) | 7.1 | $12,744 | $10,120 | $0 | $11,610 | $-1,490 | $-28,447 |
| Q10 (m28–30) | 8.2 | $14,836 | $11,794 | $0 | $5,310 | $6,484 | $-21,963 |
| Q11 (m31–33) | 9.4 | $17,108 | $13,614 | $0 | $4,860 | $8,754 | $-13,209 |
| Q12 (m34–36) | 10.7 | $19,577 | $15,597 | $0 | $6,860 | $8,737 | $-4,472 |

### Downside — monthly, months 1–24

| Month | New cities | Paying cities | Revenue | COGS | Opex | Operating income | Ending cash | Runway (mo) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 (2026-10) | 0.20 | 0.2 | $120 | $26 | $9,170 | $-9,076 | $924 | 0.1 |
| 2 (2026-11) | 0.21 | 0.4 | $243 | $52 | $9,870 | $-9,679 | $-8,755 | 0.0 |
| 3 (2026-12) | 0.21 | 0.6 | $368 | $78 | $1,370 | $-1,080 | $-9,835 | 0.0 |
| 4 (2027-01) | 0.22 | 0.8 | $496 | $105 | $1,370 | $-980 | $-10,815 | 0.0 |
| 5 (2027-02) | 0.23 | 1.0 | $627 | $133 | $1,370 | $-876 | $-11,691 | 0.0 |
| 6 (2027-03) | 0.23 | 1.3 | $760 | $161 | $3,170 | $-2,571 | $-14,262 | 0.0 |
| 7 (2027-04) | 0.24 | 1.5 | $897 | $190 | $1,370 | $-663 | $-14,924 | 0.0 |
| 8 (2027-05) | 0.25 | 1.7 | $1,037 | $219 | $1,370 | $-552 | $-15,476 | 0.0 |
| 9 (2027-06) | 0.25 | 1.9 | $1,180 | $249 | $1,370 | $-439 | $-15,915 | 0.0 |
| 10 (2027-07) | 0.26 | 2.2 | $1,327 | $280 | $1,370 | $-322 | $-16,237 | 0.0 |
| 11 (2027-08) | 0.27 | 2.4 | $1,477 | $311 | $1,370 | $-203 | $-16,441 | 0.0 |
| 12 (2027-09) | 0.28 | 2.7 | $1,631 | $343 | $3,370 | $-2,081 | $-18,522 | 0.0 |
| 13 (2027-10) | 0.29 | 2.9 | $1,789 | $375 | $5,370 | $-3,956 | $-22,479 | 0.0 |
| 14 (2027-11) | 0.29 | 3.2 | $1,950 | $408 | $10,620 | $-9,078 | $-31,557 | 0.0 |
| 15 (2027-12) | 0.30 | 3.5 | $2,116 | $442 | $1,620 | $53 | $-31,504 | — |
| 16 (2028-01) | 0.31 | 3.7 | $2,285 | $477 | $1,620 | $188 | $-31,316 | — |
| 17 (2028-02) | 0.32 | 4.0 | $2,459 | $513 | $1,620 | $327 | $-30,989 | — |
| 18 (2028-03) | 0.33 | 4.3 | $2,638 | $549 | $2,070 | $19 | $-30,970 | — |
| 19 (2028-04) | 0.34 | 4.6 | $2,821 | $587 | $1,620 | $614 | $-30,356 | — |
| 20 (2028-05) | 0.35 | 4.9 | $3,009 | $625 | $1,620 | $764 | $-29,592 | — |
| 21 (2028-06) | 0.36 | 5.2 | $3,202 | $664 | $1,620 | $918 | $-28,674 | — |
| 22 (2028-07) | 0.37 | 5.5 | $3,400 | $704 | $1,620 | $1,076 | $-27,598 | — |
| 23 (2028-08) | 0.38 | 5.8 | $3,603 | $745 | $1,620 | $1,238 | $-26,361 | — |
| 24 (2028-09) | 0.39 | 6.1 | $3,811 | $787 | $3,620 | $-596 | $-26,956 | 0.0 |

### Downside — one-variable sensitivities (engine)

| Variable | Change | 3-year revenue | Ending cash | Capital need |
|---|---:|---:|---:|---:|
| price | +10% | $118,262 | $5,957 | $30,208 |
| win_rate | +10% | $118,262 | $4,063 | $30,460 |
| churn | +10% | $106,248 | $-5,475 | $31,610 |
| hiring_pace | +3 months | $107,511 | $-4,472 | $31,557 |

> Estimates for planning; not legal, tax, or investment advice. Review with an accountant before external use.
