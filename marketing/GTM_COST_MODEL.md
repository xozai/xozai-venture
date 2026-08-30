# GTM cost model — UCM (Utility Conflict Matrix automation)

Feeds `financial-model` → `sales_marketing.items[]` (and, where noted, `personnel.roster[]`).
Venture brief: `product/FINANCIAL_BRIEF_UCM.md`. Horizon: 36 months from 2026-09 (m1 = Sep 2026).

| Section | Owner | Status |
|---|---|---|
| A. Content, brand, SEO, tooling | Scribe | **complete** (this PR) |
| B. Sales, channel, events, pilots | HermesX | **straw man only** — see §B; HermesX to confirm or replace |
| C. GTM personnel | Scribe (structure) + HermesX (ramp) | structure complete; upside hire timing needs HermesX |

Every line below carries `source` + `date` + `confidence` per the schema convention. `source: assumption`
means nobody has a citation yet — it is a placeholder, not a finding. Prices verified 2026-08-30.

---

## 0. Schema mapping (read before pasting)

The merged schema (`product/finance/tests/fixtures/*/assumptions.*.json`, main @ 82232bc) shapes a
sales & marketing line as:

```json
{ "name": {...}, "amount": {...}, "cadence": {...}, "start_month": {...}, "end_month": {...} }
```

with `cadence ∈ {one_time, monthly, annual}` and the fixture convention `end_month: 0` meaning
"runs to the end of the horizon". Note this differs from the brief in thread `3c541c66…` 15:18,
which described the basis as "per-head / per-month / one-time" — **there is no per-head basis in the
merged schema.** Three consequences, all flagged to Codex in §E:

1. Spend that scales with logos or headcount (CAC-driven media, per-rep tooling) cannot be expressed.
2. Sales compensation has no variable component — `personnel.roster[]` has `annual_base` only.
3. Costs that step up mid-horizon must be modelled as two items (one ending, one starting), not one
   item with a schedule. All step-ups below are written that way.

---

## 1. The GTM posture, in one paragraph per scenario

**Base — near-zero cash, founder-led, association-access-first.** UCM's buyer is an individual PE or
small-firm principal who buys on a card. There is no procurement to fund, no enterprise sales motion
to staff, and — the binding constraint — no keyword volume to buy. The searchable demand for "utility
conflict matrix" is a few hundred queries a month against a practitioner population that finds tools
through PDH credit, state DOT utility-coordination training, and UESI/APWA peers. **GTM cost in the
base case is therefore dominated by association access and founder time, not media.** Total base
GTM cash across 36 months is roughly $13k — of which $7.5k is annual conference attendance and
$5.5k is the entire content, brand and tooling program. Against the build cost in
`product/finance/ucm/BUILD_ESTIMATE.md` that is a rounding error. That is the finding, not an omission.

**Upside — buy reach where reach exists.** The upside does not turn on more ad budget; it turns on
(a) contract content production to convert PDH/tutorial intent faster, (b) one exhibit presence per
year at UESI Pipelines or APWA PWX, and (c) a founding technical AE from m20. Paid search is included
at a deliberately small number because the inventory ceiling, not the budget, is the limit — doubling
it would buy nothing.

**Downside — memberships and nothing else.** If revenue is late, everything except ASCE/UESI dues is
cancellable within one billing cycle. Downside GTM cash across 36 months is ~$960. This is the
point of an organic-first plan: the GTM line is not what runs the company out of cash — personnel is.

---

## A. Content, brand, SEO, tooling — Scribe (owned)

### A.1 Base case

| # | Line item | Amount | Cadence | Start m | End m | Source | Conf |
|---|---|---|---|---|---|---|---|
| A1 | Domain + DNS (registrar at cost) | $12 | annual | 1 | 0 | assumption (Cloudflare Registrar at-cost model) | M |
| A2 | Marketing site hosting | $0 | monthly | 1 | 0 | rides the product's Vercel Pro seat — see note | H |
| A3 | Email / newsletter (Kit free tier) | $0 | monthly | 1 | 0 | kit.com/pricing — free to 10,000 subscribers | H |
| A4 | ASCE professional dues + UESI institute add-on | $307 | annual | 1 | 0 | asce.org/membership/join ($277) + institute add-on ($30, secondary) | M |
| A5 | SEO tooling — Ahrefs Starter | $29 | monthly | 4 | 0 | ahrefs.com/pricing | H |
| A6 | Design — Canva Pro (1 seat) | $15 | monthly | 4 | 0 | assumption (vendor list price, not re-verified) | M |
| A7 | Webinar platform — Zoom Webinars 500 (PDH delivery) | $79 | monthly | 7 | 0 | zoom.us/pricing/events, $79/mo Webinar 500 | M |
| A8 | Tutorial video production tooling (Descript or equiv.) | $24 | monthly | 7 | 0 | assumption (vendor list price, not re-verified) | M |

**Base steady state: $147/mo from m7, plus $319/yr in annual lines.** 36-month §A total ≈ **$5,500**
($1,333 in year 1 as lines phase in, $2,083 in each of years 2 and 3).

Note on A2: the marketing site is a route in the same Next.js app the product ships on, so its
hosting is already inside the R&D/infra line in `BUILD_ESTIMATE.md`. Listing it at $0 here is
deliberate anti-double-counting, not an oversight. If the site is later split onto its own project,
add $20/mo (vercel.com/pricing, Pro).

Note on A4: dues are the single line I would not cut. UESI institute membership is the entry
condition for speaking slots and the PDH-credit webinar track, which is the base case's only
distribution. $307/yr buying the sole channel is the highest-leverage dollar in this model.

### A.2 Upside — deltas from base (add to A.1, with the base line ended where noted)

| # | Line item | Amount | Cadence | Start m | End m | Source | Conf |
|---|---|---|---|---|---|---|---|
| A5-U | SEO tooling — Ahrefs Lite (replaces A5 from m10) | $129 | monthly | 10 | 0 | ahrefs.com/pricing | H |
| A9 | Contract technical writer — 4 practitioner articles/mo | $2,000 | monthly | 8 | 0 | assumption ($500/article, 1,500-word technical) | L |
| A10 | Contract video editor — tutorial SEO track | $1,500 | monthly | 10 | 0 | assumption | L |
| A11 | Paid search, high-intent terms only | $1,200 | monthly | 12 | 0 | assumption — **volume-capped, see below** | L |
| A12 | Launch collateral + brand refresh (one-time) | $6,000 | one_time | 9 | 9 | assumption (contract designer, 2–3 wks) | L |

If A5-U is used, A5 must be re-emitted with `end_month: 9` rather than `0`.

**On A11.** I have set paid search at $1,200/mo and I do not recommend raising it. The exact-match
terms a UCM buyer types ("utility conflict matrix template", "SUE conflict matrix", "SHRP2 UCM
spreadsheet") are low-hundreds-of-searches-per-month terms. Above roughly this spend the money goes
into broad match against general civil-engineering-software intent, where the click is not our buyer
and CAC degrades sharply. **The upside lever in this market is content volume and association
presence, not media budget.** If HermesX or Researcher can produce actual keyword volumes, this line
should be re-derived from them rather than guessed — it is currently my least defensible number.

### A.3 Downside — deltas from base

| # | Line item | Amount | Cadence | Start m | End m | Source | Conf |
|---|---|---|---|---|---|---|---|
| A1 | Domain + DNS | $12 | annual | 1 | 0 | as base | M |
| A4 | ASCE dues + UESI add-on | $307 | annual | 1 | 0 | as base | M |
| — | A2, A3 | $0 | — | — | — | free tiers, unchanged | H |
| — | A5, A6, A7, A8 | **dropped** | — | — | — | Ahrefs → free tier; Canva free; webinars move to a free meeting product with YouTube replay; screen capture unedited | H |

**Downside total: $319/yr, ≈ $960 across 36 months.** All four dropped lines are month-to-month and cancel
within one billing cycle; none carries a contract or a migration cost. That cancellability is the
reason to prefer this tool stack over annual-commit alternatives at the same headline price.

---

## B. Sales, channel, events, pilots — HermesX (straw man only)

**This section is a Scribe-drafted straw man so the schema has something to bind to and §D can total.
HermesX owns it. Do not merge these numbers into a model presented to joseleos without his sign-off.**

| # | Line item | Base | Upside | Downside | Cadence | Start m | Source | Conf |
|---|---|---|---|---|---|---|---|---|
| B1 | CRM + outbound tooling (1 seat) | $0 | $99/mo | $0 | monthly | 12 | assumption; base uses a spreadsheet at this volume | L |
| B2 | UESI Pipelines or APWA PWX exhibit — booth + travel | $0 | $8,000 | $0 | one_time | 14, 26 | **quote required** — ASCE exhibits, Sean Scully, 703-295-6154 | L |
| B3 | Conference attendance (no booth) — 1 event/yr, registration + travel | $2,500 | $2,500 | $0 | one_time | 12, 24, 36 | assumption | L |
| B4 | State DOT utility-coordination training sponsorship | $0 | $3,000 | $0 | one_time | 18 | assumption — **is this even purchasable?** | L |
| B5 | Design-partner / pilot incentives (credits, not cash) | $0 | $0 | $0 | — | — | credits reduce revenue, not S&M — see §E.4 | M |

Two things HermesX should resolve rather than accept:

- **B2 is unpriced.** Published exhibitor prospectuses for UESI Pipelines 2026 (Detroit, Aug 1–5) and
  APWA PWX 2026 are not public; the only figures I could find were third-party aggregator estimates
  of $15k–$40k *all-in cost to attend*, which is a different quantity from booth price and is not
  citable. $8,000 is my placeholder for a small booth plus one person's travel. Someone should call
  the number above and replace it with a real quote before this reaches a memo.
- **B3 appears in the base case** and is the only base-case line I have put in HermesX's section
  rather than mine. A founder attending one UESI event a year is not optional if PDH-track speaking
  is the distribution plan; but whether it belongs in S&M or in founder T&E under `ga_ops` is his call.

---

## C. GTM personnel — goes to `personnel.roster[]`, NOT `sales_marketing`

**Base: no GTM hire in the 36-month horizon.** The founder allocates roughly 30% of time to GTM.
That cost is already carried by the deferred-founder-comp row in `personnel.roster[]` per the brief.
It must **not** be added again as an S&M line. This is the most common way a bootstrapped model
double-counts, and it would inflate base GTM cash by six figures.

**Upside: one founding technical AE from m20**, sized against the brief's ~$2–6k/firm/year ACV:

| Field | Value | Source | Conf |
|---|---|---|---|
| role | Founding AE (technical) | — | — |
| headcount | 1 | — | — |
| start_month | 20 | assumption — after gross-margin cash covers loaded cost, per brief hiring rule | M |
| annual_base | $110,000 | assumption — needs Researcher's comparables | L |
| variable / OTE | $50,000 at plan (**not expressible — see §E.2**) | — | — |
| employer_tax_pct | 0.10 | matches fixture convention | M |
| benefits_pct | 0.10 | matches fixture convention | M |
| equipment | $2,000 | matches fixture convention | M |

**Downside: no GTM hire.** Same as base.

Loaded cost of the upside hire ≈ $132k/yr on base alone, or ≈ $192k/yr at OTE. For scale: that
single hire costs more per year than the entire upside content-and-media program above. Whatever
the model says about GTM, the number that moves it is this row — not the ad budget.

---

## D. Totals (Scribe's §A + §B straw man; excludes §C personnel)

| | Base | Upside | Downside |
|---|---|---|---|
| Year 1 (m1–12) | ~$3,800 | ~$25,900 | ~$320 |
| Year 2 (m13–24) | ~$4,600 | ~$74,400 | ~$320 |
| Year 3 (m25–36) | ~$4,600 | ~$71,400 | ~$320 |
| **36-month total** | **~$13,000** | **~$171,700** | **~$960** |

Hand-derived from the tables above and rounded to the nearest $100; the engine's output is
authoritative once these line items are loaded. Base includes §B3 conference attendance ($2,500/yr
from m12), which is $7,500 of the $13,000 — the single largest base-case GTM cost, and the one line
in §A/§B that is travel rather than software. Downside drops it. The m20 AE's cash cost is in §C
only and is **not** in this table; adding it moves upside year 3 from ~$71k to ~$203k.

---

## E. Findings for Codex (schema) and open questions

1. **No per-head or per-unit basis in `sales_marketing.items[]`.** Only fixed `amount` × `cadence`.
   CAC-driven media and per-seat sales tooling cannot scale with the roster or the logo count. UCM's
   base case does not need it; a marketplace or PLG venture would. Suggest an optional
   `basis: fixed | per_head | pct_revenue` with a matching `rate`.
2. **`personnel.roster[]` has no variable compensation.** Modelling a quota-carrying AE forces a
   choice between understating cash (base only) and overstating it in a miss year (OTE as base).
   Suggest `variable_annual` + `attainment_pct`, defaulting to 0 so existing fixtures are unaffected.
3. **No mid-horizon step-up on a single item.** Every rate change here is written as two items
   (`end_month: n` + a new item at `n+1`). Workable, but it means the Assumptions tab in the xlsx will
   show near-duplicate rows; worth a comment column so a reader can tell a step-up from a mistake.
4. **Design-partner credits are not an S&M expense.** Free or discounted pilot months reduce
   recognised revenue; booking them as marketing spend would overstate both revenue and cost.
   `revenue` has no discount or ramp field today. Related to Honey0's `revenue.start_month` finding
   (PR #8) — both are "revenue does not begin at full rate in month 1" problems and probably want
   one fix, not two.

**Open questions I could not resolve:**

- **Booth pricing (B2).** Needs a phone call, not a search.
- **Keyword volume.** A11 is a guess. Researcher: actual monthly search volume for the UCM term
  cluster would let me derive paid spend instead of asserting it, and would also tell us how much of
  the tutorial-SEO thesis is real.
- **Is DOT training sponsorship purchasable (B4)?** State DOT utility-coordination training is often
  agency-run with no sponsorship inventory. If so the line is $0 in every scenario and the access
  path is speaking, not paying.
- **Association memberships beyond ASCE.** APWA individual dues are not in A4. If APWA is a real
  channel and not just a listed one, add it; if it is aspirational, say so and leave it out.

---

Estimates for planning; not legal, tax, or investment advice.

## Sources

- ASCE professional member dues, $277/yr (29+), verified 2026-08-30 — https://www.asce.org/membership/join
- Ahrefs plan pricing, Starter $29/mo, Lite $129/mo, verified 2026-08-30 — https://ahrefs.com/pricing
- Kit (ConvertKit) free plan to 10,000 subscribers, verified 2026-08-30 — https://kit.com/pricing
- Vercel Hobby $0 / Pro $20/mo, verified 2026-08-30 — https://vercel.com/pricing
- Zoom Webinars 500, $79/mo, 2026-08-30 — https://zoom.us/pricing/events
- UESI Pipelines 2026 (Detroit, Aug 1–5), exhibitor contact; prospectus pricing not public, 2026-08-30 — https://www.pipelinesconference.org/exhibitors
- APWA PWX exhibitor information; prospectus pricing not public, 2026-08-30 — https://www.apwa.org/events/pwx-conference/pwx-for-exhibitors/
- Schema shape and `end_month: 0` convention — `product/finance/tests/fixtures/saas-tiny/assumptions.base.json`, main @ 82232bc
