# Phase 0 — Founder interview: Strata Civic Solutions

Skill: `.claude/skills/pitch-deck/SKILL.md` (Skill 5, merged PR #23).
Interviewer: Claude. Subject: joseleos. Started 2026-08-31 (Strata channel,
thread `440f6c9d…`). **Gate 0 = joseleos approves this summary.**

Six of the twelve standard questions are pre-filled from accepted artifacts
(each cites its source); joseleos corrects rather than re-answers those. The
other six are founder-only and are marked **OPEN — joseleos**.

## 1. Company — pre-filled, confirm
Strata Civic Solutions: municipal decision intelligence. AI over a city's own
published record (budgets, ordinances, minutes, contracts) with page-level
citations. Products: Ask Strata, Meeting Prep, City Snapshot. Delaware Public
Benefit Corporation, foreign-qualified in Texas; San Antonio, TX. Product is
built and live; demo city Schertz, TX.
Sources: stratacivicsolutions.com; `product/FINANCIAL_BRIEF_STRATA.md`.

## 2. Pain — pre-filled, confirm
Elected officials and appointed board members prepare for votes by Ctrl+F-ing
200–400-page packets and calling the clerk. No staff of their own. The record
that answers their questions is already public — it's just unusable at
meeting-prep speed. Errors of preparation play out on the record, in public.
Sources: `research/spaces/GOVTECH_MUNICIPAL.md`; `~/Documents/Strata_Market_Research.docx`.

## 3. Founder story — **OPEN — joseleos**
Why you, why this problem, what pulled you into municipal records?
(Skill won't accept a bio list — it wants the "why THIS founder wins THIS
problem" thread that the team slide will carry.)

## 4. Unfair advantage — **OPEN — joseleos**
What do you have that Ordinal AI's $1M seed can't buy quickly? (HermesX's
notes mention advisor insider access to Texas cities — confirm what's real
and what can be said on a slide. Cited-RAG accuracy? Relationships? Speed?)

## 5. Traction — **OPEN — joseleos** (partial pre-fill)
Known: product live; Schertz as demo city (not yet paying); 4 council
interviews done (HermesX note 2026-06-27); 90-day free pilot motion for first
5 cities planned. Needed from you: current usage numbers at Schertz, any
verbal commitments / LOIs / pipeline, pilot conversations in flight.
Anti-BS rule 4: every metric needs a rate or trend, not a bare number.

## 6. Competitors — pre-filled, confirm
AI-native: Ordinal AI ($1M seed, 7+ cities), ClerkMinutes, Aware,
CivicSummary. Incumbent suites shipping "good-enough" AI into installed
bases: CivicPlus, Granicus, OpenGov, Municode. The real incumbent: the manual
workaround (Ctrl+F + call the clerk). Full disclosure per anti-BS rule 3.
Source: `research/spaces/GOVTECH_MUNICIPAL.md`.

## 7. Business model — pre-filled, confirm
Annual subscription tiered by population: Starter $3,600 / Core $9,600 /
Growth $18,000; onboarding $500–1,500 (waived for pilots); usage bundled, no
per-seat fees. ACV held under the $50k competitive-bidding threshold. ~90%
gross margin at Core (COGS ≈ $75/city/mo, scales with packet volume).
Sources: GTM §4 pricing; `product/finance/strata/MODEL.md`.

## 8. Market size — pre-filled (bottom-up only), confirm
Beachhead: ~230 Texas cities 10k–50k pop × $9.6k Core ≈ **$2.2M SAM**;
1,224 TX municipalities total; base case captures ≈31 cities / ≈$325k ARR
run-rate by m36. Expansion beyond Texas is deliberately unmodeled — the deck
will state the beachhead honestly rather than invent a national TAM
(anti-BS rule 2). If you want a bigger stated market, Researcher runs a
bottom-up count of comparable tiers in neighboring states first.
Sources: `research/spaces/GOVTECH_MUNICIPAL.md`; `MODEL.md` base case.

## 9. Biggest risk — **OPEN — joseleos**
Candidates from the model and BMC (pick/rank/add): (a) cash — ≈$40k need vs
$10k opening; (b) founder bandwidth — sales motion caps at ~0.35 cities/mo;
(c) incumbents shipping good-enough AI into installed bases. Which one keeps
you up at night? Investors will ask; the risk onion needs your real answer.

## 10. Ask + use of funds — **OPEN — joseleos** (blocks the deck's spine)
The accepted model is **bootstrapped, no round in any scenario** — but a
pitch deck for institutional investors implies a raise. Which is it?
Options with model hooks:
- **Small round** (e.g. $150–300k pre-seed): kills the $40k cash constraint,
  pulls hiring forward — needs a financed scenario run (engine supports it).
- **Angel/F&F note** (~$50–75k): bridges the gap, deck stays traction-first.
- **No raise** — deck is for pilots/partners/grants, and the "ask" slide
  becomes pilot slots, not dollars. Skill still works; framing changes.
Whatever you pick, use-of-funds must trace to `MODEL.md` (anti-BS rules 8–9),
so a real raise number means a model re-run before Phase 4.

## 11. 3-year vision — **OPEN — joseleos**
Where is Strata in 2029? (Model says ≈31 TX cities / $325k ARR base,
≈71 cities / $651k upside — is the vision "the operating layer for small-city
governance," "every TX council member," multi-state, or something else?)

## 12. Anything else — **OPEN — joseleos**
Anything an investor should know that the documents don't capture.

---
## Update — 2026-09-01 (Scribe)

joseleos asked for the deck rather than answering the six open questions
(Strata channel, event `ef6afb97…`). Rather than block Gate 0, the deck was built from
accepted artifacts only, and the open questions were resolved as far as sourced evidence
allows:

- **Q3 founder story** — partially answered from the published team page via the 30 Aug
  research brief: Holly Richard, Founder/CEO, Doctor of Physical Therapy, previously built
  healthcare and fitness businesses. Her own account of *why municipal records* is still
  undocumented. **Still open.**
- **Q4 unfair advantage** — answered from the same source and now the deck's team slide:
  Ralph Gutierrez, Senior Municipal Advisor, two-term mayor and council member of Schertz
  (our demo city), ~50 years public service; Raquel Gutierrez, 30+ years Central Texas civic
  engagement. Distribution, not technology. **Closed on the evidence available.**
- **Q5 traction** — no verified pipeline exists in any artifact. The deck states "not
  disclosed" and carries no usage metric. **Still open.**
- **Q9 biggest risk** — ranked by Scribe from the model: execution (one founder, 0.35
  cities/mo, the −$29,069 month-18 trough) is the inner ring; incumbent good-enough AI is the
  outer. Overridable. **Answered by inference, flagged on the deck.**
- **Q10 ask** — resolved to the only figure the accepted model supports: **$40k of working
  capital plus five pilot cities**, use of funds traced to `MODEL.md` line items. An
  institutional round needs a financed model re-run. **Decision made, marked overridable.**
- **Q11 3-year vision** — the deck carries the model's own horizon (31 cities, ≈$325k ARR
  run-rate) and explicitly declines to draw a national TAM. **Answered conservatively.**

Also surfaced while building: the interview assumes joseleos is the founder, but the
published team page lists Holly Richard as Founder/CEO. The deck says nothing about
joseleos's role either way. Worth confirming.

---
## Prerequisite flags (carried to Gate 1)
- `Strata_GTM_Strategy.docx` is still a draft pending HermesX sign-off; the
  skill wants a signed-off GTM before Phase 1 foundation work hardens
  positioning. Phase 0 does not depend on it.
- `research/FINANCIAL_BENCHMARKS.md` has no govtech section — retention and
  COGS benchmarks remain tagged L; Researcher sanity-checks market sizing at
  Phase 3C.
