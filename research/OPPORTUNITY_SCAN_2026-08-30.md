---
title: "Xozai opportunity scan — discovery pass 1"
author: Researcher
created: 2026-08-30
status: marketability scored (Scribe) — Hermes to rank
---

# Xozai opportunity scan (discovery pass 1)

Scope: 6 disciplines (transportation, water/wastewater, structural, geotechnical,
land development/site, construction estimating). **Excludes OPCC/cost-estimate
exhibits and MUTCD traffic-control plans** — those belong to Jerry Project
(`docs/DECISIONS.md`, 2026-08-30).

Run against `research/PRE_SWEEP_BRIEF.md`: prioritized genuinely new candidates
over prior-art 3–9, captured the self-built-vs-named-tool sub-field, tagged
discipline before scoring.

**Known gap, stated up front, same one that bit OPCC:** for the two candidates
below the fold, I have workflow evidence (industry guides, job postings) but
**no verbatim unprompted complaint quotes yet**. Multiple targeted searches
(Eng-Tips, r/civilengineering, YouTube-comment-style queries) for both did not
surface indexed complaint threads — a tooling limitation of web search against
Reddit/forum content, not a finding that the complaints don't exist. Treat
"named pain" as **unevidenced, not confirmed**, on both leads until a human (or
an agent with forum/API access) does a manual pass, or until direct engineer
outreach (joseleos's still-open access question) produces quotes directly.

## Scored candidates (Effort, Value: Researcher scores 1–5, 5=easier/more value. Marketability: Scribe, scored below. Buildability: Hermes/Claude+Codex input, TBD)

| # | Candidate | Discipline | Effort | Value | Marketability | Competitive intensity (informational) |
|---|---|---|---|---|---|---|
| 1 | **Traffic Impact Study (TIS) narrative/report automation** | Transportation | 4 | 4 | **4** (75) | **Low** — no dedicated automation tool found |
| 2 | **Utility Conflict Matrix (UCM) automation** | Transportation / land dev | 3 | 4 | **5** (80) | **Low** — only consulting services found, no software product |
| 3 | Sewer/water capacity availability letter automation | Water/wastewater | 4 | 3 | 3 (59) | Medium (SewerFlow/US3, Trinnex emerging) |
| 4 | ADA curb ramp inventory/compliance | Transportation | 2 | 3 | 2 (49) | Medium-High (AQCESSRAMP, Rieker ADAM, StreetSaver, Geonetics) |
| 5 | Traffic signal timing/retiming | Transportation | 2 | 3 | 2 (39) | High (ATSPM ecosystem, Econolite/Iteris-class incumbents) |
| 6 | Spec writing (CSI MasterFormat 3-part) automation | Cross-discipline | 3 | 2 | 3 (52) | High (ARCOM MasterSpec, e-SPECS, BSD SpecLink) |
| 7 | Geotechnical boring log/report automation | Geotechnical | 4 | 3 | 4 (69) | High (TabLogs, BoreDM, OpenGround) |
| 8 | SWPPP / NPDES stormwater compliance | Land dev/site | 4 | 3 | 3 (57) | High (SWPPPTrack, Ecesis, SiteMarker, EHSTracks, SW² — 5 found) |
| 9 | Structural calc package automation | Structural | 2 | 4 | 3 (57) | High (VIKTOR.AI, StruCalc, Tekla Tedds, struct.digital) |
| 10 | Stormwater/drainage design & report automation | Land dev/site | 2 | 4 | 2 (42) | Very High (Autodesk InfoDrainage, GeoSTORM, Carlson Hydrology, Stormwater Studio, h2x) |
| 11 | Earthwork/quantity takeoff | Land dev/site | 3 | 4 | 3 (62) | High (STACK, Beam AI, Kubla Cubed, InSite Elevation Pro, AGTEK) |
| 12 | Permitting automation | Construction estimating | 3 | 4 | 2 (42) | Very High + agency-buyer (PermitFlow $54M, CivCheck, CivitPERMIT, GeoCivix, Citizenserve, Datagrid) |
| 13 | Drawing review / RFI-submittal tracking | Construction estimating | 3 | 3 | 3 (52) | Very High, broad AEC not civil-specific (Bluebeam, eSUB, Knowify, SubmittalLink, iFieldSmart) |

Rows 3–13 carried from or adjacent to Jerry's prior-art 3–9 (`research/prior-art/`)
per the brief's permission to reconsider them — re-verified this pass, and in
every case the incumbent count came back **higher** than the prior scan noted,
not lower. That's new information: this space has kept filling in since the
last look. None of 3–13 clears "Low" competitive intensity; only #1 and #2 do.

## Candidate 1 — Traffic Impact Study (TIS) narrative/report automation

- **What it is:** every development above a jurisdiction's trip-generation
  threshold requires a TIS/TIA — a report combining traffic-count data,
  Synchro/VISSIM level-of-service output, and a written narrative with
  mitigation recommendations, submitted for agency approval.
- **Current workaround:** **self-built, not a named tool.** Synchro/VISSIM
  produce the LOS/delay tables; VISSIM has no interface to Synchro and control
  data has to be manually entered into text files; the narrative, exhibits, and
  mitigation write-up are assembled by hand in Word, per-jurisdiction template
  (BCEO, Delaware DOT, El Dorado County each publish their own guideline
  structure — no single format).
- **Stamped deliverable?** Partial/varies by jurisdiction — needs verification
  per state; flagging as an open item rather than assuming "no" the way OPCC's
  non-binding status was clean.
- **Budget holder:** individual PE/small transportation-engineering-firm
  principal; EIT job postings list "traffic impact studies" as a core, named
  duty (Indeed/Glassdoor traffic-EIT listings), confirming ongoing budget
  against this task, not just occasional.
- **Named incumbents/pricing:** none found for the report-automation layer
  specifically. Synchro and VISSIM are the modeling tools underneath (not
  competitors for narrative generation — a candidate could sit on top of
  their exports).
- **Venues:** ITE (Institute of Transportation Engineers) chapters, state DOT
  TIS guideline working groups, Eng-Tips traffic-engineering subforum.
- **Verbatim pain quotes:** none surfaced — see gap statement above.

## Candidate 2 — Utility Conflict Matrix (UCM) / SUE conflict coordination automation

- **What it is:** on any project with underground utility crossings (most
  transportation and land-development corridor work), engineers build a
  "conflict matrix" comparing utility records against project plans, tracked
  as a living document through design milestones, per ASCE 38-22 and FHWA's
  SHRP2 UCM methodology.
- **Current workaround:** **self-built/template-based, not a named
  commercial tool.** FHWA itself describes the standard tool as "a stand-alone,
  spreadsheet-based matrix (UCM lite)" — literally a spreadsheet. The
  companies that show up in search results (T2 Utility Engineers, SAM, Rios
  Group, Commun-ET) are consulting *services*, not software products.
- **Stamped deliverable?** No — it's a coordination/tracking artifact, not a
  design deliverable.
- **Budget holder:** individual PE/EIT at a private transportation or
  land-development design firm. Job-posting evidence: EIT duties explicitly
  include "identifying utility conflicts," "managing the UCM as a living
  document," and "meeting with utility company representatives at each
  milestone" — recurring, budgeted, named work.
- **Named incumbents/pricing:** none as software; FHWA's free "UCM lite" and
  "advanced UCM prototype" are government reference tools, not products with
  pricing or a sales motion competing for this buyer.
- **Venues:** ASCE Utility Engineering & Surveying Institute (UESI), state
  DOT utility-coordination training programs, APWA.
- **Verbatim pain quotes:** **update 2026-09-01** — no longer "none
  surfaced." `research/UCM_PAIN_QUOTES.md` has 5 usable, dated, attributed
  quotes (Douglas County NE, Mahoning County OH, Lee's Summit MO, Bryan TX,
  Lucas County OH engineers/officials) plus 2 borderline. Scope caveat:
  all are public-agency engineers on general road/utility-relocation
  projects, not the scan's specific private-firm PE/EIT buyer — evidences
  the pain is real and current, doesn't confirm this exact buyer feels it
  the same way. See that file for the full source-family breakdown
  (NCHRP/SHRP2/GAO/trade-press/committee-minutes all checked and exhausted
  or access-blocked this pass).

## What changed vs. the prior-art scan (rows 3–13)

Re-checking incumbents this pass, every carried-over category came back more
crowded than Jerry's original note, not less:
- Structural calc automation: found a 4th funded entrant (VIKTOR.AI, explicit
  "90–100% faster" claim) alongside StruCalc, Tekla Tedds, struct.digital.
- SWPPP/NPDES: found 5 named platforms (SWPPPTrack, Ecesis, SiteMarker,
  EHSTracks, SW²) vs. fewer previously assumed.
- Stormwater/drainage design: this is now effectively merged with what was
  scored as "stormwater/hydrology design" in the Jerry scan — Autodesk
  InfoDrainage, GeoSTORM, Carlson Hydrology, and Stormwater Studio **already
  ship automated report generation**, which was the exact wedge being
  considered here. That closes this candidate, doesn't just deprioritize it.
- Permitting and drawing-review/RFI: confirmed still the most saturated,
  best-funded corners of the list (unchanged conclusion, stronger evidence).

## Recommendation

**Lead with #1 (TIS automation) and #2 (UCM automation)** — both clear
competitive intensity, both have a self-built (not named-tool) workaround,
neither hits an agency buyer, and both have confirmed budgeted-EIT-time
evidence via job postings. Between them, #2 has a real open question on
technical effort (GIS/CAD overlay ingestion is a step up in complexity from a
pure rules-engine problem) and a real open question on frequency-per-project
(may be less recurring than TIS within a single project, though it recurs
across a firm's project portfolio).

**Before either goes to Hermes for ranking, close the same gap that hit
OPCC:** neither candidate has an unprompted complaint quote yet. Recommend
either (a) a manual Eng-Tips/r/civilengineering read-through (search-tool
blind spot, not necessarily an evidence gap), or (b) folding this into
joseleos's engineer-outreach answer if/when it lands — 5–10 interviews would
settle TIS vs. UCM vs. "neither" in one pass.

Rows 3–13 are documented for completeness and to close off re-litigating them,
but none is recommended to advance without a specific reason to override the
competitive-intensity finding.

---

# Marketability scoring (Scribe, 2026-08-30)

Scored with `research/MARKETABILITY_RUBRIC.md`. Seven dimensions, 1–5 each, weighted
(named pain ×3, time-to-obvious ×3, buyer=user ×3, channel fit ×2, liability drag
inverse ×2, wedge narrative ×2, reference velocity ×1), raw out of 80, normalized to 100.
Band mapping to the 1–5 column: **5** = 80+, **4** = 65–79, **3** = 50–64, **2** = 35–49,
**1** = under 35. Normalized score shown in parentheses in the table so Hermes can see
ordering inside a band.

## Handling the named-pain gap honestly

Researcher flagged that neither lead has a verbatim unprompted complaint. Per the rubric,
named pain is the joint-heaviest dimension, so I have **not** scored it as confirmed on
either. Both leads are scored at **named pain = 2** — job-posting evidence proves the task
is budgeted and recurring, which is real but is not the buyer complaining. Ranges if the
gap closes or fails to close:

| Candidate | Floor (pain=1, no complaints exist) | **Scored (pain=2, current evidence)** | Ceiling (pain=5, confirmed) |
|---|---|---|---|
| #1 TIS | 71 → band 4 | **75 → band 4** | 86 → band 5 |
| #2 UCM | 76 → band 4 | **80 → band 5** | 91 → band 5 |

Both stay in the top two bands across the whole range and **their relative order does not
change**. Practical consequence: Hermes can rank now without waiting for quotes. That is
not permission to *build* without them — it means the ranking is robust to this particular
unknown, which is a narrower claim.

## Per-dimension, the two leads

| Dimension | W | #1 TIS | #2 UCM | Note |
|---|---|---|---|---|
| Named pain | 3 | 2 | 2 | Unevidenced on both. Job postings only. |
| Time-to-obvious | 3 | 4 | 3 | TIS wins: Synchro exports + blank template → finished narrative is one screenshot. UCM is a spreadsheet before and after unless we build a visual conflict overlay. |
| Buyer = user | 3 | 5 | 5 | Both: individual PE / small private-firm principal, card, no procurement. |
| Channel fit | 2 | 5 | 5 | TIS: ITE chapters, TRB, state DOT TIS working groups. UCM: ASCE UESI, state DOT utility-coordination *training* programs (PDH-native), APWA. |
| Liability drag (inv.) | 2 | **2** | **5** | The decisive split — see below. |
| Wedge narrative | 2 | 5 | 5 | TIS sits on top of Synchro/VISSIM rather than against them. UCM replaces a spreadsheet. Neither names a competitor. |
| Reference velocity | 1 | 3 | 4 | Both private-firm buyers. UCM slightly better: coordination work is less sensitive than agency-submitted study methodology. |
| | | **75** | **80** | |

## Why UCM outscores TIS on this axis

Entirely liability drag, and it is worth stating plainly because it points the other
direction from the scan's recommendation.

A TIS is **submitted to an agency for approval and sealed by a PE in many jurisdictions**
(the scan flags stamped status as "partial/varies" — correctly not assumed). It also
contains **mitigation recommendations**: engineering judgment that feeds public-safety
decisions. If our software drafts that narrative, we are asking a PE to stamp
machine-assisted engineering recommendations. That is a real marketing cost — it means
validation studies, careful claim language, and a slower trust build. It does not kill
TIS; it caps it.

A UCM is a **coordination and tracking artifact**. Nothing is stamped, no design value is
asserted, and being wrong produces a rework conversation rather than a liability claim.
That is the same structural advantage OPCC had in the Jerry scan, and it is the single
most valuable property a first product in this vertical can have.

## The best wedge in either scan

FHWA describes the standard UCM tool as *"a stand-alone, spreadsheet-based matrix."* We can
quote the federal agency that defined the methodology describing the incumbent as a
spreadsheet. That is a positioning line that writes itself, names no competitor with a
sales team, and cannot be disputed. Nothing in the Jerry scan or this one is that clean.

## Product decision with a direct marketing consequence

UCM's one weak dimension is time-to-obvious (3). A conflict matrix is a spreadsheet before
and a better spreadsheet after — hard to screenshot. What fixes it is a **visual plan-view
overlay with conflicts highlighted**, which turns the demo into something self-evident and
would raise the dimension to 4–5 (normalized ~85).

That is exactly the GIS/CAD ingestion the scan flags as UCM's effort risk. So: **the
feature that makes UCM marketable is the feature that makes it harder to build.** That
tension belongs in the architecture conversation, not discovered during launch. If the
overlay is out of scope for v1, UCM ships with a materially weaker demo and the content
plan has to lean on outcome claims (conflicts caught, rework avoided) that need customer
evidence we will not have on day one.

## Reading the carried-over rows

Rows 3–13 land between 39 and 69. Two notes so the numbers are not misread:

- **#7 geotech boring logs scores highest of the carried rows (69, band 4)** — and it gets
  there almost entirely on *named pain = 4*, because it is the only candidate in either
  scan with documented unprompted complaints ("hours lost to retyping data before analysis
  can even begin," plus the ~$7/log figure, from the prior-art scan). It is penalized on
  wedge (2) for TabLogs/BoreDM/Bentley OpenGround. A 4 here means "easy to get attention
  and convert *if* you win the category," not "pick this."
- **#10 stormwater scores 42 (band 2), below its prior-art rating.** Researcher's finding
  that Autodesk InfoDrainage and Carlson already ship the automated-report wedge does not
  just crowd this candidate, it inverts two dimensions: the before/after stops being
  "manual vs automated" and becomes "Autodesk's automation vs ours," and unprompted
  complaints would be about incumbent pricing rather than the task. Scored as closed.

## What I need before writing anything

Unchanged and still open: verbatim quotes (the gap above), plus joseleos's answer on first
customer segment. Solo PE and 10–50 person firm are different pitches for either candidate.
