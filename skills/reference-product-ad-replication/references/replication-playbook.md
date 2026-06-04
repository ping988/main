# Reference Product Ad Replication Playbook

## Contents

- Reference analysis
- Story and clip architecture
- Generation prompts
- Editing rules
- Failure modes

## Reference Analysis

Do not summarize a reference video as only "warm light" or "fast rhythm." Extract five layers:

1. **Narrative function**: what each shot contributes to the sales story.
2. **Subject progression**: ingredients, product, use, result, brand.
3. **Camera language**: angle, lens feeling, movement, focus change.
4. **Transition mechanism**: what visual or action feature joins adjacent shots.
5. **Energy curve**: where the video accelerates, breathes, lifts, and resolves.

Create:

- A full timeline contact sheet at 0.5-1.0 second intervals.
- Fine contact sheets at 0.05-0.15 second intervals around actions and transitions.
- A shot table with entry state, main action, exit state, useful duration, and audio cue.

## Story and Clip Architecture

Use a simple product-ad story:

1. **Hook**: attractive ingredients or problem/need.
2. **Reveal**: introduce the product once.
3. **Demonstration**: open, pour, use, prepare, or show texture.
4. **Result**: consumption, reaction, or benefit demonstrated visually.
5. **Close**: clean product-led ending.

Each generated clip needs edit handles:

- The first 0.3-0.8 seconds should be able to receive the previous action.
- The last 0.3-0.8 seconds should create a state that the next shot can match.
- Avoid generating clips that start and finish as isolated product hero shots.

## Generation Prompt Pattern

Describe:

- Target format and commercial genre.
- Exact product identity constraints.
- One shot's main action.
- Camera movement and focus behavior.
- Entry and exit states.
- Reference style traits.
- Forbidden drift, text, UI, claims, and warped interactions.

Example structure:

```text
Vertical 9:16 premium children's snack advertisement.
Use the supplied pouch as the exact product; preserve shape, material, logo,
illustrations, and layout. Single shot: begin with [entry state], perform
[one action], and finish with [exit state]. Camera uses [movement/focus].
Match the reference's [lighting/texture/rhythm]. No redesign, extra text,
warped hands, or unrelated scene changes.
```

## Editing Rules

- Assemble by story function, never by generation order alone.
- Cut generated clips before their repeated final hero holds.
- Keep action continuity:
  - Package reveal -> hand reaches package.
  - Open package -> pour from package.
  - Filled bowl -> hand reaches bowl.
  - Hand takes food -> child bites.
  - Happy reaction -> final product.
- Prefer hard cuts on motion or musical accents.
- Use dissolves only for a genuine passage of time, mood transition, or reference-supported visual wipe.
- Remove empty-room or empty-table lead-ins when they reset the story.

## Failure Modes

### Feeding a Contact Sheet to a Video Model

**Symptom:** multiple panels, numbers, grids, or chaotic scene mixing appear.

**Fix:** generate clean standalone first frames, one per shot.

### Using Full Generated Clips

**Symptom:** every shot starts over and ends with a product hero; the film feels compiled.

**Fix:** trim to the useful action beat and design entry/exit handles.

### Solving Narrative Problems with Dissolves

**Symptom:** transitions are soft, but the story still feels hard-stitched.

**Fix:** rewrite the causal action chain and use action matches.

### Repeating the Same Music Phrase

**Symptom:** music restarts at every shot and strengthens the stitched feeling.

**Fix:** use one continuous evolving score and cut to its real phrases.

### Generating "Same Style" Music With Excessive Section Changes

**Symptom:** technically one track, but it sounds like several songs.

**Fix:** request cohesive instrumentation, continuous development, and restrained arrangement changes. Review before mixing.

### Decorative or Synthetic Foley

**Symptom:** cartoon pops, electronic impacts, or unexplained sparkles make the video feel fake.

**Fix:** remove all unsupported sounds. Use only real visible actions.

### Foley That Is Too Short

**Symptom:** pouring or chewing sounds stop while the action continues.

**Fix:** match the Foley envelope to the full visible action and add a plausible settling or chewing tail.
