# Xozai venture pipeline plan — skills for launching a civil-engineering software startup

Owner: joseleos. Orchestrator: Claude. Created 2026-08-30.

## Why three skills

The brief has three distinct phases with different people, different gates,
and different artifacts. One skill per phase keeps each playbook short enough
to actually follow and lets a phase be re-run without re-running the others
(e.g. discovery again for a second product, or GTM again for a relaunch).

```
 Skill 1                     Skill 2                        Skill 3
 venture-discovery  ──►  product-build  ──►  go-to-market
 Researcher, Scribe,     Claude, Codex, Fizz0,             HermesX, Researcher,
 HermesX (ranking)       Honey0, Pollen0                   Scribe
 GATE: joseleos picks    GATE: release candidate           GATE: joseleos approves
 the product             passes Honey0's suite             GTM plan, then content
```

## Skill 1 — `venture-discovery`

Goal: a ranked shortlist of civil-engineering problems that software automation
could solve, scored on four **separate** axes, and a one-page decision memo so
joseleos can pick one.

Four axes (from the brief), each 1–5:
1. **Effort to build** (inverse — lower effort scores higher)
2. **Value to the market**
3. **Ease of marketing** — scored with Scribe's 7-dimension rubric
   (`research/MARKETABILITY_RUBRIC.md`). Rule: *ease of marketing ≠ market size*.
   Market size belongs on axis 2 only.
4. **Our ability to build it** — lean AI-native team, no CAD/FEA engine, no
   procurement sales motion.

Per-candidate evidence Researcher must capture (Scribe's list): verbatim pain
quotes with URLs (3–5), budget holder + dollar authority, current workaround,
stamped-deliverable touch (yes/no/assists), named incumbents + public pricing,
2–3 venues where the audience gathers, and discipline tag.

Current state: **not started for Xozai.** A scan from the separate Jerry Project
venture is kept in `research/prior-art/` as reference for method and candidate
coverage only — Xozai runs its own discovery pass and makes its own pick.
Whether Xozai must exclude Jerry Project's candidates (OPCC, TCP) is an open
question for joseleos.

Exit: joseleos posts "pick: <candidate>" in the channel. That message is the gate.

## Skill 2 — `product-build`

Goal: turn the picked problem into a shipped v1.

Stages:
1. **Architecture** — Claude (senior) and Codex (junior) pair. Claude drafts
   `product/ARCHITECTURE.md` (scope, data model, stack, non-goals, milestones);
   Codex challenges it and writes the issue breakdown. Both sign off.
2. **Build** — Claude/Codex file issues in the repo; Codex and Fizz0 implement in
   parallel on separate issues; PRs reviewed by whichever of Claude/Codex did not
   author.
3. **QA** — Honey0 writes test cases from `ARCHITECTURE.md` acceptance criteria
   *while* build is in progress, then executes against each release candidate
   and files bugs as issues labelled `bug`.
4. **Fix loop** — Codex triages bugs (severity, reproducibility, duplicate),
   assigns to Pollen0; Pollen0 fixes via PR; Honey0 re-verifies.

Exit: a tagged release where Honey0's suite passes with zero open `severity:high`
bugs.

## Skill 3 — `go-to-market`

Goal: a GTM plan and a ready-to-run campaign for the shipped product.

Gate (Scribe's rule): no content drafting until three inputs exist — named
audience (discipline + role + firm size), the named incumbent/workaround being
replaced, and the verbatim quotes. Sequence: HermesX's GTM plan and positioning
are signed off by joseleos **first**; Scribe's campaign assets **second**.

Civil-specific channel hard-coded into the skill: **PDH-credit webinars** — PEs
need continuing-education hours and will attend vendor webinars to earn them.
Also: state PE society newsletters, ASCE branch meetings, Eng-Tips /
r/civilengineering, YouTube "how do I do X in <tool>" SEO, discipline
conferences.

Exit: joseleos approves the campaign; assets live in `marketing/`, site in
`website/`.

## Repo

`xozai/xozai-venture` (this repo) holds skills, research, product, website, marketing.
One repo so cross-references (rubric → positioning → copy; architecture →
tests) are relative links, not hunts across accounts.

## Decision (joseleos, 2026-08-30)

Xozai and Jerry Project are **different ventures**. This repo and these skills
belong to Xozai; Skill 1 runs a fresh discovery pass here.
