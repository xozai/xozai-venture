---
name: pitch-deck
description: >
  Produce and stress-test an investor-grade pitch deck for a venture raising
  from institutional investors. Narrative-first: story before slides, writing
  before design. Gated phases, each requiring joseleos's approval. Draws on
  `financial-model`'s MODEL.md and `go-to-market`'s GTM_PLAN.md as inputs
  rather than re-deriving numbers or positioning.
version: 1
---

# Skill 5 — Pitch deck

Methodology adapted from [dkorobtsov/pitch-deck](https://github.com/dkorobtsov/pitch-deck)
(MIT license, copyright notice preserved in `THIRD_PARTY_LICENSE`) —
narrative-first phase-gate structure, anti-BS rules, and the 7-test audit
battery are reused near-verbatim from that plugin's `AGENTS.md` and
`commands/create.md`/`commands/audit.md`; the roles, inputs, and gates below
are adapted to this repo's convention (see `research/SKILL_SOURCES.md`
entry 4). `assets/theme.css` and `references.md` are vendored unmodified from
the same source for Phase 5 slide rendering and deeper framework detail
(Onion Theory, Seven Moats, Traction Rules).

## When to run
After `financial-model` has an accepted `MODEL.md` and `go-to-market` has a
signed-off `GTM_PLAN.md` — a pitch deck built before either exists will
either invent numbers or contradict them later. Re-run `/audit` alone anytime
an existing deck needs a stress test before an investor meeting.

## Inputs
- `product/finance/<VENTURE>/MODEL.md` + `model.xlsx` — financials, ask
  sizing, use-of-funds must trace to the accepted model, not be re-invented.
- `marketing/GTM_PLAN.md` — positioning, wedge narrative, channel plan.
- Discovery evidence in `research/` — pain quotes, incumbents, market sizing
  inputs (bottom-up only, per Anti-BS Rule 2 below).
- `docs/DECISIONS.md` — funding plan, scenario picked, any joseleos overrides.
- Founder/team background — Claude interviews joseleos directly (Phase 0).

## Roles
| Who | Does |
|---|---|
| Claude | Orchestrates all 6 phases, runs the founder interview, assembles the deck, applies CoVe |
| Researcher | Investor-target research (Phase 3C), market-sizing sanity check against `research/FINANCIAL_BENCHMARKS.md` |
| Scribe | Headline and body copy pass (Phase 2), tone/brand consistency |
| Hermes | Reviews positioning slides against `GTM_PLAN.md` for contradiction |
| joseleos | Founder interview subject; approves every phase gate; owns the final deck |

## Anti-BS rules (never violate)
1. No "revolutionary"/"game-changing" language — show, don't hype.
2. No unsubstantiated market sizes — bottom-up only, sourced from `research/`.
3. Never claim "no competition" — full disclosure, always.
4. Every metric needs context (rate/trend, not a bare absolute number).
5. No vanity metrics without a stated business impact.
6. Team slide answers "why THIS team wins THIS problem," not a bio list.
7. No feature lists — capabilities tied to outcomes only.
8. Financial projections state their assumptions explicitly (link to `MODEL.md`).
9. The ask is specific: amount, use of funds, milestones it unlocks.
10. Every slide earns its place — cut ruthlessly.
11. Never invent a metric. Unknown → "needs verification" or omit; the deck
    must not assert anything `MODEL.md` or `research/` doesn't support.

## Sequence — 6 gated phases (never skip a gate)
0. **Founder interview.** Claude asks the 12 standard questions one at a
   time (company, pain, founder story, unfair advantage, traction,
   competitors, business model, market size, biggest risk, ask + use of
   funds, 3-year vision, anything else). Save to `pitch/<VENTURE>/interview.md`.
   **Gate 0**: joseleos approves the summary.
1. **Foundation.** Business audit (pain / inevitable future / blockers /
   solution / hard+soft value), investor psychology map (reasons to invest,
   reasons not to, moat analysis, risk onion), traction narrative, team
   assessment, competitive positioning — cross-checked against `GTM_PLAN.md`
   and `MODEL.md` so nothing here contradicts the accepted model.
   Save to `pitch/<VENTURE>/foundation.md`. **CoVe pass** (skeptical VC,
   domain expert, storyteller, first-time reader). **Gate 1**: joseleos
   approves strategy.
2. **Story.** 30-second commercial (3-4 versions), slide budget with a
   team-placement decision (founder-led vs. product-led — document the
   reasoning), 20-headline narrative that must read as a complete story with
   no body text, minimal body copy per slide (Scribe pass). Save to
   `pitch/<VENTURE>/story.md`. **CoVe pass** (read headlines aloud test).
   **Gate 2**: joseleos approves the narrative.
3. **Objections.** 15+ hardest investor questions with appendix answers;
   investor-targeting notes if specific investors are named (Researcher
   pulls their last 6-10 investments and thesis). Save to
   `pitch/<VENTURE>/objections.md`. **Gate 3**: joseleos approves.
4. **Design brief.** Per-slide spec: headline, body (if any), visual
   suggestion, speaker notes, timing — 5-second-test compliant (one message
   per slide, readable or intentionally decorative text only). Save to
   `pitch/<VENTURE>/visual-brief.md`. **Gate 4**: joseleos approves.
5. **Slides.** Render as Marp markdown + PDF, using the theme and slide
   classes (`lead`, `invert`, `big-number`, `quote`, `comparison`, `light`)
   from the source plugin's `assets/theme.css`, copied into
   `pitch/<VENTURE>/theme.css`. Financials slide(s) pull numbers directly
   from `model.xlsx`/`MODEL.md` — never re-typed by hand. Save to
   `pitch/<VENTURE>/deck.md`, build to `pitch/<VENTURE>/deck.pdf`. Final
   review with joseleos.

## Audit (standalone, run anytime)
Given an existing `deck.md`/`.pdf`, run the 7-test battery: headlines-tell-
the-story (most important — an investor should want a meeting from headlines
alone), team placement, 5-second test per slide, narrative arc, anti-BS
check, investor psychology (partner talking points, risk onion visibility),
structural completeness. Output PASS/WEAK/FAIL per test with evidence, grade
A-F, to `pitch/<VENTURE>/audit.md`.

## Exit
joseleos accepts `deck.pdf` in-channel. Record the accepted version and any
overrides in `docs/DECISIONS.md`. Update `pitch/<VENTURE>/objections.md`
after every real investor meeting — it is a living arsenal, not a one-time
artifact.

## Rules
- Never touch slides before the narrative (Phase 2) is approved.
- Numbers on the deck must trace to `MODEL.md`; if the two disagree, fix the
  deck, not the model, and check whether the disagreement means the model
  needs a re-run.
- Space-specific evidence stays in `research/spaces/<SPACE>.md`; this skill
  only assembles and narrates it.
- Branch + PR for every artifact; Claude reviews.
