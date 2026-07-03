# JUCE Custom OpenGL Rendering — Fractional DPI Scaling Pitfall

## Problem

On Windows with fractional display scaling (125%, 150%, 175%), text rendered to OpenGL textures appears **pixelated/blurry** while text drawn directly into the main background texture looks crisp. This is because JUCE's `Display::scale` property is a `float`, but the OpenGL texture code truncates it to `int`.

## Root Cause

```cpp
// WRONG — truncates 1.5 to 1, textures render at 1x then stretch to 1.5x → pixelated
int pixel_scale = Desktop::getInstance().getDisplays()
    .findDisplayForPoint(getScreenPosition()).scale;
int width = component->getWidth() * pixel_scale;   // 100 * 1 = 100 (should be 150)
int height = component->getHeight() * pixel_scale;  // 30 * 1 = 30  (should be 45)
```

On a 2x Retina display this works fine (2.0 truncates to 2). On 1x it's fine (1.0 → 1). **Only fractional scales break**, which is why it's hard to catch in development.

## Diagnostic Pattern

When some UI text is crisp and other text is pixelated in a custom OpenGL pipeline:

| Crisp text | Pixelated text |
|---|---|
| Drawn into the main background texture | Drawn via `OpenGlImageComponent` or similar per-component texture |
| Background uses `float pixel_scale` | Component uses `int pixel_scale` |
| e.g., knob labels, section tabs (ENV1/LFO1), preset title | e.g., main tabs (VOICE/EFFECTS), button text, slider values |

## Fix

```cpp
// CORRECT — preserves fractional scale, texture matches physical pixels
float pixel_scale = Desktop::getInstance().getDisplays()
    .findDisplayForPoint(getScreenPosition()).scale;
int width = std::ceil(component->getWidth() * pixel_scale);
int height = std::ceil(component->getHeight() * pixel_scale);
// Graphics transform still uses the float directly:
g.addTransform(AffineTransform::scale(pixel_scale));
```

## Files to Check in a Custom OpenGL JUCE App

Search for `int pixel_scale` or `.scale` in all `.cpp` files. Every occurrence that feeds into `Image` construction needs to be `float`. The JUCE `OpenGLBackground` pattern (full-screen texture) usually already uses `float` — it's the per-component `OpenGlImageComponent` that typically has the bug.

## Verified On

- Windows 10/11 with 125%, 150%, 175% scaling
- JUCE 8.0.x
- Vial synthesizer (custom OpenGL rendering pipeline with `setComponentPaintingEnabled(false)`)
