# Jerry Project — Civil Engineering Software Opportunity Scan

Date: 2026-08-30
Author: Researcher
Status: discovery pass 1 (web research only, no primary interviews yet)

## Method
Web research across forums (Eng-Tips, general search proxies for r/civilengineering),
vendor/review sites (Capterra, G2), and startup/funding trackers, spanning six
disciplines: land development/site, transportation, geotechnical, structural,
water/wastewater (stormwater), and construction estimating. Scored candidates on
four axes per joseleos's brief (effort, value, marketability, our buildability),
cross-checked against Scribe's marketability rubric (named pain, time-to-obvious,
buyer=user, channel fit, liability drag, wedge narrative, reference velocity).

## Ranked shortlist

| Rank | Candidate | Effort | Value | Marketability | Our buildability | Competitive intensity |
|---|---|---|---|---|---|---|
| 1 | OPCC / cost-estimate exhibit automation (design-phase) | Low-Med | Med-High | High | High | Low-Med |
| 2 | Traffic Control Plan (TCP) generation (MUTCD) | Medium | High | Med-High | Medium | Medium (1 AI entrant) |
| 3 | Geotechnical boring-log & report automation | Medium | Medium | Medium | Medium-High | High (3+ funded incumbents) |
| 4 | SWPPP/stormwater compliance software | Low-Med | Medium | Medium | Medium | High (crowded, low-price incumbents) |
| 5 | Structural calc-package automation | Medium | Medium | Low-Med (liability drag) | Low-Med | High (4+ incumbents) |
| 6 | Stormwater/hydrology design (HydroCAD-class) | High | High | Low (entrenched, jurisdiction lock-in) | Low | High (industry standard incumbent) |
| 7 | Earthwork/quantity takeoff | High | High | Medium | Low (needs volumetric/CAD engine) | High (AGTEK, Civils.ai, iBeam, Bentley) |
| 8 | Permitting automation (multi-discipline) | Very High | High | Low (procurement/govtech-adjacent) | Low (resource gap vs. funded players) | Very High (PermitFlow $54M Series B) |
| 9 | Drawing review / clash detection / RFI generation | High | High | Medium | Low (vision-heavy, funded competitors) | High (Buildcheck AI $5.9M seed, Helonic) |

## Recommendation: #1, OPCC / cost-estimate exhibit automation

**What it is:** Every land-development and site-civil project produces an
Engineer's Opinion of Probable [Construction] Cost at each design milestone
(30/60/90/100%) — a quantity × unit-price exhibit engineers currently build by
hand in Excel, re-keying quantities off Civil 3D takeoffs and stale unit-price
lists.

**Why it ranks #1:**
- **Named pain, recurring at high frequency** — every civil site-design project
  needs one at every milestone, across every sub-discipline (site dev,
  transportation, water/wastewater all produce OPCCs).
- **Time-to-obvious** — before/after is a single screenshot: messy milestone
  spreadsheet vs. a clean, regionally-priced, stamped-ready cost exhibit.
- **Buyer = user** — individual PE or small-firm principal, card-purchase,
  no procurement cycle.
- **Low liability drag** — OPCCs are explicitly disclaimed as non-binding
  estimates, not stamped design values, so this avoids the trust/liability
  wall that blocks automation of actual engineering calcs.
- **Buildable by a lean AI-native team** — this is fundamentally a rules
  engine (regional unit-price database + quantity list ingestion) with an LLM
  assist for line-item classification and PDF/Excel exhibit generation, not a
  CAD-geometry or FEA problem. No incumbent AI-native player found in this
  specific design-phase niche (existing "AI cost estimating" tools found —
  ProEst, Kreo, Civils.ai — are contractor-bid-estimating tools for
  construction-phase takeoffs, not engineer's-opinion exhibits during design).
- **Channel fit** — PDH webinars, state PE society newsletters, ASCE branch
  meetings (per Scribe's rubric) all apply directly.

**Runner-up: #2, Traffic Control Plan (TCP) generation.** MUTCD is a discrete,
well-documented rule set (good LLM/template fit), high per-project frequency,
buyer is a traffic-control company or small transportation firm (direct
sale). One AI entrant found (Mastt AI) — moderate rather than low
competition. Requires more build effort than #1 (diagram/CAD generation, not
just tabular output), and a PE stamp is typically required on the plan
itself even though the layout generation is the time sink.

## Notes for Scribe (per your data-capture request)

- **Verbatim pain quotes found so far** (attributable, will keep collecting):
  - Structural: *"It shouldn't take four days and 50 YouTube videos to model a
    basic wood frame"* — Eng-Tips forum member, re: software usability.
  - Geotechnical: field teams report *"hours lost to retyping data before
    analysis can even begin"* and ~$7/log in wasted wages from manual
    re-entry across field/lab/report stages (vendor-published, treat as
    directional not neutral).
- **Current workaround for OPCC pick:** ad hoc Excel workbooks per firm,
  manually re-keyed from Civil 3D quantity takeoffs against static or
  memorized unit-price lists; no dominant incumbent tool.
- **Named incumbents + pricing surfaced this pass:**
  - Geotechnical: TabLogs, BoreDM, Aldoa (gINT replacement), SO-Log.
  - SWPPP: 4RIVRS, Ecesis, SW².
  - Structural calc: Calcs.com, struct.digital, SkyCiv, StruCalc, ENERCALC.
  - Stormwater/hydrology: HydroCAD (industry standard), Hydrology Studio.
  - Earthwork takeoff: AGTEK, Earthworks OS, Civils.ai, iBeam (Beam AI).
  - Permitting: PermitFlow ($54M Series B, Accel/Kleiner/Felicis), Permitify
    (YC).
  - Drawing review/RFI: Buildcheck AI ($5.9M seed, 10-35x ROI claims,
    AvalonBay customer), Helonic (Procore/Autodesk integration).
  - Traffic control plans: Mastt AI, PurposeBuilt DTCD, Transoft, Autodesk
    Civil 3D (native).
- **Discipline tag for #1 pick:** land development / site-civil (cross-cuts
  transportation and water/wastewater as a shared deliverable type).
- **Discipline tag for #2 pick:** transportation.

## Open gaps before this is decision-ready
- No primary-source interviews or verbatim quotes yet specific to OPCC pain
  (this candidate surfaced from workflow-description searches, not direct
  complaints — worth a targeted forum/Reddit pass before locking the pick).
- Named incumbent pricing not yet gathered for the #1 and #2 picks
  specifically (no dedicated OPCC-automation competitor was found to price
  against).
- Budget-holder dollar authority not yet sized for either pick.
