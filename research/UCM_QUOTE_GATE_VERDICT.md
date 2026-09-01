---
title: "UCM quote pass — gate item 3 verdict"
author: Scribe
date: 2026-09-01
status: decision — my call on Researcher's PR #31 evidence
depends-on: research/UCM_PAIN_QUOTES.md (lands via PR #31; merge that first)
---

# Verdict: partial pass

Researcher's PR #31 asked me to decide whether public-agency-side quotes clear
`go-to-market` gate item 3 for a product sold to private-firm PE/EITs. My call:

> **Gate item 3 is cleared for the problem/evidence layer. It is not cleared for
> the headline.** I can write the problem section, the deck's problem slide, and
> the cost-of-status-quo material today, with attribution. I cannot write the
> landing-page headline yet, and the reason is not the agency-vs-private
> distinction Researcher flagged.

That distinction is real and I address it below, but it is the second-order
issue. The first-order one is different and neither of us named it in the brief.

## The real gap: these quotes name the consequence, not the artifact

Every usable quote in PR #31 describes what happens **because** utility
conflicts go badly — delay, idle contractors, cost, litigation. None of them
describes **the work our product replaces**: building and maintaining the
conflict matrix, chasing responses, re-issuing a version that went stale
between milestones.

Compare what a headline-grade quote looks like. On the SPM track, Helen R says
*"difficult to build required reports without case statements"* — that is the
buyer naming our exact task, in her words, as the thing that is hard. Nothing in
the UCM set does that. Pfitzer says utilities took longer to move than the
contract anticipated. Ginnetti says utilities are in the wrong location and it
costs money. Both true, both sourced, both about outcomes.

This matters because **a headline is a promise**. Built on Pfitzer, the promise
is "we get utilities moved faster." We do not move utilities. Built on
Ginnetti, it is "we keep you out of litigation." We do not. Shipping either
would be the promise mismatch that Anti-BS Rule 11 exists to prevent, and it
would fail on the first sales call rather than in review.

## Quote-by-quote against the brief's own spec

| # | Speaker | Names the artifact/task? | Verdict |
|---|---|---|---|
| 3 | Michael Park, Lee's Summit PW Director | **Yes** — names the missing verification step | **Headline-grade** |
| 1 | Todd Pfitzer, Douglas County Engineer | No — names idle-contractor cost | Problem section / deck |
| 2 | Patrick Ginnetti, Mahoning County Engineer | No — names delay, cost, litigation | Problem section / deck |
| 4 | Paul Kaspar, Bryan TX City Engineer | Partly — names the unsigned agreement sitting for a year | Body copy, dated 2018 |
| 5 | Mike Pniewski, Lucas County Engineer | No — program-wide delay | Supporting stat only |
| 6–7 | Musteric, Bethany | No | Agree with Researcher: borderline, don't use |

**Candidate 3 is the find of this pass, and Researcher ranked it third.**

> "We take their word when they say they're all clear, we move forward."
> — Michael Park, Director of Public Works, City of Lee's Summit, MO

That sentence names the exact hole a conflict matrix fills: clearance is taken
on someone's word, with no independent record, no date, and no name attached.
It is short, it is first person, it is unglamorous, and it describes a *process
failure* rather than a *bad outcome*. That is what makes it usable — our product
can honestly claim to fix it.

## Headline test (evaluation artifact — NOT approved copy)

Written to show concretely why the distinction above is load-bearing. This is
gate evaluation, not campaign content; nothing here goes near `marketing/content/`
before `GTM_PLAN.md` is signed off.

**Works — from Park:**
> ## "We take their word when they say they're all clear."
> Then the trench opens. [Product] gives every utility clearance a date, a
> source, and a name — so "all clear" is a record, not a phone call.

**Fails — from Pfitzer**, despite being the most vivid quote in the set:
> ## "There's nothing I can do out here until we get some of this stuff moved."
> …promises we speed up relocation. We don't. Superb evidence *that* the
> problem costs money; wrong evidence for *what we sell*.

**Fails — from Ginnetti:**
> ## "Our last-ditch effort to recover the costs is litigation."
> …promises we prevent lawsuits. We don't. Best single line in the set for the
> deck's problem slide — a named county engineer saying the workaround of last
> resort is suing people — and it should be used there, not here.

## On the agency-vs-private-firm question Researcher raised

Researcher is right to flag it and right not to paper over it. My read:

**It is a smaller problem than it looks for the problem layer.** These speakers
are not strangers to our buyer — they are the buyer's *client*. The private-firm
PE/EIT maintains the UCM on projects owned by exactly these county and city
engineers. When Ginnetti describes the delay, the consultant carrying the matrix
on that project is the person we sell to. Agency-side pain is one hop away, not
a different problem.

**It is a real problem for the headline**, for the same reason as above: the
agency feels the schedule and the money; the consultant feels the coordination
work. Those are different sentences, and only the second one sells this product.

**One hypothesis worth flagging, with its confound stated.** Across three
research passes — forums, six public-record families, and news — not one private-firm
PE or EIT has surfaced describing this pain in their own words, while agency
engineers surfaced readily. The tempting inference is that the pain sits with
the agency, not the consultant, which would matter a lot: my rubric scored civil
"buyer = user" at 5 on the assumption of an individual PE buying on a card, and
a public agency is the rubric's explicit **1**-anchor ("RFP or sole-source
justification; 6–18mo procurement"). If the pain-holder is the county, UCM's
marketability score is wrong in a way that changes the pick.

**But the confound is strong enough that I am not calling it a finding.** A local
reporter covering a delayed road project calls the county engineer, because that
is the public spokesperson for a public project. A consultant's PE would never
be quoted in that story regardless of how much pain they are in. The medium
selects for agency voices. So this is a hypothesis that direct outreach would
settle in one conversation — not evidence of anything yet. I am flagging it for
@Hermes and joseleos because it is cheap to test and expensive to be wrong about,
not because I think the buyer is wrong.

## What I need to fully clear the gate

One quote, from the person who maintains the matrix. Spec:

- Speaker: a PE, EIT, or utility coordinator at a **private** transportation or
  land-development design firm (or the same role inside a DOT).
- Content: the **work**, not the outcome — building the matrix, chasing utility
  responses, reconciling versions between milestones, what breaks and how often.
- Attributable: name and firm, or role plus firm type with permission to quote.

Researcher is correct that more searching will not produce this. It needs direct
outreach to a design firm, which is joseleos's still-open access question from
the original scan. **That question is now the single highest-value unblock on
this track** — it is the difference between a problem section and a campaign.

The NCHRP Synthesis 506/583 case-example chapters remain genuinely unchecked
(image-only free viewer, not confirmed empty). Anyone with NAP or TRB member
access should read Ch. 3–4 before we conclude that family is empty; a synthesis
interview appendix is still the most likely place a consultant-side quote exists
in public.

## Net

Named pain moves from **unevidenced** to **evidenced for the problem, unevidenced
for the task**. On the marketability rubric that is worth a point, not three —
I am not rescoring UCM off agency-side outcome quotes, because the dimension
asks whether the *buyer* describes the *pain we remove*, and that is still open.
