# UCM — 3-year financial model (v1)

Venture: Utility Conflict Matrix automation (CIVIL lead). Horizon: 36 months from 2026-10, monthly m1–24 then
quarterly. US Delaware C-Corp. Produced by `financial-model` skill at `xozai/xozai-venture` commit `81533e8`
(engine #16, assumptions #14) on 2026-08-30; upside re-run same day after §B2 was repriced from published
UESI booth fees (#21). Workbook: `output/model.xlsx` (formula-driven; Checks tab all TRUE).
Engine JSON in `output/*.model.json` is the source of truth; every figure below is copied from it.

**Estimates for planning; not legal, tax, or investment advice.** Review with an accountant before external use.

## Memo

**What it costs.** Running cost is ≈ $293k in year 1, $310k in year 2, $330k in year 3 (base). Personnel is
88% of that — two salaried engineers (senior geospatial from m1, second from m3, $110k/$100k base × 1.30
loaded, per Codex's build plan) at $256–273k/yr. Everything else is small: G&A/ops ≈ $15.6k/yr, formation +
legal ≈ $7.3k in year 1 then $5.4k, R&D infra $9.5k → $31.8k as usage grows, and sales & marketing only
$3.8k–4.6k/yr because the base GTM is association dues plus one conference (Scribe/Researcher: the UCM search
cluster is too thin for paid media). Founder comp of $150k/yr is deferred until funding and shown as a memo
line, never as cash.

**When it pays back.** First revenue in m8 (after the ~7-month build to M3). Base reaches 112 paying firms and
$489k revenue in year 3, with operating income turning positive in **m27**. Upside (3 seats/firm at $250,
3 logos/mo, 5%/mo growth): break-even **m19**, $1.24M year-3 revenue, ending cash +$598k. Downside (1 seat at
$200, 1 logo/mo, 3% growth, 15%/yr churn): **never breaks even** in the horizon; cumulative loss ≈ $740k.

**Capital needed.** With the assumed $50k opening cash, cash goes negative in **m3** in every scenario.
Additional cash required to stay above zero: **$383k base**, $280k upside, $740k downside. This is the
headline: *under joseleos's "bootstrapped, no round" parameter, the two-engineer build plan is not
self-funding.* Two levers close the gap and both are decisions, not modelling: (a) build with founder time
and/or contractors instead of two salaried engineers until first revenue — the model's hiring-pace
sensitivity shows delaying hires 3 months alone cuts the need by $68k; (b) raise the difference (a
~$400k SAFE) — which also un-defers founder comp, so the true need would be higher. Recommend joseleos
pick one before Skill 2 Stage A commits to the team shape.

**The five assumptions that move the answer most** (all confidence L or M; see Sources tab):
1. Salaried engineer count and start months (`personnel.roster`) — drives ~88% of spend.
2. New logos per month after m8 (2 base) — no win-rate benchmark exists for low-touch individual-buyer SaaS;
   this is the pain-quote gap from discovery, unresolved until the 5–10 engineer interviews.
3. Seats per firm × price per seat (2 × $225 base, anchored on Civil 3D at $239/seat/mo).
4. Annual churn (12% base, SMB band) — NRR is 93% base; retention, not price, is the revenue-quality risk.
5. Opening cash ($50k) — an assumption; joseleos to confirm.

**Caveats.** CAC, payback, and LTV:CAC are reported by the engine but are not meaningful here: S&M cash is
near zero (organic), so CAC ≈ $104 and LTV:CAC ≈ 400× are artefacts of the organic assumption, not evidence
of efficiency. Section B of the GTM cost model is priced from published UESI sources (rev #21); the two items
still awaiting HermesX sign-off are the exhibit-at-all decision and B4 purchasability — neither touches the
base case. The upside carries both B2 (booth, m14/m26) and B3 (attendance) even though the booth includes one
registration, i.e. it assumes a second person attends in exhibit years; resolving that overlap is HermesX's
call and would only lower the upside. Gross margin of 93–94% reflects only LLM/hosting COGS; support
labour is not yet a COGS line.

## Scenario summary

| | Base | Upside | Downside |
|---|---:|---:|---:|
| Seats × price/seat/mo | 2 × $225 | 3 × $250 | 1 × $200 |
| ACV per firm | $5,400 | $9,000 | $2,400 |
| New logos/mo from m8; growth/mo | 2; 5% | 3; 5% | 1; 3% |
| Churn (annual) | 12% | 10% | 15% |
| Engineer 2 start | m3 | m3 | m5 |
| 36-mo revenue | $676,126 | $1,716,936 | $116,971 |
| Break-even month | 27 | 19 | none |
| Cash-out month (from $50k) | 3 | 3 | 4 |
| Additional capital need | $382,826 | $278,523 | $740,217 |
| Ending cash (m36) | −$250,147 | $601,083 | −$740,217 |
| Paying firms at m36 | 112 | 172 | 39 |

## Base case — annual

| | Y1 | Y2 | Y3 |
|---|---:|---:|---:|
| Revenue | 14,822 | 172,179 | 489,125 |
| COGS | 973 | 11,141 | 31,095 |
| Personnel (cash) | 256,333 | 273,000 | 273,000 |
| Founder deferred comp (memo) | 150,000 | 150,000 | 150,000 |
| Formation & legal | 7,300 | 5,400 | 5,400 |
| G&A / ops | 15,644 | 15,644 | 15,644 |
| R&D infra & tooling | 9,500 | 11,400 | 31,800 |
| Sales & marketing | 3,833 | 4,583 | 4,583 |
| Total opex (cash) | 292,610 | 310,027 | 330,427 |
| Operating income | −278,761 | −148,989 | 127,603 |
| Ending cash | −228,761 | −377,750 | −250,147 |
| Paying firms (end) | 10.8 | 48.3 | 112.3 |
| Headcount (end, excl. founder) | 2 | 2 | 2 |

Year-3 quarters (base): Q9 rev $84,841 / op. inc. −$3,092 · Q10 $107,223 / +$20,406 · Q11 $133,313 /
+$39,870 · Q12 $163,749 / +$70,420. Trough cash −$380,842 at Q9.

## Sensitivities (base, one variable at a time)

| Variable | Change | 36-mo revenue | Capital need |
|---|---|---:|---:|
| Price | +10% | $743,739 | $362,150 |
| Win rate (logos/mo) | +10% | $743,739 | $362,676 |
| Churn | +10% | $670,898 | $384,028 |
| Hiring pace | +3 months | $676,126 | $314,576 |

Monthly detail (m1–24), quarterly (Q9–Q12), headcount, opex by function, statements, cash, metrics, checks
and full sources are in `output/model.xlsx` and `output/assumptions.<scenario>.model.md`.

## Sources and overrides
All inputs: `assumptions.{base,upside,downside}.json` (generated by `build_assumptions.py`), each leaf with
source/date/confidence/kind. Overrides applied: **none** (engine `overrides: []` in all scenarios). Benchmarks:
`research/FINANCIAL_BENCHMARKS.md` (#11, #13); GTM: `marketing/GTM_COST_MODEL.md` (#12, #15, #21); build:
`BUILD_ESTIMATE.md` (Codex); parameters: `docs/DECISIONS.md` (joseleos 2026-08-30).
