"""Strata Civic Solutions — investor pitch deck (Phase 5 of the pitch-deck skill).

Narrative source: pitch/strata/story.md and visual-brief.md. Numbers: product/finance/strata/
MODEL.md (base case, engine v1). Evidence: research/spaces/GOVTECH_MUNICIPAL.md and
OUTBOX/Strata_Market_Competitive_Research.docx (Researcher, 2026-08-30).

Author: Scribe, 2026-09-01.
Regenerate: ~/.buzz/.scratch/pptx-venv/bin/python build_deck.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deckkit import *  # noqa

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "Strata_Pitch_Deck_v1.pptx")
prs = deck()
BLANK = prs.slide_layouts[6]
FOOT = "Strata Civic Solutions  ·  Pitch deck v1, 1 September 2026  ·  Draft for joseleos  ·  Confidential"
_n = [0]


def new(paper=True):
    s = prs.slides.add_slide(BLANK)
    if paper:
        bg(s, PAPER)
    _n[0] += 1
    return s


def head(s, eyebrow, title, sub=None, dark=False):
    ink = WHITE if dark else INK
    body = PALE if dark else BODY
    t = tb(s, ML, Inches(0.62), CW, Inches(0.3))
    para(t, eyebrow.upper(), 10.5, ACCENT, bold=True, first=True)
    lines = max(1, -(-len(title) // 52))
    t2 = tb(s, ML, Inches(1.0), CW, Inches(0.52 * lines))
    para(t2, title, 30, ink, bold=True, first=True, line=1.06)
    y = Inches(1.0) + Inches(0.46 * lines) + Inches(0.16)
    if sub:
        s2 = tb(s, ML, y, Inches(10.4), Inches(0.6))
        para(s2, sub, 14.5, body, first=True, line=1.32)
        y += Inches(0.235 * max(1, -(-len(sub) // 100)) + 0.26)
    rule(s, ML, y, CW, RULE if not dark else RGBColor(0x33, 0x40, 0x52))
    return y + Inches(0.42)


def foot(s, src=None, dark=False):
    c = MUTED if not dark else RGBColor(0x6B, 0x77, 0x86)
    if src:
        t = tb(s, ML, Inches(6.62), Inches(11.3), Inches(0.3))
        para(t, "Source:  " + src, 9, c, first=True, line=1.25)
    f = tb(s, ML, Inches(7.02), Inches(9.6), Inches(0.3))
    para(f, FOOT, 8.5, c, first=True)
    g = tb(s, W - MR - Inches(1.0), Inches(7.02), Inches(1.0), Inches(0.3), PP_ALIGN.RIGHT)
    para(g, str(_n[0]), 8.5, c, first=True, align=PP_ALIGN.RIGHT)


def flagbox(s, x, y, w, h, title, lines):
    c = card(s, x, y, w, h, fill=RGBColor(0xFA, 0xEE, 0xEC), edge=RGBColor(0xE4, 0xC4, 0xBF))
    t = tb(s, x + Inches(0.22), y + Inches(0.16), w - Inches(0.44), h - Inches(0.3))
    para(t, title, 10.5, FLAG, bold=True, first=True, font=MONO)
    for ln in lines:
        para(t, ln, 12, RGBColor(0x6E, 0x3C, 0x37), space_before=7, line=1.25)
    return c


# ============================================================ 1. cover
s = new(paper=False)
bg(s, INK)
strata(s, ML, Inches(1.9), ACCENT, widths=(1.6, 1.1, 0.7), gap=0.16, thick=Pt(3.5))
t = tb(s, ML, Inches(2.72), Inches(11.0), Inches(1.2))
para(t, "Strata Civic Solutions", 50, WHITE, bold=True, first=True, line=1.0)
t2 = tb(s, ML, Inches(3.75), Inches(10.0), Inches(0.7))
para(t2, "Know the record before you vote.", 25, ACCENT, first=True)
t3 = tb(s, ML, Inches(4.62), Inches(9.6), Inches(1.0))
para(t3, "Municipal decision intelligence: plain-language answers over a city's own published "
         "record — budgets, ordinances, minutes, contracts — cited to the page.",
     14.5, RGBColor(0xB6, 0xC1, 0xC8), first=True, line=1.4)
t4 = tb(s, ML, Inches(6.55), Inches(11.0), Inches(0.6))
para(t4, "Delaware Public Benefit Corporation, foreign-qualified in Texas  ·  San Antonio, TX  ·  "
         "1 September 2026", 11, RGBColor(0x6B, 0x77, 0x86), first=True)
para(t4, "Draft for joseleos — three slides carry unresolved placeholders. Do not present externally as-is.",
     10, FLAG, first=False, space_before=6, font=MONO)

# ============================================================ 2. problem
s = new()
y = head(s, "the problem", "The packet is 300 pages. The vote is Tuesday.",
         "A council member in a Texas city of 10,000–50,000 is a part-time official with a "
         "separate full-time job and no staff of their own.")
stats = [("200–400", "pages in a typical agenda packet",
          "Delivered days before the vote, read on personal time."),
         ("0", "staff reporting to an elected official",
          "City staff serve the institution. The official has no researcher, no analyst, no counsel of their own."),
         ("~5 : 1", "board volunteers per elected official",
          "Appointed planning, finance, parks, public-safety and ethics volunteers — the least-served users in govtech.")]
cw = Inches(3.6)
for i, (big, lab, body) in enumerate(stats):
    x = ML + i * Inches(3.85)
    card(s, x, y, cw, Inches(2.5))
    t = tb(s, x + Inches(0.28), y + Inches(0.3), cw - Inches(0.56), Inches(2.0))
    para(t, big, 38, ACCENT, bold=True, first=True, line=1.0)
    para(t, lab.upper(), 10, INK, bold=True, space_before=6)
    para(t, body, 12.5, BODY, space_before=10, line=1.3)
t = tb(s, ML, y + Inches(2.8), Inches(11.2), Inches(0.5))
para(t, "The cost of being under-prepared is not a bad quarter. It is being wrong on the record, "
        "in public, on video.", 15, INK, bold=True, first=True, line=1.3)
foot(s, "research/spaces/GOVTECH_MUNICIPAL.md (buyer archetypes); Strata market & competitive research, 30 Aug 2026, §3.")

# ============================================================ 3. the workaround
s = new()
y = head(s, "the incumbent", "They already tried the obvious fix.",
         "Every prospect has a working solution today. It is free, it is universally deployed, "
         "and it is the reason nobody in this category has bought anything.")
card(s, ML, y, Inches(5.5), Inches(2.75))
t = tb(s, ML + Inches(0.3), y + Inches(0.26), Inches(4.9), Inches(2.2))
para(t, "WHAT THEY DO NOW", 10, ACCENT, bold=True, first=True)
for ln in ["Ctrl+F the PDF for a word they hope appears.",
           "Call the clerk — who has their own job.",
           "Ask the one colleague who has been on council longest.",
           "Vote, and find out afterwards."]:
    para(t, "—  " + ln, 14, BODY, space_before=11, line=1.3)
card(s, ML + Inches(5.85), y, Inches(5.5), Inches(2.75), fill=TINT, edge=RGBColor(0xC3, 0xD8, 0xD3))
t = tb(s, ML + Inches(6.15), y + Inches(0.26), Inches(4.9), Inches(2.2))
para(t, "WHAT IT COSTS THEM", 10, ACCENT, bold=True, first=True)
for ln in ["Hours per packet, on unpaid time.",
           "Precedent they never find, because they did not know the word for it.",
           "Cost history that lives three budgets back.",
           "Deferring to staff on a decision that is legally theirs."]:
    para(t, "—  " + ln, 14, BODY, space_before=11, line=1.3)
t = tb(s, ML, y + Inches(3.05), Inches(11.2), Inches(0.5))
para(t, "The competitor we actually have to beat is Ctrl+F.", 17, INK, bold=True, first=True)
foot(s, "research/spaces/GOVTECH_MUNICIPAL.md — \"the real incumbent is the manual workaround.\"")

# ============================================================ 4. the insight
s = new(paper=False)
bg(s, PAPER)
y = head(s, "the insight", "Your city already published the answer.")
t = tb(s, ML, y + Inches(0.35), Inches(10.6), Inches(2.2))
para(t, "“Search returns documents and leaves the reading to you.\n"
        "Strata returns an answer, and the documents behind it.”",
     27, INK, first=True, line=1.35, italic=True)
strata(s, ML, y + Inches(2.35), ACCENT, widths=(1.35, 0.95, 0.6), gap=0.13, thick=Pt(3))
t2 = tb(s, ML, y + Inches(3.0), Inches(10.6), Inches(1.2))
para(t2, "Strata creates no new data and asks the city to change nothing. Budgets, ordinances, "
         "minutes and contracts are already published under the Public Information Act. The "
         "record is not missing — it is unusable at meeting-prep speed.",
     15, BODY, first=True, line=1.4)
foot(s, "stratacivicsolutions.com (fetched 30 Aug 2026), quoted verbatim; Tex. Gov't Code ch. 552.")

# ============================================================ 5. why now
s = new()
y = head(s, "why now", "2026 is the year cities wrote their AI policies.",
         "The most common AI-related item on a council agenda this year is adopting an AI-use "
         "policy. That changes which products a city can actually say yes to.")
items = [("Incumbents shipped AI into installed bases.",
          "CivicPlus, Granicus and OpenGov all released AI summarization in 2026 — built for the staff who prepare the meeting."),
         ("Councils responded with governance, not enthusiasm.",
          "67% of municipal leaders report actively integrating AI; the agenda item is the use policy, and the objection is hallucination."),
         ("So the adoptable form is citation-first.",
          "A tool that shows the page the answer came from clears an AI-use policy. A tool that summarizes without one does not.")]
yy = y
for i, (lead, rest) in enumerate(items):
    chip(s, ML, yy + Inches(0.04), str(i + 1), fill=ACCENT, w=Inches(0.3))
    t = tb(s, ML + Inches(0.55), yy, Inches(10.6), Inches(0.9))
    para(t, lead, 16, INK, bold=True, first=True, line=1.25)
    para(t, rest, 13.5, BODY, space_before=6, line=1.35)
    yy += Inches(1.12)
t = tb(s, ML, yy + Inches(0.1), Inches(11.2), Inches(0.5))
para(t, "The window is the gap between incumbents serving staff and someone serving the official.",
     15, INK, bold=True, first=True, line=1.3)
foot(s, "CivicPlus/Granicus AI releases 2026; EY 2025 municipal-leader survey; civiciq.com, \"Government AI Adoption in 2026.\"")

# ============================================================ 6. product
s = new()
y = head(s, "the product", "Ask a question. See the page it came from.",
         "Three surfaces, one job: walk into the meeting knowing the record. Built and live today.")
mods = [("Ask Strata", "Plain-language Q&A over the city's own budgets, ordinances, minutes "
         "and contracts. Every answer resolves to a specific document page.",
         "Outcome: the question you had at 10pm, answered before the meeting."),
        ("Meeting Prep", "Each agenda item briefed with its own history and what it has cost "
         "the city before.", "Outcome: hours of packet reading become minutes of reading that matters."),
        ("City Snapshot", "One page: revenue, spending, tax rates, payroll by position.",
         "Outcome: a new board volunteer is useful in their first month, not their first year.")]
for i, (name, desc, out) in enumerate(mods):
    x = ML + i * Inches(3.85)
    card(s, x, y, Inches(3.6), Inches(2.85))
    rule(s, x, y, Inches(3.6), ACCENT, Pt(3))
    t = tb(s, x + Inches(0.28), y + Inches(0.32), Inches(3.05), Inches(2.3))
    para(t, name, 18, INK, bold=True, first=True)
    para(t, desc, 12.5, BODY, space_before=10, line=1.32)
    para(t, out, 12, ACCENT, space_before=10, line=1.3, italic=True)
t = tb(s, ML, y + Inches(3.15), Inches(11.2), Inches(0.5))
para(t, "Setup is on us. The city does not change how it works, and nothing migrates.",
     14.5, INK, bold=True, first=True)
foot(s, "stratacivicsolutions.com — /what-is-strata, /how-it-works (fetched 30 Aug 2026).")

# ============================================================ 7. trust — full bleed
s = new(paper=False)
bg(s, INK)
strata(s, ML, Inches(1.5), ACCENT, widths=(1.35, 0.95, 0.6), gap=0.13, thick=Pt(3))
t = tb(s, ML, Inches(2.35), Inches(11.0), Inches(2.0))
para(t, "“An answer you cannot check\nis an answer you cannot use.”",
     40, WHITE, bold=True, first=True, line=1.18)
t2 = tb(s, ML, Inches(4.55), Inches(10.2), Inches(1.4))
para(t2, "The citation is not a feature of the product. It is the product. The official "
         "verifies the page and then speaks — so the vote, the discussion and the judgment "
         "stay exactly where the law puts them.", 16, RGBColor(0xB6, 0xC1, 0xC8), first=True, line=1.42)
t3 = tb(s, ML, Inches(6.1), Inches(10.2), Inches(0.6))
para(t3, "Strata assists; it does not draft the record or determine the vote. An error is an "
         "embarrassment and a churn event — not statutory liability. That boundary is a design decision.",
     12.5, ACCENT, first=True, line=1.35)
foot(s, "stratacivicsolutions.com, quoted verbatim; liability framing per research/spaces/GOVTECH_MUNICIPAL.md.", dark=True)

# ============================================================ 8. buyer & procurement
s = new()
y = head(s, "who buys, and how fast", "One city manager can sign this.",
         "Texas requires competitive bidding above $50,000. Our top tier is $18,000. "
         "That is a design decision, not an accident.")
card(s, ML, y, Inches(11.3), Inches(1.55), fill=WHITE)
t = tb(s, ML + Inches(0.3), y + Inches(0.24), Inches(10.7), Inches(0.4))
para(t, "ANNUAL CONTRACT VALUE AGAINST THE §252.021 COMPETITIVE-BIDDING THRESHOLD", 9.5, ACCENT, bold=True, first=True)
bar_y = y + Inches(0.78)
rule(s, ML + Inches(0.3), bar_y + Inches(0.42), Inches(10.7), RULE, Pt(1))
scale = 10.7 / 55000.0
for val, lab in [(3600, "Starter\n$3,600"), (9600, "Core\n$9,600"), (18000, "Growth\n$18,000")]:
    bx = ML + Inches(0.3) + Inches(val * scale)
    ln = rule(s, bx, bar_y + Inches(0.18), Inches(0.035), ACCENT, Pt(18))
    tt = tb(s, bx - Inches(0.5), bar_y - Inches(0.16), Inches(1.0), Inches(0.3), PP_ALIGN.CENTER)
    para(tt, lab.split("\n")[1], 11, INK, bold=True, first=True, align=PP_ALIGN.CENTER)
tx = ML + Inches(0.3) + Inches(50000 * scale)
rule(s, tx, bar_y + Inches(0.02), Inches(0.02), FLAG, Pt(58))
tt = tb(s, tx - Inches(3.1), bar_y + Inches(0.5), Inches(3.05), Inches(0.4), PP_ALIGN.RIGHT)
para(tt, "$50,000 — bid required above this line", 10, FLAG, bold=True, first=True, align=PP_ALIGN.RIGHT)
y2 = y + Inches(1.85)
bullets(s, ML, y2, Inches(5.4), [
    ("Economic buyer: the city manager. ", "Controls the software line and can sign alone below the threshold."),
    ("Champion and user: mayors, council, boards. ", "They feel the pain; they do not hold the budget."),
    ("Gatekeepers: the clerk, and IT in 50k+ cities. ", "Ally or blocker — and a security questionnaire."),
], size=13.5)
bullets(s, ML + Inches(5.85), y2, Inches(5.4), [
    ("Demo to signature: 4–8 weeks. ", "Not a procurement season."),
    ("Buying window is Aug–Sep. ", "Texas fiscal years start Oct 1; budgets adopt just before."),
    ("No sales tax, no per-seat fees. ", "Municipalities are exempt (Tex. Tax Code §151.309); pricing is by population tier."),
], size=13.5)
foot(s, "Tex. Loc. Gov't Code §§252.021, 252.0215; Tex. Tax Code §151.309; research/spaces/GOVTECH_MUNICIPAL.md.")

# ============================================================ 9. team
s = new()
y = head(s, "team", "Our senior advisor was mayor of our reference city. Twice.",
         "Elected officials buy from people who have sat in their chair. In this category the "
         "differentiated asset is distribution, not technology.")
people = [("Ralph Gutierrez", "Senior Municipal Advisor",
           "Two-term mayor and council member of Schertz — our demo city. ~50 years public "
           "service, USAF veteran, 20 years of federal judiciary leadership."),
          ("Raquel Gutierrez", "Municipal Outreach Advisor",
           "30+ years of Central Texas civic engagement. Drives municipal partnerships and "
           "pilot development — the warm-intro channel is hers."),
          ("Holly Richard", "Founder / CEO",
           "Doctor of Physical Therapy; previously built healthcare and fitness businesses. "
           "An outsider to govtech — which is why the product is built for the official, not the staff.")]
for i, (nm, role, bio) in enumerate(people):
    x = ML + i * Inches(2.9)
    card(s, x, y, Inches(2.68), Inches(2.7))
    rule(s, x, y, Inches(2.68), ACCENT, Pt(3))
    t = tb(s, x + Inches(0.24), y + Inches(0.3), Inches(2.2), Inches(2.2))
    para(t, nm, 15, INK, bold=True, first=True, line=1.15)
    para(t, role.upper(), 9.5, ACCENT, bold=True, space_before=4)
    para(t, bio, 11.5, BODY, space_before=9, line=1.3)
flagbox(s, ML + Inches(8.7), y, Inches(2.6), Inches(2.7),
        "[ NEEDS JOSELEOS ]",
        ["Helena Carre, Founder / CTO — no published bio.",
         "A blank CTO on an investor deck is a live objection, not a gap.",
         "Also missing: Holly's own account of why municipal records."])
t = tb(s, ML, y + Inches(2.95), Inches(11.2), Inches(0.5))
para(t, "A former mayor's recommendation is how you get into 230 city halls. It is not "
        "purchasable at any seed size.", 14.5, INK, bold=True, first=True, line=1.3)
foot(s, "stratacivicsolutions.com /company/team; Strata market & competitive research, 30 Aug 2026, §2.5.")

# ============================================================ 10. traction
s = new()
y = head(s, "where we actually are", "Live product. One demo city. Zero paying customers.",
         "Said first, with dates, because the alternative is having it discovered.")
rows = [["Product", "Built and live — Ask Strata, Meeting Prep, City Snapshot in production",
         "Aug 2026", "Company site"],
        ["Reference city", "Schertz, TX (~50k) — live demo city with cached example queries; "
         "has not committed to paying", "Aug 2026", "Site + joseleos"],
        ["Customer discovery", "4 council interviews completed", "Jun 2026", "HermesX note — second-hand"],
        ["Entity", "Delaware Public Benefit Corporation, foreign-qualified in Texas", "Aug 2026", "joseleos"],
        ["Revenue", "$0. Zero paying cities is an explicit model input, not an oversight.", "—", "MODEL.md"],
        ["Pipeline", "NOT DISCLOSED — no verified commitments, LOIs or pilots in flight", "—", "NEEDS JOSELEOS"]]
cols_col = [[None] * 4] * 5 + [[FLAG, FLAG, FLAG, FLAG]]
grid(s, ML, y, ["", "Status", "As of", "Source"], rows, [2.2, 6.0, 1.15, 1.95],
     size=12, colors=cols_col)
t = tb(s, ML, Inches(6.15), Inches(11.2), Inches(0.4))
para(t, "No usage metric appears on this deck because no one has given us a verified one. "
        "A number we cannot defend is worth less than the blank.", 13, INK, bold=True, first=True, line=1.3)
foot(s, "product/FINANCIAL_BRIEF_STRATA.md; product/finance/strata/MODEL.md; joseleos 30 Aug 2026.")

# ============================================================ 11. competition
s = new()
y = head(s, "the field", "Everyone else built AI for the people who prepare the meeting.",
         "Full disclosure — the category is young but no longer empty.")
rows = [["Strata", "Elected & appointed officials", "Prep before a vote, cited answers", "1 demo city, pre-revenue", "—"],
        ["Ordinal AI", "Officials + staff, multi-dept", "Research, live meeting Q&A, public chatbot", "$1M seed; 7+ live cities", "High"],
        ["CivicSummary", "Public + officials", "Summaries + follow-through tracking", "Early pilots (West Hollywood)", "Medium"],
        ["Aware", "Public, press, residents", "Post-meeting summaries, news digest", "3,800+ cities claimed; thin usage", "Low–Med"],
        ["CivicPlus", "City staff", "AI-assisted agenda & minutes drafting", "Large installed base; AI as upsell", "Med–High"],
        ["Granicus", "City staff, larger governments", "Records & comms summarization", "Entrenched enterprise incumbent", "Medium"],
        ["OpenGov", "Finance & budget staff", "Budgeting, ERP, performance reporting", "Well-funded incumbent", "Low"],
        ["Ctrl+F", "Everyone, today", "Find the word, hope it is the right one", "Free. Universally deployed.", "The one to beat"]]
colors = [[ACCENT, None, None, None, ACCENT]] + [[None] * 5] * 6 + [[FLAG, None, None, None, FLAG]]
grid(s, ML, y, ["Vendor", "Primary buyer", "Core job", "Scale signal", "Overlap"], rows,
     [1.75, 2.55, 3.15, 2.6, 1.45], size=10.5, row_h=Inches(0.34), colors=colors)
foot(s, "Strata market & competitive research, 30 Aug 2026, §5 — sources cited inline in that brief.")

# ============================================================ 12. business model
s = new()
y = head(s, "business model", "$3,600 to $18,000 a year. 89% gross margin.",
         "Population-tiered annual subscription. No per-seat fees — the category norm, and the "
         "reason a whole council and every board volunteer can use it on one contract.")
tiers = [("Starter", "$3,600", "Smallest cities. Under 10,000."),
         ("Core", "$9,600", "The modeled ACV. Cities 10,000–50,000 — our beachhead tier."),
         ("Growth", "$18,000", "Larger cities, more boards, more packet volume.")]
for i, (nm, price, note) in enumerate(tiers):
    x = ML + i * Inches(2.65)
    card(s, x, y, Inches(2.45), Inches(1.85), fill=(TINT if i == 1 else WHITE),
         edge=(ACCENT if i == 1 else RULE))
    t = tb(s, x + Inches(0.24), y + Inches(0.26), Inches(2.0), Inches(1.4))
    para(t, nm.upper(), 10, ACCENT, bold=True, first=True)
    para(t, price, 27, INK, bold=True, space_before=5)
    para(t, note, 11.5, BODY, space_before=7, line=1.28)
card(s, ML + Inches(8.05), y, Inches(3.25), Inches(1.85), fill=INK, edge=INK)
t = tb(s, ML + Inches(8.3), y + Inches(0.26), Inches(2.8), Inches(1.4))
para(t, "GROSS MARGIN", 10, ACCENT, bold=True, first=True)
para(t, "89%", 34, WHITE, bold=True, space_before=3)
para(t, "COGS is ≈$75/city/month — inference and retrieval. It scales with packet volume, "
        "not seats.", 10.5, RGBColor(0xB6, 0xC1, 0xC8), space_before=6, line=1.28)
y2 = y + Inches(2.12)
bullets(s, ML, y2, Inches(5.4), [
    ("Annual invoice, ACH or check. ", "Onboarding $500–1,500, waived for pilots."),
    ("Usage bundled. ", "An official who uses it twice a week costs the same as one who uses it twice a year."),
], size=13.5)
bullets(s, ML + Inches(5.85), y2, Inches(5.4), [
    ("ACV is capped by design. ", "Everything stays under the $50k bid threshold, which is what makes the 4–8 week cycle possible."),
    ("Retention is budget-line retention. ", "Model uses 0.6%/mo logo churn ≈93%/yr; the 90–95% public-sector figure is vendor-reported, low-confidence."),
], size=13.5)
foot(s, "product/finance/strata/MODEL.md (engine v1, base case); GTM pricing table §4.")

# ============================================================ 13. market
s = new()
y = head(s, "market", "230 Texas cities in our tier. We counted them one at a time.",
         "Bottom-up only. The national number is shown for context and is deliberately not modeled.")
bars = [("230", "Texas cities, 10k–50k pop.", 3.8, ACCENT,
         "× $9,600 Core  =  ≈ $2.2M SAM"),
        ("1,224", "Texas municipalities, all sizes", 5.6, RGBColor(0x6E, 0x9E, 0x97),
         "The state expansion path, unmodeled"),
        ("19,519", "U.S. municipalities (+16,360 towns)", 8.1, RGBColor(0xC3, 0xD8, 0xD3),
         "Context only. We do not claim it.")]
yy = y
for big, lab, wdt, col, note in bars:
    r = card(s, ML, yy, Inches(wdt), Inches(0.62), fill=col, edge=col)
    t = tb(s, ML + Inches(0.24), yy + Inches(0.16), Inches(wdt - 0.42), Inches(0.4))
    para(t, big + "  ·  " + lab, 13, (WHITE if col == ACCENT else INK), bold=True, first=True)
    t2 = tb(s, ML + Inches(8.5), yy + Inches(0.16), Inches(2.8), Inches(0.4))
    para(t2, note, 12.5, (INK if col == ACCENT else MUTED), bold=(col == ACCENT), first=True)
    yy += Inches(0.8)
t = tb(s, ML, yy + Inches(0.26), Inches(11.2), Inches(1.2))
para(t, "A $2.2M beachhead is a small number and we are not going to dress it up.", 16, INK, bold=True, first=True)
para(t, "It is the number we can defend, city by city, against a published population table. "
        "If a fund needs a national TAM underwritten today, this is the wrong stage of this company.",
     13.5, BODY, space_before=9, line=1.35)
foot(s, "research/spaces/GOVTECH_MUNICIPAL.md (TX counts); U.S. Census / National League of Cities via Strata research brief §4.1.")

# ============================================================ 14. the plan
s = new()
y = head(s, "the plan", "Thirty-one cities and break-even in month 19 — on founder effort alone.",
         "Base case from the accepted three-year model. Founder pay is deferred and no financing "
         "appears in any scenario.")
rows = [["Year 1 (FY27)", "5.4", "$26,660", "−$13,104", "−$3,104"],
        ["Year 2 (FY28)", "14.8", "$103,894", "−$16,398", "−$19,502"],
        ["Year 3 (FY29)", "31.2", "$248,290", "+$51,103", "+$31,600"]]
grid(s, ML, y, ["", "Paying cities (end)", "Revenue", "Operating income", "Ending cash"],
     rows, [2.6, 2.3, 2.2, 2.3, 1.9], size=13, row_h=Inches(0.48))
y2 = y + Inches(1.85)
facts = [("Month 19", "first month of positive operating income"),
         ("≈$325k", "ARR run-rate exiting month 36"),
         ("$1,225", "CAC, paid back in 1.7 months")]
for i, (big, lab) in enumerate(facts):
    x = ML + i * Inches(3.85)
    card(s, x, y2, Inches(3.6), Inches(1.1), fill=WHITE)
    t = tb(s, x + Inches(0.26), y2 + Inches(0.22), Inches(3.1), Inches(1.0))
    para(t, big, 26, ACCENT, bold=True, first=True, line=1.0)
    para(t, lab, 12, BODY, space_before=7, line=1.28)
t = tb(s, ML, Inches(6.15), Inches(11.3), Inches(0.4))
para(t, "Five assumptions move this answer:  opening cash ($10k) · new cities/mo (0.35, +5%) · "
        "ACV ($9,600 Core) · hire timing (contractor m13, engineer m28) · COGS ($75/city/mo).",
     11, INK, bold=True, first=True, line=1.28)
foot(s, "product/finance/strata/MODEL.md — engine v1, deterministic; upside and downside in the appendix.")

# ============================================================ 15. risk
s = new(paper=False)
bg(s, INK)
y = head(s, "what kills us", "The risks, from the one you will ask about to the one that "
         "actually ends it.", dark=True)
risks = [("OUTER — market", "“Isn't this a feature CivicPlus ships next quarter?”",
          "It already did — for staff. Our user has no seat in those systems and no staff. An "
          "incumbent would have to build a different product for a different person and sell it "
          "into a body that did not procure it.", PALE),
         ("MIDDLE — competition", "Ordinal AI is funded and ahead.",
          "$1M seed, 7+ live cities, and a broader surface: planners, clerks, code enforcement, "
          "311, plus a public chatbot. Broad and shallow. We are narrow and deep on one buyer "
          "inside the same building.", PALE),
         ("INNER — execution", "One founder, 0.35 cities a month, and a $29,069 cash trough at month 18.",
          "This is the one that actually ends it, and it is the reason the ask on the next slide "
          "is the size it is. Hire timing is the most sensitive input in the model; an earlier "
          "draft that hired an engineer at month 16 sank the base case to −$101k.", WHITE)]
yy = y
for tag, q, a, col in risks:
    inner = tag.startswith("INNER")
    chip(s, ML, yy + Inches(0.02), tag, fill=(FLAG if inner else ACCENT), w=Inches(0.16 * len(tag) + 0.3))
    tx0 = ML + Inches(0.16 * len(tag) + 0.55)
    t = tb(s, tx0, yy - Inches(0.03), W - MR - tx0, Inches(0.9))
    para(t, q, 16, (WHITE if inner else RGBColor(0xD8, 0xDF, 0xE4)), bold=True, first=True, line=1.25)
    para(t, a, 12.5, (RGBColor(0xC9, 0xD1, 0xDA) if inner else RGBColor(0x92, 0x9E, 0xA9)),
         space_before=6, line=1.35)
    yy += Inches(1.45)
foot(s, "product/finance/strata/MODEL.md sensitivities; pitch/strata/objections.md.", dark=True)

# ============================================================ 16. the ask
s = new(paper=False)
bg(s, INK)
strata(s, ML, Inches(0.75), ACCENT, widths=(1.35, 0.95, 0.6), gap=0.13, thick=Pt(3))
t = tb(s, ML, Inches(1.5), Inches(11.0), Inches(1.4))
para(t, "We do not need a round.\nWe need $40,000 and five pilot cities.", 34, WHITE, bold=True,
     first=True, line=1.18)
t2 = tb(s, ML, Inches(3.15), Inches(6.6), Inches(3.0))
para(t2, "USE OF FUNDS — TRACED TO THE MODEL", 10, ACCENT, bold=True, first=True)
for lead, rest in [("≈$29k  ", "covers the cash trough — the base case bottoms at −$29,069 in month 18"),
                   ("$11.7k  ", "year-1 sales and marketing: the TML annual conference plus about one regional event a month"),
                   ("$6k  ", "formation and Texas foreign qualification"),
                   ("$10.6k  ", "G&A — the $1M GL + cyber certificate cities require before data access, accounting, software")]:
    p = t2.add_paragraph(); p.space_before = Pt(9); p.line_spacing = 1.32
    r = p.add_run(); r.text = lead
    r.font.size = Pt(13.5); r.font.bold = True; r.font.color.rgb = WHITE; r.font.name = FONT
    r2 = p.add_run(); r2.text = rest
    r2.font.size = Pt(13); r2.font.color.rgb = RGBColor(0xB6, 0xC1, 0xC8); r2.font.name = FONT
p = t2.add_paragraph(); p.space_before = Pt(12); p.line_spacing = 1.3
r = p.add_run(); r.text = "What it unlocks:  five pilot cities converting in months 4–9, the first paying cities by month 6, and positive operating income from month 19 without a second raise."
r.font.size = Pt(12.5); r.font.color.rgb = ACCENT; r.font.name = FONT
flagbox(s, ML + Inches(7.05), Inches(3.15), Inches(4.25), Inches(3.1),
        "[ NEEDS JOSELEOS — THE ONE OPEN DECISION ]",
        ["$40k is the only ask the accepted model supports: bootstrapped, no financing in any scenario.",
         "If you want an institutional round instead, say the number and the model has to be re-run financed before this slide is true.",
         "If the deck is for pilots and partners rather than capital, the ask becomes five pilot slots and the dollar figure comes off."])
foot(s, "product/finance/strata/MODEL.md — capital need $29,069 base / $32,738 upside / $31,557 downside; ≈$40k from launch in every scenario.", dark=True)

# ============================================================ A1. scenarios
s = new()
y = head(s, "appendix 1", "All three scenarios, side by side.",
         "The engine is deterministic; cash and personnel reconcile every period.")
rows = [["3-year revenue", "$378,843", "$922,560", "$107,511"],
        ["Paying cities at month 36", "31.2", "71.3", "10.7"],
        ["Ending cash, month 36", "$31,600", "$309,645", "−$4,472"],
        ["Capital need to break-even", "$29,069", "$32,738", "$31,557"],
        ["First month operating income ≥ 0", "7", "4", "15"],
        ["Gross margin", "89.0%", "91.0%", "79.0%"],
        ["ACV", "$9,600", "$11,000", "$7,200"],
        ["CAC / payback", "$1,225 / 1.7 mo", "$592 / 0.7 mo", "$3,009 / 6.3 mo"],
        ["Net revenue retention", "98.0%", "103.0%", "88.0%"],
        ["What it assumes", "0.35 cities/mo +5%/mo; contractor m13, engineer m28",
         "0.5 cities/mo +7%/mo; Core-heavy mix; hires pulled forward",
         "0.2 cities/mo; discounting to $7.2k; 1.2%/mo churn; never hires"]]
grid(s, ML, y, ["Metric", "Base", "Upside", "Downside"], rows, [3.5, 2.6, 2.6, 2.6],
     size=11.5, row_h=Inches(0.35))
foot(s, "product/finance/strata/MODEL.md, engine v1 (30 Aug 2026). Estimates for planning; not investment advice.")

# ============================================================ A2. procurement
s = new()
y = head(s, "appendix 2", "How a Texas city actually buys this.",
         "The mechanics that shaped the pricing, the calendar and the cost model.")
bullets(s, ML, y, Inches(5.4), [
    ("Competitive bidding above $50,000. ", "Tex. Loc. Gov't Code §252.021. Below it the city manager can usually sign; many charters set lower internal thresholds, so we verify per city."),
    ("$3k–$50k needs two HUB quotes where practicable. ", "§252.0215 — a form, not a season."),
    ("Cooperative purchasing is the shortcut for larger cities. ", "BuyBoard, TIPS, DIR — later-stage, not the beachhead motion."),
    ("TX-RAMP binds state agencies, not cities. ", "Tex. Gov't Code §2054.0593 — but cities borrow the questionnaire."),
], size=13)
bullets(s, ML + Inches(5.85), y, Inches(5.4), [
    ("Everything is a public record. ", "Public Information Act, Tex. Gov't Code ch. 552 — contracts and data handling are disclosable. We hold documents the city already published, so there is little that was not public to begin with."),
    ("$1M GL + cyber certificate before data access. ", "A routine precondition — an early G&A line in the model, not a later one."),
    ("Buying and renewal cluster Aug–Sep. ", "Texas city fiscal years mostly begin Oct 1 (Loc. Gov't Code ch. 102)."),
    ("Channels: TML, TCMA, ELGL. ", "TML annual conference 11–13 Nov 2026, San Antonio. Advisor-led warm intros are the highest-ROI channel at zero budget."),
], size=13)
foot(s, "research/spaces/GOVTECH_MUNICIPAL.md — statutes cited inline.")

# ============================================================ A3. open items — internal
s = new()
y = head(s, "internal — pull before any external meeting",
         "Six things this deck does not know.",
         "The pitch-deck skill forbids inventing a metric. Each item below is a hole we left "
         "visible rather than filled.")
rows = [["1", "Founder story", "Holly's own account of why municipal records. The team slide is complete but flat without it.", "joseleos"],
        ["2", "CTO bio", "Helena Carre has no published bio. Researcher flagged it as a website trust gap; on this deck it is a live objection.", "joseleos"],
        ["3", "Traction specifics", "Schertz usage, verbal commitments, LOIs, pilots in flight. Slide 10 says \"not disclosed\" because nothing is verified.", "joseleos"],
        ["4", "The ask", "$40k is the only figure the accepted model supports. An institutional round needs a financed model re-run before slide 16 is true.", "joseleos"],
        ["5", "Pricing contradiction", "The model prices Core at $9,600; the June/July meeting notes floated ~$50k/yr and a ~$20k 60-day pilot. Both cannot be true — and $50k breaks the no-bid design.", "joseleos + HermesX"],
        ["6", "Missing GTM source", "Strata_GTM_Strategy.docx and Strata_Market_Research.docx are cited by the brief but are not on disk. Positioning here was rebuilt from the space profile and the BMC.", "HermesX"]]
grid(s, ML, y, ["", "Item", "Why it matters", "Owner"], rows, [0.5, 2.3, 6.85, 1.65],
     size=11.5, row_h=Inches(0.4))
foot(s, "pitch/strata/foundation.md §Gate 1; pitch/strata/objections.md Q16–Q18.")

prs.save(OUT)
print("saved:", OUT, "slides:", len(prs.slides._sldIdLst))
