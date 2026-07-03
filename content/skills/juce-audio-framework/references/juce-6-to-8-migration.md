# JUCE 6 → 8 Migration Guide

## Font API Breaking Changes

JUCE 8 deprecated the direct `Font` constructors in favor of `FontOptions`:

### Font Construction

**JUCE 6 pattern (deprecated in JUCE 8):**
```cpp
Font font(Typeface::createSystemTypefaceFor(data, size));
```

**JUCE 8 pattern:**
```cpp
Font font(FontOptions(Typeface::createSystemTypefaceFor(data, size)));
```

### Default Constructor

**JUCE 6 pattern (deprecated in JUCE 8):**
```cpp
Font font;  // Default constructor
font = otherFont.withPointHeight(12.0f);
```

**JUCE 8 pattern:**
```cpp
Font font = condition 
  ? Fonts::instance()->monospace().withPointHeight(12.0f)
  : Fonts::instance()->proportional_light().withPointHeight(12.0f);
```

Or initialize with FontOptions:
```cpp
Font font(FontOptions());  // Then modify as needed
```

### Common Migration Locations

1. **Font initialization in constructor lists:**
```cpp
// JUCE 6
MyClass::MyClass() :
    my_font_(Typeface::createSystemTypefaceFor(data, size)) {}

// JUCE 8
MyClass::MyClass() :
    my_font_(FontOptions(Typeface::createSystemTypefaceFor(data, size))) {}
```

2. **Conditional font selection:**
```cpp
// JUCE 6
Font font;
if (condition)
  font = Fonts::instance()->monospace();

// JUCE 8
Font font = condition 
  ? Fonts::instance()->monospace()
  : Fonts::instance()->proportional_light();
```

## Font Metrics Changes

JUCE 8 font metrics differ from JUCE 6, potentially causing:
- Vertical text misalignment
- Different ascent/descent ratios
- Changed `getStringWidthFloat()` results

### Text Positioning Adjustments

If text appears misaligned after migration, check these locations:
- `LookAndFeel::drawRotarySlider()` - slider value popups
- `LookAndFeel::drawToggleButton()` - button text
- `SynthSection::drawLabel()` methods - section headers
- Custom `paintToImage()` implementations

**Adjustment pattern:**
```cpp
// If text is off-center vertically:
int adjusted_y = y + (height - font.getHeight()) / 2;
g.drawText(text, x, adjusted_y, width, font.getHeight(), justification, false);
```

## Migration Checklist

- [ ] Search for `Font(` and wrap `Typeface::Ptr` arguments in `FontOptions()`
- [ ] Replace `Font font;` default constructions with conditional expressions or `FontOptions()`
- [ ] Build and check for deprecation warnings
- [ ] Test all text rendering locations for vertical alignment
- [ ] Verify slider popups are centered
- [ ] Verify button text is centered
- [ ] Verify section headers render correctly
- [ ] Check HiDPI display rendering (pixel_scale handling)

## OpenGL Texture Sizing

JUCE 8's `Desktop::getInstance().getDisplays().findDisplayForPoint()` returns proper scale factors. Ensure `OpenGlImageComponent::redrawImage()` uses:

```cpp
int pixel_scale = Desktop::getInstance().getDisplays().findDisplayForPoint(getScreenPosition()).scale;
int width = component->getWidth() * pixel_scale;
int height = component->getHeight() * pixel_scale;
```

Then apply `g.addTransform(AffineTransform::scale(pixel_scale))` before rendering.
