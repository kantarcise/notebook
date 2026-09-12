---
name: shortform-knowledge-angle
description: Make a short-form content script by asking what the user already believes or knows about a topic, prioritizing this notebook's Success, Personal Brand, and relevant topic files, then saving the angle to content/shortform/angles/knowledge/YYYY-MM-DD-<slug>.md.
---

# Shortform Knowledge Angle

Use this skill when the user wants a short-form content script, angle, TikTok/Reels/Shorts draft, or content idea based on what they already believe, know, practice, or have written in this repo.

Core question: **What do I already believe or know about this topic?**

## Workflow

1. Identify the topic from the user's request. If the topic is materially ambiguous, ask one targeted clarification question.
2. Search notebook sources before drafting. Prioritize:
   - `Success/`
   - `Personal Brand/`
   - relevant topic folders or files
   - `content/` strategy or prior short-form files when useful
3. Prefer repo knowledge and the user's worldview over generic advice. Use outside knowledge only as light connective tissue unless the user asks for research.
4. Extract beliefs, phrases, examples, and tensions from the sources. Look for:
   - repeated principles
   - personal rules
   - strong opinions
   - examples, stories, or metaphors
   - advice that can become a clear short-form claim
5. Draft a concise script with a specific angle, not a broad essay.
6. Save the output to:
   `content/shortform/angles/knowledge/YYYY-MM-DD-<slug>.md`

Use the current local date for `YYYY-MM-DD`. Create a lowercase kebab-case slug from the topic or central claim.

## Output File Format

Each generated file must include:

```markdown
# <Title>

Topic: <topic>
Angle: <one-sentence angle>
Date: YYYY-MM-DD

## Hook

<1-3 punchy opening lines>

## Draft

<short-form script, usually 90-180 words>

## Examples

- <repo-grounded example, story, or analogy>
- <repo-grounded example, story, or analogy>

## CTA

<one clear action, question, or reflection prompt>

## Self-Check Answers

- What do I already believe or know about this topic? <answer>
- What is the strongest claim? <answer>
- Why would this matter to the viewer? <answer>
- What should be removed if the script is too generic? <answer>

## Brain Sources

- `<source path>`
- `<source path>`
```

## Drafting Guidance

- Keep the voice direct, practical, and belief-led.
- Make the hook specific enough to create curiosity.
- Make the draft feel like a spoken script, not an article.
- Use the user's own phrasing when it is strong, but avoid over-quoting.
- Include source paths in `Brain Sources`; do not include sources that were not actually used.
- If the repo does not contain much on the topic, say that in `Self-Check Answers` and build from the closest related principles.
- Before finalizing, confirm the file exists and that all required sections are present.

