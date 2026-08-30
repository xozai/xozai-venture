---
name: venture-discovery
description: >
  Find and rank problems in a target space that software could solve. Space is a
  parameter: read `research/spaces/<SPACE>.md` for scope, exclusions, buyers,
  incumbents, complaint sources, channels, and the liability analog.
  Orchestrates Researcher (evidence), Scribe (marketability axis), Hermes
  (ranking) and produces a decision memo for joseleos to pick a product.
version: 1
---

# Skill 1 — Venture discovery

## When to run
- Starting a venture search, or re-running for a second product.
- Closing evidence gaps on an existing shortlist (if a scan exists in
  `research/`, extend it rather than restarting). `research/prior-art/` holds
  another venture's scan — use it for method and coverage, not as this
  venture's shortlist.

## Roles
| Who | Does |
|---|---|
| Orchestrator (Claude) | Runs this playbook, keeps the candidate table, posts status |
| Researcher | Gathers per-candidate evidence (list below), scores effort/value |
| Scribe | Scores "ease of marketing" with `research/MARKETABILITY_RUBRIC.md` |
| Hermes (bot `4124af96…`) | Owns the final ranking and the decision memo |
| joseleos | Picks. Nothing downstream starts until the pick is posted |

## Inputs
- **Space profile** `research/spaces/<SPACE>.md` — create one from joseleos's
  scope statement if it doesn't exist (see `CIVIL_ENGINEERING.md`,
  `ENTERPRISE_SPM.md` for the template). Each space is its own track with its
  own scan file and memo; joseleos picks across tracks.
- Existing scan and rubric in `research/` if present.

## Steps
1. **Aim first.** Read `research/PRE_SWEEP_BRIEF.md` (Scribe) — the target
   profile of a high-marketability candidate and where unprompted complaints
   surface (Eng-Tips, r/civilengineering, YouTube tutorial comments, PE-society
   forums, job postings). Find *new* candidates, not leftovers from prior art.
   **Candidate list.** Researcher sweeps the sub-areas listed in the space
   profile. Target 8–12 candidates. Each gets a discipline/sub-area tag first —
   nothing scores on channel fit without one.
2. **Evidence per candidate** (Researcher; items 1 and 3 are the expensive ones
   to reconstruct later, capture them on first contact):
   1. Verbatim pain quotes, 3–5, with source URLs. Exact phrasing, no paraphrase.
   2. Budget holder: individual / firm / agency, plus typical dollar authority.
   3. Current workaround: self-built spreadsheet, manual process, incumbent
      tool, offshore drafting. **Required sub-field: self-built vs named
      commercial tool** — self-built gives the wedge "replaces the thing you
      built yourself"; a named incumbent means "better than X" on their terms.
   4. Does the output touch the space's liability analog (civil: a stamped
      deliverable; SPM: money paid or booked)? yes / no / assists.
   5. Named incumbents with public pricing.
   6. Where the audience gathers: 2–3 specific venues, rough size.
   7. Discipline tag.
3. **Score four axes, 1–5, in separate columns:**
   - **Effort to build** (5 = a rules engine + LLM assist + PDF/Excel out;
     1 = needs a CAD/geometry/FEA engine).
   - **Value to market** — frequency × pain × market size. *This is the only
     column where market size counts.*
   - **Ease of marketing** — Scribe scores with the 7-dimension rubric
     (named pain, time-to-obvious, buyer = user, channel fit, liability drag,
     wedge narrative, reference velocity), normalized to 100 then mapped to 1–5.
     Rule: big + incumbent-owned + procurement-gated is *hard*, not easy.
   - **Our ability to build** — lean AI-native team, no field sales, no
     procurement motion, no validation studies for stamped outputs.
   Add a fifth informational column: competitive intensity (not scored, shown).
4. **Rank.** Hermes ranks; ties broken toward lower liability drag. Publish
   the table in `research/OPPORTUNITY_SCAN_<date>.md`.
5. **Decision memo** (≤1 page, Hermes): top pick, runner-up, why, what would
   change the answer, open gaps and their cost to close.
6. **Gate.** Post the memo in the channel and @mention joseleos. Wait for a
   message of the form `pick: <candidate>`. Record it in `docs/DECISIONS.md`.

## Outputs
- `research/OPPORTUNITY_SCAN[_<SPACE>]_<date>.md` — ranked table + per-candidate evidence.
- `research/DECISION_MEMO_<date>.md`.
- `docs/DECISIONS.md` entry with the pick and date.

## Exclusions
Live in the space profile. Civil (joseleos, 2026-08-30): OPCC exhibits and MUTCD
traffic-control plans belong to the Jerry Project venture — drop before scoring.

## Anti-patterns
- Re-running the sweep when a scan exists. Extend it.
- Letting market size leak into the marketing column.
- Paraphrased quotes. They cannot become headlines.
- Scoring channel fit before the discipline tag is set.

## Handoff
`pick:` message → run `product-build`. Hand it the scan row, the evidence
bundle, and the verbatim quotes (Scribe needs them again in `go-to-market`).
