# Strata build / run estimate (Claude, 2026-08-30 — placeholder until Codex refines)

Codex is not a member of the Strata channel, so this is Claude's planning estimate from the
public product (stratacivicsolutions.com: Ask Strata, Meeting Prep, City Snapshot; Schertz
demo) and HermesX's 2026-06-27 note (domain live, Claude API in use, 4 council interviews).
Confidence **L** throughout. Feeds `rnd`, `cogs`, and the founder's deferred-comp memo line in
`assumptions.*.json`.

## Where the product is
Built and demoable for one city. The model therefore carries **no greenfield build**; the
founder's time is the R&D input and is deferred compensation ($0 cash) in every scenario.

## Hardening needed before paid multi-city use (founder time, months 1–6)
| Item | Why | Effort |
|---|---|---:|
| Per-city tenancy + admin console (users, roles, board seats) | 5–7 council members + boards per city; clerk as admin | 3–4 wk |
| Ingestion pipeline for agenda portals (CivicPlus / Granicus / Legistar exports, PDF upload) with re-ingestion on each new packet | Meeting Prep depends on fresh packets; manual ingestion does not scale past ~5 cities | 4–6 wk |
| Citation QA + eval set per city (answer must point to the right page) | Core promise; churn driver if wrong | 2–3 wk |
| Usage metering per city (queries, pages) | Bundled-token tiers still need caps and a COGS view | 1 wk |
| Audit log, backups, retention policy, security questionnaire answers | Insurance + IT review pre-conditions (see space profile) | 2 wk |
| Pilot signup page + onboarding flow (GTM §9 Q6) | Free-pilot CTA has nowhere to land | 1–2 wk |

≈ 3.5–4.5 founder-months alongside selling; the model buys 1 design contract ($4k, month 2) and
a third-party security review ($6k, month 14, before Growth-tier cities).

## Run cost (feeds `rnd` fixed floor and `cogs.per_active_logo_monthly`)
| Line | Base | Notes |
|---|---:|---|
| Fixed hosting floor (app, Postgres, object storage, vector index, monitoring) | $250/mo | managed services' minimum fees dominate at <10 cities |
| Dev tooling | $100/mo | GitHub, CI, error tracking, LLM eval |
| Per city per month (inference + retrieval + storage + re-ingestion) | $75 base / $60 upside / $110 downside | assumes hundreds to low thousands of cited queries per month per city, Sonnet-class model with citation retrieval, ~2 packets/month ingested; the 15k-query Core cap is a ceiling, not expected usage |

## What Codex should check when refining
Parse success and cost per packet on 10–20 real Texas agenda packets (several portals); actual
queries per official per month from Schertz; whether Meeting Prep briefs are generated per
agenda item (cost scales with items, not users).
