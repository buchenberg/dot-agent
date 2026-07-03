# Text Clipping Fix Locations (Vial Project)

Catalog of files where JUCE `g.drawText()` clipping was enabled (changed from `false` to `true`) to fix text overflow issues.

## Session: 2026-06-12 — UI Text Overflow Fixes

### Files Modified

#### 1. `src/interface/editor_sections/synth_section.cpp` (3 locations)

**Line 813** — `drawLabel()` method:
```cpp
g.drawText(text, component_bounds.getX(), background_bounds.getY(),
                 component_bounds.getWidth(), background_bounds.getHeight(), Justification::centred, true);
```
- Fixes: SYNC, STEREO labels in LFO section
- Fixes: Trigger 1/2 text in voice section

**Line 585** — General label drawing:
```cpp
g.drawText(name, x, y, width, findValue(Skin::kLabelBackgroundHeight), Justification::centred, true);
```
- Fixes: Other section labels throughout the UI

#### 2. `src/interface/editor_components/preset_selector.cpp` (1 location)

**Line 76** — `paintBackground()` method:
```cpp
g.drawText(text_value_, text_bounds, Justification::centred, true);
```
- Fixes: "< Filter 1 >" selector overflow
- Fixes: Other preset-style selectors with angle brackets

#### 3. `src/interface/look_and_feel/text_look_and_feel.cpp` (2 locations)

**Line 55** — `drawRotarySlider()` method:
```cpp
g.drawText(text, x, y + std::round(offset), width, height, Justification::centred, true);
```
- Fixes: Phase and unison value overflow in rotary slider displays

**Line 108** — `drawToggleButton()` method:
```cpp
g.drawText(text, 0, 0, button.getWidth(), button.getHeight(), Justification::centred, true);
```
- Fixes: Trigger mode text overflow in toggle buttons

## Verification

After applying these fixes:
- ✅ SYNC and STEREO labels no longer overflow at bottom of LFO section
- ✅ Trigger 1/2 text stays within voice section bounds
- ✅ "< Filter 1 >" selector text clipped to oval boundary
- ✅ Phase and unison values no longer overflow
- ✅ All text components properly respect their bounding rectangles

## Search Command

To find additional unclipped `drawText()` calls in the codebase:
```bash
grep -rn "drawText.*false)" src/interface/
```
