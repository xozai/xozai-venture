#!/usr/bin/env python3
"""Generate product/finance/ucm/assumptions.{base,upside,downside}.json.

Sources: research/FINANCIAL_BENCHMARKS.md (Researcher, 2026-08-30, merged #11),
product/finance/ucm/BUILD_ESTIMATE.md (Codex, 2026-08-30), product/FINANCIAL_BRIEF_UCM.md,
joseleos defaults (docs/DECISIONS.md 2026-08-30). Re-run after editing; never hand-edit the JSON.
`revenue.start_month` requires schema >= 1.1.0 (Codex engine PR); strip it to run on 1.0.0.
"""
import json, pathlib
D = "2026-08-30"
BENCH = "research/FINANCIAL_BENCHMARKS.md"
BUILD = "product/finance/ucm/BUILD_ESTIMATE.md"
BRIEF = "product/FINANCIAL_BRIEF_UCM.md"
DEC = "docs/DECISIONS.md (joseleos 2026-08-30)"
GTMA = "marketing/GTM_COST_MODEL.md §A (Scribe, merged #12)"
GTMB = "marketing/GTM_COST_MODEL.md §B (Scribe straw man; HermesX sign-off pending)"

def a(value, unit, source, conf, kind="benchmark"):
    return {"value": value, "unit": unit, "source": source, "date": D, "confidence": conf, "override": None, "kind": kind}

def cost(name, amount, cadence, start, end, source, conf, kind="benchmark"):
    return {"name": a(name, "text", source, conf, "input"), "amount": a(amount, "USD", source, conf, kind),
            "cadence": a(cadence, "cadence", source, "H", "input"), "start_month": a(start, "month", source, conf, "input"),
            "end_month": a(end, "month", source, conf, "input")}

def person(role, hc, start, end, base, tax, ben, equip, founder, defer, source, conf):
    return {"role": a(role, "text", source, "H", "input"), "headcount": a(hc, "FTE", source, conf, "input"),
            "start_month": a(start, "month", source, conf, "input"), "end_month": a(end, "month", source, conf, "input"),
            "annual_base": a(base, "USD/year", source, conf), "employer_tax_pct": a(tax, "decimal", BENCH + " §3 (~10%)", "M"),
            "benefits_pct": a(ben, "decimal", BENCH + " §3 (25–30% at full benefits; 20% lean)", "M"),
            "equipment": a(equip, "USD/FTE", "assumption", "L"), "founder": a(founder, "boolean", DEC, "H", "input"),
            "defer_until_funding": a(defer, "boolean", DEC, "H", "input")}

def build(scn, eng2_start, seats, seat_price, logos_m, growth, churn_m, sm_extra, opening, a5_end=0, b3=2500):
    return {
      "schema_version": "1.0.0",
      "meta": {
        "venture": a("ucm", "text", BRIEF, "H", "input"), "scenario": a(scn, "text", BRIEF, "H", "input"),
        "currency": a("USD", "iso-4217", BRIEF, "H", "input"), "start_month": a("2026-10", "YYYY-MM", "assumption — first full month after kickoff", "L", "input"),
        "horizon_months": a(36, "months", DEC, "H", "input"),
        "opening_cash": a(opening, "USD", "assumption — joseleos to confirm bootstrapped opening cash", "L", "input")},
      "formation_legal": {"items": [
        cost("DE C-Corp formation (Stripe Atlas, all-in)", 500, "one_time", 1, 1, BENCH + " §1", "M"),
        cost("Registered agent", 100, "annual", 13, 0, BENCH + " §1", "M"),
        cost("DE franchise tax + annual report", 500, "annual", 12, 0, BENCH + " §1", "M"),
        cost("Ad hoc counsel (contracts, employment docs)", 400, "monthly", 1, 0, BENCH + " §1 ($3–8k/yr, L)", "L"),
        cost("Trademark filing", 1500, "one_time", 6, 6, "assumption — USPTO fee + counsel", "L")]},
      "ga_ops": {"items": [
        cost("Bookkeeping (fractional)", 300, "monthly", 1, 0, BENCH + " §2 (no $ figure found)", "L"),
        cost("Payroll provider (Gusto Simple, 2–3 employees)", 67, "monthly", 1, 0, BENCH + " follow-up #13 ($61–79/mo)", "M"),
        cost("Software/tooling (~$160/head × 2 eng)", 320, "monthly", 1, 0, BENCH + " follow-up #13 ($117–200/head/mo)", "M"),
        cost("Banking + fees", 25, "monthly", 1, 0, "assumption", "L"),
        cost("Cyber liability", 1500, "annual", 1, 0, BENCH + " §2 ($500–3,000)", "M"),
        cost("Tech E&O (from launch)", 5000, "annual", 8, 0, BENCH + " §2 (~$5k floor)", "L"),
        cost("General liability", 600, "annual", 1, 0, "assumption — small-office GL", "L")]},
      "personnel": {"roster": [
        person("Founder — product/domain (deferred comp)", 1, 1, 0, 150000, 0, 0, 0, True, True, DEC + "; base = memo line", "L"),
        person("Engineer 1 — senior full-stack/geospatial", 1, 1, 0, 110000, 0.10, 0.20, 2500, False, False, BENCH + " §3 ($90–130k non-Bay) + " + BUILD + " team shape", "M"),
        person("Engineer 2 — full-stack/product", 1, eng2_start, 0, 100000, 0.10, 0.20, 2500, False, False, BUILD + " (M2 add) + " + BENCH + " §3", "M")]},
      "rnd": {"items": [
        cost("Data/parser spike (one-time)", 3500, "one_time", 1, 1, BUILD + " ($2–5k)", "M"),
        cost("Dev tooling", 150, "monthly", 1, 0, "assumption", "L"),
        cost("Hosting/data/monitoring — build + ≤10 users", 350, "monthly", 1, 12, BUILD + " run-rate table (10 users: $250–450)", "M"),
        cost("Hosting/data/monitoring — ~100 users", 800, "monthly", 13, 24, BUILD + " run-rate table (100 users: $500–1,100)", "M"),
        cost("Hosting/data/monitoring — 100–1,000 users", 2500, "monthly", 25, 0, BUILD + " run-rate table (1,000 users: $2.5–7k)", "L")]},
      "sales_marketing": {"items": [
        cost("A1 Domain + DNS", 12, "annual", 1, 0, GTMA, "M"),
        cost("A4 ASCE dues + UESI add-on", 307, "annual", 1, 0, GTMA, "M"),
        cost("A5 SEO tooling — Ahrefs Starter", 29, "monthly", 4, a5_end, GTMA, "H"),
        cost("A6 Design — Canva Pro", 15, "monthly", 4, 0, GTMA, "M"),
        cost("A7 Webinar platform — Zoom Webinars 500 (PDH delivery)", 79, "monthly", 7, 0, GTMA, "M"),
        cost("A8 Tutorial video tooling", 24, "monthly", 7, 0, GTMA, "M"),
        cost("B3 Conference attendance (no booth), 1/yr", b3, "annual", 12, 0, GTMB, "L")] + sm_extra},
      "cogs": {
        "revenue_pct": a(0.04, "decimal", "assumption — card processing ~3% + support tooling", "L"),
        "per_active_logo_monthly": a(round(6 * seats), "USD/logo/month", BUILD + " LLM $3–9/active user/mo × seats per logo", "M")},
      "revenue": {
        "starting_logos": a(0, "logos", BRIEF, "H", "input"),
        "start_month": a(8, "month", BUILD + " (M3 release month 7 → first paid month 8)", "M"),
        "new_logos_monthly": a(logos_m, "logos/month", "assumption — no win-rate benchmark for low-touch individual-buyer SaaS (" + BENCH + " §7)", "L"),
        "new_logo_growth_monthly_pct": a(growth, "decimal", "assumption", "L"),
        "monthly_logo_churn_pct": a(churn_m, "decimal", BENCH + " §7 SMB band 10–15%/yr → monthly", "M"),
        "acv": a(round(seats * seat_price * 12), "USD/logo/year", BENCH + " §7 Civil 3D anchor $239/seat/mo → $200–250; seats/logo assumption", "M"),
        "annual_expansion_pct": a(0.05, "decimal", "assumption — seat expansion within firm", "L"),
        "billing_terms_months": a(12, "months", BRIEF + " (annual upfront preferred)", "M", "input")},
      "financing": {"events": []}}

upside_sm = [
  cost("A5-U SEO tooling — Ahrefs Lite (from m10)", 129, "monthly", 10, 0, GTMA, "H"),
  cost("A9 Contract technical writer", 2000, "monthly", 8, 0, GTMA, "L"),
  cost("A10 Contract video editor", 1500, "monthly", 10, 0, GTMA, "L"),
  cost("A11 Paid search, high-intent (volume-capped)", 1200, "monthly", 12, 0, GTMA + " — Researcher search-volume check pending", "L"),
  cost("A12 Launch collateral + brand refresh", 6000, "one_time", 9, 9, GTMA, "L"),
  cost("B1 CRM + outbound tooling", 99, "monthly", 12, 0, GTMB, "L"),
  cost("B2 UESI/APWA exhibit booth + travel (m14)", 8000, "one_time", 14, 14, GTMB + " — quote required", "L"),
  cost("B2 UESI/APWA exhibit booth + travel (m26)", 8000, "one_time", 26, 26, GTMB + " — quote required", "L"),
  cost("B4 State DOT training sponsorship", 3000, "one_time", 18, 18, GTMB + " — purchasability unconfirmed", "L")]
# Downside per §A.3: only A1 + A4 survive; §B $0.
scenarios = {
  "base":     build("base",     3, 2, 225, 2.0, 0.05, 0.010, [], 50000),
  "upside":   build("upside",   3, 3, 250, 3.0, 0.05, 0.008, upside_sm, 50000, a5_end=9),
  "downside": build("downside", 5, 1, 200, 1.0, 0.03, 0.013, [], 50000, b3=0)}
for scn in ("downside",):
    scenarios[scn]["sales_marketing"]["items"] = [i for i in scenarios[scn]["sales_marketing"]["items"] if i["name"]["value"].split()[0] in ("A1","A4")]
out = pathlib.Path(__file__).parent
for name, doc in scenarios.items():
    (out / f"assumptions.{name}.json").write_text(json.dumps(doc, indent=2) + "\n")
    print("wrote", name)
