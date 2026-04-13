---
name: podcast-thinking-brain
description: Generate podcast thinking documents from this repository as a content brain. Use when the user wants a podcast prep document or exploratory back-and-forth built from notebook sources around agency, responsibility, truth, craft, technology, and growth.
---

# Podcast Thinking Brain

Use this skill when the user wants podcast preparation generated from the repository itself rather than from generic prior knowledge.

This skill is the podcast Codex equivalent of `.github/scripts/generate_brain_content.py --mode podcast` and `.github/workflows/podcast_thinking.yml`.

## Scope

This skill supports only podcast thinking and prep documents.

Do not use this skill for:

- short-form content
- long-form video drafting
- newsletter writing

If the user wants one of those, use or create a different skill.

## Audience And Voice

Default audience:

- Founders, operators, and technical professionals interested in applied learning

Primary topics to emphasize:

- Agency
- Responsibility
- Truth
- Craft
- Technology
- Growth

Voice target:

- Deep
- Serious
- Exploratory
- Clear
- Practical
- Tension-bearing

## Repository Role

Treat this repository as the author's external brain:

- worldview
- examples
- references
- recurring themes
- language patterns

Prefer these notebook areas when building context:

- `Success/`
- `Personal Brand/`
- topic folder `readme.md` files
- any files directly relevant to the requested focus

## Required Workflow

1. Determine the focus:
   - use the user's requested focus if present
   - otherwise select the strongest angle from the notebook
2. Build context from the repository:
   - inspect top-level topic folders
   - prioritize `readme.md` files
   - always include:
     - `Success/readme.md`
     - `Success/Mind/who_i_am.md`
     - `Success/Mind/growth_without_goals.md`
     - `Success/Mind/lessons_from_2025.md`
   - include:
     - `Personal Brand/flywheels.md`
     - `Personal Brand/magnum_opus_content.md`
     - `Personal Brand/readme.md`
   - include additional relevant topic files based on focus
3. Build a compact brain context from:
   - selected topic clusters
   - representative document inventory
   - key notebook excerpts
   - relevant worldview statements
4. Generate one podcast thinking document built around a real back-and-forth.
5. Write the result into `content/podcast/`.
6. Include the notebook source paths used.

## Output Contract

Goal:

- one podcast preparation document that helps think through a real conversation

Must include:

- episode title
- premise
- expert persona
- 4 to 6 big ideas
- 6 opening questions
- conversation draft
- takeaways
- self-check questions
- self-check answers
- brain sources

Constraints:

- `conversation_markdown` equivalent should be around 900-1500 words
- the conversation should be a real back-and-forth between `Me` and `Expert`
- include tension, clarification, and practical examples
- do not produce generic interview filler

Write to:

- `content/podcast/YYYY-MM-DD-<slug>.md`

Recommended markdown structure:

```md
# Title

- Date:
- Focus:
- Audience:
- Premise:
- Expert persona:

## Big Ideas

- ...

## Opening Questions

- ...

## Conversation Draft

...

## Takeaways

- ...

## Self-Check Questions

- Does this sentence make sense instantly?
- Is this something I'd say out loud?
- Can I cut any fluff without losing meaning?

## Self-Check Answers

- ...

## Brain Topics

- ...

## Brain Sources

- ...
```

## Writing Rules

Always:

- prefer real tension over polite agreement
- use dialogue to clarify, not decorate
- make the expert push back where useful
- keep the conversation useful for real thinking and real decisions
- ground hard ideas in practical examples

Never:

- write empty podcast banter
- make both voices sound identical
- drift into vague self-help language
- avoid disagreement when disagreement would sharpen the idea

## File Use

Before drafting, inspect these files if they exist:

- [../../.github/content_profile.md](../../.github/content_profile.md)
- [../../Success/readme.md](../../Success/readme.md)
- [../../Success/Mind/who_i_am.md](../../Success/Mind/who_i_am.md)
- [../../Success/Mind/growth_without_goals.md](../../Success/Mind/growth_without_goals.md)
- [../../Success/Mind/lessons_from_2025.md](../../Success/Mind/lessons_from_2025.md)
- [../../Personal Brand/flywheels.md](../../Personal%20Brand/flywheels.md)
- [../../Personal Brand/magnum_opus_content.md](../../Personal%20Brand/magnum_opus_content.md)
- [../../Personal Brand/readme.md](../../Personal%20Brand/readme.md)

Then inspect additional relevant topic files based on focus.

## Operational Notes

When the user wants the content generated now:

- do the repository scan
- draft the conversation document
- write the markdown file directly

When the user wants the system changed:

- update the podcast prompt logic, structure, or routing
- preserve the output contract above

Canonical implementation references:

- [../../.github/scripts/generate_brain_content.py](../../.github/scripts/generate_brain_content.py)
- [../../.github/workflows/podcast_thinking.yml](../../.github/workflows/podcast_thinking.yml)
