---
name: reference-product-ad-replication
description: Replicate a supplied reference product advertisement while preserving the target product, visual style, camera language, narrative rhythm, continuous music, and action-synchronized real Foley. Use when Codex must analyze a reference video, plan or generate matching product-ad clips, assemble AI-generated shots into one coherent commercial, fix a video that feels hard-stitched, or redesign music and sound effects to match visible actions.
---

# Reference Product Ad Replication

Treat replication as directing one coherent advertisement, not generating several attractive clips.

## Non-Negotiable Rules

1. Preserve the target product. A beautiful clip with a changed package, logo, color, structure, or usage is rejected.
2. Analyze the reference's filmmaking grammar, not only its visual style.
3. Build a causal narrative chain before generating video.
4. Never feed a storyboard contact sheet or nine-grid image directly into a video model. Generate or use one clean frame per shot.
5. Generate one test clip first. Review it locally before spending credits on the remaining clips.
6. Do not use every generated clip in full. Trim each clip to its useful action beat.
7. Use one continuous evolving score for the full advertisement. Do not restart or loop the same phrase at every shot.
8. Add Foley only for visible, physically plausible actions. Continuous actions require continuous sound.
9. Keep music, Foley, and final mix as separate reviewable stems.
10. Review the completed video before presenting it to the user.

## Core Workflow

### 1. Establish Product Truth

- Inspect the real product images, packaging, logo, script, storyboard, reference video, and target format.
- List the product elements that must not change.
- Confirm aspect ratio, desired duration, model, number of test clips, faces/no-faces policy, and audio policy.
- Preserve source files. Create new output folders and versioned files.

Stop if the only available generation method cannot preserve the product.

### 2. Reverse-Engineer the Reference

Create timeline contact sheets and identify:

- Narrative stages: hook, product reveal, demonstration, consumption/result, brand close.
- Shot grammar: macro, overhead, handheld push, arc, rack focus, stop-motion-like beats.
- Transition logic: action match, shape match, whip pan, motivated light wipe, hard cut on a beat.
- Rhythm: shot duration, acceleration, pauses, and final hold.
- Audio grammar: music energy curve, action sounds, and moments of silence.

Use `scripts/make_timeline_contact_sheet.py` for frame-level inspection.

Read [references/replication-playbook.md](references/replication-playbook.md) for detailed analysis and generation guidance.

### 3. Write the Causal Action Chain

Express the advertisement as actions that cause the next shot:

`ingredients appear -> product is revealed -> package opens -> food pours into bowl -> child picks up food -> child bites -> product closes`

For every planned clip, specify:

- Entry state: what the previous shot hands into this shot.
- Main action: one clear action or benefit.
- Exit state: the visual/action state that the next shot can receive.
- Approximate useful edit range, not merely generated duration.

If two adjacent clips both restart with a product hero, the sequence will feel stitched together. Redesign or trim them.

### 4. Generate in Small Batches

- Use the product reference or an approved product-accurate first frame.
- Use a single clean image per shot when product consistency matters.
- Generate one test clip and inspect it locally.
- Continue only after the user accepts the direction.
- Prompt for a single controllable shot. Do not ask one short clip to contain several unrelated scenes.
- Generate transition handles when adjacent actions cannot connect naturally.

Before generation, state the model, references, clip count, duration, aspect ratio, and known risks.

### 5. Edit for Narrative, Not Clip Completeness

- Start with the action chain, not file-name order.
- Trim repeated product reveals, dead air, empty-table resets, and long hero holds.
- Prefer motivated action-match hard cuts. Use short transitions only when the reference supports them.
- Match bowl-to-bowl, hand-to-hand, ingredient-to-ingredient, or motion direction across cuts.
- Hold the final product frame long enough to read, but do not repeatedly stop on the product throughout the middle.
- Review muted. The narrative must still be understandable.

### 6. Build One Continuous Music Arc

Interpret "same music style" as one continuous composition with evolving sections, not the same phrase repeated.

- Remove or mute each generated clip's native music.
- Use one score source for the full cut.
- Structure the score with the narrative: light hook, growing demonstration rhythm, joyful consumption lift, resolved brand ending.
- Analyze the score's real phrases and accents before adjusting cut points.
- Let the score develop continuously; never restart it at every shot.

### 7. Add Minimal, Realistic Foley

First inspect the video frame by frame and mark exact physical-contact windows.

- Add sound only when a visible action can realistically produce it.
- Use real recorded Foley or high-fidelity generated Foley. Reject electronic, cartoon, or abstract placeholder sounds.
- Match duration to the action:
  - A continuous pour needs continuous granular collisions plus a short settling tail.
  - Opening a bag without visible tearing needs crinkling, not a tear.
  - A bite needs an initial crunch followed by restrained intermittent chewing while the child continues eating.
- Do not add unexplained flying, sparkle, transition, landing, or hero sounds.
- Duck music briefly under important Foley, then restore it naturally.

Always export:

1. Music-only stem.
2. Foley-only synchronized audit video.
3. Final mix.

Read [references/audio-and-qa.md](references/audio-and-qa.md) before sound design or final delivery.

### 8. Review Before Delivery

Reject or revise the output if any check fails:

- Correct shot order and causal narrative.
- Exact product identity.
- No repeated scene resets or unnecessary hero shots.
- One continuous music identity.
- Foley exists only at visible actions and lasts as long as the action.
- No strange decorative sounds.
- Audio does not clip and music does not mask key Foley.
- Correct resolution, aspect ratio, frame rate, duration, and compatible pixel format.
- Final video, Foley-only audit, and source stems are saved as new files.

## Delivery Report

State:

- What was generated and what was only edited.
- The narrative order.
- Music source and whether native clip audio was removed.
- Foley events and exact action windows.
- Local output paths.
- Verification results and remaining limitations.
