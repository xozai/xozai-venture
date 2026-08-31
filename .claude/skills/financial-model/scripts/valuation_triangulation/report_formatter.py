#!/usr/bin/env python3
"""
financial-model/scripts/valuation_triangulation/report_formatter.py

Reads model_output.json (from financial_calc.py) and prints the formatted
triangulation report. Supplementary to the deterministic engine's MODEL.md
— see financial_calc.py's module docstring.

Vendored + adapted (MIT) from davepoon/buildwithclaude
plugins/venture-capital-intelligence/skills/financial-model. See
../../THIRD_PARTY_LICENSE and research/SKILL_SOURCES.md for provenance.
"""

import json
import sys
import os


def fmt_usd(val) -> str:
    if val == "N/A" or val is None:
        return "N/A"
    v = float(val)
    if abs(v) >= 1_000_000:
        return f"${v/1_000_000:.1f}M"
    if abs(v) >= 1_000:
        return f"${v/1_000:.0f}K"
    return f"${v:.0f}"


def health_icon(status: str) -> str:
    return {"HEALTHY": "\u2705", "WATCH": "\u26a0\ufe0f ", "CRITICAL": "\u274c"}.get(status, " ")


def main():
    if len(sys.argv) < 2:
        print(
            "Usage: report_formatter.py <venture>\n"
            "  Reads product/finance/<venture>/triangulation/model_output.json",
            file=sys.stderr,
        )
        sys.exit(1)

    venture = sys.argv[1]
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", ".."))
    output_dir = os.path.join(repo_root, "product", "finance", venture, "triangulation")
    output_path = os.path.join(output_dir, "model_output.json")

    if not os.path.exists(output_path):
        print("ERROR: model_output.json not found. Run financial_calc.py first.", file=sys.stderr)
        sys.exit(1)

    with open(output_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    sep = "\u2501" * 54
    sm  = data.get("saas_metrics", {})
    rm  = data.get("revenue_multiple", {})
    dcf = data.get("dcf", {})
    h   = sm.get("health", {})
    vr  = data.get("valuation_range", {})
    bm  = data.get("benchmarks", {})

    lines = [
        "",
        sep,
        f"VALUATION TRIANGULATION (supplementary)  \u00b7  {data.get('company', 'Unknown')}  \u00b7  {data.get('stage', '')}",
        sep,
        "",
        "  NOT a replacement for MODEL.md / model.xlsx \u2014 sanity-check only.",
        "",
        f"  ARR: {fmt_usd(data.get('arr', 0))}",
        "",
        "VALUATION RANGE",
        f"  Low:   {fmt_usd(vr.get('low', 0))}",
        f"  High:  {fmt_usd(vr.get('high', 0))}",
        "",
        "  DCF Intrinsic Value:     " + fmt_usd(dcf.get("dcf_value", 0)),
        f"  Revenue Multiple (low):  {fmt_usd(rm.get('implied_value_low', 0))}  ({rm.get('multiples', {}).get('low', 0)}x ARR)",
        f"  Revenue Multiple (mid):  {fmt_usd(rm.get('implied_value_mid', 0))}  ({rm.get('multiples', {}).get('mid', 0)}x ARR)",
        f"  Revenue Multiple (high): {fmt_usd(rm.get('implied_value_high', 0))}  ({rm.get('multiples', {}).get('high', 0)}x ARR)",
        "",
        sep,
        "SAAS HEALTH METRICS",
        sep,
        f"  {health_icon(h.get('ltv_cac'))}  LTV:CAC Ratio       {sm.get('ltv_cac_ratio', 'N/A')}x   (target: > 3x)",
        f"  {health_icon(h.get('payback'))}  CAC Payback         {sm.get('cac_payback_months', 'N/A')} months  (target: < 18 months)",
        f"  {health_icon(h.get('nrr'))}  Net Revenue Retention {sm.get('nrr_pct', 'N/A')}%   (target: > 100%)",
        f"  {health_icon(h.get('burn'))}  Burn Multiple       {sm.get('burn_multiple', 'N/A')}x   (target: < 2x)",
        f"     LTV                 {fmt_usd(sm.get('ltv', 0))}",
        f"     Cust. Lifetime      {sm.get('customer_lifetime_months', 'N/A')} months",
        f"     Runway              {sm.get('runway_months', 'N/A')} months",
        f"     Rule of 40 Score    {sm.get('rule_of_40', 'N/A')}",
        f"     ARR Growth (annual) {sm.get('arr_growth_annual_pct', 'N/A')}%",
        "",
    ]

    if bm:
        lines += [sep, "STAGE BENCHMARKS", sep]
        for k, v in bm.items():
            label = k.replace("_", " ").title().ljust(24)
            lines.append(f"  {label}  {v}")
        lines.append("")

    # DCF projection table
    revs = dcf.get("revenues", [])
    fcfs = dcf.get("fcfs", [])
    if revs:
        lines += [sep, "DCF PROJECTION", sep]
        lines.append(f"  {'Year':<6} {'Revenue':>12} {'FCF':>12}")
        lines.append(f"  {'----':<6} {'--------':>12} {'---':>12}")
        for i, (r, f) in enumerate(zip(revs, fcfs), start=1):
            lines.append(f"  Yr {i:<3} {fmt_usd(r):>12} {fmt_usd(f):>12}")
        lines += [
            f"  Terminal Value: {fmt_usd(dcf.get('terminal_value', 0))}",
            "",
        ]

    lines += [
        sep,
        f"Audit files: product/finance/<venture>/triangulation/model_inputs.json, model_output.json",
        "Source of truth remains: product/finance/<venture>/MODEL.md + model.xlsx",
        sep,
        "",
    ]

    print("\n".join(lines))


if __name__ == "__main__":
    main()
