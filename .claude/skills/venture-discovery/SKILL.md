---
name: venture-discovery
description: >
  Find and rank civil-engineering problems that software automation could solve.
  Orchestrates Researcher (evidence), Scribe (marketability axis), HermesX
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
| HermesX | Owns the final ranking and the decision memo |
| joseleos | Picks. Nothing downstream starts until the pick is posted |

## Inputs
- Scope statement from joseleos (space, constraints, team size).
- Existing scan and rubric in `research/` if present.

## Steps
1. **Candidate list.** Researcher sweeps disciplines: transportation, water/
   wastewater, structural, geotechnical, land development/site, construction
   estimating. Target 8–12 candidates. Each gets a discipline tag first —
   nothing scores on channel fit without one.
2. **Evidence per candidate** (Researcher; items 1 and 3 are the expensive ones
   to reconstruct later, capture them on first contact):
   1. Verbatim pain quotes, 3–5, with source URLs. Exact phrasing, no paraphrase.
   2. Budget holder: individual / firm / agency, plus typical dollar authority.
   3. Current workaround: self-built spreadsheet, manual process, incumbent
      tool, offshore drafting.
   4. Does the output touch a stamped deliverable? yes / no / assists.
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
4. **Rank.** HermesX ranks; ties broken toward lower liability drag. Publish
   the table in `research/OPPORTUNITY_SCAN_<date>.md`.
5. **Decision memo** (≤1 page, HermesX): top pick, runner-up, why, what would
   change the answer, open gaps and their cost to close.
6. **Gate.** Post the memo in the channel and @mention joseleos. Wait for a
   message of the form `pick: <candidate>`. Record it in `docs/DECISIONS.md`.

## Outputs
- `research/OPPORTUNITY_SCAN_<date>.md` — ranked table + per-candidate evidence.
- `research/DECISION_MEMO_<date>.md`.
- `docs/DECISIONS.md` entry with the pick and date.

## Anti-patterns
- Re-running the sweep when a scan exists. Extend it.
- Letting market size leak into the marketing column.
- Paraphrased quotes. They cannot become headlines.
- Scoring channel fit before the discipline tag is set.

## Handoff
`pick:` message → run `product-build`. Hand it the scan row, the evidence
bundle, and the verbatim quotes (Scribe needs them again in `go-to-market`).
