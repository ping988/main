# Audio and Final QA

## Contents

- Continuous music
- Foley spotting
- Realistic Foley rules
- Stem workflow
- Final review checklist

## Continuous Music

Use a single score identity across the finished commercial.

- Remove native music from generated clips.
- Do not loop a short phrase at each shot.
- Do not assume a generated "continuous" track is cohesive; audition its full arc.
- Map narrative stages to musical energy:
  - Hook: sparse and curious.
  - Demonstration: clearer pulse and forward motion.
  - Result: joyful lift.
  - Close: confident resolution and final hold.
- Adjust edit points to meaningful accents, but do not force every shot to equal length.

## Foley Spotting

Create fine contact sheets around each candidate action at 50-150 ms intervals.

Record for each action:

| Action | Visible start | Visible end | Plausible sound |
|---|---:|---:|---|
| Fingers manipulate pouch | first contact | hand leaves/open state | light package crinkle |
| Food pours into bowl | first piece exits/lands | last pieces settle | continuous granular pour + bowl contacts |
| Child bites crisp | food contacts mouth | visible chewing ends | initial crunch + restrained intermittent chewing |

Do not add Foley to:

- Floating ingredients without contact.
- Stop-motion rearrangement unless contact is clearly visible and intended.
- Generic transitions.
- Product hero holds.
- Light flares or brand reveals unless explicitly requested.

## Realistic Foley Rules

- Prefer real recorded Foley.
- If generated Foley is used, audition it in isolation and reject cartoon/electronic artifacts.
- Do not label a synthetic tone as a real impact.
- Match material:
  - Dry cereal/crisps: many small dry collisions.
  - Ceramic bowl: subtle hard resonance, not a metallic clang.
  - Flexible pouch: crinkle/rustle; use tearing only if a tear is visible.
  - Eating: short dry crunch, then low-level irregular chewing.
- Match duration:
  - Start at physical contact.
  - Continue while the action is visibly active.
  - Add only a short natural tail after the action.
- Keep mouth sounds restrained for children's food advertising.

## Stem Workflow

Maintain separate files:

1. `music_stem.wav`
2. `foley_stem.wav`
3. `foley_only_sync_audit.mp4`
4. `final_mix.mp4`

Before mixing:

- Verify the Foley stem is silent outside marked action windows.
- Verify the music stem has one source and covers the full video.
- Listen to the Foley-only audit while watching the video.

During mixing:

- Briefly duck music under important actions.
- Do not duck music under every minor sound.
- Use gentle limiting; avoid crushing the Foley tail.
- Never mix old rejected Foley stems into a new version.

## Final Review Checklist

### Visual

- Correct aspect ratio and resolution.
- Correct narrative order.
- No product drift.
- No repeated scene resets.
- No accidental grid, storyboard number, or reference branding.

### Music

- One coherent music identity.
- Full-duration coverage.
- No phrase restart at every cut.
- Energy supports the story arc.

### Foley

- Every sound has a visible source.
- Sound begins at contact.
- Sound duration matches the visible action.
- Continuous actions have continuous sound.
- No unexplained decorative effects.
- Foley-only audit passes.

### Technical

- Compatible `yuv420p` output.
- Expected frame rate, duration, and audio sample rate.
- No clipping.
- Source files and approved outputs are preserved.
