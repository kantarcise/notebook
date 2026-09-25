---
name: shortform-science-angle
description: Make a short-form content script by asking what evidence makes the idea more credible, grounding the script in repo notes, research, scientific framing, and source-linked external claims, then saving it to content/shortform/angles/science/YYYY-MM-DD-<slug>.md.
---

# Shortform Science Angle

Use this skill when the user wants a short-form content script, TikTok/Reels/Shorts draft, or content angle grounded in evidence, research, data, experiments, or scientific framing.

Core question: **What evidence makes this idea more credible?**

## Workflow

1. Identify the topic, claim, or behavior from the user's request. If the claim is materially ambiguous, ask one targeted clarification question.
2. Search repo notes first. Prioritize:
   - relevant topic folders or files
   - `Success/`
   - `Books/`
   - `Personal Brand/` and `content/` when voice, positioning, or prior content matters
3. Extract the user's existing belief, then look for evidence that supports, sharpens, qualifies, or challenges it.
4. Use web research when repo notes do not provide enough credible evidence or when scientific support is needed.
5. External claims must include source links in `Brain Sources`. Prefer:
   - peer-reviewed papers
   - official institutional pages
   - reputable scientific, medical, or academic sources
   - primary datasets or reports when relevant
6. Frame evidence accurately. Do not overclaim causality from correlation, single studies, anecdotes, or preliminary findings.
7. Turn the evidence into a short-form script that is clear, useful, and credible without sounding like a research abstract.
8. Save the output to:
   `content/shortform/angles/science/YYYY-MM-DD-<slug>.md`

Use the current local date for `YYYY-MM-DD`. Create a lowercase kebab-case slug from the topic, evidence, or central claim.

## Output File Format

Each generated file must include:

```markdown
# <Title>

Topic: <topic>
Angle: <one-sentence evidence-backed angle>
Date: YYYY-MM-DD

## Hook

<1-3 opening lines that introduce the evidence or credibility gap>

## Evidence

- <plain-language evidence point with source>
- <plain-language evidence point with source>

## Draft

<short-form script, usually 100-200 words>

## Scientific Framing

- Claim: <what the script claims>
- Evidence Type: <study, review, mechanism, data, expert consensus, repo note, etc.>
- Confidence: <high, medium, or low, with a short reason>
- Caveat: <what the evidence does not prove>

## Examples

- <example, behavior, or analogy grounded in the evidence>
- <example, behavior, or analogy grounded in the evidence>

## CTA

<one clear action, question, or reflection prompt>

## Self-Check Answers

- What evidence makes this idea more credible? <answer>
- Is the evidence strong enough for the claim? <answer>
- What caveat should be included to avoid overclaiming? <answer>
- What should be removed if the script sounds too generic or too academic? <answer>

## Brain Sources

- `<source path>`
- `[source title](https://source-link.example)`
```

## Drafting Guidance

- Make the evidence the engine of the script, not a footnote.
- Translate technical findings into plain language without flattening uncertainty.
- Use numbers only when they improve credibility or clarity.
- If evidence is mixed, make that tension part of the angle.
- Use phrases like "suggests," "is associated with," or "researchers found" when causality is uncertain.
- Do not cite external claims without links.
- Do not invent study details, sample sizes, institutions, dates, or author names.
- Before finalizing, confirm the file exists and that all required sections are present.

