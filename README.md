# Xozai venture — software startup

Monorepo for the Xozai startup pipeline (a venture separate from the Jerry Project): the agent skills that
run the pipeline, the research that feeds it, and everything the team produces
(product, website, marketing).

| Path | What lives here |
|---|---|
| `.claude/skills/venture-discovery/` | Skill 1 — find and rank problems worth solving |
| `.claude/skills/product-build/` | Skill 2 — architecture → build → QA → bug-fix loop |
| `.claude/skills/go-to-market/` | Skill 3 — GTM plan, marketing research, campaign content |
| `docs/PLAN.md` | The pipeline plan: roles, stage gates, artifacts |
| `research/` | Discovery outputs; `research/spaces/` holds one profile per target space (the skills are space-agnostic); `research/prior-art/` holds other ventures' scans as reference only |
| `product/` | The selected product's source code |
| `website/` | Marketing site |
| `marketing/` | GTM plan, positioning, campaign content |

Start with `docs/PLAN.md`. Each skill's `SKILL.md` is a self-contained playbook
an orchestrating agent can follow from the Buzz `Xozai` channel.
