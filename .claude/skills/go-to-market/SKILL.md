---
name: go-to-market
description: >
  Take the shipped product to market in any space. Hermes owns the GTM plan and
  positioning, Researcher supplies marketing research, Scribe produces campaign
  content. Gated: no copy until audience, replaced incumbent, and verbatim
  quotes exist. Channels come from the space profile, not from this skill.
version: 2
---

# Skill 3 — Go-to-market

## When to run
After `product-build` tags a release candidate (M3) — GTM planning can overlap
the fix loop; content production waits for real screenshots.

## Inputs
- `research/spaces/<SPACE>.md` — channels, buyer archetypes, venues.
- The discovery evidence for the picked candidate (quotes, workaround,
  incumbents, pricing) from `research/`.
- `product/ARCHITECTURE.md`, screenshots, acceptance criteria from `product-build`.
- `research/SKILL_SOURCES.md` — generic GTM playbooks and tooling to cross-check
  the plan against.

## Roles
| Who | Does |
|---|---|
| Hermes | GTM plan, positioning, pricing recommendation, channel sequencing |
| Researcher | Any research Hermes requests: audience sizing, incumbent pricing, venue lists, quote collection |
| Scribe | All campaign content: site copy, emails, event/talk outline, social, one-pager |
| Claude | Orchestrator; builds `website/` from Scribe's copy with Codex/Fizz0 if needed |
| joseleos | Signs off the GTM plan, then the content |

## Gate — do not draft content until all three exist
1. **Named audience**: role + segment + organisation size (e.g. "<role> at
   <size>-person <type of organisation>"). Not "SMBs", not "professionals".
2. **The named incumbent or workaround being replaced** (e.g. "the spreadsheet
   you re-key from <system> every <cadence>").
3. **Verbatim pain quotes** with sources, from `research/`.
Copy written without these is filler. Hermes confirms the gate is met in the
channel before Scribe starts.

## Sequence (order is mandatory — reversed, everything gets rewritten)
1. **Research brief** — Hermes lists questions; Researcher answers in
   `marketing/RESEARCH_<topic>.md` with URLs.
2. **GTM plan** — Hermes writes `marketing/GTM_PLAN.md`: audience, positioning
   statement, wedge narrative (one sentence, names no unwinnable competitor),
   pricing, channel plan with sequencing and budget, 90-day targets, metrics.
   joseleos signs off. Record in `docs/DECISIONS.md`.
3. **Content** — Scribe produces from the approved plan into `marketing/content/`:
   - Landing page copy (headline from a verbatim quote, before/after in one
     screenshot).
   - Launch email sequence (3 emails).
   - One educational-event asset in the space's native format (webinar,
     workshop, talk, live demo): title, abstract, outline.
   - One community/newsletter blurb for the space's associations or
     publications, 2 forum-appropriate posts, 5 social posts.
   - One-pager PDF copy.
4. **Website** — Claude/Codex build `website/` from the landing copy; deploy
     preview; Scribe reviews rendered copy.
5. **Sign-off** — joseleos approves; campaign calendar in `marketing/CALENDAR.md`.

## Channels
Take the channel list from `research/spaces/<SPACE>.md`. The profile must
answer, for this audience:
- **Native incentive** — is there something this audience already needs
  (continuing-education credit, certification, compliance updates, tooling
  tutorials) that a vendor can legitimately supply? Lead with that; it is the
  highest-leverage top-of-funnel motion wherever it exists.
- **Associations and publications** — professional societies, trade bodies,
  newsletters, trade press.
- **Peer communities** — forums, subreddits, Slack/Discord groups, Q&A sites.
  Follow community rules; lead with the workaround story, not the product.
- **Search intent** — "how do I do X in <incumbent tool>" content and SEO.
- **Events** — the 2–3 conferences or meetups this sub-area actually attends.
If the profile's channel section is empty, Hermes sends Researcher a brief to
fill it before writing the plan. Generic GTM playbooks (see
`research/SKILL_SOURCES.md`) are a checklist, not a substitute.

## Outputs
- `marketing/GTM_PLAN.md`, `marketing/RESEARCH_*.md`, `marketing/content/*`,
  `marketing/CALENDAR.md`, `website/`.

## Anti-patterns
- Positioning as "a better <incumbent>".
- Content before plan sign-off.
- Paraphrasing the quotes.
- Treating market size as a marketing argument.
- Copying another space's channel list because it worked there.
