"""Generate product/finance/strata/assumptions.{base,upside,downside}.json for the
xozai-venture financial-model engine (schema 1.0.0).

Every leaf carries value/unit/source/date/confidence/override/kind per SKILL.md step 3.
Run: python3 strata_assumptions.py <outdir>
"""
import json, sys, copy

D = "2026-08-30"
RESEARCH = "~/Documents/Strata_Market_Research.docx (Researcher, 2026-08-29)"
GTM = "~/Documents/Strata_GTM_Strategy.docx (HermesX, 2026-08-29, draft pending sign-off)"
JOSE = "joseleos in Strata channel 2026-08-30 04:47 (event d9d225ef)"
ASSUME = "assumption"


def a(value, unit, source, conf, kind, date=D):
    return {"value": value, "unit": unit, "source": source, "date": date,
            "confidence": conf, "override": None, "kind": kind}


def cost(name, amount, cadence, start, end, source, conf, kind="benchmark"):
    return {
        "name": a(name, "text", source, conf, "input"),
        "amount": a(amount, "USD", source, conf, kind),
        "cadence": a(cadence, "cadence", source, "H", "input"),
        "start_month": a(start, "month", source, conf, "input"),
        "end_month": a(end, "month", source, conf, "input"),
    }


def person(role, headcount, start, end, base, founder, defer, source, conf):
    return {
        "role": a(role, "text", source, conf, "input"),
        "headcount": a(headcount, "FTE", source, conf, "input"),
        "start_month": a(start, "month", source, conf, "input"),
        "end_month": a(end, "month", source, conf, "input"),
        "annual_base": a(base, "USD/yr", source, conf, "benchmark"),
        "employer_tax_pct": a(0.09, "ratio", "FICA 7.65% (irs.gov Topic 751) + FUTA 0.6% + TX SUTA new-employer 2.7% on first $9k (twc.texas.gov) ≈ 9% blended", "M", "benchmark"),
        "benefits_pct": a(0.12, "ratio", ASSUME + ": small-employer health + 401k match, no equity accounting", "L", "benchmark"),
        "equipment": a(2500, "USD one-time", ASSUME + ": laptop + peripherals", "M", "benchmark"),
        "founder": a(founder, "bool", source, "H", "input"),
        "defer_until_funding": a(defer, "bool", "docs/FINANCIAL_MODEL_PLAN.md answers 2026-08-30 (founder pay deferred until funding) — carried over to Strata pending confirmation", "M", "input"),
    }


def build(scenario):
    s = scenario
    # ---- revenue drivers per scenario (from FINANCIAL_BRIEF_STRATA.md scenario table)
    rev = {
        "base":     dict(new=0.35, growth=0.05, churn=0.006, acv=9600,  exp=0.05, conf="L"),
        "upside":   dict(new=0.50, growth=0.07, churn=0.004, acv=11000, exp=0.08, conf="L"),
        "downside": dict(new=0.20, growth=0.03, churn=0.012, acv=7200,  exp=0.02, conf="L"),
    }[s]
    # Hiring rule (brief): hire only after gross-margin cash covers the loaded cost.
    # Loaded FTE engineer ≈ $13.1k/mo ⇒ needs ≈18 paying Core cities; contractor first.
    contractor = {"base": (13, 27), "upside": (7, 15), "downside": (0, 0)}[s]
    hire_eng = {"base": 28, "upside": 16, "downside": 0}[s]      # 0 = never
    hire_cs = {"base": 0, "upside": 25, "downside": 0}[s]
    events_y2 = {"base": 3, "upside": 4, "downside": 2}[s]

    formation = [
        cost("Delaware C-Corp formation (Clerky/Stripe Atlas incl. 83(b), IP assignment)", 800, "one_time", 1, 1,
             "stripe.com/atlas ($500) / clerky.com (~$800 formation + post-incorporation); HermesX wiki note 2026-06-27 says C Corp already forming — may already be spent", "M"),
        cost("Delaware registered agent", 150, "annual", 1, 36, "delawareregisteredagent.com / harvardbusiness services $50–$300/yr range", "M"),
        cost("Delaware franchise tax + annual report (assumed-par-value minimum)", 450, "annual", 6, 36, "corp.delaware.gov: $400 min tax (assumed par value method) + $50 report fee", "H"),
        cost("Texas foreign qualification (Form 301)", 750, "one_time", 1, 1, "sos.state.tx.us fee schedule: $750 foreign for-profit corporation registration", "H"),
        cost("Municipal pilot agreement + MSA/DPA templates (counsel)", 2500, "one_time", 1, 1, ASSUME + ": GTM open question #3 says pilot agreement not yet drafted; municipal data terms + TX Public Information Act clauses", "L"),
        cost("Trademark filing (USPTO 1 class + counsel)", 1350, "one_time", 6, 6, "uspto.gov: $350/class electronic filing fee (2025) + ~$1,000 counsel", "M"),
        cost("Financing counsel reserve", 0, "one_time", 1, 1, "Bootstrapped base case per joseleos (minimal budget until revenue or investment) — $0; add on override if a SAFE is raised", "H", kind="input"),
    ]
    ga = [
        cost("Bookkeeping + accounting (outsourced)", 300, "monthly", 1, 36, ASSUME + ": Bench/Pilot starter tiers $300–$700/mo; low end while transactions are few", "M"),
        cost("Annual tax prep (federal 1120 + DE + TX franchise no-tax-due report)", 2000, "annual", 12, 36, ASSUME + ": small C-Corp return $1.5–2.5k; TX franchise tax no-tax-due threshold $2.47M (comptroller.texas.gov)", "M"),
        cost("Insurance: cyber liability $1M + tech E&O + GL", 3600, "annual", 1, 36, ASSUME + ": early-stage SaaS packages (Vouch/Embroker) $2–5k/yr; TX cities commonly require a certificate of insurance before pilot data access", "L"),
        cost("Software seats + domain + email + banking", 120, "monthly", 1, 36, ASSUME + ": Google Workspace, 1Password, Mercury (free), domain — per active person", "M"),
        cost("Payroll provider (Gusto) — starts with first paid employee", 60, "monthly", hire_eng if hire_eng else 37, 36, "gusto.com Simple plan $40/mo + $6/person", "H"),
        cost("Remote stipend / coworking", 0, "monthly", 1, 36, JOSE + " — minimal budget; $0 until funded", "H", kind="input"),
    ]
    rnd = [
        cost("Hosting: app + Postgres + object storage + vector index + monitoring (fixed floor)", 250, "monthly", 1, 36, ASSUME + ": Vercel/Railway + managed Postgres + S3-class storage; per-city variable cost is in COGS", "M"),
        cost("Dev tooling (GitHub, CI, error tracking, LLM eval)", 100, "monthly", 1, 36, ASSUME, "M"),
        cost("Security review + SOC2-lite readiness (pen test, policies) before Growth-tier cities", 6000, "one_time", 14, 14, ASSUME + ": 50K+ cities and TX DIR-style questionnaires expect a third-party review; single vendor pen test $4–8k", "L"),
        cost("Contract design/UX (pilot onboarding flow, City Snapshot polish)", 4000, "one_time", 2, 2, ASSUME + ": product already live (stratacivicsolutions.com, Schertz demo); hardening not greenfield — see product/finance/strata/BUILD_ESTIMATE.md", "L"),
    ]
    sm = [
        cost("TML Annual Conference exhibitor booth (Nov 11–13, San Antonio)", 3000, "one_time", 2, 2, RESEARCH + " + " + GTM + " (Week 1: register booth); fee not yet quoted by TML — GTM open question #1", "L"),
        cost("TML booth travel, lodging, collateral, demo hardware", 1500, "one_time", 2, 2, ASSUME + ": 2 nights San Antonio + printed one-pagers + banner", "M"),
        cost("TML Region meetings / TCMA regionals (travel, per event)", 300, "monthly", 1, 12, RESEARCH + " §5.3 event calendar (Sep 2 Region 8, Sep 9 Small City, Sep–Oct TCMA) — ~1 event/mo year 1", "M"),
        cost("Year-2/3 conferences (TML, TCMA, ELGL) incl. travel", 4500 * events_y2 / 3, "annual", 14, 36, ASSUME + f": {events_y2} events/yr at ~$4.5k all-in", "L"),
        cost("Website hosting, pilot signup form, CRM (HubSpot free → Starter)", 100, "monthly", 1, 36, GTM + " §9 open question #6 (pilot signup page needed) + HubSpot Starter ~$20–50/seat", "M"),
        cost("Content + LinkedIn (Scribe-drafted, organic, no paid media year 1)", 0, "monthly", 1, 12, JOSE + " — minimal budget; organic only per GTM §5", "H", kind="input"),
        cost("Paid LinkedIn / sponsored ELGL / GovTech placement (year 2+)", 750, "monthly", 13, 36, ASSUME + ": light paid targeting once testimonials exist (GTM §5 sequencing)", "L"),
        cost("Pilot onboarding cost (document ingestion labor/tooling per pilot city, ~1.5 pilots/mo year 1)", 200, "monthly", 1, 12, ASSUME + ": GTM §4.1 waives the $1,000 onboarding fee for pilots; ingestion is mostly automated", "L"),
    ]
    roster = [
        person("Founder / CEO + product (joseleos)", 1, 1, 36, 150000, True, True, JOSE + "; base is memo-only (deferred) per FINANCIAL_MODEL_PLAN answer #2", "M"),
    ]
    if contractor[0]:
        c = person("Contract full-stack engineer, 0.5 FTE (1099; no payroll burden)", 1, contractor[0], contractor[1], 72000, False, False,
                   ASSUME + ": ~$12k/mo full-time-equivalent US contractor rate at half time; ends the month before the FTE hire", "M")
        c["employer_tax_pct"] = a(0.0, "ratio", "1099 contractor — no employer payroll tax", "H", "input")
        c["benefits_pct"] = a(0.0, "ratio", "1099 contractor — no benefits", "H", "input")
        c["equipment"] = a(0, "USD one-time", "contractor supplies own equipment", "H", "input")
        roster.append(c)
    if hire_eng:
        roster.append(person("Full-stack engineer, FTE (hired once gross-margin cash covers ≈$13.1k/mo loaded cost ≈ 18 paying Core cities)", 1, hire_eng, 36, 130000, False, False,
                             ASSUME + ": Texas remote senior full-stack $120–150k base (levels.fyi/BuiltIn Austin 2025 ranges); timing rule from FINANCIAL_BRIEF_STRATA.md", "M"))
    if hire_cs:
        roster.append(person("Customer success / onboarding + Texas field sales (ex-city staff)", 1, hire_cs, 36, 85000, False, False,
                             ASSUME + ": TX municipal-experienced CS/AE base $75–95k; timing rule from brief", "L"))

    cogs = {
        "revenue_pct": a(0.03, "ratio", ASSUME + ": support tooling + occasional card fees (most cities pay by ACH/check; TX municipalities are sales-tax exempt)", "L", "benchmark"),
        "per_active_logo_monthly": a({"base": 75, "upside": 60, "downside": 110}[s], "USD/city/month",
                                     ASSUME + ": LLM inference (Claude API) + retrieval + storage per city at realistic usage (hundreds to low thousands of cited queries/mo, not the 15K/mo Core cap) + re-ingestion of new packets; scenario-varied like Codex's UCM per-user API envelope (product/finance/ucm/BUILD_ESTIMATE.md)", "L", "benchmark"),
    }
    revenue = {
        "starting_logos": a(0, "paying cities", RESEARCH + " §1: Schertz is a live demo/pilot city, not disclosed as paying — counted as $0 ARR at start", "M", "input"),
        "new_logos_monthly": a(rev["new"], "paying cities/month (month-1 rate)", GTM + " §8: 15 demos → 5 pilots → 1 paid contract by day 90; base 0.35/mo ≈ 5–6 paid cities in year 1", rev["conf"], "derived"),
        "new_logo_growth_monthly_pct": a(rev["growth"], "ratio/month", ASSUME + ": compounding from testimonials + TML pipeline; base 5%/mo ⇒ ≈34 paying cities cumulative by month 36 (≈15% of the ~230-city beachhead)", rev["conf"], "derived"),
        "monthly_logo_churn_pct": a(rev["churn"], "ratio/month", ASSUME + ": public-sector SaaS gross logo retention typically 90–95%/yr (vendor-reported; no independent source yet) ⇒ 0.4–1.2%/mo", "L", "benchmark"),
        "acv": a(rev["acv"], "USD/city/year", GTM + " §4 pricing table: Starter $3,600 / Core $9,600 / Growth $18,000; base = Core (beachhead tier), upside = Core-heavy mix with some Growth, downside = discounting to ~$600/mo", "M", "input"),
        "annual_expansion_pct": a(rev["exp"], "ratio/year", GTM + " §3.2: boards & commissions add-on and tier upgrades as cities grow", "L", "derived"),
        "billing_terms_months": a(12, "months billed upfront", RESEARCH + " §6: annual license; engine v1 recognizes ratably and does not yet model upfront cash (conservative)", "M", "input"),
    }
    doc = {
        "schema_version": "1.0.0",
        "meta": {
            "venture": a("strata", "text", "product/FINANCIAL_BRIEF_STRATA.md", "H", "input"),
            "scenario": a(s, "text", "product/FINANCIAL_BRIEF_STRATA.md", "H", "input"),
            "currency": a("USD", "iso-4217", "brief", "H", "input"),
            "start_month": a("2026-10", "YYYY-MM", JOSE + " — launch in 6–8 weeks from 2026-08-30", "M", "input"),
            "horizon_months": a(36, "months", "docs/FINANCIAL_MODEL_PLAN.md answer #1 (3-year default) — carried over pending confirmation", "M", "input"),
            "opening_cash": a(25000, "USD", ASSUME + ": company cash at launch not yet stated by joseleos — PLACEHOLDER, please override", "L", "input"),
        },
        "formation_legal": {"items": formation},
        "ga_ops": {"items": ga},
        "personnel": {"roster": roster},
        "rnd": {"items": rnd},
        "sales_marketing": {"items": sm},
        "cogs": cogs,
        "revenue": revenue,
        "financing": {"events": []},
    }
    return doc


if __name__ == "__main__":
    out = sys.argv[1]
    for s in ("base", "upside", "downside"):
        with open(f"{out}/assumptions.{s}.json", "w") as f:
            json.dump(build(s), f, indent=2)
            f.write("\n")
    print("wrote", out)
