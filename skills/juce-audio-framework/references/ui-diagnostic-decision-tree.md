# JUCE Text-Clipping Diagnostic Decision Tree

When the user reports a clipped/misaligned/misrendered text label in a JUCE app, work down this tree before changing code. Most of these bugs look identical at first glance — different root causes, different fixes, easy to misattribute.

## Step 1: Capture the symptom precisely

Get from the user (or screenshot):
- **Which label** clips and **what it should say vs what's shown** (e.g. `OCTAVE SCALE` → `OCTAVE`).
- **At what window size** does it clip? Specifically: only at maximized / large scales, only at default (~1.0), or all scales uniformly?
- **Is it horizontal clipping** (right side cut off, letters missing from the end), **vertical clipping** (tops/bottoms of glyphs sliced), or **doubled/skewed glyphs** (e.g. `EFFFECTS`)?
- **One label or a whole class?** A single button, or every preset selector in the app?

The window-size axis and the cut-direction axis are the two highest-signal disambiguators.

## Step 2: Decision tree

### Clip appears only at large window sizes, not at `window_size: 1.0`

→ **`size_ratio_` compounding bug** (see SKILL.md pitfall).

Look for `findValue(kTextComponentFontSize)` (or any other non-excluded skin value) being passed to `withHeight()` / `setBounds()` on a widget whose parent already laid it out at scaled size. Vial-confirmed sites: `preset_selector.cpp::paintBackground` and `::resized` in the `text_component_=true` branch.

Fix: switch to the proportional pattern `widget->getHeight() * font_height_ratio_`.

### Clip appears uniformly at every window size

→ **`withPointHeight()` vs `withHeight()`** (see SKILL.md pitfall).

The point→pixel ratio (~1.333×) is bloating font size beyond the widget's tuned bounds. Grep `withPointHeight` across `src/` — if there are any hits, sweep them.

Fix: `grep -rl withPointHeight src/ | xargs sed -i 's/withPointHeight(/withHeight(/g'`.

### Clip is vertical (glyph tops/bottoms cut), or letters appear doubled (`EFFFECTS`, `FII TER`)

→ **Sideways-heading paint path** (`synth_section.cpp::paintSidewaysHeadingText` or equivalent) and/or **OpenGL `pixel_scale` int-truncation** (see SKILL.md pitfall for both).

Check `open_gl_image_component.cpp` — `pixel_scale` should be `float`, with `roundToInt()` in width/height calculations. If that's already fixed and the doubling persists, the sideways-paint loop is laying down strokes twice. Investigate the rotation transform and the text-position increment.

### Clip is horizontal at all sizes, but `withPointHeight` is already gone and the skin values are correct

→ Likely **layout box too narrow** (absolute pixel allocation in the section's `resized()`). Not a font-API bug.

Common Vial offender: `portamento_section.cpp` — button widths are allocated as fixed pixel constants that don't accommodate `OCTAVE SCALE` or `LEGATO` at the chosen font size. The fix is in the layout, not in the rendering.

### Section / row renders at reduced opacity at large sizes only

→ **Render-path `setAlpha()` / `isActive()` decision tied to a derived scale value.** Not a text bug at all — the entire row is being drawn semi-transparent. Search for `setAlpha`, `getAlpha`, `isActive`, `isEnabled` in the affected section's render method. Vial 2026-06-12: OSC 2/3, SMP, FILTER rows showed this at maximized window — not investigated, listed as separate axis.

### Tab row clips at top of window at default size, disappears entirely at maximized

→ **Layout/sizing bug in the tab strip itself**, not a font bug. The tabs aren't adapting their Y position to window resize. Likely in the top-level interface's `resized()` method.

## Step 3: Verify before declaring victory

After any fix, **capture a fresh full-window screenshot at multiple sizes** (default + maximized minimum). The session that produced this reference burned several iterations because each fix resolved some symptoms while leaving others — and without a side-by-side, it's easy for the user to perceive "nothing changed" even when one cluster of clips is gone.

Useful: keep a `docs/screenshots/` directory in the repo with named baselines (`text-rendering-default-size.png`, `text-rendering-maximized.png`) and overwrite them after each fix so git history carries a visual diff.

## Step 4: Don't bundle fixes from different categories

If you identified two root causes (e.g. a `withPointHeight` sweep AND a `size_ratio_` compounding fix), land them as separate commits with separate before/after screenshots. If you ship both in one build and a regression appears, you can't tell which cluster caused it without bisecting. The SKILL.md pitfall "Land the pixel_scale fix ALONE first" generalizes — same logic for every JUCE text-clipping fix category.

## Vial residual catalog (as of 2026-06-12)

After the `withPointHeight` sweep, skin font/offset restores, and `preset_selector` size_ratio fix landed, the following remained visibly broken — kept here as a target list for future sessions:

1. **Sideways `VOICE`, `EFFECTS` section headings** — vertical clipping at top of window, occasional doubled letters (`EFFFECTS`). Suspect: `paintSidewaysHeadingText` paint loop.
2. **Tab row** (`VOICE / EFFECTS / MATRIX / ADVANCED`) — clips at small window, vanishes at maximized. Suspect: top-level layout's tab Y/height calculation.
3. **`OCTAVE SCALE` → `OCTAVE`, `LEGATO` → `LEGA`** — button width allocation in `portamento_section.cpp`. Independent of font sizing.
4. **OSC 2/3, SMP, FILTER 1/2 row opacity at maximized** — entire rows drawn dim. Suspect: `setAlpha` decision tied to derived scale.
5. **OSC 1 `FILTER 1` → `FILTER` at maximized** — another selector not yet routed through the `preset_selector.cpp` patched path. Worth `grep`ing for other `findValue(kTextComponentFontSize)` callers that haven't been migrated to the proportional pattern.
6. **`LNK4006`** for `SynthEditor::resized` / `~SynthEditor` — pre-existing ODR violation; non-fatal but worth tracking.

Issues 1–5 are visible in `docs/screenshots/text-rendering-default-size.png` and `text-rendering-maximized.png` on the `fix/juce8-text-rendering` branch.
