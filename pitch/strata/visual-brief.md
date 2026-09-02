# Phase 4 — Visual brief: Strata Civic Solutions

Scribe, 2026-09-01. Per-slide spec. Implemented by `build_deck.py` (PPTX, 16:9 13.333×7.5in)
and mirrored in `deck.md` (Marp). 5-second test: one message per slide; if a reader needs
more than five seconds to name the point, the slide is wrong.

## Design system
Reuses the Strata deck system in `deckkit.py` (Scribe, 2026-08-30) so the pitch deck, the GTM
deck and the research deck read as one house.

- **Verdigris on civic navy** — `INK #16202E` ground, `ACCENT #1F7A6C` verdigris, `PAPER
  #F5F6F4` slide field, `FLAG #B3382E` for gaps and unresolved items only.
- **The strata motif** — three stacked rules of decreasing width. Cover, dividers, close.
- Helvetica Neue throughout; Menlo for placeholders so an unfilled slide is unmistakable.
- Every factual slide carries a 9pt source line at the foot. No slide without a source.
- Full-bleed navy is reserved for four moments: cover, the trust line, the risk slide, the ask.

## Slides

| # | Headline | Body | Visual | Notes / timing |
|---|---|---|---|---|
| 1 | Strata Civic Solutions — *Know the record before you vote.* | One line: AI over a city's own published record, cited to the page. | Navy full bleed, strata motif, no logo yet | Say the promise, then stop. **10s** |
| 2 | The packet is 300 pages. The vote is Tuesday. | Part-time official, full-time job, no staff of their own. | Three stat cards: 200–400pp packet · 0 staff · ~5:1 volunteers to officials | This is the whole pitch. Do not rush it. **45s** |
| 3 | They already tried the obvious fix. | Ctrl+F, then call the clerk. Free, universal, and the reason nobody has bought anything. | Two-column: "what they do now" vs "what it costs them" | Names the real incumbent early. **30s** |
| 4 | Your city already published the answer. | Nothing to migrate. The record exists; it is just unusable at meeting-prep speed. | Verbatim site quote, large, on paper | Site copy, quoted. **20s** |
| 5 | 2026 is the year cities wrote their AI policies. | The most common AI item on a council agenda is adopting an AI-use policy. Uncheckable answers are disqualified before they are evaluated. | Timeline strip: incumbents ship AI → cities write policy → citation-first becomes the adoptable form | Why-now slide. **35s** |
| 6 | Ask a question. See the page it came from. | Ask Strata · Meeting Prep · City Snapshot — each tied to an outcome, not a feature list. | Three cards, verdigris rules | No screenshots until we have approved ones. **50s** |
| 7 | An answer you cannot check is an answer you cannot use. | The vote, the discussion and the judgment stay exactly where they were. | Navy full bleed, single quote, nothing else | The emotional centre. Pause after. **25s** |
| 8 | One city manager can sign this. | $18,000 top tier against a $50,000 competitive-bidding threshold. Demo to signature: 4–8 weeks. | Threshold bar: tiers plotted under the §252.021 line | Procurement as product design. **40s** |
| 9 | Our senior advisor was mayor of our reference city. Twice. | Team as distribution, not credentials. | Four cards; **CTO card carries a visible FLAG placeholder** | Team placement per `story.md`. **50s** |
| 10 | Live product. One demo city. Zero paying customers. | Stated plainly, with dates. | Status grid: asset / status / date / source; unknowns in FLAG | Credibility comes from saying this first. **35s** |
| 11 | Everyone else built AI for the people who prepare the meeting. | Six named competitors and the workaround. | Full competitor grid with overlap column | Full disclosure, anti-BS rule 3. **60s** |
| 12 | $3,600 to $18,000 a year. 89% gross margin. | Population-tiered, no per-seat fees, annual invoice, sales-tax exempt buyer. | Three price tiers + margin/COGS callout | **30s** |
| 13 | 230 Texas cities in our tier. We counted them one at a time. | ≈$2.2M beachhead SAM. National frame shown for context and explicitly not modeled. | Nested bars: 230 tier cities ⊂ 1,224 TX municipalities ⊂ 19,519 US municipalities | Bottom-up only, rule 2. **40s** |
| 14 | Thirty-one cities and break-even in month 19 — on founder effort alone. | Base case; upside and downside in the appendix. Assumptions stated. | Model table: Y1/Y2/Y3 revenue, cities, operating income, ending cash | Numbers read from `MODEL.md`. **50s** |
| 15 | What kills us. | Cash trough, founder bandwidth, incumbent good-enough AI — inner ring named. | Risk onion, three rings, inner ring in FLAG | Never skip. Investors trust the deck that says it. **40s** |
| 16 | We do not need a round. We need $40,000 and five pilot cities. | Use of funds traced to `MODEL.md` line items. Alternative framings shown as an explicit open decision. | Navy full bleed; use-of-funds list; FLAG box for the open decision | **60s** |
| A1 | Scenarios | Base / upside / downside side by side | Engine metrics table | Appendix |
| A2 | Procurement mechanics | Statutes, thresholds, insurance, PIA | Grid | Appendix |
| A3 | Open items before this deck is shown | The six flags from Gate 1 | FLAG list | **Internal — pull before any external meeting** |

## Placeholder policy
Three slides carry visible `[ NEEDS JOSELEOS ]` blocks in Menlo/FLAG red: the CTO card
(slide 9), the founder-story line (slide 9), and the ask-framing decision (slide 16).
Slide A3 lists all six open items. They are deliberately ugly. A deck that quietly omits an
unknown is worse than one that shows where the hole is — and nobody will present a red
monospaced block by accident.
