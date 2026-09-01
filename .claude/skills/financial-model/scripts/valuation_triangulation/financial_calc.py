#!/usr/bin/env python3
"""
financial-model/scripts/valuation_triangulation/financial_calc.py

OPTIONAL v3 supplement to the venture's deterministic financial-model
engine (product/finance/engine/). This does NOT replace that engine — it
is a fast, standalone triangulation check that runs three classic
valuation methods (DCF, revenue multiple / comps, SaaS health metrics)
off a small set of top-line inputs, for a quick sanity range and a
HEALTHY/WATCH/CRITICAL verdict on unit economics.

Use it to sanity-check the deterministic engine's output, not to author
MODEL.md. All numbers here are simplified/order-of-magnitude; the engine
remains the source of truth for anything going into a memo or the .xlsx.

Vendored + adapted (MIT) from davepoon/buildwithclaude
plugins/venture-capital-intelligence/skills/financial-model. See
../../THIRD_PARTY_LICENSE and research/SKILL_SOURCES.md for provenance.

Reads model_inputs.json, computes DCF, revenue multiple, and SaaS metrics.
Writes model_output.json.
"""

import json
import sys
import os


# ── Stage-default revenue multiples ──────────────────────────────────────────
STAGE_MULTIPLES = {
    "pre-seed": {"low": 12, "mid": 18, "high": 25},
    "seed":     {"low": 10, "mid": 12, "high": 15},
    "series a": {"low": 8,  "mid": 11, "high": 15},
    "series b": {"low": 5,  "mid": 8,  "high": 12},
    "series c": {"low": 3,  "mid": 6,  "high": 9},
    "default":  {"low": 6,  "mid": 10, "high": 15},
}


def get_multiples(stage: str) -> dict:
    key = stage.lower().strip()
    for k in STAGE_MULTIPLES:
        if k in key:
            return dict(STAGE_MULTIPLES[k])
    return dict(STAGE_MULTIPLES["default"])


# ── DCF Valuation ─────────────────────────────────────────────────────────────
def dcf_valuation(
    arr: float,
    growth_rates: list,          # list of annual growth rates (decimal), len = projection_years
    gross_margin: float,         # decimal, e.g. 0.70
    discount_rate: float,        # WACC, e.g. 0.20
    terminal_growth_rate: float, # long-term growth, e.g. 0.03
    opex_ratio: float = 0.80,    # opex as % of revenue (FCF = Gross Profit - OpEx)
) -> dict:
    """Simplified DCF for early-stage SaaS. Order-of-magnitude only — the
    deterministic engine's cash roll-forward is the authoritative model."""
    if arr <= 0:
        return {"error": "ARR must be > 0 for DCF", "dcf_value": 0}

    revenues, fcfs, dcf_flows = [], [], []
    rev = arr

    for t, g in enumerate(growth_rates, start=1):
        rev = rev * (1 + g)
        revenues.append(rev)
        gross_profit = rev * gross_margin
        fcf = gross_profit - (rev * opex_ratio)
        fcfs.append(fcf)
        pv = fcf / ((1 + discount_rate) ** t)
        dcf_flows.append(round(pv, 0))

    # Terminal value (Gordon Growth Model on last FCF)
    last_fcf = fcfs[-1]
    terminal_value = last_fcf * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)
    terminal_pv    = terminal_value / ((1 + discount_rate) ** len(growth_rates))

    dcf_equity_value = sum(dcf_flows) + terminal_pv

    return {
        "dcf_value":      round(dcf_equity_value, 0),
        "terminal_value": round(terminal_pv, 0),
        "sum_pv_fcfs":    round(sum(dcf_flows), 0),
        "revenues":       [round(r, 0) for r in revenues],
        "fcfs":           [round(f, 0) for f in fcfs],
        "assumptions": {
            "discount_rate":        discount_rate,
            "terminal_growth_rate": terminal_growth_rate,
            "gross_margin":         gross_margin,
        },
    }


# ── Revenue Multiple Valuation ────────────────────────────────────────────────
def revenue_multiple_valuation(arr: float, stage: str, comparables: list) -> dict:
    # SKILL.md step 5: sourced comparables take precedence; stage defaults are
    # a fallback that must be flagged. Mirrors the TS engine's selection rule.
    comp_mults = [c.get("ev_revenue_multiple", 0) for c in (comparables or []) if c.get("ev_revenue_multiple", 0) > 0]
    if comp_mults:
        source = "comparables"
        mults = {
            "low":  min(comp_mults),
            "mid":  round(sum(comp_mults) / len(comp_mults), 1),
            "high": max(comp_mults),
        }
    else:
        source = "stage_default"
        mults = get_multiples(stage)

    return {
        "arr": arr,
        "stage": stage,
        "source": source,
        "multiples": mults,
        "implied_value_low":  round(arr * mults["low"], 0),
        "implied_value_mid":  round(arr * mults["mid"], 0),
        "implied_value_high": round(arr * mults["high"], 0),
    }


# ── SaaS Metrics ──────────────────────────────────────────────────────────────
def saas_metrics(inputs: dict) -> dict:
    arpu          = inputs.get("arpu_monthly", 0)
    churn         = max(inputs.get("monthly_churn", 0.01), 0.001)  # floor at 0.1%
    gross_margin  = inputs.get("gross_margin", 0.70)
    cac           = inputs.get("cac", 0)
    mrr           = inputs.get("mrr", 0)
    monthly_burn  = inputs.get("monthly_burn", 0)
    cash          = inputs.get("cash_on_hand", 0)
    nrr           = inputs.get("nrr", 1.0)
    mrr_growth    = inputs.get("mrr_growth_rate", 0)

    # LTV
    customer_lifetime_months = 1.0 / churn
    ltv = (arpu * gross_margin) / churn if arpu > 0 else 0

    # LTV:CAC
    ltv_cac = (ltv / cac) if cac > 0 and ltv > 0 else 0

    # CAC Payback Period (months)
    cac_payback = (cac / (arpu * gross_margin)) if arpu > 0 and gross_margin > 0 else 0

    # Burn multiple (net burn / net new ARR)
    net_new_arr_monthly = mrr * mrr_growth if mrr > 0 and mrr_growth > 0 else 0
    burn_multiple = (monthly_burn / net_new_arr_monthly) if net_new_arr_monthly > 0 else None

    # Runway
    runway_months = (cash / monthly_burn) if monthly_burn > 0 and cash > 0 else None

    # Rule of 40 (ARR growth rate % + EBITDA margin %)
    arr_growth_annual_pct = ((1 + mrr_growth) ** 12 - 1) * 100 if mrr_growth > 0 else 0
    ebitda_margin_pct = ((mrr * gross_margin - monthly_burn) / mrr * 100) if mrr > 0 else None
    rule_of_40 = (arr_growth_annual_pct + ebitda_margin_pct) if ebitda_margin_pct is not None else None

    # Health verdicts
    # SKILL.md benchmark table: LTV:CAC best-in-class >5x, good >3x, concerning <2x.
    ltv_cac_health = "HEALTHY" if ltv_cac >= 5 else ("WATCH" if ltv_cac >= 2 else "CRITICAL")
    # SKILL.md benchmark table: CAC payback best-in-class <12mo, good <18mo, concerning >24mo.
    payback_health = "HEALTHY" if 0 < cac_payback <= 12 else ("WATCH" if cac_payback <= 24 else "CRITICAL")
    # SKILL.md benchmark table: burn multiple best-in-class <1x, good <2x, concerning >2x.
    burn_health    = "HEALTHY" if burn_multiple is not None and burn_multiple <= 1 else \
                     ("WATCH" if burn_multiple is not None and burn_multiple <= 2 else "CRITICAL")
    # SKILL.md benchmark table: NDR best-in-class >120%, good >110%, concerning <100%.
    nrr_health     = "HEALTHY" if nrr >= 1.2 else ("WATCH" if nrr >= 1.0 else "CRITICAL")

    return {
        "ltv":                      round(ltv, 0),
        "customer_lifetime_months": round(customer_lifetime_months, 1),
        "ltv_cac_ratio":            round(ltv_cac, 2),
        "cac_payback_months":       round(cac_payback, 1),
        "burn_multiple":            round(burn_multiple, 2) if burn_multiple is not None else "N/A",
        "runway_months":            round(runway_months, 1) if runway_months is not None else "N/A",
        "rule_of_40":               round(rule_of_40, 1) if rule_of_40 is not None else "N/A",
        "nrr_pct":                  round(nrr * 100, 1),
        "arr_growth_annual_pct":    round(arr_growth_annual_pct, 1),
        "health": {
            "ltv_cac":  ltv_cac_health,
            "payback":  payback_health,
            "burn":     burn_health,
            "nrr":      nrr_health,
        },
    }


# ── Overall verdict (added by Honey0, not part of the upstream vendor — see
#    SKILL.md step 5: "a single HEALTHY/WATCH/CRITICAL verdict ... never in
#    prose"; the vendored per-metric flags above didn't roll up into one) ──────
def overall_verdict(saas: dict) -> dict:
    health = saas.get("health", {})
    concerning = sorted(k for k, v in health.items() if v == "CRITICAL")
    runway = saas.get("runway_months")
    runway_critical = isinstance(runway, (int, float)) and runway < 6

    if runway_critical or len(concerning) >= 2:
        verdict = "CRITICAL"
    elif len(concerning) == 0:
        verdict = "HEALTHY"
    else:
        verdict = "WATCH"

    return {
        "verdict": verdict,
        "concerning_metrics": concerning,
        "runway_implies_critical": runway_critical,
    }


# ── Stage benchmarks ──────────────────────────────────────────────────────────
STAGE_BENCHMARKS = {
    "seed": {
        "mrr_growth_mom_pct": "15-20%",
        "burn_multiple":      "< 2x",
        "runway_months":      "18+",
        "ltv_cac":            "> 3x",
        "gross_margin":       "> 60%",
    },
    "series a": {
        "arr_target":     "$1M-$3M",
        "arr_growth_yoy": "3x YoY",
        "nrr":            "> 100%",
        "gross_margin":   "> 65%",
        "ltv_cac":        "> 3x",
        "cac_payback":    "< 18 months",
    },
    "series b": {
        "arr_target":   "$10M+",
        "nrr":          "> 115%",
        "rule_of_40":   "> 40",
        "gross_margin": "> 70%",
    },
}


def get_benchmarks(stage: str) -> dict:
    key = stage.lower().strip()
    for k in STAGE_BENCHMARKS:
        if k in key:
            return STAGE_BENCHMARKS[k]
    return STAGE_BENCHMARKS.get("seed", {})


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    if len(sys.argv) < 2:
        print(
            "Usage: financial_calc.py <venture>\n"
            "  Reads product/finance/<venture>/triangulation/model_inputs.json\n"
            "  Writes product/finance/<venture>/triangulation/model_output.json",
            file=sys.stderr,
        )
        sys.exit(1)

    venture = sys.argv[1]
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", ".."))
    output_dir = os.path.join(repo_root, "product", "finance", venture, "triangulation")
    os.makedirs(output_dir, exist_ok=True)

    inputs_path = os.path.join(output_dir, "model_inputs.json")
    output_path = os.path.join(output_dir, "model_output.json")

    if not os.path.exists(inputs_path):
        print(f"ERROR: model_inputs.json not found at {inputs_path}", file=sys.stderr)
        print("Create it first — see .claude/skills/financial-model/scripts/valuation_triangulation/model_inputs.example.json", file=sys.stderr)
        sys.exit(1)

    with open(inputs_path, "r", encoding="utf-8") as f:
        inputs = json.load(f)

    # Derive ARR from MRR if not provided
    arr = inputs.get("arr", 0)
    mrr = inputs.get("mrr", 0)
    if arr == 0 and mrr > 0:
        arr = mrr * 12
        inputs["arr"] = arr

    # DCF
    proj_years  = inputs.get("projection_years", 5)
    base_growth = inputs.get("mrr_growth_rate", 0.15)
    # Decay growth rate over projection period (optimistic decay)
    annual_base = (1 + base_growth) ** 12 - 1
    growth_rates = [max(annual_base * (0.85 ** t), 0.05) for t in range(proj_years)]

    dcf_result  = dcf_valuation(
        arr=arr,
        growth_rates=growth_rates,
        gross_margin=inputs.get("gross_margin", 0.70),
        discount_rate=inputs.get("discount_rate", 0.20),
        terminal_growth_rate=inputs.get("terminal_growth_rate", 0.03),
    )

    # Revenue Multiple
    rev_mult_result = revenue_multiple_valuation(
        arr=arr,
        stage=inputs.get("stage", "seed"),
        comparables=inputs.get("comparables", []),
    )

    # SaaS Metrics
    saas_result = saas_metrics(inputs)
    saas_result["overall"] = overall_verdict(saas_result)

    # Combined valuation range
    dcf_val  = dcf_result.get("dcf_value", 0)
    rev_low  = rev_mult_result.get("implied_value_low", 0)
    rev_high = rev_mult_result.get("implied_value_high", 0)
    vals = [v for v in [dcf_val, rev_low, rev_high] if v > 0]
    valuation_range_low  = round(min(vals), 0) if vals else 0
    valuation_range_high = round(max(vals), 0) if vals else 0

    output = {
        "company":  inputs.get("company", venture),
        "stage":    inputs.get("stage", "Unknown"),
        "arr":      arr,
        "verdict":  saas_result["overall"]["verdict"],
        "valuation_range": {
            "low":  valuation_range_low,
            "high": valuation_range_high,
        },
        "dcf":             dcf_result,
        "revenue_multiple": rev_mult_result,
        "saas_metrics":    saas_result,
        "benchmarks":      get_benchmarks(inputs.get("stage", "seed")),
        "_note": "Supplementary triangulation only — not a substitute for "
                 "product/finance/<venture>/model.xlsx and MODEL.md, which "
                 "remain the accepted source of truth.",
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"financial_calc.py: ARR=${arr:,.0f}, DCF=${dcf_val:,.0f}, Rev-mult range ${rev_low:,.0f}-${rev_high:,.0f}, verdict={output['verdict']}")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
