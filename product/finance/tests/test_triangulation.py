#!/usr/bin/env python3
"""
TC-10 — v3 valuation-triangulation fixtures (Honey0's CI ownership,
SKILL.md financial-model v3 step 6: "Honey0's fixtures run in CI, including
v3 triangulation fixtures (known-input -> known-verdict cases per benchmark
band)"). Covers `.claude/skills/financial-model/scripts/valuation_triangulation/
financial_calc.py`. See TEST_PLAN.md TC-10 for the narrative version of
every case below; re-verify both together if a number here stops matching.

Run: python3 product/finance/tests/test_triangulation.py
"""

import importlib.util
import json
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SCRIPT_PATH = os.path.join(
    REPO_ROOT, ".claude", "skills", "financial-model", "scripts",
    "valuation_triangulation", "financial_calc.py",
)

spec = importlib.util.spec_from_file_location("financial_calc", SCRIPT_PATH)
fc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fc)

failures = []


def check(label, condition):
    if condition:
        print(f"  PASS  {label}")
    else:
        print(f"  FAIL  {label}")
        failures.append(label)


# ── TC-10a: per-metric bands — financial_calc.py's own coded thresholds ──────
# Note: these pin the *script's* thresholds (HEALTHY/WATCH/CRITICAL cutpoints
# above the code's `saas_metrics()`). PR #30 flagged burn-multiple and NRR as
# narrower than SKILL.md's published benchmark table; Pollen0's spec-
# conformance pass (2026-09-01) closed that gap by tightening the code to
# match the doc, so these now pin the doc's own bands.

def ltv_cac_case(cac):
    return fc.saas_metrics({"arpu_monthly": 100, "gross_margin": 1.0, "monthly_churn": 0.1, "cac": cac})["health"]["ltv_cac"]

check("LTV:CAC = 3.0x -> HEALTHY (boundary)", ltv_cac_case(1000 / 3) == "HEALTHY")
check("LTV:CAC = 1.5x -> WATCH (boundary)", ltv_cac_case(1000 / 1.5) == "WATCH")
check("LTV:CAC = 1.4x -> CRITICAL", ltv_cac_case(1000 / 1.4) == "CRITICAL")


def payback_case(cac):
    return fc.saas_metrics({"arpu_monthly": 100, "gross_margin": 1.0, "monthly_churn": 0.1, "cac": cac})["health"]["payback"]

check("CAC payback = 12mo -> HEALTHY (boundary)", payback_case(1200) == "HEALTHY")
check("CAC payback = 18mo -> WATCH (boundary)", payback_case(1800) == "WATCH")
check("CAC payback = 19mo -> CRITICAL", payback_case(1900) == "CRITICAL")


def burn_case(monthly_burn):
    return fc.saas_metrics({"mrr": 10000, "mrr_growth_rate": 0.1, "monthly_burn": monthly_burn, "monthly_churn": 0.1})["health"]["burn"]

check("Burn multiple = 1.0x -> HEALTHY (boundary)", burn_case(1000) == "HEALTHY")
check("Burn multiple = 2.0x -> WATCH (boundary)", burn_case(2000) == "WATCH")
check("Burn multiple = 2.1x -> CRITICAL", burn_case(2100) == "CRITICAL")


def nrr_case(nrr):
    return fc.saas_metrics({"nrr": nrr, "monthly_churn": 0.1})["health"]["nrr"]

check("NRR = 120% -> HEALTHY (boundary)", nrr_case(1.20) == "HEALTHY")
check("NRR = 100% -> WATCH (boundary)", nrr_case(1.00) == "WATCH")
check("NRR = 99% -> CRITICAL", nrr_case(0.99) == "CRITICAL")


# ── TC-10b: overall_verdict() aggregation — SKILL.md's rule, exercised directly
def verdict_of(health, runway_months=None):
    return fc.overall_verdict({"health": health, "runway_months": runway_months})["verdict"]

all_healthy = {"ltv_cac": "HEALTHY", "payback": "HEALTHY", "burn": "HEALTHY", "nrr": "HEALTHY"}
one_critical = {**all_healthy, "nrr": "CRITICAL"}
two_critical = {**one_critical, "burn": "CRITICAL"}

check("0 CRITICAL metrics -> HEALTHY", verdict_of(all_healthy) == "HEALTHY")
check("1 CRITICAL metric -> WATCH", verdict_of(one_critical) == "WATCH")
check("2 CRITICAL metrics -> CRITICAL", verdict_of(two_critical) == "CRITICAL")
check(
    "0 CRITICAL metrics but runway < 6mo -> CRITICAL (runway overrides metric count)",
    verdict_of(all_healthy, runway_months=3) == "CRITICAL",
)
check(
    "0 CRITICAL metrics, runway == 6mo exactly -> HEALTHY (not < 6)",
    verdict_of(all_healthy, runway_months=6) == "HEALTHY",
)
check(
    "'N/A' runway (cash-generating) never triggers the runway override",
    verdict_of(all_healthy, runway_months="N/A") == "HEALTHY",
)


# ── TC-10c: UCM golden fixture — real venture data, end-to-end script run ───
# product/finance/ucm/triangulation/model_inputs.json is the actual first v3
# run (PR #27, 2026-09-01), reproduced here from that PR's committed input.
# This is a regression check: if financial_calc.py's math changes, this
# fixture's numbers (and the committed model_output.json) must be
# re-verified together, per this file's own convention.
ucm_inputs_path = os.path.join(REPO_ROOT, "product", "finance", "ucm", "triangulation", "model_inputs.json")
ucm_output_path = os.path.join(REPO_ROOT, "product", "finance", "ucm", "triangulation", "model_output.json")

if os.path.exists(ucm_inputs_path) and os.path.exists(ucm_output_path):
    with open(ucm_inputs_path) as f:
        ucm_inputs = json.load(f)
    with open(ucm_output_path) as f:
        ucm_expected = json.load(f)

    arr = ucm_inputs["mrr"] * 12
    proj_years = ucm_inputs["projection_years"]
    base_growth = ucm_inputs["mrr_growth_rate"]
    annual_base = (1 + base_growth) ** 12 - 1
    growth_rates = [max(annual_base * (0.85 ** t), 0.05) for t in range(proj_years)]
    dcf_result = fc.dcf_valuation(
        arr=arr, growth_rates=growth_rates, gross_margin=ucm_inputs["gross_margin"],
        discount_rate=ucm_inputs["discount_rate"], terminal_growth_rate=ucm_inputs["terminal_growth_rate"],
    )
    saas_result = fc.saas_metrics(ucm_inputs)
    saas_result["overall"] = fc.overall_verdict(saas_result)

    check("UCM golden fixture: DCF value matches committed model_output.json", dcf_result["dcf_value"] == ucm_expected["dcf"]["dcf_value"])
    check("UCM golden fixture: NRR health = CRITICAL (93% < 100%)", saas_result["health"]["nrr"] == "CRITICAL")
    check("UCM golden fixture: overall verdict = WATCH (1 concerning metric, cash-generating so no runway override)", saas_result["overall"]["verdict"] == "WATCH")
    check("UCM golden fixture: overall verdict matches committed model_output.json's top-level 'verdict'", saas_result["overall"]["verdict"] == ucm_expected.get("verdict"))
else:
    print("  SKIP  UCM golden fixture: product/finance/ucm/triangulation/{model_inputs,model_output}.json not present")


print()
if failures:
    print(f"{len(failures)} FAILURE(S): {failures}")
    sys.exit(1)
print("All triangulation fixtures passed.")
