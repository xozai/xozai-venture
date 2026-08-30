---
name: venture-discovery
description: >
  Find and rank problems in any target space that software could solve. Space
  is a parameter: read `research/spaces/<SPACE>.md` for scope, exclusions,
  buyers, incumbents, complaint sources, channels, and the liability analog.
  Orchestrates Researcher (evidence), Scribe (marketability axis), Hermes
  (ranking) and produces a decision memo for joseleos to pick a product.
version: 2
---

# Skill 1 — Venture discovery

## When to run
- Starting a venture search in a new space, or re-running for a second product.
- Closing evidence gaps on an existing shortlist (if a scan exists in
  `research/` for this space, extend it rather than restarting).
  `research/prior-art/` holds other ventures' scans — use them for method and
  coverage, never as this venture's shortlist.

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
  scope statement if it doesn't exist. Every space profile must define:
  - **Scope** — one sentence: who the software is for.
  - **Exclusions** — candidates that belong to another venture or are out of
    bounds. Drop them before scoring.
  - **Sub-areas to sweep** — 4–8 segments, disciplines, functions, or
    workflows within the space. Every candidate gets one as its tag.
  - **Buyer archetypes** — individual / small team (card) / mid-size (seats)
    / enterprise or public sector (procurement). Note which to avoid.
  - **Liability analog** — the thing in this space that makes an output
    high-stakes (a signed/sealed deliverable, money moved, a regulatory
    filing, a medical or legal decision, …). The rubric's "liability drag"
    dimension scores against this.
  - **Where unprompted complaints live** — specific forums, subreddits,
    Q&A sites, tutorial comment sections, job postings, review sites.
  - **Channels** — where this audience can actually be reached (see
    `go-to-market`).
  - **Rubric addendum** (optional) — `research/<SPACE>_RUBRIC_ADDENDUM.md`
    re-anchoring the 7 marketability dimensions to this space.
  Existing profiles in `research/spaces/` are worked examples of the format.
  Each space is its own track with its own scan file and memo; joseleos
  picks across tracks.
- `research/PRE_SWEEP_BRIEF.md` (Scribe) — the target profile of a
  high-marketability candidate. Space-independent; read before sweeping.
- `research/MARKETABILITY_RUBRIC.md` — the 7-dimension marketing rubric.
- Existing scan for this space in `research/`, if present.

## Steps
1. **Aim first.** Read the pre-sweep brief and the space profile. Find *new*
   candidates, not leftovers from prior art or from the exclusions list.
   **Candidate list.** Researcher sweeps the sub-areas listed in the space
   profile. Target 8–12 candidates. Each gets a sub-area tag first — nothing
   scores on channel fit without one.
2. **Evidence per candidate** (Researcher; items 1 and 3 are the expensive ones
   to reconstruct later, capture them on first contact):
   1. Verbatim pain quotes, 3–5, with source URLs. Exact phrasing, no paraphrase.
   2. Budget holder: individual / team / company / institution, plus typical
      dollar authority.
   3. Current workaround: self-built spreadsheet, manual process, incumbent
      tool, outsourced labor. **Required sub-field: self-built vs named
      commercial tool** — self-built gives the wedge "replaces the thing you
      built yourself"; a named incumbent means "better than X" on their terms.
   4. Does the output touch the space's liability analog (from the profile)?
      yes / no / assists.
   5. Named incumbents with public pricing.
   6. Where the audience gathers: 2–3 specific venues, rough size.
   7. Sub-area tag.
3. **Score four axes, 1–5, in separate columns:**
   - **Effort to build** (5 = rules engine + LLM assist + document/spreadsheet
     in-and-out; 1 = needs a specialised engine — geometry, simulation,
     real-time, hardware, or a regulated data integration).
   - **Value to market** — frequency × pain × market size. *This is the only
     column where market size counts.*
   - **Ease of marketing** — Scribe scores with the 7-dimension rubric
     (named pain, time-to-obvious, buyer = user, channel fit, liability drag,
     wedge narrative, reference velocity), normalized to 100 then mapped to 1–5.
     Rule: big + incumbent-owned + procurement-gated is *hard*, not easy.
     **Re-anchor per space**: 5 means "best achievable in this space." Use the
     space's rubric addendum if one exists; never score a new space on another
     space's anchors.
   - **Our ability to build** — lean AI-native team, no field sales, no
     procurement motion, no certification or validation studies before v1.
   Add a fifth informational column: competitive intensity (not scored, shown).
4. **Rank.** Hermes ranks; ties broken toward lower liability drag. Publish
   the table in `research/OPPORTUNITY_SCAN_<SPACE>_<date>.md`.
5. **Decision memo** (≤1 page, Hermes): top pick, runner-up, why, what would
   change the answer, open gaps and their cost to close.
6. **Gate.** Post the memo in the channel and @mention joseleos. Wait for a
   message of the form `pick: <candidate>`. Record it in `docs/DECISIONS.md`.
7. **Across tracks** (when more than one space has a memo): Hermes writes a
   **prose** structural comparison — buyer motion, distribution, liability,
   time-to-revenue, what the team can build — with each track's top candidate.
   **Never put scores from different tracks in one ranked table.** Scores are
   only comparable within a track.

## Outputs
- `research/OPPORTUNITY_SCAN_<SPACE>_<date>.md` — ranked table + per-candidate evidence.
- `research/DECISION_MEMO_<SPACE>_<date>.md`.
- `docs/DECISIONS.md` entry with the pick and date.

## Exclusions
Live only in the space profile, never in this skill. If joseleos states an
exclusion in the channel, add it to the profile and record it in
`docs/DECISIONS.md`.

## Anti-patterns
- Cross-track numeric rankings. An 80 in one space and an 80 in another are
  not the same thing.
- Re-running the sweep when a scan exists. Extend it.
- Letting market size leak into the marketing column.
- Paraphrased quotes. They cannot become headlines.
- Scoring channel fit before the sub-area tag is set.
- Hard-coding one space's venues, jargon, or exclusions into this skill.

## Handoff
`pick:` message → run `product-build`. Hand it the scan row, the evidence
bundle, the space profile, and the verbatim quotes (Scribe needs them again
in `go-to-market`).
