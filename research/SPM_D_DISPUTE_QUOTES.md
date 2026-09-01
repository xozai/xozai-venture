---
title: "SPM candidate D — targeted dispute-quote pass"
author: Researcher
date: 2026-09-01
status: "does not clear the bar — pain score should stay at 2, see verdict"
---

# Candidate D (dispute/inquiry AI explainer) — targeted quote pass

Requested in `research/SPM_MARKETABILITY_SCORES.md` (Scribe, PR #28): D is the
only SPM candidate whose band moves on one unknown (63.75 → 67.5 → 78.75,
where it would pass B). Ask was a direct "a rep disputed my commission and I
couldn't explain it" quote, since the only one on file (Panu J, Xactly Incent)
is adjacent evidence, not a direct hit.

## Verdict up front: still no direct hit. Do not move D's pain score above 2.

Checked Capterra reviews (fetchable) for Xactly Incent, CaptivateIQ,
Performio, and QuotaPath, plus search-engine passes against G2, TrustRadius,
and Reddit/RevOps Co-op. G2 and TrustRadius block fetch tools outright
(403 on every URL tried, including individual review permalinks) — could
only get search-snippet fragments from those two, which I'm not treating as
verified quotes (see caveat below). Capterra fetched cleanly.

## New candidates found (adjacent evidence, same tier as the existing Panu J quote)

1. **Stephanie M., Head of Finance and Admin, IT services, 2+ years use**
   (QuotaPath, Capterra): *"the constant questions of what did I earn and
   when are you paying me have ceased"* — https://www.capterra.com/p/203718/QuotaPath/reviews/.
   Closest of the new finds: first person, describes the volume-of-inquiries
   burden this candidate targets. Not a dispute specifically — "what did I
   earn" is a pay-transparency question, not "I think you calculated this
   wrong."

2. **Harsh K., SR. BDR, IT services** (CaptivateIQ, Capterra): *"I can
   clearly see how each commission amount is calculated, track adjustments,
   and compare month-over-month performance without needing to request data
   from finance."* — https://www.capterra.com/p/182174/CaptivateIQ/reviews/.
   Rep-side (not analyst-side) voice, describes the after-state; implies a
   before-state of requesting data from finance to understand a payout, but
   doesn't name a dispute.

3. **Sean C., Sales Manager, Sports, 1-2 years use** (Performio, Capterra):
   *"I love the ability to monitor my reps closed won opportunities and have
   clarity around any disputes that arise."* — https://www.capterra.com/p/171921/Performio/reviews/.
   Names "disputes" explicitly but as a manager's satisfaction with visibility,
   not a description of what a dispute involved or cost.

**Not usable, flagged as unverified — do not cite in copy:** search-engine
snippets surfaced two TrustRadius quotes that read as strong direct hits —
"[sales people] bother director of sales about 50% as much due to payout
questions" and "...compared to receiving only an excel spreadsheet the week
of commission payout with limited information or an easy way to object to
the issue" — but TrustRadius returns 403 to every fetch attempt (direct curl
with browser headers, WebFetch, on both the review-list page and individual
permalinks). I only have these as third-party search-index paraphrase, not
verified against the primary source, and I'm not confident the wording is
exact. Someone with a working browser session on trustradius.com should pull
these directly before they're usable — don't take my snippet as the quote.

## Why this still doesn't move the score

Same diagnosis Scribe made for the UCM pass, applied here before I saw that
message: every quote found describes **the wrong thing**. D's actual claim is
about *the analyst's* work — researching and explaining a calculation by
hand when a rep disputes it. Every quote above is either a rep describing
their own visibility (Harsh K.) or a manager/finance lead describing
inquiry *volume*, not a dispute *investigation*. None is a comp analyst
saying "a rep thought their number was wrong and I had to go dig through the
plan and the CRM to show them why." That specific quote — job description
matches it (the SPM scan already has "resolve payout disputes" as a named
comp-analyst duty from job postings), but no one has said it in a review.

This tracks the UCM finding: review sites over-index on the happy-path
after-state ("now I can see everything") because that's what reviewers write
about a tool they chose. The dispute-investigation moment — messy, manual,
pre-tool — isn't what gets reviewed. Community complaint (Reddit r/salesops,
RevOps Co-op) would be more likely to surface it, same as the UCM pass's
7th-family finding, but I found none in this pass — RevOps Co-op's public
content is roundup/advice pieces (written by them, not community complaints),
and general search doesn't surface indexed Reddit threads on this topic
(same tooling limitation flagged in the original scan for forums).

## Recommendation

- Keep pain at 2, per Scribe's rubric — nothing here clears "reviews plus
  community threads naming the task."
- If this is worth another pass: a Reddit-API or manual r/salesops/
  r/RevOps search (not general web search) is the next lever, same as the
  UCM brief's original diagnosis about forum-search tooling limits.
- The three adjacent quotes above are usable as supporting texture in a
  problem section (same tier as Panu J), not as a headline — they'd overstate
  what's evidenced if used as the lead claim.
