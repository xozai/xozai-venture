# Xozai venture pipeline plan — skills for launching a software startup in any space

Owner: joseleos. Orchestrator: Claude. Created 2026-08-30.

## Why three skills

The brief has three distinct phases with different people, different gates,
and different artifacts. One skill per phase keeps each playbook short enough
to actually follow and lets a phase be re-run without re-running the others
(e.g. discovery again for a second product, or GTM again for a relaunch).

```
 Skill 1                     Skill 2                        Skill 3
 venture-discovery  ──►  product-build  ──►  go-to-market
 Researcher, Scribe,     Claude, Codex, Fizz0,             Hermes, Researcher,
 Hermes (ranking)       Honey0, Pollen0                   Scribe
 GATE: joseleos picks    GATE: release candidate           GATE: joseleos approves
 the product             passes Honey0's suite             GTM plan, then content
```

## Skill 1 — `venture-discovery`

Goal: a ranked shortlist of problems in the target space that software
automation could solve, scored on four **separate** axes, and a one-page
decision memo so joseleos can pick one. The space is a parameter
(`research/spaces/<SPACE>.md`); the skill contains no space-specific content.

Four axes (from the brief), each 1–5:
1. **Effort to build** (inverse — lower effort scores higher)
2. **Value to the market**
3. **Ease of marketing** — scored with Scribe's 7-dimension rubric
   (`research/MARKETABILITY_RUBRIC.md`). Rule: *ease of marketing ≠ market size*.
   Market size belongs on axis 2 only.
4. **Our ability to build it** — lean AI-native team, no specialised
   engine, no procurement sales motion.

Per-candidate evidence Researcher must capture (Scribe's list): verbatim pain
quotes with URLs (3–5), budget holder + dollar authority, current workaround,
liability-analog touch (yes/no/assists), named incumbents + public pricing,
2–3 venues where the audience gathers, and sub-area tag.

Current state: two tracks scanned (`research/spaces/CIVIL_ENGINEERING.md`,
`research/spaces/ENTERPRISE_SPM.md`); memos pending. Other ventures' scans in
`research/prior-art/` are reference for method only. Exclusions live in each
space profile.

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
audience (role + segment + organisation size), the named incumbent/workaround
being replaced, and the verbatim quotes. Sequence: Hermes's GTM plan and
positioning are signed off by joseleos **first**; Scribe's campaign assets
**second**.

Channels are not hard-coded in the skill. They come from the space profile,
which must answer: native incentive the audience already needs (e.g.
continuing-education credit), associations/publications, peer communities,
search intent, events. Civil's list (PDH webinars first, PE societies, ASCE,
Eng-Tips, tutorial SEO) is the worked example in
`research/spaces/CIVIL_ENGINEERING.md`.

Exit: joseleos approves the campaign; assets live in `marketing/`, site in
`website/`.

## Repo

`xozai/xozai-venture` (this repo) holds skills, research, product, website, marketing.
One repo so cross-references (rubric → positioning → copy; architecture →
tests) are relative links, not hunts across accounts.

## Decision (joseleos, 2026-08-30)

Xozai and Jerry Project are **different ventures**. This repo and these skills
belong to Xozai; Skill 1 runs a fresh discovery pass here.
