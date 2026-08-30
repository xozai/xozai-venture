---
name: product-build
description: >
  Turn the selected problem — in any space — into a shipped v1. Claude (senior)
  and Codex (junior) design the architecture; Codex and Fizz0 build; Honey0
  writes and runs tests; Codex triages bugs to Pollen0.
version: 2
---

# Skill 2 — Product build

## When to run
After `venture-discovery` produced a `pick:` and it is recorded in
`docs/DECISIONS.md`. Do not start on a "probably" pick.

## Inputs
- The picked candidate's scan row and evidence bundle (verbatim quotes,
  workaround, incumbents, budget holder) from `research/`.
- The space profile `research/spaces/<SPACE>.md` — for the liability analog
  (what makes an output high-stakes) and buyer archetype.
- `research/SKILL_SOURCES.md` — public repos/boilerplates worth reusing;
  check it before writing anything from scratch.

## Roles
| Who | Does |
|---|---|
| Claude | Senior engineer: architecture owner, reviewer, orchestrator of this skill |
| Codex | Junior engineer in architecture (challenges, breaks into issues); builder; bug triage |
| Fizz0 | Builder |
| Honey0 | Test cases + execution; files bugs |
| Pollen0 | Bug fixes |
| joseleos | Answers product-intent questions; approves release |

## Stage A — Architecture (Claude + Codex)
1. Claude drafts `product/ARCHITECTURE.md`:
   - Problem statement (copy the verbatim quotes in — they are the spec).
   - v1 scope and explicit non-goals.
   - User flow (one primary path, end to end).
   - Inputs and outputs: the real document, data, or file formats the user
     already works with. Spike parsers/exporters early — format handling is
     where domain surprises live.
   - Data model, stack, external dependencies (data sources, LLM usage, hosting).
   - Liability boundary: what the product asserts vs what it leaves to the
     human, given the space's liability analog. Write it down; it drives
     disclaimers, review steps, and what v1 must *not* automate.
   - Acceptance criteria per feature — written so Honey0 can test them without
     asking.
   - Milestones: M1 walking skeleton, M2 feature-complete, M3 release candidate.
2. Codex reviews as junior-with-teeth: every section gets either "agree" or a
   concrete objection with an alternative. Codex then writes
   `product/ISSUES.md` — the breakdown into ≤1-day issues with dependencies.
3. Claude resolves objections, both sign off in the channel. Claude files the
   issues (`buzz issues create` or GitHub) and labels them `M1`/`M2`/`M3`.
4. Product-intent questions go to joseleos in one batched message, not a trickle.

Default stack unless joseleos vetoes: TypeScript + Next.js, Postgres, Claude API
for classification/extraction/generation, plus whatever import/export libs the
space's formats need. Prefer boring, hosted, cheap. Start from a permissively
licensed boilerplate listed in `research/SKILL_SOURCES.md` when one fits; never
vendor copyleft (AGPL/GPL) code.

## Stage B — Build (Codex + Fizz0)
- Assign M1 issues alternately to Codex and Fizz0; no shared files on
  concurrent issues.
- Each issue → branch/worktree → PR → review by whichever of Claude/Codex did
  **not** author. Reviewer runs the full test suite, not a scoped run.
- Merge only with green CI and one approving review. Squash.
- Builders post "picked up" and "PR up" in the channel, nothing in between
  unless blocked.

## Stage C — QA (Honey0)
- Starts during Stage A step 3: Honey0 derives `product/tests/TEST_PLAN.md`
  from the acceptance criteria. Each test has an ID, preconditions, steps,
  expected result. Include realistic sample inputs from the space (real-shaped
  documents/data, anonymised if needed) — synthetic toy inputs miss the bugs
  users hit.
- At each milestone tag, Honey0 executes the plan (automated where practical,
  in `product/tests/`), and files every failure as an issue labelled `bug`
  with: test ID, repro steps, expected vs actual, severity
  (`severity:high|medium|low`), environment.

## Stage D — Fix loop (Codex → Pollen0)
1. Codex triages each `bug`: confirms repro, sets severity, marks duplicates,
   assigns to Pollen0 with `buzz issues assign` (or GitHub assignee).
2. Pollen0 fixes on a branch, adds a regression test, opens a PR referencing
   the issue. Codex reviews.
3. Honey0 re-runs the failing test ID and closes the issue or reopens it.
4. Loop until zero open `severity:high` and joseleos accepts remaining mediums.

## Exit
- Tag `v1.0.0`. Honey0 posts the final run: total/pass/fail, open bugs by severity.
- Claude posts the release summary and @mentions joseleos. Hand `product/
  ARCHITECTURE.md`, screenshots, and the acceptance criteria to `go-to-market`.

## Rules
- Nobody commits to `main`. Worktrees per issue.
- Attribute results to the exact commit that produced them.
- No architecture changes after Stage A sign-off without a note in
  `docs/DECISIONS.md`.
- Scale review depth to risk: auth, persistence, money/quantity math, and
  anything that crosses the liability boundary get a second reviewer.
