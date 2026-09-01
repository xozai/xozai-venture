---
title: "Marketability scores — enterprise SPM (discovery pass 1)"
author: Scribe
created: 2026-09-01
status: complete — fills the Marketability column in OPPORTUNITY_SCAN_SPM_2026-08-30.md
scored-with: research/SPM_RUBRIC_ADDENDUM.md (SPM anchors, NOT the civil anchors)
---

# SPM marketability scores

Scored against `research/SPM_RUBRIC_ADDENDUM.md`. Seven dimensions, 1–5, weighted
(named pain ×3, time-to-obvious ×3, **buying-committee friction** ×3, channel fit ×2,
liability drag inverse ×2, wedge narrative ×2, reference velocity ×1). Raw out of 80,
normalized to 100. Band map, same as the civil scan: **5** = 80+, **4** = 65–79,
**3** = 50–64, **2** = 35–49, **1** = under 35.

> **These numbers cannot be compared to the civil scores.** Addendum rule 2. A 5 means
> "best achievable in enterprise SPM," and enterprise SPM's ceiling is not civil's.
> Candidate A at 85 is **not** "better than UCM at 80." For the cross-track question,
> read the structural comparison at the end of this file — that is the output the
> addendum permits, and a side-by-side of the two numbers is the one it forbids.

## Scores

| Rank | # | Candidate | Pain ×3 | Obvious ×3 | Friction ×3 | Channel ×2 | Liability ×2 | Wedge ×2 | Refs ×1 | Raw | **Norm** | Band |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **A** | Comp analytics/reporting copilot | 4 | 5 | 4 | 4 | 5 | 4 | 3 | 68 | **85** | **5** |
| 2 | F | SPIF/contest management | 3 | 5 | 4 | 4 | 4 | 2 | 3 | 59 | **73.75** | 4 |
| 3 | **B** | Plan-config admin copilot | 4 | 5 | 2 | 3 | 3 | 4 | 2 | 55 | **68.75** | 4 |
| 4 | **D** | Dispute/inquiry AI explainer | 2 | 5 | 3 | 4 | 3 | 4 | 2 | 54 | **67.5** | 4 |
| 5 | H | Territory design optimizer | 2 | 5 | 2 | 4 | 4 | 2 | 3 | 50 | **62.5** | 3 |
| 6 | C | Cross-system reconciliation detector | 2 | 5 | 2 | 4 | 4 | 2 | 2 | 49 | **61.25** | 3 |
| 7 | G | Quota/capacity planning advisor | 2 | 2 | 2 | 4 | 3 | 2 | 2 | 38 | **47.5** | 2 |
| 8 | J | Core plan design & calc engine | 4 | 4 | 1 | 2 | 1 | 1 | 2 | 37 | **46.25** | 2 |
| 9 | E | Plan-document drafting + compliance | 2 | 3 | 1 | 2 | 1 | 4 | 1 | 33 | **41.25** | 2 |
| 10 | I | ASC 606 accrual automation | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 24 | **30** | 1 |

## Five things the scores say

### 1. A is the lead, and it is the only candidate whose pain evidence is real

A is the one candidate where an attributed practitioner names **our exact task** in their
own words. Helen R's *"Analytics is cumbersome and sometimes difficult to build required
reports without case statements"* is a headline as it stands — I could ship that on a
landing page tomorrow. Three reviewers, two incumbents, one complaint.

It scores pain 4 rather than 5 only because the addendum's 5 wants incumbent reviews
**plus** community threads naming the task, and Researcher cited reviews only. One
r/salesops or RevOps Co-op thread on ad hoc comp reporting moves it to 5.

A is also robust: pain 3 → 81.25, pain 5 → 88.75. **Band 5 across the whole range.** Its
rank does not depend on the one unknown.

### 2. B outranks D on my axis — reversing the scan's ordering

Researcher recommends "lead with A and D," with B a "credible third." On marketability
that ordering flips: **B 68.75 > D 67.5**, and the gap is entirely named pain (B: 4,
D: 2).

This is not a disagreement about the candidates. Researcher ranked on Effort and Value;
those are different axes and B's per-platform integration cost is real and belongs there.
On my axis the scan's own words decide it — D is *"the weakest direct hit in this scan,"*
with no direct dispute quote and vendor marketing standing in for buyer complaint. Named
pain carries ×3, so that costs D six raw points it cannot recover elsewhere.

**This is exactly the trap that bit the civil track's OPCC pick**: a candidate scoring
well on every dimension except the heaviest one, because *we* described the workflow.
D's "the analyst answers each inquiry by hand" is our summary of job postings and
dispute-handling blogs, not a comp analyst complaining.

D is the only candidate whose **band** moves on this unknown:

| Candidate | Floor (pain 1) | **Scored (pain 2)** | Ceiling (pain 5) |
|---|---|---|---|
| D | 63.75 → band 3 | **67.5 → band 4** | 78.75 → band 4, ahead of B |

So the targeted quote pass Researcher already flagged for D ("worth one more targeted
pass if D advances") is the highest-value research action on this track. It decides
whether D is second or fifth.

### 3. F at 73.75 is the rubric's own anti-pattern firing — do not read it as "pick F"

F (SPIF/contest management) is genuinely **easy to market**: a live leaderboard replacing
a spreadsheet is a one-frame demo, a SPIF budget is discretionary sales-manager money,
and the audience is squarely RevOps. It scores second.

It is also a category with **five named vendors already in it** (QuotaPath, Performio,
Bentega, Fullcast, Introw), which is why its wedge is a 2.

The base rubric warns about precisely this: *"Do not score an idea highly on marketability
because the market is big."* The mirror-image error is live here — F is easy to market
*into a fight we would enter sixth*. Marketability measures how hard my job is, not
whether the venture should exist. F's score is high and F is not the pick. Hermes should
weight the wedge, not the headline number.

### 4. E is quantified at 41.25 — the clean gap cannot rescue it

Researcher says explicitly not to lead with E. The scoring shows *why*, and it is not
close. E has the **best wedge in the set outside A/B/D** (4 — nobody drafts the document;
"replaces the Word template your GC redlines" names no unwinnable competitor), and it
still lands in band 2, because:

- **Friction 1** — HR plus Legal plus GC. The addendum's literal anchor-1 description.
- **Liability 1** — a legally binding wage document. Wrong is a wage-and-hour claim.
- **Refs 1** — no company will publicly say an AI wrote their comp plan.
- **Channel 2** — the buyer is comp/HR/legal, reachable through WorldatWork and the
  employment-law bar, **not** through the RevOps channels this track's plan is built on.
  Every other candidate reuses one channel set; E needs a second one built from scratch.

A good story cannot outrun three floor scores. Confirmed: don't lead with E.

### 5. The track has a ceiling no candidate can win back

Channel fit tops out at **4** and reference velocity at **3** across all ten candidates.
That is not ten coincidences — it is the property the addendum was written to expose.
There is no PDH equivalent in this market, and an enterprise logo needs comms sign-off.
Roughly five normalized points are unavailable to *any* SPM candidate before merit is
considered. Worth stating to Hermes so a 73 here is not read as a disappointing 73.

### AI-credibility check (addendum capture, feeds wedge)

Wedge capped at 3 where we cannot state in one concrete sentence what the AI does that
an incumbent cannot also say. **Passes:** A (no incumbent offers natural-language ad hoc
query), B (cuts the specialist-config cycle incumbents *sell as consulting*), D
(system-agnostic explain layer over someone else's engine), E (comp-specific
jurisdictional wage law). **Fails, capped:** C — reconciliation *is* every incumbent's
core integration pitch; F, G, H — Researcher's own read is that an LLM wrapper does not
change the buy; I, J — the contested middle where all thirteen already market AI.

## Cross-track structural comparison (prose only, per addendum rule 2)

joseleos's open question 3 is whether SPM is additive to civil or competing for the pick.
Not a number — the two tracks are different **kinds** of bet:

**Evidence runs opposite.** Civil/UCM has zero verbatim complaints after repeated
searches; my PR #26 argues we searched the wrong corpus, and that is still a hypothesis.
SPM candidate A had three attributed quotes on the first pass. On the dimension I weight
heaviest, SPM is evidenced **today** and civil is not.

**Distribution runs opposite.** Civil has a structural gift SPM cannot buy at any price:
PDH-credit webinars, where licensure makes engineers *want* to attend a vendor session.
In SPM we rent attention in a market where thirteen funded incumbents already spend.

**Competition runs opposite.** UCM has no software competitor at all — the scan found
consulting services and a free FHWA spreadsheet. A has no direct NL-query competitor
*yet*, but sits inside categories owned by thirteen funded vendors, and "natural-language
query over your comp data" is a feature they can ship, not a category they must build.

**So:** civil is a category-creation bet with strong distribution and unproven pain. SPM-A
is a proven-pain bet with a feature-gap wedge and no distribution advantage. The civil
risk is *"the pain isn't there."* The SPM risk is *"the pain is there and Xactly closes
the gap first."* Those fail differently, on different timelines, and PR #26 is the cheap
test that resolves the civil one.

If the tracks compete for a single pick, that is the trade. Ranking is Hermes's call and
the funding lever is joseleos's — I am supplying the axis, not the decision.

## What I still need before writing any SPM copy

The `go-to-market` gate applies to this track too. A clears gate item 3 (verbatim quotes,
sourced) — the only candidate on either track that does. Still missing for SPM: a named
audience at the addendum's precision (RevOps analyst at a company of what size, running
which incumbent), and `marketing/GTM_PLAN.md`, which does not exist for any track.
