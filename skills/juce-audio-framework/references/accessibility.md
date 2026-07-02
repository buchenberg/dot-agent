# JUCE Accessibility

JUCE supports native screen readers and keyboard navigation across platforms.

## Supported Platforms

| Platform | Screen Reader | Notes |
|----------|---------------|-------|
| Windows | Narrator | UI Automation (UIA) provider |
| macOS | VoiceOver | NSAccessibility protocol |
| iOS | VoiceOver | UIAccessibility |
| Android | TalkBack | AccessibilityService |

## Capabilities Exposed

- **Title, description, help text** for UI elements
- **Programmatic access** to UI elements and text
- **Interaction** with UI elements (click, toggle, adjust)
- **Full keyboard navigation** across the component tree
- **Notifications** posted to listening screen reader clients

## Default Behavior

Any visible and enabled `Component` is automatically accessible to screen reader clients. It exposes basic information: title, description, help text, and position in the UI hierarchy.

## Customizing Accessibility Text

```cpp
myComponent.setTitle ("Gain Knob");
myComponent.setDescription ("Controls the output gain, range 0 to 100 percent");
myComponent.setHelpText ("Drag up to increase gain, drag down to decrease");
```

## Focus Navigation

```cpp
// Explicit focus order (lower numbers first)
myComponent.setExplicitFocusOrder (1);
otherComponent.setExplicitFocusOrder (2);

// Focus container type
myComponent.setFocusContainerType (juce::Component::FocusContainerType::focusContainer);
// or
myComponent.setFocusContainerType (juce::Component::FocusContainerType::none);

// Custom focus traverser
class MyFocusTraverser : public juce::ComponentTraverser
{
public:
    juce::Component* getNextComponent (juce::Component* current) override { /* ... */ }
    juce::Component* getPreviousComponent (juce::Component* current) override { /* ... */ }
    std::vector<juce::Component*> getAllComponents (juce::Component* parent) override { /* ... */ }
};

// Override in your component
std::unique_ptr<juce::ComponentTraverser> createFocusTraverser() override
{
    return std::make_unique<MyFocusTraverser>();
}
```

## Custom AccessibilityHandler

For full control, subclass `AccessibilityHandler` and return it from `Component::createAccessibilityHandler()`:

```cpp
class MyAccessibleComponent : public juce::Component
{
public:
    class Handler : public juce::AccessibilityHandler
    {
    public:
        explicit Handler (MyAccessibleComponent& comp)
            : AccessibilityHandler (comp, juce::AccessibilityRole::slider),
              component (comp)
        {}

        juce::String getTitle() const override { return component.title; }
        juce::String getDescription() const override { return component.description; }

        juce::AccessibilityActions getActions() const override
        {
            auto actions = AccessibilityHandler::getActions();
            actions.addAction (juce::AccessibilityActionType::showMenu,
                [&] { component.showContextMenu(); });
            return actions;
        }

        juce::AccessibilityValueInterface* getValueInterface() const override
        {
            return &valueInterface;
        }

    private:
        MyAccessibleComponent& component;

        struct ValueInterface : public juce::AccessibilityValueInterface
        {
            bool isReadOnly() const override { return false; }
            juce::var getCurrentValue() const override { return 0.5; }
            void setValue (const juce::var&) override { /* update value */ }
            juce::String getCurrentValueAsString() const override { return "50%"; }
            void setValueAsString (const juce::String&) override { /* parse and set */ }
            juce::Range<double> getRange() const override { return { 0.0, 1.0 }; }
            double getInterval() const override { return 0.01; }
            juce::String getParameterID() const override { return "gain"; }
        };

        ValueInterface valueInterface;
    };

    std::unique_ptr<juce::AccessibilityHandler> createAccessibilityHandler() override
    {
        return std::make_unique<Handler> (*this);
    }

    juce::String title, description;
};
```

## AccessibilityRole Enum

Key roles for audio plugin UIs:

| Role | Use |
|------|-----|
| `slider` | Rotary/linear knobs and sliders |
| `button` | Clickable buttons, toggles |
| `comboBox` | Dropdown selectors |
| `label` | Static text labels |
| `textEditor` | Text input fields |
| `toggleButton` | On/off switches |
| `menuItem` | Menu items |
| `window` | Top-level windows |
| `group` | Logical grouping of controls |
| `ignored` | Decorative elements (skip in navigation) |

## Posting Accessibility Notifications

When a value changes programmatically (not via user interaction), notify the screen reader:

```cpp
if (auto* handler = getAccessibilityHandler())
    handler->notifyAccessibilityEvent (juce::AccessibilityEvent::valueChanged);
```

Available events:
- `valueChanged` — parameter value updated
- `textChanged` — label/text content changed
- `focusChanged` — component gained/lost focus
- `windowOpened` / `windowClosed` — window visibility
- `rowExpanded` / `rowCollapsed` — tree/list expansion

## Best Practices

- **Always set `setTitle()`** on interactive controls — screen readers announce this
- **Use `setHelpText()`** for longer descriptions (read on demand, not automatically)
- **Set `setAccessible(true)`** on decorative elements you want to exclude from navigation
- **Group related controls** using `setFocusContainerType(focusContainer)`
- **Test with actual screen readers** — Narrator on Windows, VoiceOver on macOS
- **Avoid custom drawing for text** — use `Label` components where possible so text is accessible
- **Keyboard navigation**: ensure all interactive controls are reachable via Tab/Shift+Tab

## References

- JUCE Accessibility docs: https://juce.com/learn/documentation
- NSAccessibility: https://developer.apple.com/documentation/appkit/nsaccessibility
- UI Automation (Win32): https://docs.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32
- ADC 2020 talk: https://youtu.be/BqrEv4ApH3U
