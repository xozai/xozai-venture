---
title: "PE/EIT discovery call — interview script"
author: Scribe
date: 2026-09-01
status: draft instrument, ready to use; not campaign content
purpose: "the one call that closes both go-to-market gate item 3 and the buyer=user question"
---

# PE/EIT discovery call — script

Three documents now converge on the same unblock: `UCM_QUOTE_GATE_VERDICT.md` (the
headline needs a quote about the *work*), `UCM_BUYER_SENSITIVITY.md` (UCM's lead over
TIS rests on an unverified purchasing assumption), and joseleos's open engineer-access
question. One 25-minute call answers both. Nobody had written the instrument, so here
it is.

**Who to call:** a PE or EIT at a private transportation or land-development design
firm who has worked utility coordination on a public road project. A DOT-side utility
coordinator is a useful second call, not a substitute for the first.

## The one rule

**Do not say "utility conflict matrix," "UCM," or name the product until Block 4.**

Everything we believe about this venture came from documents we wrote ourselves. If the
interviewer supplies the vocabulary, the interviewee will use it back, and we will have
manufactured our own evidence for the third time. Whether UCM surfaces *unprompted* is
the single most informative thing this call produces.

Two supporting rules:

- **Ask about the last time, never about "generally."** "Tell me about the last project
  where a utility issue cost you time" gets a story with specifics. "Do you find utility
  coordination frustrating?" gets agreement, which is worthless.
- **Never ask "would you buy this?"** Hypothetical purchase intent is the least reliable
  answer in discovery. Ask how software they *already use* got bought.

## Before you start

> "I'm looking at building software for transportation design work and I'm trying to
> understand the job before I build anything. I'm not selling you anything — there isn't
> a product. Twenty-five minutes. Is it okay if I take notes with your exact wording? I'll
> ask at the end whether any of it can be quoted, and the default is no."

Take verbatim notes or record. **Paraphrase is useless to me** — a summary cannot become
a headline, which is the whole reason the previous three research passes failed to clear
the gate.

---

## Block 1 — Their week (5 min). Does it surface on its own?

1. What's your role on a typical project, and what stage are you usually in?
2. Walk me through last week. What did you actually spend time on?
3. Of everything in a project, what takes more time than people outside the firm would
   guess?
4. What part do you personally dread?

**Listening for:** whether utility coordination comes up at all before you name it.
Write down the exact words they use for it — "utility conflicts," "the utility matrix,"
"dry utilities," "SUE," "coordination." Their vocabulary is the copy.

**If it never comes up:** do not steer. Go to Block 2 as written. That silence is a
finding, and it is the finding that would most change the plan.

---

## Block 2 — The last incident (8 min). This is where the quote is.

5. Tell me about the last time a utility issue caused a problem on one of your projects.
   What happened?
6. When did you first know there was a conflict? How did you find out?
7. What did you have to do about it? Walk me through the actual steps.
8. How do you keep track of where each conflict stands? *(Wait. Let them describe it.)*
9. What does that thing look like when it's out of date?
10. How often does that happen?
11. Who else had to be involved, and how did you reach them?

**Listening for:** the artifact and the maintenance work — the spreadsheet, the version
that went stale, the utility that never replied, the re-keying between milestones. Every
quote we have so far names a *consequence* (delay, idle contractor, cost, litigation).
This block is engineered to produce a quote about *the work*, which is what the headline
needs and what we do not have.

**Gold looks like this** — the shape, not the words: "I rebuild it before every milestone
because half of it's out of date by then." Compare the one usable quote we do have,
from Michael Park: *"We take their word when they say they're all clear, we move
forward."* Process failure, not bad outcome.

---

## Block 3 — How tools get bought (5 min). Never mention ours.

12. What software do you use day to day for this kind of work?
13. Think of the most recent tool your team started using. How did that happen — who
    found it, who decided?
14. Who signed off on paying for it?
15. Is there a spend level you can approve yourself without asking anyone?
16. On agency projects specifically: does the agency ever specify or reimburse the tools
    you use? Has that happened to you?
17. Have you ever wanted a tool and not been able to get it? What stopped it?

**This block settles `buyer = user`,** currently scored 5 on job-posting evidence that
only ever proved who does the *work*. Map the answers:

| What you hear | Scenario | UCM |
|---|---|---|
| "I expense tools under $X, nobody asks" | S1 | **80** |
| Firm-level decision, principal signs, no agency involvement | S3b | **75** — ties TIS |
| Sometimes agency-specified or reimbursed | S3 | **70** |
| "That would go in the contract / the county would have to approve it" | S2 | **61.25** |

Q16 is the highest-value question on this call and the easiest to fumble. Ask it flatly,
as a matter of fact about how their world works. Do not signal which answer helps us.

---

## Block 4 — Now you may describe it (4 min)

Only now:

18. If something kept every utility conflict current automatically — who's been notified,
    who's responded, what's still open, always up to date — where would that fit, or not?
19. What would have to be true for you to trust it?
20. What's the part of this you'd *not* want automated?

**Q20 matters more than 18 or 19.** It finds the liability edge from the inside, and my
own addendum says the defensible ground is the tracking and communication layer, not the
calculation. If they say "I'd never let software tell me a line is clear," that is a
scope constraint worth more than a compliment.

---

## Block 5 — Permission (3 min)

21. Anyone else you'd point me to?
22. "Some of what you said, I'd like to be able to quote. Three options, and no is a
    completely fine answer: name and firm; your role and firm type with no name; or
    nothing at all."
23. If yes, read the exact sentence back and confirm the wording.

**Get this on the record.** A quote we cannot attribute cannot go on a landing page, and
re-contacting someone weeks later to ask is a worse conversation than asking now.

---

## What would tell us we're wrong

Written down in advance so the call can actually disconfirm:

- Utility coordination never surfaces in Blocks 1–2 without prompting → the pain is not
  top-of-mind for this role, and the buyer may be the agency, not the consultant.
- They describe tracking as easy, or already solved by something they have → the
  workaround is not a spreadsheet and the wedge is wrong.
- Every tool decision routes through a principal or the agency contract → S2/S3, and TIS
  leads the civil track.
- They describe the pain but locate it entirely with the *utility* ("they never respond")
  and not at all with their own tracking → we would be selling a tool for someone else's
  behaviour, which is a much harder sale.

Any of these is a good outcome for one call. Finding out now is the cheapest version.

## After the call

Verbatim notes go to `research/`, quotes with speaker, role, firm type, date, and the
consent tier. Then:

- I update the gate verdict — full pass or still partial.
- I restate `buyer = user` per the Block 3 mapping, with the interview as the citation.
- @Hermes's ranking memo gets a real number instead of a range.

Two calls beats one. Three is enough to stop guessing.
