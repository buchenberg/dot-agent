# JUCE 8 Web Parameter Relays

JUCE 8 provides relay classes that automatically bind APVTS parameters to JavaScript objects inside a `WebBrowserComponent`. This is the recommended approach for WebView-based plugin UIs — simpler and more robust than manual `withNativeIntegration` callbacks.

## Relay Classes

| Class | JS Accessor | Parameter Type |
|-------|-------------|----------------|
| `WebSliderRelay` | `Juce.getSliderState("name")` | Continuous (float) |
| `WebToggleButtonRelay` | `Juce.getToggleState("name")` | Boolean |
| `WebComboBoxRelay` | `Juce.getComboBoxState("name")` | Choice/enum |

Each relay creates a named JavaScript object with getter/setter methods and event listeners.

## Attachment Classes

| Attachment | Connects To |
|------------|-------------|
| `WebSliderParameterAttachment` | `RangedAudioParameter` ↔ `WebSliderRelay` |
| `WebToggleButtonParameterAttachment` | `RangedAudioParameter` ↔ `WebToggleButtonRelay` |
| `WebComboBoxParameterAttachment` | `RangedAudioParameter` ↔ `WebComboBoxRelay` |

## Usage Pattern

```cpp
#include <juce_audio_processors/juce_audio_processors.h>
#include <juce_gui_extra/juce_gui_extra.h>

class WebViewEditor : public juce::AudioProcessorEditor
{
public:
    WebViewEditor (MyProcessor& p)
        : AudioProcessorEditor (&p), processor (p),
          gainSliderAttachment (*p.apvts.getParameter ("gain"), gainSliderRelay, nullptr),
          bypassAttachment (*p.apvts.getParameter ("bypass"), bypassRelay, nullptr),
          modeAttachment (*p.apvts.getParameter ("mode"), modeRelay, nullptr)
    {
        // Build WebBrowserComponent options from all relays
        juce::WebBrowserComponent::Options options;
        options = options.withOptionsFrom (gainSliderRelay);
        options = options.withOptionsFrom (bypassRelay);
        options = options.withOptionsFrom (modeRelay);

        // Add resource provider for serving frontend
        options = options.withResourceProvider ([this] (const juce::String& path)
            -> std::optional<juce::WebBrowserComponent::Resource>
        {
            return serveResource (path);
        });

        webBrowser.setOptions (options);
        addAndMakeVisible (webBrowser);
        setSize (600, 400);

    #ifdef DEBUG
        webBrowser.goToURL ("http://localhost:3000");
    #else
        webBrowser.goToURL ("https://plugin-app/index.html");
    #endif
    }

    void resized() override { webBrowser.setBounds (getLocalBounds()); }

private:
    MyProcessor& processor;

    // Relays (one per parameter)
    juce::WebSliderRelay        gainSliderRelay { "gainSlider" };
    juce::WebToggleButtonRelay  bypassRelay { "bypassToggle" };
    juce::WebComboBoxRelay      modeRelay { "modeCombo" };

    // Attachments (connect relay ↔ parameter)
    juce::WebSliderParameterAttachment        gainSliderAttachment;
    juce::WebToggleButtonParameterAttachment  bypassAttachment;
    juce::WebComboBoxParameterAttachment      modeAttachment;

    juce::WebBrowserComponent webBrowser;
};
```

## JavaScript Side

Install the `juce-framework-frontend` npm package:

```bash
npm install juce-framework-frontend
```

Then in your React/Vue/JS code:

```javascript
import { getSliderState, getToggleState, getComboBoxState } from "juce-framework-frontend";

// Get a slider relay
const gainState = getSliderState("gainSlider");

// Read value
console.log(gainState.getValue());  // 0.0 - 1.0 normalized

// Set value
gainState.setValue(0.75);

// Listen for changes
gainState.addListener((newValue) => {
    updateSliderUI(newValue);
});

// Toggle
const bypassState = getToggleState("bypassToggle");
bypassState.getValue();  // true/false
bypassState.setValue(true);
bypassState.addListener((toggled) => { /* ... */ });

// ComboBox
const modeState = getComboBoxState("modeCombo");
modeState.getValue();  // 0.0 - 1.0 normalized index
modeState.addListener((value) => { /* ... */ });
```

## vs Manual withNativeIntegration

| Approach | Pros | Cons |
|----------|------|------|
| **Web Relays** (recommended) | Automatic bidirectional sync, type-safe, less code, handles attach/detach | Requires `juce-framework-frontend` npm package |
| **Manual `withNativeIntegration`** | Full control, no npm dependency | Manual serialization, polling or push logic, more boilerplate |

## Custom Relay Integration

For parameters that don't fit slider/toggle/combo patterns, use `withNativeIntegration` as a fallback:

```cpp
options.withNativeIntegration ([this] (const juce::String& name, const juce::var& args) -> juce::var
{
    if (name == "getCustomState")
        return getCustomStateAsJSON();
    return {};
});
```

## References

- JUCE WebBrowserComponent: `modules/juce_gui_extra/native/juce_WebBrowserComponent.h`
- `juce-framework-frontend` npm: https://www.npmjs.com/package/juce-framework-frontend
- WebViewPluginDemo: `JUCE/examples/Plugins/WebViewPluginDemo/`
