# Public GitHub repos to accelerate the three skills

Researched 2026-08-30 in response to joseleos's ask in the Xozai channel. Scope:
find existing public repos that could plug into `venture-discovery`,
`product-build`, or `go-to-market` rather than building everything from
scratch. Every entry below was found via live search and is a real,
currently-indexed public repo — not a fabricated name. License is noted
where determinable; verify before vendoring code, especially anything
copyleft (AGPL/GPL).

**Honest gap up front:** I did not find an existing open-source tool that
does traffic-impact-study or utility-conflict-matrix automation directly —
Xozai's two live leads (TIS, UCM) have no prior art to borrow from. That
absence is itself informative (low competitive intensity, consistent with
the opportunity scan) but means product-build for either lead is closer to
greenfield than the boilerplate/extraction tooling below implies.

## 1. `venture-discovery`

| Repo | What it gives us | Plugs into | License |
|---|---|---|---|
| [Mohamedsaleh14/Reddit_Scrapper](https://github.com/Mohamedsaleh14/Reddit_Scrapper) | Scrapes Reddit threads and runs them through GPT to extract marketing pain points | Step 2.1 evidence gathering — automates part of the verbatim-pain-quote sweep (r/civilengineering) instead of manual search, which is the gap flagged in both venture's scans | Check repo (no LICENSE file confirmed at review time — verify before use) |
| [Decodo/Forum-scraper](https://github.com/Decodo/Forum-scraper) | General forum scraper (not Reddit-specific) + LLM sentiment/theme summarization | Same step — better fit for Eng-Tips and PE-society forums, which aren't Reddit | Check repo license before use |
| [QuantumNovice/awesome-civil-engineering](https://github.com/QuantumNovice/awesome-civil-engineering) | Curated index of civil-eng software/programming resources, actively maintained | Background scan input for step 1 (sub-area sweep) — a source of incumbent tools and discipline-specific software to check off against the "named incumbent" evidence field | CC0/unlicensed list-of-links repo (verify) |

Caveat on both scrapers: Reddit's 2026 "Responsible Builder Policy" tightened
scraping terms — treat bulk automation as a rate-limited assist, not a
replacement for the manual read the last scan already flagged as needed.

## 2. `product-build`

| Repo | What it gives us | Plugs into | License |
|---|---|---|---|
| [ixartz/SaaS-Boilerplate](https://github.com/ixartz/SaaS-Boilerplate) | Next.js + TypeScript + Postgres (Drizzle) + Auth + multi-tenancy + landing page + testing, already matches the skill's stated default stack | Stage A "Default stack" and Stage B M1 walking skeleton — could cut real setup time off M1 | MIT |
| [genieincodebottle/parsemypdf](https://github.com/genieincodebottle/parsemypdf) | Collection of PDF parsers (docling, Claude, OpenAI, Gemini, pdfplumber, pymupdf, unstructured-io) benchmarked for text/table/metadata extraction | Stage A data-model design for either TIS or UCM — both products fundamentally ingest source PDFs/CAD exports and need structured extraction | MIT (verify per sub-tool, some wrap paid APIs) |
| [opendatalab/MinerU](https://github.com/opendatalab/mineru) | Converts complex PDFs/DOCX/XLSX (tables, formulas, multi-column layouts) into LLM-ready markdown/JSON | Same stage — heavier-weight alternative to parsemypdf if source utility/traffic documents are scanned or have complex layouts | AGPL-3.0 — copyleft, do not vendor into a closed product without legal review; safe to use as a hosted/subprocess tool, not to fork code into the app |
| [datadrivenconstruction/OpenConstructionERP](https://github.com/datadrivenconstruction/OpenConstructionERP) | Open construction ERP with PDF/CAD/BIM takeoff → structured BOQ, AI cost-matching, 42 regional catalogues | Reference architecture only — the takeoff-from-CAD → structured-output pattern is directly analogous to what a UCM tool needs (utility plan → structured conflict table), even though this repo itself is cost estimation (excluded scope — that's Jerry's OPCC lane) | AGPL-3.0 — same caveat as above, read-only reference |
| [manuvarkey/GEstimator](https://github.com/manuvarkey/GEstimator) | Smaller Python/GTK+ civil estimation tool with rate-analysis logic | Domain-modeling reference only (how a civil tool structures line items/rates) — low direct reuse value for TIS/UCM | GPL-3.0 |

## 3. `go-to-market`

| Repo | What it gives us | Plugs into | License |
|---|---|---|---|
| [goabego/ai-gtm-playbook](https://github.com/goabego/ai-gtm-playbook) | 25-channel GTM playbook for AI startups, adapted from the Traction framework | Hermes's `marketing/GTM_PLAN.md` channel-sequencing step — a structured checklist to cross-check against the civil-specific hard-coded channel list (PDH webinars, ASCE, Eng-Tips, etc.) already in the skill | Check repo (content/playbook repo — verify reuse terms, likely fine to reference, not to copy verbatim) |
| [marketinguys/awesome-gtm-engineering](https://github.com/marketinguys/awesome-gtm-engineering) | Curated list of tools/frameworks for GTM automation, attribution, analytics, experimentation | Later execution tooling once `marketing/CALENDAR.md` exists — for tracking campaign performance across the PDH-webinar / newsletter / forum channels, not for the content step itself | List repo, unlicensed content — link only |
| [jeus0522/AI-Landing-Page-Generator](https://github.com/jeus0522/AI-Landing-Page-Generator) | Open-source AI landing-page generator, deploys to Vercel/Netlify | Sequence step 4 "Website" — build `website/` from Scribe's approved copy faster than hand-rolling | Check repo license before use |

## Recommendation

Highest-confidence, lowest-risk pick to actually adopt now: **ixartz/SaaS-Boilerplate**
(MIT, matches the skill's own default stack) for Stage A/B of `product-build`,
whichever lead (TIS or UCM) gets picked. The PDF-extraction repos
(parsemypdf, MinerU) are worth a spike once architecture names the actual
source-document formats for that lead — don't commit to one until then.
Everything else here is reference/inspiration, not a dependency to vendor.

No changes recommended to the skill files themselves — these are inputs to
cite during Stage A architecture and GTM planning, not replacements for the
playbook steps.

## 4. `pitch-deck` (new skill, added 2026-08-31)

joseleos asked for public repos with skills for startup financial modeling
and institutional-investor pitch decks (full survey posted in-channel
2026-08-30T23:50). Three were picked to act on:

| Repo | Verdict | License |
|---|---|---|
| [dkorobtsov/pitch-deck](https://github.com/dkorobtsov/pitch-deck) | **Vendored as the new `pitch-deck` skill.** Narrative-first, 6 gated phases, 10 anti-BS rules, CoVe verification with 4 critic personas, 7-test audit battery. No prior pitch-deck skill existed in this repo — pure addition, no conflict. | MIT — copyright notice preserved in `.claude/skills/pitch-deck/THIRD_PARTY_LICENSE` |
| [davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude/blob/main/plugins/venture-capital-intelligence/skills/financial-model/SKILL.md) (financial-model skill) | **Vendored as an optional v3 supplementary step, 2026-08-31 (joseleos sign-off).** Not a fork/replacement of the deterministic engine (CI-tested, live on UCM/Strata) — added as `.claude/skills/financial-model/scripts/valuation_triangulation/` (DCF + revenue-multiple + SaaS-health triangulation with HEALTHY/WATCH/CRITICAL verdicts), documented as an opt-in sanity-check step in `financial-model/SKILL.md`. Output writes to `product/finance/<venture>/triangulation/` and is explicitly barred from being pasted into `MODEL.md` — it isn't sourced/dated/confidence-tagged to that bar. Stage-default revenue multiples (Seed 10–15×, Series A 8–12×, Series B 5–8×) are the fallback when no sourced comparable exists. | MIT — copyright notice preserved in `.claude/skills/financial-model/THIRD_PARTY_LICENSE` |
| [w95/awesome-claude-corporate-skills](https://github.com/w95/awesome-claude-corporate-skills) | **Updated 2026-08-31, per joseleos's sign-off.** License confirmed MIT (checked via `gh api .../license`). Its `unit-economics` skill's benchmark bands (NDR, gross retention, LTV:CAC, CAC payback, Rule of 40, burn multiple) were folded into `financial-model` v3's health-verdict thresholds. Its `dcf-model`/`comps-analysis` skills were *not* used — they target public-equity analysis (SEC filings, stock price, shares outstanding) and explicitly disclaim pre-revenue startups as out of scope; not a fit for this repo's private 3–5yr venture models. | MIT |

Full research writeup with all 9 candidates: posted in the Xozai channel,
event `1864ff840bdaca1b51275a0e7028d4ccb60217502b3e523d72f14a7f40f234a3`.
