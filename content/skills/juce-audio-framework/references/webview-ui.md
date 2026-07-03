# JUCE WebView UIs (JUCE 8+)

Build plugin and app UIs with React, Vue, Svelte, or plain HTML/CSS/JavaScript instead of native JUCE Components.

## Why WebView

- **Rapid iteration**: Hot reloading during development
- **Mature ecosystems**: React, Vue, Svelte component libraries
- **Frontend developers can contribute**: No C++ required for UI work
- **Hardware-accelerated graphics**: WebGL for complex visualizations
- **Smaller binaries**: WebView provided by the OS

**Platform WebViews:**
- macOS: WebKit
- Windows: Edge (Chromium) — pre-installed on Win11, most Win10
- Linux: GTK WebKit2

## CMake Configuration

```cmake
juce_add_plugin(MyPlugin
    FORMATS AU VST3 Standalone
    NEEDS_WEBVIEW2 TRUE  # Required for Windows
)

target_compile_definitions(MyPlugin
    PUBLIC
        JUCE_WEB_BROWSER=1
        JUCE_USE_WIN_WEBVIEW2_WITH_STATIC_LINKING=1
)

target_link_libraries(MyPlugin PRIVATE juce::juce_gui_extra)
```

If WebView2 NuGet is in a non-standard location:
```cmake
set(JUCE_WEBVIEW2_PACKAGE_LOCATION "/path/to/webview2/nuget")
```

## WebBrowserComponent

```cpp
class MyWebViewEditor : public juce::AudioProcessorEditor
{
public:
    MyWebViewEditor (MyProcessor& p)
        : AudioProcessorEditor (&p), processor (p)
    {
        juce::WebBrowserComponent::Options options;

        options.withUserAgent ("MyPlugin/1.0");
        options.withResourceProvider ([this] (const juce::String& path)
            -> std::optional<juce::WebBrowserComponent::Resource>
        {
            return getResource (path);
        });

        options.withNativeIntegration (
            [this] (const juce::String& name, const juce::var& args) -> juce::var
            {
                if (name == "getParameterValue")
                    return processor.apvts.getRawParameterValue (args.toString())->load();
                if (name == "setParameterValue")
                {
                    auto* param = processor.apvts.getParameter (args[0].toString());
                    param->setValueNotifyingHost ((float) args[1]);
                    return {};
                }
                return {};
            });

        webBrowser.setOptions (options);
        addAndMakeVisible (webBrowser);
        setSize (600, 400);

        webBrowser.goToURL ("https://plugin-app/index.html");
    }

    void resized() override { webBrowser.setBounds (getLocalBounds()); }

private:
    std::optional<juce::WebBrowserComponent::Resource> getResource (const juce::String& path)
    {
        if (path == "/index.html")
            return juce::WebBrowserComponent::Resource {
                BinaryData::index_html, BinaryData::index_htmlSize, "text/html" };
        if (path == "/bundle.js")
            return juce::WebBrowserComponent::Resource {
                BinaryData::bundle_js, BinaryData::bundle_jsSize, "application/javascript" };
        return std::nullopt;
    }

    MyProcessor& processor;
    juce::WebBrowserComponent webBrowser;
};
```

## C++ ↔ JavaScript Communication

### JavaScript → C++ (Native Integration)

```javascript
const value = await window.juce.nativeIntegration.getParameterValue("gain");
await window.juce.nativeIntegration.setParameterValue("gain", 0.75);
```

### C++ → JavaScript (Evaluate Script)

```cpp
webBrowser.evaluateJavascript ("window.updateGainValue(0.75)");
auto json = juce::JSON::toString (myData);
webBrowser.evaluateJavascript ("window.receiveData(" + json + ")");
```

## Development Workflow

### Debug Mode (Hot Reloading)

```cpp
#ifdef DEBUG
    webBrowser.goToURL ("http://localhost:3000");
#else
    webBrowser.goToURL ("https://plugin-app/index.html");
#endif
```

### Release Mode (Embedded Resources)

```cmake
juce_add_binary_data(FrontendData
    SOURCES
        frontend/dist/index.html
        frontend/dist/bundle.js
        frontend/dist/styles.css
)
target_link_libraries(MyPlugin PRIVATE FrontendData)
```

## Best Practices

**Do:**
- Use `NEEDS_WEBVIEW2 TRUE` in CMake for Windows
- Statically link WebView2 with `JUCE_USE_WIN_WEBVIEW2_WITH_STATIC_LINKING=1`
- Use resource providers for embedded frontend assets in Release
- Load from `localhost` dev server during development
- Keep C++ ↔ JS communication minimal and asynchronous
- Use TypeScript for type safety

**Don't:**
- Bundle WebView binaries (provided by OS)
- Block message thread with synchronous JS evaluation
- Assume all WebView features work identically across platforms
- Forget to handle WebView unavailability gracefully

## Limitations

- No built-in JUCE widgets for WebView — choose your own framework
- Platform differences between WebKit, Edge, GTK WebKit2
- Parameter labels must be manually exposed to JavaScript
- WebView accessibility less mature than native JUCE Components
- Plugin hosts may have stricter requirements for WebView UIs
- WebView initialization adds small delay on first launch
