---
name: shortform-story-angle
description: Make a short-form content script by asking what story or quote makes the idea memorable, using repo notes first and source-linked quotes when using the web, then saving the angle to content/shortform/angles/story/YYYY-MM-DD-<slug>.md.
---

# Shortform Story Angle

Use this skill when the user wants a short-form content script, TikTok/Reels/Shorts draft, or content angle built around a memorable story, quote, anecdote, or narrative tension.

Core question: **What story or quote makes the idea memorable?**

## Workflow

1. Identify the topic or idea from the user's request. If the idea is materially ambiguous, ask one targeted clarification question.
2. Search repo notes first. Prioritize:
   - `Books/`
   - `Success/`
   - relevant topic folders or files
   - `Personal Brand/` and `content/` when voice, positioning, or prior content matters
3. Look for quotes, stories, anecdotes, examples, contradictions, turning points, and emotionally loaded lines.
4. Web quotes are allowed and encouraged when repo notes do not contain a strong quote or when a known quote would sharpen the script.
5. Any exact quote from the web must include a source link in `Brain Sources`. Prefer primary or reputable sources.
6. Use the quote or story as the launch point for the script's idea, not as decoration. The script should move from:
   - memorable quote/story
   - tension or problem
   - interpretation
   - practical point for the viewer
7. Save the output to:
   `content/shortform/angles/story/YYYY-MM-DD-<slug>.md`

Use the current local date for `YYYY-MM-DD`. Create a lowercase kebab-case slug from the topic, quote subject, or central claim.

## Output File Format

Each generated file must include:

```markdown
# <Title>

Topic: <topic>
Angle: <one-sentence angle>
Date: YYYY-MM-DD

## Hook

<1-3 opening lines built around the quote, story, or tension>

## Story Or Quote

<the quote, anecdote, or story seed>

## Draft

<short-form script, usually 100-200 words>

## Narrative Tension

- Before: <starting belief, problem, or situation>
- Turn: <moment, quote, conflict, or realization>
- After: <new belief, behavior, or lesson>

## Examples

- <repo-grounded or source-linked example>
- <repo-grounded or source-linked example>

## CTA

<one clear action, question, or reflection prompt>

## Self-Check Answers

- What story or quote makes the idea memorable? <answer>
- How does the story create tension? <answer>
- What practical idea does the viewer leave with? <answer>
- What should be removed if the quote feels decorative? <answer>

## Brain Sources

- `<source path>`
- `[source title](https://source-link.example)`
```

## Drafting Guidance

- Start with the strongest story pressure: surprise, contradiction, loss, risk, ambition, regret, or reversal.
- Keep the script spoken and compact; avoid turning it into a book summary.
- Do not stack quotes. One strong quote or story is usually enough.
- If using an exact quote from repo notes, list the repo path in `Brain Sources`.
- If using an exact quote from the web, include a direct source link in `Brain Sources`.
- If paraphrasing a web story, still include the source link.
- Avoid unsourced attribution for quotes. If the source is uncertain, say so in `Self-Check Answers` or choose a different quote.
- Before finalizing, confirm the file exists and that all required sections are present.

