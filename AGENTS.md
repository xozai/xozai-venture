# Agent conventions for this repo

## Roles (fixed by the pipeline owner, joseleos)

| Agent | Role |
|---|---|
| Claude | Orchestrator; senior engineer in Skill 2 |
| Codex | Junior engineer in architecture; builder; bug triage in Skill 2 |
| Researcher | Discovery research (Skill 1); marketing research (Skill 3) |
| Scribe | Marketability axis owner (Skill 1); campaign content (Skill 3) |
| Hermes (bot 4124af96…; brief said "HermesX", which is a member account e1765f6b…) | Go-to-market plan and positioning (Skill 3) |
| Fizz0 | Implementation (Skill 2) |
| Honey0 | Test cases and test execution (Skill 2) |
| Pollen0 | Bug fixes (Skill 2) |

## Working rules

- Read the relevant `.claude/skills/*/SKILL.md` before acting in that stage.
- Work in a branch/worktree, never directly on `main`. Open a PR; Claude or Codex reviews.
- Every artifact goes in the directory the skill names. Do not scatter docs.
- Cite sources: research claims carry URLs; engineering claims carry file paths or test output.
- Commit author: the accountable human (joseleos). Agents that materially authored code add `Co-authored-by`.
- Coordination happens in the Buzz `Xozai` channel (`63a6c63a-4c04-4339-b140-90f49453a1c8`). Xozai is a separate venture from the Jerry Project (channel `449a9d80-…`); do not mix their artifacts or decisions.
