---
name: shortform-content-brain
description: Generate short-form content from this repository as a content brain. Use when the user wants TikTok, Instagram, or YouTube Shorts style content built from notebook sources, especially around self improvement, responsibility, productivity, curiosity, or artificial intelligence for a 15-30 audience needing encouragement.
---

# Shortform Content Brain

Use this skill when the user wants short-form content generated from the repository itself rather than from generic prior knowledge.

This skill is the short-form Codex equivalent of `.github/scripts/generate_brain_content.py`.

## Scope

This skill supports only short-form content.

Do not use this skill for:

- long-form video drafting
- podcast preparation
- newsletter writing

If the user wants one of those, use or create a different skill.

## Audience And Voice

Default audience:

- People aged 15-30
- Curious to learn
- Desperate for encouragement

Primary topics to emphasize:

- Self improvement
- Meaning through responsibility
- Productivity
- Curiosity
- Artificial intelligence

Platform default:

- TikTok
- Instagram
- YouTube Shorts

Voice target:

- Upright
- Serious
- Encouraging
- Brave
- Specific
- Spoken clearly
- Action-oriented

Tone references:

- Jordan Peterson
- Greg Plitt
- Alex Hormozi

Do not imitate those creators directly. Use them only as rough tonal reference points.

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
   - include `Success/readme.md`
   - include:
     - `Success/Mind/who_i_am.md`
     - `Success/Mind/growth_without_goals.md`
     - `Success/Mind/lessons_from_2025.md`
   - include `Personal Brand/flywheels.md`
   - include `Personal Brand/magnum_opus_content.md`
3. Build a compact "brain context" from:
   - selected topic clusters
   - representative document inventory
   - key notebook excerpts
   - relevant worldview statements
4. Generate one short-form draft.
5. Write the result into `content/shortform/`.
6. Include the notebook source paths used.

## Output Contract

Goal:

- one short-form post draft for TikTok, Instagram, or YouTube Shorts scripting or caption planning

Must include:

- proper hook
- clear value
- direct CTA
- 2 or 3 concrete examples
- self-check questions
- self-check answers

Constraints:

- 120-260 words for the main draft
- easy to say out loud
- no motivational fog
- no vague inspiration
- every sentence must earn its place

Self-check questions must be exactly:

- `Does this sentence make sense instantly?`
- `Is this something I'd say out loud?`
- `Can I cut any fluff without losing meaning?`

Write to:

- `content/shortform/YYYY-MM-DD-<slug>.md`

Recommended markdown structure:

```md
# Title

- Date:
- Focus:
- Audience:
- Hook:
- Value:
- CTA:

## Draft

...

## Specific Examples

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

- make people more optimistic and braver
- keep the writing upright
- make points relatable and actionable
- use concrete examples
- keep sentences clear and immediate
- prefer behavior-changing insight
- sound like a serious person speaking plainly

Never:

- use soft motivational filler
- write generic self-help
- imitate Jordan Peterson, Greg Plitt, or Alex Hormozi line-for-line
- use inflated claims without a practical bridge
- rely on abstract advice when a concrete example would do

## File Use

Before drafting, inspect these files if they exist:

- [../../.github/content_profile.md](../../.github/content_profile.md)
- [../../Success/readme.md](../../Success/readme.md)
- [../../Success/Mind/who_i_am.md](../../Success/Mind/who_i_am.md)
- [../../Success/Mind/growth_without_goals.md](../../Success/Mind/growth_without_goals.md)
- [../../Success/Mind/lessons_from_2025.md](../../Success/Mind/lessons_from_2025.md)
- [../../Personal Brand/flywheels.md](../../Personal%20Brand/flywheels.md)
- [../../Personal Brand/magnum_opus_content.md](../../Personal%20Brand/magnum_opus_content.md)

Then inspect additional relevant topic files based on focus.

## Operational Notes

When the user wants the content generated now:

- do the repository scan
- draft the content
- write the markdown file directly

When the user wants the system changed:

- update the short-form prompt logic, structure, or routing
- preserve the short-form contract above

If a script-based path is preferred, the canonical implementation reference is:

- [../../.github/scripts/generate_brain_content.py](../../.github/scripts/generate_brain_content.py)
