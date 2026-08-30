---
title: "Pre-sweep marketability brief — aiming the Xozai discovery pass"
author: Scribe
created: 2026-08-30
status: active
audience: Researcher (before the sweep), Hermes (before ranking)
---

# Why this exists

The Xozai exclusion (OPCC exhibits, MUTCD traffic-control plans — `docs/DECISIONS.md`,
2026-08-30) removed the two candidates that scored **highest on the marketing axis** in
the prior-art scan. That is not a coincidence and it changes how the sweep should be run.

From `research/prior-art/JERRY_PROJECT_OPPORTUNITY_SCAN_2026-08-30.md`, the marketability
column reads:

| Rank | Candidate | Marketability |
|---|---|---|
| 1 | OPCC / cost-estimate exhibits | **High** ← excluded |
| 2 | Traffic control plans (MUTCD) | **Med-High** ← excluded |
| 3 | Geotechnical boring logs | Medium |
| 4 | SWPPP / stormwater compliance | Medium |
| 5 | Structural calc packages | Low-Med (liability drag) |
| 6 | Stormwater / hydrology design | Low (entrenched, jurisdiction lock-in) |
| 7 | Earthwork / quantity takeoff | Medium |
| 8 | Permitting automation | Low (procurement / govtech-adjacent) |
| 9 | Drawing review / RFI | Medium |

**Nothing left in the known set rates above Medium.** So if the Xozai sweep re-ranks
candidates 3–9, the top of our table will be structurally weak on my column, and we
will only find that out after the sweep is done. The sweep has to find genuinely new
candidates, not recycle the leftovers.

That is not an argument against reconsidering 3–9. It is an argument for not letting
them be the *default* answer because they are the ones already written down.

# What a 5-on-marketability candidate looks like

Aim the search at this shape. A candidate matching all six will score high on the rubric
before we score it, because the rubric is measuring these properties.

1. **Recurring deliverable, produced many times per project** — ideally at every design
   milestone or every submittal. Frequency is what turns an annoyance into named pain.
2. **Output is not stamped and carries no design liability.** This single property is the
   difference between a product we can sell in month three and one that needs validation
   studies, insurer conversations, and a reputation we do not have yet.
3. **The current workaround is a self-built spreadsheet or a manual process — not a named
   incumbent tool.** See below; this is the highest-signal field in the whole sweep.
4. **Buyer is the user, at a private firm, purchasable on a card.** Not an agency. Agencies
   bring procurement cycles *and* cannot give us a public reference, which costs us on two
   separate rubric dimensions at once.
5. **Before/after fits in one screenshot.** If the value only shows up after weeks of use,
   or depends on trusting a calculation the user cannot see, every piece of content has to
   do explanatory work before it can do persuasive work.
6. **Engineers already complain about it publicly, unprompted.** We want to find the
   complaint, not manufacture it.

# The one field that predicts the most

For each candidate, capture explicitly:

> **Is the current workaround a named commercial tool, or something the firm built itself?**

Self-built spreadsheet / manual process → the wedge is *"it replaces the thing you built
yourself,"* which names no competitor, starts no fight, and flatters the user. Named
incumbent → the wedge becomes *"better than X,"* which is a comparison we have to win on
the incumbent's terms, against their sales team and their install base.

This one distinction drives three rubric dimensions at once (named pain, wedge narrative,
and effectively channel fit, since incumbents tend to own the channels too). It is nearly
free to capture during the sweep and expensive to reconstruct afterward.

# Where unprompted complaints actually live

The evidence type we are shortest on is verbatim, unprompted pain. Places it surfaces:

- **Eng-Tips forums** and **r/civilengineering** — the two highest-yield sources.
- **YouTube comments on tutorial videos.** People who searched "how do I do X in Civil 3D"
  and are annoyed enough to comment have self-identified both the pain and the workaround.
- **State PE society forums and newsletters.**
- **Job postings.** Underused: when firms post EIT roles whose listed duties include
  "prepare/compile/update <deliverable>," that is budget already flowing to a manual task,
  stated in the firm's own words. It is a demand signal and a pain description at once.

# Note for whoever scores the axis

Discipline tag must be present before channel fit can be scored — the channel set is
discipline-specific and there is no generic answer. This is already in the skill; repeating
it because it is the step most likely to get skipped when a candidate looks obvious.
