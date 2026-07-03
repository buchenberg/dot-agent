# JUCE 6→8 Font API Migration Reference

Condensed from Vial synthesizer migration sessions (2026-06-11 through 2026-06-12).

## Font API Changes Summary

| JUCE 6 | JUCE 8 | Notes |
|--------|--------|-------|
| `Font font; font.setHeight(14.0f);` | `auto font = originalFont.withHeight(14.0f);` | Font is now immutable; use builder pattern |
| `font.setHeight(px)` — pixel units | `font.withHeight(px)` — **logical pixel** units | Same unit, but immutable now |
| N/A | `font.withPointHeight(pt)` — **point** units (96 DPI) | ~1.333× larger than `withHeight()` for same numeric value |
| `font.getHeight()` → pixels | `font.getHeight()` → logical pixels | |
| N/A | `font.getHeightInPoints()` → points | |

### Critical: `withHeight()` vs `withPointHeight()`

The ratio is exactly 4/3 ≈ 1.333. If you swap `withHeight(12)` for `withPointHeight(12)`, the font renders 33% larger.

**Rule of thumb for migrations:**
- If the original JUCE 6 code used pixel values (from widget height, skin values, etc.), use `withHeight()`
- If the original code used point values (typographic sizing), use `withPointHeight()`
- Most synth UI code uses pixel values → use `withHeight()`

### FontOptions (JUCE 8)

```cpp
// Creating a font from a typeface
FontOptions options;
options.setName("Roboto");
options.setStyle("Regular");
options.setMetricsKind(MetricsKind::portable);  // or MetricsKind::native
Font font(options);

// Then resize with builder pattern
auto sizedFont = font.withHeight(14.0f);  // logical pixels
auto sizedFont2 = font.withPointHeight(14.0f);  // points
```

## Text Drawing API

### `drawText()` — Fixed-size positioning

```cpp
// Rectangle<int> overload
void drawText(const String& text,
              Rectangle<int> area,
              Justification justificationType,
              bool useEllipsesIfTooBig = true) const;

// Rectangle<float> overload
void drawText(const String& text,
              Rectangle<float> area,
              Justification justificationType,
              bool useEllipsesIfTooBig = true) const;
```

- Does NOT scale text to fit
- If text is too wide: truncates or adds ellipsis (based on `useEllipsesIfTooBig`)
- If text is too tall: clips vertically
- `Justification::centred` centers both horizontally AND vertically

### `drawFittedText()` — Auto-scaling

```cpp
void drawFittedText(const String& text,
                    Rectangle<int> area,
                    Justification justificationFlags,
                    int maximumNumberOfLines,
                    float minimumHorizontalScale = 0.0f,
                    GlyphArrangementOptions options = {}) const;
```

- Scales text down horizontally to fit (down to `minimumHorizontalScale` fraction)
- Can break across multiple lines (up to `maximumNumberOfLines`)
- If text still won't fit: truncates with ellipsis
- `minimumHorizontalScale = 1.0f` disables horizontal scaling
- `minimumHorizontalScale = 0.7f` allows squashing to 70% width
- `maximumNumberOfLines = 1` keeps single-line (horizontal squash only)

### When to use which

| Scenario | Use |
|----------|-----|
| Label in fixed-size box | `drawFittedText()` with `minHorizScale=0.7f` |
| Button text that must fit | `drawFittedText()` |
| Tab labels that scale with tab | `drawFittedText()` |
| Numeric value display | `drawFittedText()` or `drawText()` with clipping |
| Sideways/rotated headings | `drawFittedText()` with pre-calculated rotated bounds |
| Precise typographic control | `drawText()` with known-good font size |

## Common Migration Bugs

### Bug 1: `withPointHeight()` bloat (codebase-wide)

**Symptom**: Text clipped from right end of buttons, selectors overflow pills
**Cause**: Migration script replaced `setHeight()` with `withPointHeight()` instead of `withHeight()`
**Fix**: `grep -rl withPointHeight src/ | xargs sed -i 's/withPointHeight(/withHeight(/g'`
**Verify**: Count drops to 0, rebuild, check all text elements

### Bug 2: `size_ratio_` compounding

**Symptom**: Text fine at default size, clipped at maximized/large window
**Cause**: `findValue(kFontSize)` returns value already multiplied by `size_ratio_`, then widget is also laid out at `size_ratio_` scale → double-scaled
**Fix**: Use proportional sizing: `getHeight() * font_height_ratio_` instead of `findValue(kFontSize)`

### Bug 3: Skin value shrinks masking font bloat

**Symptom**: After fixing `withPointHeight` → `withHeight`, text is now too small
**Cause**: Migration also shrunk skin font sizes to compensate (e.g., 15→13, 11→9)
**Fix**: Revert skin value shrinks in same commit as font API fix
**Verify**: `git show <migration-commit> -- '*.vialskin' '*.skin' '*.json'`

### Bug 4: OpenGL texture coordinate mismatch

**Symptom**: Text in OpenGL components at wrong size/position, non-OpenGL components fine
**Cause**: Font height in texture coordinate space, not screen space; `pixel_scale` truncated to int
**Fix**: Use `float pixel_scale`, calculate font height relative to texture size

### Bug 5: Rotation transform clips text

**Symptom**: Sideways headings have tops of letters cut off
**Cause**: `AffineTransform::rotation()` applied after `drawText()`, rotation point doesn't account for text bounding box
**Fix**: Use `drawFittedText()` with pre-calculated rotated bounds

## Diagnostic Decision Tree

```
User reports clipped/misaligned text
│
├─ Does it happen at ALL window sizes?
│  ├─ YES → Font API bug (withPointHeight vs withHeight)
│  │        OR absolute layout box too narrow
│  │
│  └─ NO (only at large/maximized sizes)
│     └─ size_ratio_ compounding bug
│        OR proportional vs absolute font sizing
│
├─ Is it only in OpenGL-rendered components?
│  ├─ YES → pixel_scale truncation
│  │        OR texture coordinate mismatch
│  │
│  └─ NO (affects all components)
│     └─ Font API bug or layout issue
│
├─ Is text clipped from the RIGHT end?
│  ├─ YES → Font too wide (withPointHeight bloat)
│  │        OR container too narrow
│  │
│  └─ NO (clipped from top/bottom)
│     └─ Font too tall
│        OR rotation transform issue
│
└─ Are some elements fine and others broken?
   ├─ YES → Check proportional vs absolute sizing pattern
   │        (proportional tolerates bloat, absolute exposes it)
   │
   └─ NO (all elements broken uniformly)
      └─ Codebase-wide withPointHeight sweep needed
```

## Vial-Specific File Locations

| Component | File | Key Methods |
|-----------|------|-------------|
| Text look-and-feel | `src/interface/look_and_feel/text_look_and_feel.cpp` | `drawRotarySlider()` ~line 54, `drawToggleButton()` ~line 107 |
| Preset selectors | `src/interface/editor_components/preset_selector.cpp` | `paintBackground()`, `resized()` |
| Synth section base | `src/interface/editor_sections/synth_section.cpp` | `paintLabel()`, `paintHeadingLabel()`, `paintSidewaysHeadingText()` |
| Tab selector | `src/interface/editor_components/tab_selector.cpp` | `paint()` |
| Header section | `src/interface/editor_sections/header_section.cpp` | `paintSidewaysHeadingText()` |
| OpenGL image component | `src/interface/editor_components/open_gl_image_component.h` | `paintToImage()` ~line 217 |
| Fonts | `src/interface/look_and_feel/fonts.cpp` | `proportional_light()`, `proportional_regular()`, `proportional_bold()` |
| Skin values | `default.vialskin` | `Button Font Size`, `Text Component Font Size`, `Label Background Height`, `Label Height` |

## Verification Checklist

After applying fixes, verify at these window sizes:
1. **Default size** (`window_size: 1.0`) — baseline check
2. **Maximized** — catch `size_ratio_` compounding bugs
3. **HiDPI** (150%, 200%) — catch `pixel_scale` issues

Check these elements:
- [ ] Button text not clipped from right end
- [ ] Preset selector text centered in pill
- [ ] Numeric values centered in boxes
- [ ] Sideways headings fully visible (no chopped tops)
- [ ] Tab text scales with tab size
- [ ] Labels centered in their containers
- [ ] No text overlapping other text
