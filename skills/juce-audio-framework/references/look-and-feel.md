# JUCE LookAndFeel — Complete Customization Reference

## Built-in Themes

| Class | Style |
|-------|-------|
| `LookAndFeel_V2` | Flat, modern default |
| `LookAndFeel_V3` | Subtle refinements over V2 |
| `LookAndFeel_V4` | Color scheme API, more customizable |

## Setting a LookAndFeel

```cpp
// Globally (application-wide)
juce::LookAndFeel::setDefaultLookAndFeel (&myLookAndFeel);

// Per-component (and children)
myEditor.setLookAndFeel (&myLookAndFeel);
```

## Custom LookAndFeel

```cpp
class MyLookAndFeel final : public juce::LookAndFeel_V4
{
public:
    MyLookAndFeel()
    {
        setColourScheme (juce::LookAndFeel_V4::getMidnightColourScheme());
        setColour (juce::Slider::thumbColourId, juce::Colours::orange);
        setColour (juce::Slider::rotarySliderFillColourId, juce::Colours::darkorange);
        setColour (juce::TextButton::buttonColourId, juce::Colour (0xff3b3b3b));
    }

    void drawRotarySlider (juce::Graphics& g, int x, int y, int width, int height,
                           float sliderPos, float rotaryStartAngle,
                           float rotaryEndAngle, juce::Slider& slider) override
    {
        auto bounds = juce::Rectangle<int> (x, y, width, height).toFloat().reduced (10);
        auto radius = juce::jmin (bounds.getWidth(), bounds.getHeight()) / 2.0f;
        auto centreX = bounds.getCentreX();
        auto centreY = bounds.getCentreY();
        auto angle = rotaryStartAngle + sliderPos * (rotaryEndAngle - rotaryStartAngle);

        // Background arc
        juce::Path backgroundArc;
        backgroundArc.addCentredArc (centreX, centreY, radius, radius, 0.0f,
                                     rotaryStartAngle, rotaryEndAngle, true);
        g.setColour (juce::Colours::grey);
        g.strokePath (backgroundArc, juce::PathStrokeType (3.0f,
            juce::PathStrokeType::curved, juce::PathStrokeType::rounded));

        // Value arc
        juce::Path valueArc;
        valueArc.addCentredArc (centreX, centreY, radius, radius, 0.0f,
                                rotaryStartAngle, angle, true);
        g.setColour (findColour (juce::Slider::rotarySliderFillColourId));
        g.strokePath (valueArc, juce::PathStrokeType (3.0f,
            juce::PathStrokeType::curved, juce::PathStrokeType::rounded));

        // Thumb indicator
        juce::Path thumb;
        auto thumbWidth = 8.0f;
        thumb.addRoundedRectangle (-thumbWidth * 0.5f, -radius + 4.0f,
                                    thumbWidth, 16.0f, 3.0f);
        g.setColour (findColour (juce::Slider::thumbColourId));
        g.fillPath (thumb, juce::AffineTransform::rotation (angle).translated (centreX, centreY));
    }

    void drawLinearSlider (juce::Graphics& g, int x, int y, int width, int height,
                           float sliderPos, float minPos, float maxPos,
                           juce::Slider::SliderStyle style, juce::Slider& slider) override
    {
        auto trackWidth = 4.0f;
        juce::Point<float> startPoint ((float) x, (float) y + (float) height * 0.5f);
        juce::Point<float> endPoint ((float) (x + width), startPoint.y);

        // Track background
        juce::Path backgroundTrack;
        backgroundTrack.startNewSubPath (startPoint);
        backgroundTrack.lineTo (endPoint);
        g.setColour (juce::Colours::grey);
        g.strokePath (backgroundTrack, juce::PathStrokeType (trackWidth,
            juce::PathStrokeType::curved, juce::PathStrokeType::rounded));

        // Track value
        juce::Path valueTrack;
        valueTrack.startNewSubPath (startPoint);
        valueTrack.lineTo (juce::Point<float> (sliderPos, startPoint.y));
        g.setColour (findColour (juce::Slider::trackColourId));
        g.strokePath (valueTrack, juce::PathStrokeType (trackWidth,
            juce::PathStrokeType::curved, juce::PathStrokeType::rounded));

        // Thumb
        auto thumbRadius = 8.0f;
        g.setColour (findColour (juce::Slider::thumbColourId));
        g.fillEllipse (sliderPos - thumbRadius, startPoint.y - thumbRadius,
                       thumbRadius * 2.0f, thumbRadius * 2.0f);
    }
};
```

## Complete Virtual Methods Reference

### Buttons
```
drawButtonBackground(Graphics&, Button&, const Colour&, bool isHighlighted, bool isDown)
drawButtonText(Graphics&, TextButton&, bool isHighlighted, bool isDown)
getTextButtonFont(TextButton&, int buttonHeight) -> Font
getTextButtonWidthToFitText(TextButton&, int buttonHeight) -> int
drawToggleButton(Graphics&, ToggleButton&, bool isHighlighted, bool isDown)
changeToggleButtonWidthToFitText(ToggleButton&)
drawTickBox(Graphics&, Component&, float x, y, w, h, bool ticked, bool isEnabled, bool isHighlighted, bool isDown)
drawDrawableButton(Graphics&, DrawableButton&, bool isHighlighted, bool isDown)
drawImageButton(Graphics&, Image*, int x, y, w, h, const Colour& overlay, float opacity, ImageButton&)
```

### Sliders
```
drawLinearSlider(Graphics&, int x, y, width, height, float sliderPos, minPos, maxPos, SliderStyle, Slider&)
drawLinearSliderBackground(Graphics&, int x, y, width, height, float sliderPos, minPos, maxPos, SliderStyle, Slider&)
drawLinearSliderOutline(Graphics&, int x, y, width, height, SliderStyle, Slider&)
drawLinearSliderThumb(Graphics&, int x, y, width, height, float sliderPos, minPos, maxPos, SliderStyle, Slider&)
drawRotarySlider(Graphics&, int x, y, width, height, float sliderPosProportional, float rotaryStartAngle, float rotaryEndAngle, Slider&)
getSliderThumbRadius(Slider&) -> int
createSliderButton(Slider&, bool isIncrement) -> Button*
createSliderTextBox(Slider&) -> Label*
getSliderEffect(Slider&) -> ImageEffectFilter*
getSliderPopupFont(Slider&) -> Font
getSliderPopupPlacement(Slider&) -> int
getSliderLayout(Slider&) -> Slider::SliderLayout
```

### ComboBox
```
drawComboBox(Graphics&, int width, height, bool isMouseButtonDown, int buttonX, buttonY, buttonW, buttonH, ComboBox&)
getComboBoxFont(ComboBox&) -> Font
createComboBoxTextBox(ComboBox&) -> Label*
positionComboBoxText(ComboBox&, Label&)
getOptionsForComboBoxPopupMenu(ComboBox&, Label&) -> PopupMenu::Options
drawComboBoxTextWhenNothingSelected(Graphics&, ComboBox&, Label&)
```

### Label
```
drawLabel(Graphics&, Label&)
getLabelFont(Label&) -> Font
getLabelBorderSize(Label&) -> BorderSize<int>
```

### TextEditor
```
fillTextEditorBackground(Graphics&, int width, height, TextEditor&)
drawTextEditorOutline(Graphics&, int width, height, TextEditor&)
createCaretComponent(Component* keyFocusOwner) -> CaretComponent*
```

### ScrollBar
```
drawScrollbar(Graphics&, ScrollBar&, int x, y, width, height, bool isVertical, int thumbStartPosition, int thumbSize, bool isMouseOver, bool isMouseDown)
drawScrollbarButton(Graphics&, ScrollBar&, int width, height, int buttonDirection, bool isVertical, bool isHighlighted, bool isDown)
areScrollbarButtonsVisible() -> bool
getScrollbarEffect() -> ImageEffectFilter*
getMinimumScrollbarThumbSize(ScrollBar&) -> int
getDefaultScrollbarWidth() -> int
getScrollbarButtonSize(ScrollBar&) -> int
```

### TreeView
```
drawTreeviewPlusMinusBox(Graphics&, const Rectangle<float>& area, Colour background, bool isOpen, bool isMouseOver)
areLinesDrawnForTreeView(TreeView&) -> bool
getTreeViewIndentSize(TreeView&) -> int
```

### PopupMenu
```
drawPopupMenuBackground(Graphics&, int width, height)
drawPopupMenuBackgroundWithOptions(Graphics&, int width, height, const PopupMenu::Options&)
drawPopupMenuItem(Graphics&, const Rectangle<int>& area, bool isSeparator, bool isActive, bool isHighlighted, bool isTicked, bool hasSubMenu, const String& text, const String& shortcutKeyText, const Drawable* icon, const Colour* textColour)
drawPopupMenuItemWithOptions(Graphics&, const Rectangle<int>& area, bool isHighlighted, const PopupMenu::Item&, const PopupMenu::Options&)
drawPopupMenuSectionHeader(Graphics&, const Rectangle<int>& area, const String& sectionName)
getPopupMenuFont() -> Font
drawPopupMenuUpDownArrow(Graphics&, int width, height, bool isScrollUpArrow)
getIdealPopupMenuItemSize(const String& text, bool isSeparator, int standardMenuItemHeight, int& idealWidth, int& idealHeight)
getMenuWindowFlags() -> int
getPopupMenuBorderSize() -> int
getPopupMenuBorderSizeWithOptions(const PopupMenu::Options&) -> int
drawPopupMenuColumnSeparatorWithOptions(Graphics&, const Rectangle<int>& bounds, const PopupMenu::Options&)
shouldPopupMenuScaleWithTargetComponent(const PopupMenu::Options&) -> bool
```

### MenuBar
```
drawMenuBarBackground(Graphics&, int width, height, bool isMouseOverBar, MenuBarComponent&)
getMenuBarItemWidth(MenuBarComponent&, int itemIndex, const String& itemText) -> int
getMenuBarFont(MenuBarComponent&, int itemIndex, const String& itemText) -> Font
getDefaultMenuBarHeight() -> int
drawMenuBarItem(Graphics&, int width, height, int itemIndex, const String& itemText, bool isMouseOverItem, bool isMenuOpen, bool isMouseOverBar, MenuBarComponent&)
```

### Window
```
drawDocumentWindowTitleBar(DocumentWindow&, Graphics&, int w, h, int titleSpaceX, titleSpaceW, const Image* icon, bool drawTitleTextOnLeft)
createDocumentWindowButton(int buttonType) -> Button*
positionDocumentWindowButtons(DocumentWindow&, int titleBarX, titleBarY, titleBarW, titleBarH, Button* minimise, Button* maximise, Button* close, bool positionTitleBarButtonsOnLeft)
drawCornerResizer(Graphics&, int w, h, bool isMouseOver, bool isMouseDragging)
drawResizableFrame(Graphics&, int w, h, const BorderSize<int>&)
fillResizableWindowBackground(Graphics&, int w, h, const BorderSize<int>&, ResizableWindow&)
drawResizableWindowBorder(Graphics&, int w, h, const BorderSize<int>& border, ResizableWindow&)
```

### AlertWindow
```
createAlertWindow(const String& title, message, button1, button2, button3, MessageBoxIconType, int numButtons, Component* associated) -> AlertWindow*
drawAlertBox(Graphics&, AlertWindow&, const Rectangle<int>& textArea, TextLayout&)
getAlertBoxWindowFlags() -> int
getAlertWindowButtonHeight() -> int
getAlertWindowTitleFont() -> Font
getAlertWindowMessageFont() -> Font
getAlertWindowFont() -> Font
```

### ProgressBar
```
drawProgressBar(Graphics&, ProgressBar&, int width, height, double progress, const String& textToShow)
isProgressBarOpaque(ProgressBar&) -> bool
```

### TabbedButtonBar
```
drawTabButton(TabBarButton&, Graphics&, bool isMouseOver, bool isMouseDown)
getTabButtonFont(TabBarButton&, float height) -> Font
drawTabButtonText(TabBarButton&, Graphics&, bool isMouseOver, bool isMouseDown)
drawTabbedButtonBarBackground(TabbedButtonBar&, Graphics&)
drawTabAreaBehindFrontButton(TabbedButtonBar&, Graphics&, int w, h)
createTabButtonShape(TabBarButton&, Path&, bool isMouseOver, bool isMouseDown)
fillTabButtonShape(TabBarButton&, Graphics&, const Path&, bool isMouseOver, bool isMouseDown)
getTabButtonSpaceAroundImage() -> int
getTabButtonOverlap(int tabDepth) -> int
getTabButtonBestWidth(TabBarButton&, int tabDepth) -> int
```

### TableHeader
```
drawTableHeaderBackground(Graphics&, TableHeaderComponent&)
drawTableHeaderColumn(Graphics&, TableHeaderComponent&, const String& columnName, int columnId, int width, height, bool isMouseOver, bool isMouseDown, int columnFlags)
```

### Toolbar
```
paintToolbarBackground(Graphics&, int width, height, Toolbar&)
createToolbarMissingItemsButton(Toolbar&) -> Button*
paintToolbarButtonBackground(Graphics&, int width, height, bool isMouseOver, bool isMouseDown, ToolbarItemComponent&)
paintToolbarButtonLabel(Graphics&, int x, y, width, height, const String& text, ToolbarItemComponent&)
```

### Tooltip
```
getTooltipBounds(const String& tipText, Point<int> screenPos, Rectangle<int> parentArea) -> Rectangle<int>
drawTooltip(Graphics&, const String& text, int width, height)
```

### GroupComponent
```
drawGroupComponentOutline(Graphics&, int w, h, const String& text, const Justification&, GroupComponent&)
```

### CallOutBox
```
drawCallOutBoxBackground(CallOutBox&, Graphics&, const Path& path, Image& cachedImage)
getCallOutBoxBorderSize(const CallOutBox&) -> int
getCallOutBoxCornerSize(const CallOutBox&) -> float
```

### PropertyComponent
```
drawPropertyPanelSectionHeader(Graphics&, const String& name, bool isOpen, int width, height)
drawPropertyComponentBackground(Graphics&, int width, height, PropertyComponent&)
drawPropertyComponentLabel(Graphics&, int width, height, PropertyComponent&)
getPropertyComponentContentPosition(PropertyComponent&) -> Rectangle<int>
getPropertyPanelSectionHeaderHeight(const String& sectionTitle) -> int
```

### Other
```
drawSpinningWaitAnimation(Graphics&, const Colour&, int x, y, w, h)
getTickShape(float height) -> Path
getCrossShape(float height) -> Path
drawBubble(Graphics&, BubbleComponent&, const Point<float>& tip, const Rectangle<float>& body)
drawConcertinaPanelHeader(Graphics&, const Rectangle<int>& area, bool isMouseOver, bool isMouseDown, ConcertinaPanel&, Component& panel)
drawStretchableLayoutResizerBar(Graphics&, int w, h, bool isVerticalBar, bool isMouseOver, bool isMouseDragging)
drawLasso(Graphics&, Component& lassoComp)
drawKeymapChangeButton(Graphics&, int width, height, Button&, const String& keyDescription)
drawLevelMeter(Graphics&, int width, height, float level)
getTypefaceForFont(const Font&) -> Typeface::Ptr
createGraphicsContext(const Image& imageToRenderInto, Point<int> origin, const Image::PixelFormat format, bool isForSaving) -> std::unique_ptr<LowLevelGraphicsContext>
```
