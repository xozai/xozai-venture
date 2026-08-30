---
title: "Xozai opportunity scan — discovery pass 1"
author: Researcher
created: 2026-08-30
status: draft — Scribe to score marketability, Hermes to rank
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

## Scored candidates (Effort, Value: Researcher scores 1–5, 5=easier/more value. Marketability: Scribe, TBD. Buildability: Hermes/Claude+Codex input, TBD)

| # | Candidate | Discipline | Effort | Value | Marketability | Competitive intensity (informational) |
|---|---|---|---|---|---|---|
| 1 | **Traffic Impact Study (TIS) narrative/report automation** | Transportation | 4 | 4 | TBD | **Low** — no dedicated automation tool found |
| 2 | **Utility Conflict Matrix (UCM) automation** | Transportation / land dev | 3 | 4 | TBD | **Low** — only consulting services found, no software product |
| 3 | Sewer/water capacity availability letter automation | Water/wastewater | 4 | 3 | TBD | Medium (SewerFlow/US3, Trinnex emerging) |
| 4 | ADA curb ramp inventory/compliance | Transportation | 2 | 3 | TBD | Medium-High (AQCESSRAMP, Rieker ADAM, StreetSaver, Geonetics) |
| 5 | Traffic signal timing/retiming | Transportation | 2 | 3 | TBD | High (ATSPM ecosystem, Econolite/Iteris-class incumbents) |
| 6 | Spec writing (CSI MasterFormat 3-part) automation | Cross-discipline | 3 | 2 | TBD | High (ARCOM MasterSpec, e-SPECS, BSD SpecLink) |
| 7 | Geotechnical boring log/report automation | Geotechnical | 4 | 3 | TBD | High (TabLogs, BoreDM, OpenGround) |
| 8 | SWPPP / NPDES stormwater compliance | Land dev/site | 4 | 3 | TBD | High (SWPPPTrack, Ecesis, SiteMarker, EHSTracks, SW² — 5 found) |
| 9 | Structural calc package automation | Structural | 2 | 4 | TBD | High (VIKTOR.AI, StruCalc, Tekla Tedds, struct.digital) |
| 10 | Stormwater/drainage design & report automation | Land dev/site | 2 | 4 | TBD | Very High (Autodesk InfoDrainage, GeoSTORM, Carlson Hydrology, Stormwater Studio, h2x) |
| 11 | Earthwork/quantity takeoff | Land dev/site | 3 | 4 | TBD | High (STACK, Beam AI, Kubla Cubed, InSite Elevation Pro, AGTEK) |
| 12 | Permitting automation | Construction estimating | 3 | 4 | TBD | Very High + agency-buyer (PermitFlow $54M, CivCheck, CivitPERMIT, GeoCivix, Citizenserve, Datagrid) |
| 13 | Drawing review / RFI-submittal tracking | Construction estimating | 3 | 3 | TBD | Very High, broad AEC not civil-specific (Bluebeam, eSUB, Knowify, SubmittalLink, iFieldSmart) |

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
- **Verbatim pain quotes:** none surfaced — see gap statement above. FHWA/NAP
  sources confirm the *cost* of getting this wrong (delays, safety issues,
  redesign) but that's institutional framing, not an engineer's own words.

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
