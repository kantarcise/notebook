---
name: longform-video-brain
description: Generate long-form video preparation drafts from this repository as a content brain. Use when the user wants a YouTube or other long-form video script or prep document built from notebook sources around responsibility, agency, meaningful work, truth, craft, technology, and growth.
---

# Longform Video Brain

Use this skill when the user wants long-form video content generated from the repository itself rather than from generic prior knowledge.

This skill is the long-form video Codex equivalent of `.github/scripts/generate_brain_content.py --mode longform_video` and `.github/workflows/longform_video.yml`.

## Scope

This skill supports only long-form video preparation drafts.

Do not use this skill for:

- short-form content
- podcast preparation
- newsletter writing

If the user wants one of those, use or create a different skill.

## Audience And Voice

Default audience:

- Founders, operators, and technical professionals interested in applied learning

Primary topics to emphasize:

- Responsibility
- Agency
- Meaningful work
- Truth
- Craft
- Technology
- Growth

Voice target:

- Upright
- Serious
- Practical
- Specific
- Optimistic without being soft
- Brave
- Action-forcing

## Repository Role

Treat this repository as the author's external brain:

- worldview
- examples
- references
- recurring themes
- language patterns

Prefer these notebook areas when building context:

- `Success/` as the weekly compass
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
4. Add current web insight when useful:
   - use recent web research to sharpen the argument
   - do not let web material replace the notebook's core voice
   - capture the actual web source links used
5. Generate one long-form video preparation draft.
6. Write the result into `content/longform-video/`.
7. Include notebook source paths and any web sources used.

## Output Contract

Goal:

- one long-form video preparation draft for YouTube or similar long-form spoken content

Must include:

- proper opening hook
- clear core thesis
- 5 to 8 section outline
- script draft
- action steps
- recent web takeaways
- self-check questions
- self-check answers
- brain sources
- web sources

Constraints:

- `script_markdown` equivalent should be 900-1600 words
- suitable to speak out loud
- use `Success/` as the weekly compass
- every section should push toward action, clarity, or practical reflection

Write to:

- `content/longform-video/YYYY-MM-DD-<slug>.md`

Recommended markdown structure:

```md
# Title

- Week of:
- Focus:
- Audience:
- Opening hook:
- Core thesis:

## Outline

- ...

## Script Draft

...

## Action Steps

- ...

## Recent Web Takeaways

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

## Web Sources

- ...
```

## Writing Rules

Always:

- use clear, direct spoken language
- make people more optimistic and braver
- ground abstract claims in concrete examples
- tie ideas back to responsibility, agency, truth, craft, or action
- make the structure useful for actual recording or script iteration

Never:

- use generic inspiration
- bury the thesis
- inflate claims without a practical bridge
- substitute web novelty for notebook substance

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
- add recent web insight when it materially improves the argument
- draft the content
- write the markdown file directly

When the user wants the system changed:

- update the long-form prompt logic, structure, or routing
- preserve the output contract above

Canonical implementation references:

- [../../.github/scripts/generate_brain_content.py](../../.github/scripts/generate_brain_content.py)
- [../../.github/workflows/longform_video.yml](../../.github/workflows/longform_video.yml)
