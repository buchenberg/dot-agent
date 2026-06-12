---
description: JUCE C++ audio framework — plugin development, DSP chains, GUI components, LookAndFeel customization, font rendering, OpenGL rendering, state management. Use when building audio plugins (VST/AU/AAX), standalone audio apps, DSP processing chains, custom GUIs, or any JUCE C++ project. WHEN: JUCE, juce, AudioProcessor, AudioPlugin, VST, AU plugin, AAX, AudioProcessorEditor, processBlock, prepareToPlay, DSP, ProcessorChain, AudioBlock, LookAndFeel, custom slider, custom knob, OpenGL, OpenGLContext, OpenGLRenderer, shader, Font rendering, Typeface, Graphics, FlexBox, Grid layout, AudioDeviceManager, AudioFormatManager, APVTS, AudioProcessorValueTreeState, Projucer, CMake juce.
---

# JUCE Audio Framework — Complete Development Reference

## What is JUCE?

JUCE (Jules' Useful Class Extensions) is an open-source C++ framework for cross-platform audio application development. It provides everything from low-level audio I/O to high-level GUI widgets, all in a single integrated library. Target platforms: Windows, macOS, Linux, iOS, Android.

- **License**: ISC (core modules), GPL/commercial (some modules)
- **Build systems**: CMake (primary), Projucer (legacy GUI project editor)
- **Current version**: 8.x (as of 2026)
- **C++ standard**: C++17 minimum

---

## 1. Project Setup

### CMake (recommended)

```cmake
cmake_minimum_required(VERSION 3.22)
project(MyPlugin VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 17)

# Add JUCE as a subdirectory or via find_package / FetchContent
add_subdirectory(JUCE)

# Standalone app
juce_add_gui_app(MyApp PRODUCT_NAME "My App")

# Audio plugin
juce_add_plugin(MyPlugin
    COMPANY_NAME "MyCompany"
    IS_SYNTH FALSE
    NEEDS_MIDI_INPUT TRUE
    NEEDS_MIDI_OUTPUT FALSE
    IS_MIDI_EFFECT FALSE
    EDITOR_WANTS_KEYBOARD_FOCUS FALSE
    COPY_PLUGIN_AFTER_BUILD TRUE
    PLUGIN_MANUFACTURER_CODE Mnc1
    PLUGIN_CODE Mpl1
    FORMATS AU VST3 Standalone
    PRODUCT_NAME "My Plugin"
)

# Link modules
target_link_libraries(MyPlugin
    PRIVATE
        juce::juce_audio_utils
        juce::juce_dsp
        juce::juce_opengl
    PUBLIC
        juce::juce_recommended_config_flags
        juce::juce_recommended_lto_flags
        juce::juce_recommended_warning_flags
)

# Enable binary data
juce_add_binary_data(AudioPluginData SOURCES resources/myfile.wav)
target_link_libraries(MyPlugin PRIVATE AudioPluginData)
```

### Key CMake functions

| Function | Purpose |
|----------|---------|
| `juce_add_gui_app(name ...)` | Standalone GUI application |
| `juce_add_console_app(name ...)` | Console/CLI application |
| `juce_add_plugin(name ...)` | Audio plugin (VST3/AU/AAX/Standalone) |
| `juce_add_binary_data(name ...)` | Embed files as C++ binary data |
| `juce_generate_juce_header(target)` | Generate a JuceHeader.h (legacy) |

### Plugin format targets

When `juce_add_plugin` specifies `FORMATS AU VST3 Standalone`, CMake creates:
- `MyPlugin_AU` — Audio Unit (macOS only)
- `MyPlugin_VST3` — VST3 (all platforms)
- `MyPlugin_Standalone` — Standalone app wrapper

---

## 2. Module Inventory

JUCE is organized into self-contained modules. Each lives in `modules/juce_<name>/`.

### Audio Modules
| Module | Purpose |
|--------|---------|
| `juce_audio_basics` | AudioBuffer, MidiMessage, MidiBuffer, IIRFilter, decibels, FFT |
| `juce_audio_devices` | AudioDeviceManager, audio/MIDI I/O, device enumeration |
| `juce_audio_formats` | AudioFormatManager, WAV/AIFF/FLAC/OGG readers/writers |
| `juce_audio_processors` | AudioProcessor, AudioProcessorEditor, plugin hosting, APVTS |
| `juce_audio_utils` | AudioAppComponent, MidiKeyboardComponent, convenience wrappers |
| `juce_dsp` | DSP building blocks: ProcessorChain, AudioBlock, filters, effects |
| `juce_audio_plugin_client` | Plugin format wrappers (VST3, AU, AAX, Standalone) |

### GUI Modules
| Module | Purpose |
|--------|---------|
| `juce_gui_basics` | Component, Button, Slider, Label, ComboBox, ListBox, TreeView, windows, layout, LookAndFeel |
| `juce_gui_extra` | CodeEditorComponent, SystemTrayIconComponent, extra widgets |
| `juce_graphics` | Graphics, Colour, Path, Image, Font, Typeface, drawing primitives |

### OpenGL & Rendering
| Module | Purpose |
|--------|---------|
| `juce_opengl` | OpenGLContext, OpenGLRenderer, shaders, framebuffers, 3D geometry |

### Other Important Modules
| Module | Purpose |
|--------|---------|
| `juce_core` | String, File, URL, streams, threading, JSON, XML, logging |
| `juce_data_structures` | ValueTree, UndoManager, identifiers |
| `juce_events` | MessageManager, AsyncUpdater, Timer, ChangeBroadcaster |
| `juce_osc` | OSC sender/receiver |
| `juce_midi_ci` | MIDI-CI (Capability Inquiry) |
| `juce_product_unlocking` | Licensing, in-app purchases |
| `juce_video` | Video playback, camera capture |
| `juce_cryptography` | Hashing, encryption, RSA |
| `juce_analytics` | Analytics event tracking |
| `juce_boxes_and_arrows` | Graph/flowchart GUI component |

---

## 3. Audio Plugin Development

### 3.1 AudioProcessor — The Engine

Every plugin extends `juce::AudioProcessor`. The key lifecycle methods:

```cpp
class MyProcessor final : public juce::AudioProcessor
{
public:
    MyProcessor()
        : AudioProcessor (BusesProperties()
                            .withInput  ("Input",  juce::AudioChannelSet::stereo(), true)
                            .withOutput ("Output", juce::AudioChannelSet::stereo(), true)),
          apvts (*this, nullptr, "Parameters", createParameterLayout())
    {}

    // --- Lifecycle ---
    void prepareToPlay (double sampleRate, int maxBlockSize) override;
    void releaseResources() override;
    void processBlock (juce::AudioBuffer<float>&, juce::MidiBuffer&) override;

    // --- State ---
    void getStateInformation (juce::MemoryBlock& destData) override;
    void setStateInformation (const void* data, int sizeInBytes) override;

    // --- Editor ---
    juce::AudioProcessorEditor* createEditor() override;
    bool hasEditor() const override { return true; }

    // --- Identity ---
    const juce::String getName() const override { return JucePlugin_Name; }
    bool acceptsMidi() const override { return true; }
    bool producesMidi() const override { return false; }
    double getTailLengthSeconds() const override { return 0.0; }
    int getNumPrograms() override { return 1; }
    int getCurrentProgram() override { return 0; }
    void setCurrentProgram (int) override {}
    const juce::String getProgramName (int) override { return {}; }
    void changeProgramName (int, const juce::String&) override {}

    // --- Parameters ---
    juce::AudioProcessorValueTreeState apvts;

private:
    static juce::AudioProcessorValueTreeState::ParameterLayout createParameterLayout()
    {
        std::vector<std::unique_ptr<juce::RangedAudioParameter>> params;
        params.push_back (std::make_unique<juce::AudioParameterFloat>(
            juce::ParameterID { "gain", 1 }, "Gain",
            juce::NormalisableRange<float> (0.0f, 1.0f, 0.01f), 0.7f));
        params.push_back (std::make_unique<juce::AudioParameterInt>(
            juce::ParameterID { "delay", 1 }, "Delay ms", 1, 2000, 500));
        params.push_back (std::make_unique<juce::AudioParameterBool>(
            juce::ParameterID { "bypass", 1 }, "Bypass", false));
        params.push_back (std::make_unique<juce::AudioParameterChoice>(
            juce::ParameterID { "mode", 1 }, "Mode",
            juce::StringArray { "Clean", "Warm", "Aggressive" }, 0));
        return { params.begin(), params.end() };
    }

    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR (MyProcessor)
};
```

#### prepareToPlay

Called before audio starts or when sample rate / block size changes. Initialize DSP, allocate buffers, reset filters:

```cpp
void prepareToPlay (double sampleRate, int maxBlockSize) override
{
    juce::dsp::ProcessSpec spec;
    spec.sampleRate = sampleRate;
    spec.maximumBlockSize = (juce::uint32) maxBlockSize;
    spec.numChannels = (juce::uint32) getTotalNumOutputChannels();

    myChain.prepare (spec);
    delayBuffer.setSize (getTotalNumOutputChannels(), (int) sampleRate * 2);
    delayBuffer.clear();
}
```

#### processBlock

The real-time audio callback. **Must be lock-free, allocation-free, and fast.**

```cpp
void processBlock (juce::AudioBuffer<float>& buffer, juce::MidiBuffer& midi) override
{
    juce::ScopedNoDenormals noDenormals;
    auto totalNumInputChannels  = getTotalNumInputChannels();
    auto totalNumOutputChannels = getTotalNumOutputChannels();

    // Clear unused output channels
    for (auto i = totalNumInputChannels; i < totalNumOutputChannels; ++i)
        buffer.clear (i, 0, buffer.getNumSamples());

    // Process with DSP chain
    juce::dsp::AudioBlock<float> block (buffer);
    juce::dsp::ProcessContextReplacing<float> context (block);
    chain.process (context);
}
```

#### State Serialization

```cpp
void getStateInformation (juce::MemoryBlock& destData) override
{
    auto state = apvts.copyState();
    if (auto xml = state.createXml())
        copyXmlToBinary (*xml, destData);
}

void setStateInformation (const void* data, int sizeInBytes) override
{
    if (auto xml = getXmlFromBinary (data, sizeInBytes))
        apvts.replaceState (juce::ValueTree::fromXml (*xml));
}
```

### 3.2 Parameter Types

| Class | Use |
|-------|-----|
| `AudioParameterFloat` | Continuous values (gain, frequency, Q) |
| `AudioParameterInt` | Discrete integer values (delay ms, octave) |
| `AudioParameterBool` | On/off toggles |
| `AudioParameterChoice` | Named options from a StringArray |

All require a `ParameterID { stringID, versionHint }` for stable serialization.

### 3.3 AudioProcessorValueTreeState (APVTS)

The standard way to manage parameters with automatic host sync:

```cpp
// In processor
AudioProcessorValueTreeState apvts;

// Create attachments in editor
AudioProcessorValueTreeState::SliderAttachment  gainSliderAttach  { apvts, "gain",  gainSlider };
AudioProcessorValueTreeState::ComboBoxAttachment modeComboAttach  { apvts, "mode",  modeCombo };
AudioProcessorValueTreeState::ButtonAttachment   bypassBtnAttach   { apvts, "bypass", bypassBtn };
```

APVTS stores parameters in a ValueTree, which can be serialized to XML for state save/restore. It also handles parameter automation from the host DAW.

### 3.4 AudioProcessorEditor — The UI

```cpp
class MyEditor final : public juce::AudioProcessorEditor
{
public:
    explicit MyEditor (MyProcessor& p)
        : AudioProcessorEditor (&p), processor (p),
          gainAttachment (p.apvts, "gain", gainSlider)
    {
        addAndMakeVisible (gainSlider);
        gainSlider.setSliderStyle (juce::Slider::RotaryVerticalDrag);
        gainSlider.setTextBoxStyle (juce::Slider::TextBoxBelow, false, 80, 20);

        addAndMakeVisible (titleLabel);
        titleLabel.setText ("My Plugin", juce::dontSendNotification);
        titleLabel.setFont (juce::FontOptions (24.0f, juce::Font::bold));
        titleLabel.setJustificationType (juce::Justification::centred);

        setSize (400, 300);
        setResizable (true, true);
        setResizeLimits (300, 200, 800, 600);
    }

    void resized() override
    {
        auto area = getLocalBounds().reduced (10);
        titleLabel.setBounds (area.removeFromTop (40));
        gainSlider.setBounds (area.removeFromTop (120));
    }

    void paint (juce::Graphics& g) override
    {
        g.fillAll (getLookAndFeel().findColour (juce::ResizableWindow::backgroundColourId));
    }

private:
    MyProcessor& processor;
    juce::Slider gainSlider;
    juce::Label titleLabel;
    juce::AudioProcessorValueTreeState::SliderAttachment gainAttachment;

    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR (MyEditor)
};
```

---

## 4. DSP Module — Audio Processing Building Blocks

The `juce_dsp` module provides composable audio processing units.

### 4.1 ProcessSpec

All DSP processors are configured with a `ProcessSpec`:

```cpp
juce::dsp::ProcessSpec spec;
spec.sampleRate = sampleRate;
spec.maximumBlockSize = (juce::uint32) maxBlockSize;
spec.numChannels = (juce::uint32) getMainBusNumOutputChannels();
```

### 4.2 AudioBlock

A lightweight, non-owning view over audio data:

```cpp
juce::dsp::AudioBlock<float> block (buffer);  // wraps AudioBuffer
auto numCh = block.getNumChannels();
auto numSamp = block.getNumSamples();
float* leftChannel = block.getChannelPointer (0);
auto subBlock = block.getSubsetChannelBlock (0, 2);  // first 2 channels
```

### 4.3 ProcessContext

Wraps an AudioBlock with processing metadata:

```cpp
// In-place processing (input and output share the same buffer)
juce::dsp::ProcessContextReplacing<float> context (block);

// Separate input/output buffers
juce::dsp::ProcessContextNonReplacing<float> context (inputBlock, outputBlock);
```

### 4.4 ProcessorChain

Compose processors in series:

```cpp
using MyChain = juce::dsp::ProcessorChain<
    juce::dsp::NoiseGate<float>,       // index 0
    juce::dsp::Gain<float>,            // index 1
    juce::dsp::Compressor<float>,      // index 2
    juce::dsp::LadderFilter<float>,    // index 3
    juce::dsp::Limiter<float>,         // index 4
    juce::dsp::Panner<float>           // index 5
>;

MyChain chain;

// In prepareToPlay:
chain.prepare (spec);

// Access individual processors by index:
auto& gate = chain.get<0>();
gate.setThreshold (-20.0f);
gate.setRatio (0.1f);

auto& gain = chain.get<1>();
gain.setGainDecibels (-6.0f);

// In processBlock:
chain.process (context);

// Bypass individual processors:
chain.setBypassed<0> (shouldBypassGate);
```

### 4.5 Key DSP Processors

| Processor | Purpose | Key Methods |
|-----------|---------|-------------|
| `dsp::Gain<T>` | Volume control | `setGainLinear()`, `setGainDecibels()` |
| `dsp::Compressor<T>` | Dynamic compression | `setThreshold()`, `setRatio()`, `setAttack()`, `setRelease()` |
| `dsp::Limiter<T>` | Peak limiting | `setThreshold()`, `setRelease()` |
| `dsp::NoiseGate<T>` | Noise gate | `setThreshold()`, `setRatio()`, `setAttack()`, `setRelease()` |
| `dsp::LadderFilter<T>` | Analog-modeled filter | `setCutoffFrequency()`, `setResonance()`, `setMode()` |
| `dsp::StateVariableFilter<T>` | SVF (LP/HP/BP/Notch) | `setCutoffFrequency()`, `setResonance()`, `setType()` |
| `dsp::IIR::Filter<T>` | Biquad IIR | `coefficients` (static design methods) |
| `dsp::Phaser<T>` | Phaser effect | `setRate()`, `setDepth()`, `setCentreFrequency()` |
| `dsp::Chorus<T>` | Chorus effect | `setRate()`, `setDepth()`, `setCentreDelay()`, `setFeedback()`, `setMix()` |
| `dsp::DelayLine<T, Interpolation>` | Delay line | `setDelay()`, `pushSample()`, `popSample()`, `setMaximumDelayInSamples()` |
| `dsp::Convolution` | Convolution reverb | `loadImpulseResponse()`, uses background thread |
| `dsp::Oscillator<T>` | Signal generator | `setFrequency()`, `initialise()` with waveform lambda |
| `dsp::DryWetMixer<T>` | Parallel blend | `setWetMixProportion()`, `pushDrySamples()`, `mixWetSamples()` |
| `dsp::Oversampling<T>` | Oversampling | `initProcessing()`, `processSamplesUp()`, `processSamplesDown()` |
| `dsp::Panner<T>` | Stereo panning | `setPan()`, `setRule()` |

### 4.6 Interpolation types for DelayLine

```cpp
dsp::DelayLine<float, dsp::DelayLineInterpolationTypes::None>
dsp::DelayLine<float, dsp::DelayLineInterpolationTypes::Linear>
dsp::DelayLine<float, dsp::DelayLineInterpolationTypes::Lagrange3rd>
dsp::DelayLine<float, dsp::DelayLineInterpolationTypes::Thiran>
```

### 4.7 Custom Processor Pattern

Any class with `prepare()`, `process()`, and `reset()` can go in a ProcessorChain:

```cpp
class MyEffect
{
public:
    void prepare (const juce::dsp::ProcessSpec& spec)
    {
        sampleRate = spec.sampleRate;
        // allocate buffers, initialize state
    }

    void reset()
    {
        // clear internal state
    }

    template <typename ProcessContext>
    void process (const ProcessContext& context)
    {
        const auto& inputBlock  = context.getInputBlock();
        auto& outputBlock       = context.getOutputBlock();
        const auto numChannels  = outputBlock.getNumChannels();
        const auto numSamples   = outputBlock.getNumSamples();

        jassert (inputBlock.getNumChannels() == numChannels);
        jassert (inputBlock.getNumSamples() == numSamples);

        if (context.isBypassed)
        {
            outputBlock.copyFrom (inputBlock);
            return;
        }

        for (size_t ch = 0; ch < numChannels; ++ch)
        {
            auto* src = inputBlock.getChannelPointer (ch);
            auto* dst = outputBlock.getChannelPointer (ch);
            for (size_t i = 0; i < numSamples; ++i)
                dst[i] = /* your DSP here */ src[i];
        }
    }

private:
    double sampleRate = 44100.0;
};
```

---

## 5. GUI Fundamentals

### 5.1 Component — The Base of Everything

Every visual element is a `juce::Component`:

```cpp
class MyComponent final : public juce::Component
{
public:
    void paint (juce::Graphics& g) override { /* draw */ }
    void resized() override { /* layout children */ }
    void mouseDown (const juce::MouseEvent& e) override { /* handle click */ }
    void mouseDrag (const juce::MouseEvent& e) override { /* handle drag */ }
    void mouseUp (const juce::MouseEvent& e) override { /* handle release */ }

private:
    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR (MyComponent)
};
```

Key Component methods:
- `addAndMakeVisible(component)` — add child and make visible
- `setBounds(x, y, w, h)` — position and size
- `getLocalBounds()` — bounds relative to self
- `repaint()` — trigger redraw
- `setWantsKeyboardFocus(true)` — accept keyboard input
- `setInterceptsMouseClicks(true, false)` — mouse event handling

### 5.2 Advanced Rectangle Layout Techniques

The `juce::Rectangle` class provides powerful subdivision methods for laying out components without manual coordinate calculations. This technique is more elegant and less error-prone than traditional `setBounds(x, y, w, h)` calls.

**Core concept:** Start with `getLocalBounds()` and repeatedly "remove" slices from the edges to create sub-rectangles for child components.

**Key Rectangle subdivision methods:**
- `removeFromTop(height)` — returns top slice, shrinks original downward
- `removeFromBottom(height)` — returns bottom slice, shrinks original upward
- `removeFromLeft(width)` — returns left slice, shrinks original rightward
- `removeFromRight(width)` — returns right slice, shrinks original leftward
- `reduced(amount)` — returns rectangle inset on all sides
- `reduced(horizAmount, vertAmount)` — returns rectangle inset independently
- `withSizeKeepingCentre(w, h)` — returns rectangle centered in original

**Example 1: Basic header/body/footer layout**

```cpp
void resized() override
{
    auto bounds = getLocalBounds();
    
    // Remove 36px header from top
    auto headerBounds = bounds.removeFromTop (36);
    header.setBounds (headerBounds);
    
    // Remove 24px footer from bottom
    auto footerBounds = bounds.removeFromBottom (24);
    footer.setBounds (footerBounds);
    
    // Remaining bounds go to body
    body.setBounds (bounds);
}
```

**Example 2: Sidebar + main content with top toolbar**

```cpp
void resized() override
{
    auto bounds = getLocalBounds();
    
    // Toolbar across the top
    auto toolbarBounds = bounds.removeFromTop (40);
    toolbar.setBounds (toolbarBounds);
    
    // Sidebar on the left (200px wide)
    auto sidebarBounds = bounds.removeFromLeft (200);
    sidebar.setBounds (sidebarBounds);
    
    // Everything else is main content
    mainContent.setBounds (bounds);
}
```

**Example 3: Complex plugin editor with multiple sections**

```cpp
void resized() override
{
    auto bounds = getLocalBounds().reduced (10); // 10px padding all around
    
    // Top section: preset bar
    auto presetBarBounds = bounds.removeFromTop (30);
    presetBar.setBounds (presetBarBounds);
    
    // Add some vertical spacing
    bounds.removeFromTop (10);
    
    // Split remaining space: left panel (30%) and right panel (70%)
    auto leftWidth = bounds.getWidth() * 0.3f;
    auto leftPanelBounds = bounds.removeFromLeft ((int) leftWidth);
    leftPanel.setBounds (leftPanelBounds);
    
    // Gap between panels
    bounds.removeFromLeft (15);
    
    // Right panel gets the rest
    rightPanel.setBounds (bounds);
}
```

**Example 4: Grid of equal-sized buttons using Rectangle subdivision**

```cpp
void resized() override
{
    auto bounds = getLocalBounds();
    
    // Split into 2 rows
    auto topRow = bounds.removeFromTop (bounds.getHeight() / 2);
    auto bottomRow = bounds;
    
    // Top row: split into 2 columns
    auto topLeft = topRow.removeFromLeft (topRow.getWidth() / 2);
    auto topRight = topRow;
    
    // Bottom row: split into 2 columns
    auto bottomLeft = bottomRow.removeFromLeft (bottomRow.getWidth() / 2);
    auto bottomRight = bottomRow;
    
    button1.setBounds (topLeft.reduced (5));
    button2.setBounds (topRight.reduced (5));
    button3.setBounds (bottomLeft.reduced (5));
    button4.setBounds (bottomRight.reduced (5));
}
```

**Benefits over manual coordinate calculations:**
1. **No arithmetic errors** — Rectangle methods handle all math
2. **Easy reordering** — just move the `removeFrom*` call earlier or later in the function
3. **Automatic resize handling** — when parent resizes, all children adapt proportionally
4. **Readable code** — layout intent is clear from the sequence of removals
5. **Less verbose** — no need to track cumulative x/y offsets

**Pro tips:**
- Always start with `getLocalBounds()` (returns rectangle at position 0,0 with component's width/height)
- Use `reduced()` for padding/margins around the entire bounds
- Use `removeFrom*()` with small gaps (e.g., `bounds.removeFromTop(5)`) for spacing between sections
- The order of `removeFrom*` calls determines layout order — move calls around to reorder components
- For variable-width/height content, calculate proportions: `bounds.removeFromLeft(bounds.getWidth() / 3)`
- Combine with FlexBox/Grid for complex nested layouts (subdivide with Rectangle, then use FlexBox inside each section)

### 5.3 Layout — FlexBox and Grid (Responsive GUIs)

JUCE's `FlexBox` and `Grid` classes are inspired by CSS Flexbox and CSS Grid, enabling responsive layouts that adapt to different screen sizes and orientations.

#### FlexBox — One-Dimensional Layout

`FlexBox` arranges items along a single axis (main axis). The perpendicular direction is the cross axis.

**Key FlexBox properties:**
- `flexDirection` — `row` (horizontal) or `column` (vertical); defines the main axis
- `justifyContent` — alignment along main axis (`flexStart`, `center`, `spaceBetween`, `spaceAround`)
- `alignItems` / `alignContent` — alignment along cross axis (`flexStart`, `center`, `stretch`, `spaceBetween`)
- `flexWrap` — `noWrap` (single line) or `wrap` (items flow to next line on overflow)

**Key FlexItem properties:**
- `withFlex(n)` — flex-grow factor (how much item grows relative to siblings)
- `withFlexShrink(n)` — flex-shrink factor (how much item shrinks when space is tight)
- `withFlexBasis(size)` — default size before growing/shrinking
- `withMinWidth(w)` / `withMinHeight(h)` — minimum size constraints
- `withMargin(margin)` — spacing around the item

**Example 1: Responsive button grid with wrapping**

```cpp
void resized() override
{
    juce::FlexBox fb;
    fb.flexWrap = juce::FlexBox::Wrap::wrap; // wrap buttons to next line
    fb.justifyContent = juce::FlexBox::JustifyContent::center;
    fb.alignContent = juce::FlexBox::AlignContent::center;
    
    for (auto* b : buttons)
        fb.items.add (juce::FlexItem (*b).withMinWidth (50.0f).withMinHeight (50.0f));
    
    fb.performLayout (getLocalBounds());
}
```

**Example 2: Nested FlexBox — knobs panel with proportional sizing**

```cpp
void resized() override
{
    // Inner FlexBox for the knobs (wraps and spaces evenly)
    juce::FlexBox knobBox;
    knobBox.flexWrap = juce::FlexBox::Wrap::wrap;
    knobBox.justifyContent = juce::FlexBox::JustifyContent::spaceBetween;
    for (auto* k : knobs)
        knobBox.items.add (juce::FlexItem (*k).withMinHeight (50.0f).withMinWidth (50.0f).withFlex (1));
    
    // Outer FlexBox stacks knob panel vertically
    juce::FlexBox fb;
    fb.flexDirection = juce::FlexBox::Direction::column;
    fb.items.add (juce::FlexItem (knobBox).withFlex (2.5));
    fb.performLayout (getLocalBounds());
}
```

**Example 3: Audio plugin editor with FlexBox**

```cpp
void resized() override
{
    juce::FlexBox fb;
    fb.flexDirection = juce::FlexBox::Direction::row;
    fb.flexWrap = juce::FlexBox::Wrap::noWrap;
    fb.justifyContent = juce::FlexBox::JustifyContent::spaceAround;
    fb.alignItems = juce::FlexBox::AlignItems::center;
    
    fb.items.add (juce::FlexItem (gainSlider).withFlex (1).withMargin (10));
    fb.items.add (juce::FlexItem (toneSlider).withFlex (1).withMargin (10));
    fb.items.add (juce::FlexItem (mixSlider).withFlex (1).withMargin (10));
    
    fb.performLayout (getLocalBounds().toFloat());
}
```

#### Grid — Two-Dimensional Layout

`Grid` arranges items in rows and columns (like CSS Grid), ideal for complex 2D layouts.

**Key Grid properties:**
- `templateRows` — defines row heights using `Fr` (fractional units) or fixed pixels
- `templateColumns` — defines column widths
- `justifyItems` — alignment of items within their grid cells (along row axis)
- `alignItems` — alignment of items within their cells (along column axis)
- `justifyContent` / `alignContent` — alignment of the entire grid within bounds
- `columnGap` / `rowGap` — spacing between columns/rows
- `autoFlow` — `row` (fill rows first) or `column` (fill columns first)

**Key GridItem properties:**
- `withArea(row, column, rowSpan, colSpan)` — place item at specific grid position with span
- `withMargin(margin)` — spacing around the item
- `columnNumber` / `rowNumber` — explicit placement

**Example 1: 2×3 knob grid**

```cpp
void resized() override
{
    using Track = juce::Grid::TrackInfo;
    using Fr = juce::Grid::Fr;
    
    juce::Grid grid;
    grid.templateRows = { Track (Fr (1)), Track (Fr (1)) };
    grid.templateColumns = { Track (Fr (1)), Track (Fr (1)), Track (Fr (1)) };
    grid.columnGap = 10;
    grid.rowGap = 10;
    grid.justifyItems = juce::Grid::JustifyItems::center;
    grid.alignItems = juce::Grid::AlignItems::center;
    
    grid.items = {
        juce::GridItem (slider1),
        juce::GridItem (slider2),
        juce::GridItem (slider3),
        juce::GridItem (knob1),
        juce::GridItem (knob2),
        juce::GridItem (knob3),
    };
    
    grid.performLayout (getLocalBounds());
}
```

**Example 2: Complex layout with spanning**

```cpp
void resized() override
{
    using Track = juce::Grid::TrackInfo;
    using Fr = juce::Grid::Fr;
    
    juce::Grid grid;
    grid.templateRows = { Track (Fr (1)), Track (Fr (1)), Track (Fr (1)) };
    grid.templateColumns = { Track (Fr (1)), Track (Fr (2)) }; // second column is 2x wider
    
    grid.items = {
        juce::GridItem (label).withArea (1, 1, 1, 1),           // row 1, col 1
        juce::GridItem (valueBox).withArea (1, 2, 1, 2),        // row 1, col 2
        juce::GridItem (slider1).withArea (2, 1, 2, 2),         // row 2, spans both cols
        juce::GridItem (slider2).withArea (3, 1, 3, 1),         // row 3, col 1
        juce::GridItem (slider3).withArea (3, 2, 3, 2),         // row 3, col 2
    };
    
    grid.performLayout (getLocalBounds());
}
```

**Example 3: Orientation-aware layout (portrait vs landscape)**

```cpp
void resized() override
{
    auto bounds = getLocalBounds();
    bool isPortrait = bounds.getHeight() > bounds.getWidth();
    
    using Track = juce::Grid::TrackInfo;
    using Fr = juce::Grid::Fr;
    
    juce::Grid grid;
    
    if (isPortrait)
    {
        grid.templateRows = { Track (Fr (1)), Track (Fr (1)) };
        grid.templateColumns = { Track (Fr (1)) };
    }
    else
    {
        grid.templateRows = { Track (Fr (1)) };
        grid.templateColumns = { Track (Fr (1)), Track (Fr (1)) };
    }
    
    grid.items = {
        juce::GridItem (leftPanel),
        juce::GridItem (rightPanel),
    };
    
    grid.performLayout (bounds);
}
```

#### FlexBox vs Grid — When to Use Which

| Scenario | Use |
|----------|-----|
| Single row or column of items | `FlexBox` |
| Items should wrap to next line | `FlexBox` with `Wrap::wrap` |
| Proportional sizing (flex-grow) | `FlexBox` |
| 2D grid of controls | `Grid` |
| Items spanning multiple cells | `Grid` with `withArea()` |
| Fixed row/column track definitions | `Grid` with `Fr` units |
| Responsive portrait/landscape | Either (check bounds aspect ratio) |

**Best practices:**
- Always call `performLayout()` with the actual bounds (not hardcoded sizes)
- Use `withFlex()` for proportional sizing instead of fixed pixel widths
- Use `withMinWidth()` / `withMinHeight()` to prevent items from collapsing
- Nest FlexBox inside Grid (or vice versa) for complex layouts
- Test with different window sizes to ensure responsiveness
- For audio plugins, prefer FlexBox for simple horizontal/vertical arrangements; use Grid for mixer-style multi-row layouts

### 5.5 Widget Reference Table

| Widget | Purpose | LookAndFeel customization |
|--------|---------|--------------------------|
| `Slider` | Rotary/linear value control | `drawRotarySlider()`, `drawLinearSlider()` |
| `TextButton` | Clickable button | `drawButtonBackground()`, `drawButtonText()` |
| `ToggleButton` | On/off switch | `drawToggleButton()`, `drawTickBox()` |
| `ComboBox` | Dropdown selector | `drawComboBox()`, `getComboBoxFont()` |
| `Label` | Text display | `drawLabel()`, `getLabelFont()` |
| `TextEditor` | Text input | `fillTextEditorBackground()`, `drawTextEditorOutline()` |
| `ListBox` | Scrollable list | Custom `ListBoxModel` for rows |
| `TreeView` | Hierarchical tree | `drawTreeviewPlusMinusBox()` |
| `TabbedComponent` | Tab panels | `drawTabButton()`, `getTabButtonFont()` |

---

## 6. LookAndFeel — Complete Customization Reference

The LookAndFeel system controls the visual appearance of every widget. JUCE provides four built-in themes:

| Class | Style |
|-------|-------|
| `LookAndFeel_V2` | Flat, modern default |
| `LookAndFeel_V3` | Subtle refinements over V2 |
| `LookAndFeel_V4` | Color scheme API, more customizable |

### 6.1 Setting a LookAndFeel

```cpp
// Globally (application-wide)
juce::LookAndFeel::setDefaultLookAndFeel (&myLookAndFeel);

// Per-component (and children)
myEditor.setLookAndFeel (&myLookAndFeel);
```

### 6.2 Custom LookAndFeel

```cpp
class MyLookAndFeel final : public juce::LookAndFeel_V4
{
public:
    MyLookAndFeel()
    {
        // Set colour scheme
        setColourScheme (juce::LookAndFeel_V4::getMidnightColourScheme());

        // Or set individual colours
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
        auto rx = centreX - radius;
        auto ry = centreY - radius;
        auto rw = radius * 2.0f;
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

### 6.3 Complete Virtual Methods Reference

These are ALL the methods you can override in a custom LookAndFeel. Grouped by widget.

#### Buttons
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

#### Sliders
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

#### ComboBox
```
drawComboBox(Graphics&, int width, height, bool isMouseButtonDown, int buttonX, buttonY, buttonW, buttonH, ComboBox&)
getComboBoxFont(ComboBox&) -> Font
createComboBoxTextBox(ComboBox&) -> Label*
positionComboBoxText(ComboBox&, Label&)
getOptionsForComboBoxPopupMenu(ComboBox&, Label&) -> PopupMenu::Options
drawComboBoxTextWhenNothingSelected(Graphics&, ComboBox&, Label&)
```

#### Label
```
drawLabel(Graphics&, Label&)
getLabelFont(Label&) -> Font
getLabelBorderSize(Label&) -> BorderSize<int>
```

#### TextEditor
```
fillTextEditorBackground(Graphics&, int width, height, TextEditor&)
drawTextEditorOutline(Graphics&, int width, height, TextEditor&)
createCaretComponent(Component* keyFocusOwner) -> CaretComponent*
```

#### ScrollBar
```
drawScrollbar(Graphics&, ScrollBar&, int x, y, width, height, bool isVertical, int thumbStartPosition, int thumbSize, bool isMouseOver, bool isMouseDown)
drawScrollbarButton(Graphics&, ScrollBar&, int width, height, int buttonDirection, bool isVertical, bool isHighlighted, bool isDown)
areScrollbarButtonsVisible() -> bool
getScrollbarEffect() -> ImageEffectFilter*
getMinimumScrollbarThumbSize(ScrollBar&) -> int
getDefaultScrollbarWidth() -> int
getScrollbarButtonSize(ScrollBar&) -> int
```

#### TreeView
```
drawTreeviewPlusMinusBox(Graphics&, const Rectangle<float>& area, Colour background, bool isOpen, bool isMouseOver)
areLinesDrawnForTreeView(TreeView&) -> bool
getTreeViewIndentSize(TreeView&) -> int
```

#### PopupMenu
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

#### MenuBar
```
drawMenuBarBackground(Graphics&, int width, height, bool isMouseOverBar, MenuBarComponent&)
getMenuBarItemWidth(MenuBarComponent&, int itemIndex, const String& itemText) -> int
getMenuBarFont(MenuBarComponent&, int itemIndex, const String& itemText) -> Font
getDefaultMenuBarHeight() -> int
drawMenuBarItem(Graphics&, int width, height, int itemIndex, const String& itemText, bool isMouseOverItem, bool isMenuOpen, bool isMouseOverBar, MenuBarComponent&)
```

#### Window
```
drawDocumentWindowTitleBar(DocumentWindow&, Graphics&, int w, h, int titleSpaceX, titleSpaceW, const Image* icon, bool drawTitleTextOnLeft)
createDocumentWindowButton(int buttonType) -> Button*
positionDocumentWindowButtons(DocumentWindow&, int titleBarX, titleBarY, titleBarW, titleBarH, Button* minimise, Button* maximise, Button* close, bool positionTitleBarButtonsOnLeft)
drawCornerResizer(Graphics&, int w, h, bool isMouseOver, bool isMouseDragging)
drawResizableFrame(Graphics&, int w, h, const BorderSize<int>&)
fillResizableWindowBackground(Graphics&, int w, h, const BorderSize<int>&, ResizableWindow&)
drawResizableWindowBorder(Graphics&, int w, h, const BorderSize<int>& border, ResizableWindow&)
```

#### AlertWindow
```
createAlertWindow(const String& title, message, button1, button2, button3, MessageBoxIconType, int numButtons, Component* associated) -> AlertWindow*
drawAlertBox(Graphics&, AlertWindow&, const Rectangle<int>& textArea, TextLayout&)
getAlertBoxWindowFlags() -> int
getAlertWindowButtonHeight() -> int
getAlertWindowTitleFont() -> Font
getAlertWindowMessageFont() -> Font
getAlertWindowFont() -> Font
```

#### ProgressBar
```
drawProgressBar(Graphics&, ProgressBar&, int width, height, double progress, const String& textToShow)
isProgressBarOpaque(ProgressBar&) -> bool
```

#### TabbedButtonBar
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

#### TableHeader
```
drawTableHeaderBackground(Graphics&, TableHeaderComponent&)
drawTableHeaderColumn(Graphics&, TableHeaderComponent&, const String& columnName, int columnId, int width, height, bool isMouseOver, bool isMouseDown, int columnFlags)
```

#### Toolbar
```
paintToolbarBackground(Graphics&, int width, height, Toolbar&)
createToolbarMissingItemsButton(Toolbar&) -> Button*
paintToolbarButtonBackground(Graphics&, int width, height, bool isMouseOver, bool isMouseDown, ToolbarItemComponent&)
paintToolbarButtonLabel(Graphics&, int x, y, width, height, const String& text, ToolbarItemComponent&)
```

#### Tooltip
```
getTooltipBounds(const String& tipText, Point<int> screenPos, Rectangle<int> parentArea) -> Rectangle<int>
drawTooltip(Graphics&, const String& text, int width, height)
```

#### GroupComponent
```
drawGroupComponentOutline(Graphics&, int w, h, const String& text, const Justification&, GroupComponent&)
```

#### CallOutBox
```
drawCallOutBoxBackground(CallOutBox&, Graphics&, const Path& path, Image& cachedImage)
getCallOutBoxBorderSize(const CallOutBox&) -> int
getCallOutBoxCornerSize(const CallOutBox&) -> float
```

#### PropertyComponent
```
drawPropertyPanelSectionHeader(Graphics&, const String& name, bool isOpen, int width, height)
drawPropertyComponentBackground(Graphics&, int width, height, PropertyComponent&)
drawPropertyComponentLabel(Graphics&, int width, height, PropertyComponent&)
getPropertyComponentContentPosition(PropertyComponent&) -> Rectangle<int>
getPropertyPanelSectionHeaderHeight(const String& sectionTitle) -> int
```

#### Other
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

---

## 7. Font Rendering

### 7.1 Font Class

Modern JUCE uses `FontOptions` for construction:

```cpp
// Modern constructor (recommended)
juce::Font myFont (juce::FontOptions (16.0f));
juce::Font boldFont (juce::FontOptions (24.0f, juce::Font::bold));
juce::Font namedFont (juce::FontOptions ("Helvetica", 18.0f, juce::Font::plain));

// Fluent API
auto f = juce::FontOptions (14.0f)
    .boldened()
    .italicised();
```

#### Key methods

```cpp
// Size
font.withHeight (16.0f);
font.withPointHeight (12.0f);
font.getHeight();          // pixel height
font.getAscent();          // distance above baseline
font.getDescent();         // distance below baseline

// Style
font.withStyle (juce::Font::bold | juce::Font::italic);
font.boldened();
font.italicised();
font.withExtraKerningFactor (0.05f);
font.withHorizontalScale (0.9f);  // condensed

// Typeface
font.withTypefaceStyle ("Bold Italic");
font.getAvailableStyles();  // StringArray of available styles
font.setPreferredFallbackFamilies ({ "Noto Sans", "Segoe UI" });

// Discovery
juce::Font::findAllTypefaceNames();         // all system fonts
juce::Font::findAllTypefaceStyles ("Arial"); // styles for a family
juce::Font::getDefaultSansSerifFontName();
juce::Font::getDefaultMonospacedFontName();
juce::Font::getSystemUIFontName();

// Feature settings (OpenType)
font.setFeatureSetting (juce::FontFeatureSetting { "liga", 1 });  // ligatures
font.setFeatureSetting (juce::FontFeatureSetting { "smcp", 1 });  // small caps

// Serialization
auto str = font.toString();
auto restored = juce::Font::fromString (str);
```

### 7.2 Custom Fonts from Binary Data

Embed font files as binary data and load at runtime:

```cpp
// In CMakeLists.txt
juce_add_binary_data (FontData SOURCES resources/MyFont-Regular.ttf resources/MyFont-Bold.ttf)

// In code
auto fontData = BinaryData::MyFontRegular_ttf;
auto fontSize = BinaryData::MyFontRegular_ttfSize;
auto typeface = juce::Typeface::createSystemTypefaceFor (fontData, (size_t) fontSize);
juce::Font customFont (juce::FontOptions (typeface));
```

Or load from a file:

```cpp
auto file = juce::File::getCurrentWorkingDirectory().getChildFile ("MyFont.ttf");
auto typeface = juce::Typeface::createSystemTypefaceFor (
    file.loadFileAsData().getData(),
    (size_t) file.loadFileAsData().getSize());
```

### 7.3 Drawing Text

```cpp
void paint (juce::Graphics& g) override
{
    // Simple text
    g.setFont (juce::FontOptions (18.0f, juce::Font::bold));
    g.setColour (juce::Colours::white);
    g.drawText ("Hello", getLocalBounds(), juce::Justification::centred);

    // With AttributedString for rich text
    juce::AttributedString as;
    as.append ("Normal ", juce::FontOptions (14.0f), juce::Colours::white);
    as.append ("Bold ",   juce::FontOptions (14.0f, juce::Font::bold), juce::Colours::yellow);
    as.append ("Italic",  juce::FontOptions (14.0f, juce::Font::italic), juce::Colours::cyan);
    as.draw (g, getLocalBounds().toFloat());

    // TextLayout for word wrapping
    juce::TextLayout layout;
    layout.createLayout (as, (float) getWidth());
    layout.draw (g, getLocalBounds().toFloat());
}
```

### 7.4 Typeface

Low-level glyph access:

```cpp
auto typeface = font.getTypefacePtr();
auto metrics = typeface->getMetrics (juce::TypefaceMetricsKind::legacy);

// Get glyph outline as Path (for custom rendering)
juce::Path glyphPath;
typeface->getOutlineForGlyph (glyphNumber, glyphPath);
auto bounds = typeface->getGlyphBounds (glyphNumber);

// Colour glyph support (emoji, etc.)
int formats = typeface->getColourGlyphFormats();
// colourGlyphFormatBitmap, colourGlyphFormatSvg, colourGlyphFormatCOLRv0, colourGlyphFormatCOLRv1

// Cache management
juce::Typeface::clearTypefaceCache();
juce::Typeface::setTypefaceCacheSize (50);
juce::Typeface::scanFolderForFonts (juce::File ("/path/to/fonts"));
```

---

## 8. Graphics & Painting

### 8.1 Graphics Class

```cpp
void paint (juce::Graphics& g) override
{
    // Fill background
    g.fillAll (juce::Colours::black);

    // Gradient fill
    g.setGradientFill (juce::ColourGradient (
        juce::Colours::darkblue, 0.0f, 0.0f,
        juce::Colours::black, 0.0f, (float) getHeight(), false));
    g.fillAll();

    // Shapes
    g.setColour (juce::Colours::white);
    g.drawRect (10, 10, 100, 50, 2);  // x, y, w, h, lineThickness
    g.fillRoundedRectangle (10.0f, 70.0f, 100.0f, 50.0f, 8.0f);
    g.drawEllipse (120.0f, 10.0f, 80.0f, 50.0f, 2.0f);

    // Path (complex shapes)
    juce::Path p;
    p.startNewSubPath (0.0f, 0.0f);
    p.lineTo (50.0f, 100.0f);
    p.lineTo (100.0f, 0.0f);
    p.closeSubPath();
    g.setColour (juce::Colours::red);
    g.fillPath (p, juce::AffineTransform::translation (10, 130));

    // Images
    g.drawImage (myImage, getLocalBounds().toFloat());

    // Drop shadow
    juce::DropShadow shadow (juce::Colours::black.withAlpha (0.5f), 6, juce::Point<int> (2, 2));
    shadow.drawForRectangle (g, getLocalBounds().reduced (20));
}
```

### 8.2 Colour

```cpp
juce::Colour c (0xff336699);                    // ARGB hex
juce::Colour c2 (0.2f, 0.4f, 0.6f);            // RGB floats 0-1
juce::Colour c3 (0.2f, 0.4f, 0.6f, 0.8f);      // RGBA floats
auto c4 = juce::Colour::fromHSV (0.5f, 0.8f, 0.9f, 1.0f);
auto c5 = c.brighter (0.3f);
auto c6 = c.darker (0.2f);
auto c7 = c.withAlpha (0.5f);
auto c8 = c.withMultipliedBrightness (1.2f);
auto c9 = c.withMultipliedSaturation (0.8f);
auto c10 = c.interpolatedWith (juce::Colours::white, 0.5f);  // blend
```

---

## 9. OpenGL Integration

### 9.1 OpenGLContext — The Entry Point

Attach to any Component to enable hardware-accelerated rendering:

```cpp
class MyGLComponent : public juce::Component,
                      public juce::OpenGLRenderer
{
public:
    MyGLComponent()
    {
        openGLContext.setRenderer (this);
        openGLContext.attachTo (*this);
        openGLContext.setOpenGLVersionRequired (juce::OpenGLContext::OpenGLVersion::openGL3_2);
    }

    ~MyGLComponent() override
    {
        openGLContext.detach();
    }

    // --- OpenGLRenderer interface ---

    void newOpenGLContextCreated() override
    {
        // Called once when context is ready. Create shaders, buffers here.
        shaderProgram = std::make_unique<juce::OpenGLShaderProgram> (openGLContext);
        // ... compile shaders, create VAO/VBO
    }

    void renderOpenGL() override
    {
        // Called on every frame (driven by the display link / VSync)
        jassert (juce::OpenGLHelpers::isContextActive());

        auto scale = (float) openGLContext.getRenderingScale();
        glViewport (0, 0, juce::roundToInt (getWidth() * scale),
                          juce::roundToInt (getHeight() * scale));

        glClearColor (0.1f, 0.1f, 0.1f, 1.0f);
        glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        // Draw with shaders
        shaderProgram->use();
        // ... bind VAO, draw calls
    }

    void openGLContextClosing() override
    {
        // Release all GL resources
        shaderProgram.reset();
    }

    void paint (juce::Graphics& g) override
    {
        // Can still use JUCE Graphics on top of OpenGL
        // This renders via the OpenGL-backed graphics context
    }

private:
    juce::OpenGLContext openGLContext;
    std::unique_ptr<juce::OpenGLShaderProgram> shaderProgram;

    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR (MyGLComponent)
};
```

### 9.2 OpenGLShaderProgram

```cpp
auto shader = std::make_unique<juce::OpenGLShaderProgram> (openGLContext);

juce::String vertexShader = R"(
    attribute vec2 position;
    attribute vec2 texCoord;
    varying vec2 vTexCoord;
    uniform mat4 projectionMatrix;
    void main()
    {
        vTexCoord = texCoord;
        gl_Position = projectionMatrix * vec4 (position, 0.0, 1.0);
    }
)";

juce::String fragmentShader = R"(
    uniform sampler2D texture0;
    uniform float opacity;
    varying vec2 vTexCoord;
    void main()
    {
        gl_FragColor = texture2D (texture0, vTexCoord) * opacity;
    }
)";

shader->addVertexShader (juce::OpenGLHelpers::translateVertexShaderToV3 (vertexShader));
shader->addFragmentShader (juce::OpenGLHelpers::translateFragmentShaderToV3 (fragmentShader));

// Bind attributes and uniforms
juce::OpenGLShaderProgram::Attribute position (*shader, "position");
juce::OpenGLShaderProgram::Attribute texCoord (*shader, "texCoord");
juce::OpenGLShaderProgram::Uniform projectionMatrix (*shader, "projectionMatrix");
juce::OpenGLShaderProgram::Uniform textureUniform (*shader, "texture0");

shader->link();
shader->use();
```

### 9.3 OpenGLFrameBuffer

Off-screen rendering:

```cpp
juce::OpenGLFrameBuffer fbo;

// In newOpenGLContextCreated():
fbo.initialise (openGLContext, 512, 512);

// In renderOpenGL():
fbo.makeCurrentRenderingTarget();
// ... render to FBO
openGLContext.makeActive();  // switch back to screen
fbo.drawAt (0.0f, 0.0f);   // draw FBO contents to screen
```

### 9.4 OpenGLTexture

Load JUCE Image into GL texture:

```cpp
juce::OpenGLTexture texture;

// Load from Image
juce::Image img = juce::ImageCache::getFromFile (juce::File ("texture.png"));
texture.loadImage (img);

// In shader, bind:
glActiveTexture (GL_TEXTURE0);
texture.bind();
glUniform1i (textureUniform.uniformID, 0);
```

### 9.5 OpenGLAppComponent

For standalone GL applications (no Component tree needed):

```cpp
class MyApp : public juce::OpenGLAppComponent
{
public:
    void initialise() override { /* create GL resources */ }
    void shutdown() override { /* release GL resources */ }
    void render() override { /* GL draw calls */ }
};

// In Main.cpp
class MainWindow : public juce::DocumentWindow { /* ... */ };
START_JUCE_APPLICATION_WITH_CUSTOM_CLASS(MyApp, MyApplication)
```

### 9.6 Using OpenGL as JUCE Graphics Backend

You can use OpenGL to accelerate standard JUCE Component rendering without writing any GL code:

```cpp
class MyEditor : public juce::AudioProcessorEditor
{
public:
    MyEditor (MyProcessor& p) : AudioProcessorEditor (&p)
    {
        openGLContext.setOpenGLVersionRequired (juce::OpenGLContext::OpenGLVersion::openGL3_2);
        openGLContext.attachTo (*this);
        // All paint() calls now render through OpenGL
    }

    ~MyEditor() override { openGLContext.detach(); }

private:
    juce::OpenGLContext openGLContext;
};
```

### 9.7 Complete OpenGL Application Example (from JUCE Tutorial)

This example demonstrates a complete OpenGL application that renders a 3D teapot from a Wavefront .obj file, showcasing key OpenGL concepts in JUCE.

**OpenGLAppComponent — The Foundation:**

```cpp
class OpenGLDemo : public juce::OpenGLAppComponent
{
public:
    OpenGLDemo() {}

    void initialise() override
    {
        // Create shader program
        shaderProgram = std::make_unique<juce::OpenGLShaderProgram> (openGLContext);
        
        // Vertex shader
        juce::String vertexShader = R"(
            attribute vec4 position;
            attribute vec4 sourceColour;
            attribute vec2 textureCoordIn;
            uniform mat4 projectionMatrix;
            uniform mat4 viewMatrix;
            varying vec4 destinationColour;
            varying vec2 textureCoordOut;
            void main()
            {
                destinationColour = sourceColour;
                textureCoordOut = textureCoordIn;
                gl_Position = projectionMatrix * viewMatrix * position;
            }
        )";
        
        // Fragment shader
        juce::String fragmentShader = R"(
            varying vec4 destinationColour;
            varying vec2 textureCoordOut;
            void main()
            {
                vec4 colour = vec4 (0.95, 0.57, 0.03, 0.7);
                gl_FragColor = colour;
            }
        )";
        
        shaderProgram->addVertexShader (juce::OpenGLHelpers::translateVertexShaderToV3 (vertexShader));
        shaderProgram->addFragmentShader (juce::OpenGLHelpers::translateFragmentShaderToV3 (fragmentShader));
        shaderProgram->link();
        
        // Bind attributes and uniforms
        positionAttribute = std::make_unique<juce::OpenGLShaderProgram::Attribute> (*shaderProgram, "position");
        colourAttribute = std::make_unique<juce::OpenGLShaderProgram::Attribute> (*shaderProgram, "sourceColour");
        textureCoordAttribute = std::make_unique<juce::OpenGLShaderProgram::Attribute> (*shaderProgram, "textureCoordIn");
        projectionMatrixUniform = std::make_unique<juce::OpenGLShaderProgram::Uniform> (*shaderProgram, "projectionMatrix");
        viewMatrixUniform = std::make_unique<juce::OpenGLShaderProgram::Uniform> (*shaderProgram, "viewMatrix");
        
        // Load 3D object (teapot from .obj file)
        loadTeapot();
        
        // Set up projection matrix
        updateProjectionMatrix();
    }

    void shutdown() override
    {
        shaderProgram.reset();
        positionAttribute.reset();
        colourAttribute.reset();
        textureCoordAttribute.reset();
        projectionMatrixUniform.reset();
        viewMatrixUniform.reset();
    }

    void render() override
    {
        jassert (juce::OpenGLHelpers::isContextActive());
        
        auto scale = (float) openGLContext.getRenderingScale();
        glViewport (0, 0, juce::roundToInt (getWidth() * scale),
                          juce::roundToInt (getHeight() * scale));
        
        glClearColor (0.1f, 0.1f, 0.2f, 1.0f);
        glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        
        glEnable (GL_DEPTH_TEST);
        glEnable (GL_BLEND);
        glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        
        shaderProgram->use();
        
        // Update view matrix (camera position)
        auto viewMatrix = createViewMatrix();
        viewMatrixUniform->set (viewMatrix);
        
        // Draw the teapot
        drawTeapot();
    }

private:
    std::unique_ptr<juce::OpenGLShaderProgram> shaderProgram;
    std::unique_ptr<juce::OpenGLShaderProgram::Attribute> positionAttribute;
    std::unique_ptr<juce::OpenGLShaderProgram::Attribute> colourAttribute;
    std::unique_ptr<juce::OpenGLShaderProgram::Attribute> textureCoordAttribute;
    std::unique_ptr<juce::OpenGLShaderProgram::Uniform> projectionMatrixUniform;
    std::unique_ptr<juce::OpenGLShaderProgram::Uniform> viewMatrixUniform;
    
    // Vertex data for teapot
    std::vector<float> vertices;
    std::vector<unsigned int> indices;
    GLuint vbo = 0, ebo = 0;
    
    void loadTeapot()
    {
        // Parse Wavefront .obj file from Resources folder
        auto objFile = juce::File::getSpecialLocation (juce::File::currentApplicationFile)
                          .getParentDirectory().getChildFile ("Resources").getChildFile ("teapot.obj");
        
        if (! objFile.existsAsFile())
            return;
        
        // Simple .obj parser (vertices and faces)
        auto lines = objFile.readLinesOfFile();
        std::vector<juce::Vector3D<float>> positions;
        
        for (auto& line : lines)
        {
            auto tokens = juce::StringArray::fromTokens (line, " ", "");
            
            if (tokens[0] == "v" && tokens.size() >= 4)
            {
                // Vertex position
                positions.add ({ tokens[1].getFloatValue(),
                                 tokens[2].getFloatValue(),
                                 tokens[3].getFloatValue() });
            }
            else if (tokens[0] == "f" && tokens.size() >= 4)
            {
                // Face (triangle indices, 1-based)
                for (int i = 1; i < tokens.size(); ++i)
                {
                    auto index = tokens[i].getIntValue() - 1;
                    indices.push_back ((unsigned int) index);
                }
            }
        }
        
        // Convert positions to vertex buffer (with dummy colors and texcoords)
        for (auto& pos : positions)
        {
            vertices.push_back (pos.x);
            vertices.push_back (pos.y);
            vertices.push_back (pos.z);
            vertices.push_back (1.0f);  // color r
            vertices.push_back (1.0f);  // color g
            vertices.push_back (1.0f);  // color b
            vertices.push_back (1.0f);  // color a
            vertices.push_back (0.0f);  // texcoord u
            vertices.push_back (0.0f);  // texcoord v
        }
        
        // Create VBO and EBO
        glGenBuffers (1, &vbo);
        glBindBuffer (GL_ARRAY_BUFFER, vbo);
        glBufferData (GL_ARRAY_BUFFER, vertices.size() * sizeof(float), vertices.data(), GL_STATIC_DRAW);
        
        glGenBuffers (1, &ebo);
        glBindBuffer (GL_ELEMENT_ARRAY_BUFFER, ebo);
        glBufferData (GL_ELEMENT_ARRAY_BUFFER, indices.size() * sizeof(unsigned int), indices.data(), GL_STATIC_DRAW);
    }
    
    void updateProjectionMatrix()
    {
        float aspectRatio = (float) getWidth() / (float) getHeight();
        projectionMatrix = juce::Matrix3D<float>::fromFrustum (-aspectRatio, aspectRatio, -1.0f, 1.0f, 1.0f, 100.0f);
        projectionMatrixUniform->set (projectionMatrix);
    }
    
    juce::Matrix3D<float> createViewMatrix()
    {
        // Simple camera positioned at (0, 0, 5) looking at origin
        return juce::Matrix3D<float>::fromTranslation ({ 0.0f, 0.0f, -5.0f });
    }
    
    void drawTeapot()
    {
        glBindBuffer (GL_ARRAY_BUFFER, vbo);
        glBindBuffer (GL_ELEMENT_ARRAY_BUFFER, ebo);
        
        // Set up vertex attributes
        glEnableVertexAttribArray (positionAttribute->attributeID);
        glVertexAttribPointer (positionAttribute->attributeID, 3, GL_FLOAT, GL_FALSE, 9 * sizeof(float), (void*) 0);
        
        glEnableVertexAttribArray (colourAttribute->attributeID);
        glVertexAttribPointer (colourAttribute->attributeID, 4, GL_FLOAT, GL_FALSE, 9 * sizeof(float), (void*) (3 * sizeof(float)));
        
        glEnableVertexAttribArray (textureCoordAttribute->attributeID);
        glVertexAttribPointer (textureCoordAttribute->attributeID, 2, GL_FLOAT, GL_FALSE, 9 * sizeof(float), (void*) (7 * sizeof(float)));
        
        // Draw indexed geometry
        glDrawElements (GL_TRIANGLES, (GLsizei) indices.size(), GL_UNSIGNED_INT, 0);
    }
    
    juce::Matrix3D<float> projectionMatrix;
    
    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR (OpenGLDemo)
};
```

**Main Application:**

```cpp
class MainWindow : public juce::DocumentWindow
{
public:
    MainWindow() : DocumentWindow ("OpenGL Demo",
                                   juce::Desktop::getInstance().getDefaultLookAndFeel()
                                       .findColour (juce::ResizableWindow::backgroundColourId),
                                   DocumentWindow::allButtons)
    {
        setUsingNativeTitleBar (true);
        setResizable (true, true);
        setBounds (100, 100, 800, 600);
        
        openGLDemo = std::make_unique<OpenGLDemo>();
        setContentOwned (openGLDemo.get(), true);
        setVisible (true);
    }

    void closeButtonPressed() override
    {
        juce::JUCEApplication::getInstance()->systemRequestedQuit();
    }

private:
    std::unique_ptr<OpenGLDemo> openGLDemo;
};

class OpenGLApplication : public juce::JUCEApplication
{
public:
    OpenGLApplication() {}

    const juce::String getApplicationName() override { return "OpenGL Demo"; }
    const juce::String getApplicationVersion() override { return "1.0.0"; }
    bool moreThanOneInstanceAllowed() override { return true; }

    void initialise (const juce::String&) override
    {
        mainWindow = std::make_unique<MainWindow>();
    }

    void shutdown() override
    {
        mainWindow.reset();
    }

private:
    std::unique_ptr<MainWindow> mainWindow;
};

START_JUCE_APPLICATION (OpenGLApplication)
```

**Key Concepts Demonstrated:**

1. **GLSL Shaders**: Vertex shader transforms 3D positions using projection and view matrices. Fragment shader outputs a solid orange color with alpha blending.

2. **Projection Matrix**: Converts 3D scene to 2D screen space using perspective projection (`Matrix3D::fromFrustum`).

3. **View Matrix**: Positions the camera in 3D space (translation to move camera back from origin).

4. **Wavefront .obj Parsing**: Loads 3D geometry from a standard file format (vertices and triangle indices).

5. **Vertex Attributes**: Position (3 floats), color (4 floats), texture coordinates (2 floats) packed into a single VBO.

6. **Indexed Drawing**: Uses element buffer to draw triangles efficiently, reusing vertices.

**CMake Configuration:**

```cmake
juce_add_gui_app(OpenGLDemo
    NEEDS_OPENGL TRUE
)

target_compile_definitions(OpenGLDemo
    PUBLIC
        JUCE_WEB_BROWSER=0
        JUCE_USE_CURL=0
        JUCE_APPLICATION_NAME_STRING="$<TARGET_PROPERTY:OpenGLDemo,JUCE_PROJECT_NAME>"
        JUCE_APPLICATION_VERSION_STRING="$<TARGET_PROPERTY:OpenGLDemo,JUCE_VERSION>"
)

target_link_libraries(OpenGLDemo
    PRIVATE
        juce::juce_gui_extra
        juce::juce_opengl
)
```

**Important Notes:**

- **Resources folder**: The .obj file must be in a `Resources` folder next to the built application
- **OpenGL ES compatibility**: For mobile platforms, use `lowp` precision qualifiers in fragment shaders
- **Depth testing**: Enable `GL_DEPTH_TEST` for proper 3D rendering order
- **Blending**: Use `GL_BLEND` with `GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA` for transparency
- **Viewport scaling**: Always multiply viewport by `getRenderingScale()` for Retina/HiDPI displays

---
};
```

### 9.8 OpenGL Versions and Profiles

OpenGL has evolved through several versions and profiles. Understanding these is critical for JUCE development:

**OpenGL Version History:**
- **2.1** (2006): Last version with fixed-function pipeline. Deprecated in modern OpenGL.
- **3.0** (2008): Introduced deprecation model, VAOs, FBOs as core features
- **3.2** (2009): **JUCE's default** — Core Profile introduced, geometry shaders
- **3.3** (2010): Compute shaders, sampler objects, texture swizzling
- **4.0-4.6** (2010-2017): Tessellation, indirect drawing, bindless textures, SPIR-V

**Core Profile vs Compatibility Profile:**
- **Core Profile**: Removes deprecated fixed-function pipeline. Forces modern practices (shaders, VAOs, VBOs). **JUCE 8 defaults to Core Profile.**
- **Compatibility Profile**: Retains legacy functions (glBegin/glEnd, display lists, fixed-function lighting). Easier for porting old code but not recommended.

**Why JUCE uses OpenGL 3.2 Core:**
- Widely supported across all modern platforms (macOS 10.7+, Windows Vista+, Linux Mesa)
- Forces modern, efficient rendering practices
- Compatible with WebGL 2.0 (important for future web-based UIs)
- macOS deprecated OpenGL in 10.14 but still supports 4.1 Core

**Setting OpenGL version in JUCE:**

```cpp
// Request specific version
openGLContext.setOpenGLVersionRequired (juce::OpenGLContext::OpenGLVersion::openGL3_2);

// Or for newer features (if platform supports it)
openGLContext.setOpenGLVersionRequired (juce::OpenGLContext::OpenGLVersion::openGL4_1);

// Check actual version at runtime
auto version = openGLContext.getOpenGLVersion();
// Returns: openGL2_1, openGL3_2, openGL4_1, etc.
```

**Platform considerations:**
- **macOS**: Only Core Profile supported (Apple removed Compatibility Profile). Max version is 4.1.
- **Windows**: Both Core and Compatibility supported. Version depends on GPU driver.
- **Linux**: Depends on Mesa/NVIDIA driver. Typically supports up to 4.6 on modern hardware.

### 9.9 Modern OpenGL Rendering Pipeline

Modern OpenGL (3.2+) uses a programmable pipeline. Understanding this is essential for custom rendering:

**Pipeline Stages:**
1. **Vertex Specification**: Define geometry (positions, colors, texture coords) in VBOs
2. **Vertex Shader**: Transform vertices (model → view → projection space)
3. **Primitive Assembly**: Connect vertices into triangles/lines/points
4. **Rasterization**: Convert primitives to fragments (pixels)
5. **Fragment Shader**: Compute color for each fragment
6. **Output Merging**: Depth test, blending, write to framebuffer

**Vertex Array Objects (VAO) — Required in Core Profile:**

VAOs store vertex attribute state. You MUST use them in Core Profile:

```cpp
GLuint vao;
glGenVertexArrays (1, &vao);
glBindVertexArray (vao);

// Now configure vertex attributes (they're stored in the VAO)
GLuint vbo;
glGenBuffers (1, &vbo);
glBindBuffer (GL_ARRAY_BUFFER, vbo);

// Upload vertex data
struct Vertex { float x, y, z; float r, g, b; };
Vertex vertices[] = {
    { -0.5f, -0.5f, 0.0f,  1.0f, 0.0f, 0.0f },  // red
    {  0.5f, -0.5f, 0.0f,  0.0f, 1.0f, 0.0f },  // green
    {  0.0f,  0.5f, 0.0f,  0.0f, 0.0f, 1.0f }   // blue
};
glBufferData (GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

// Configure vertex attributes
glEnableVertexAttribArray (0);  // position
glVertexAttribPointer (0, 3, GL_FLOAT, GL_FALSE, sizeof(Vertex), (void*) 0);

glEnableVertexAttribArray (1);  // color
glVertexAttribPointer (1, 3, GL_FLOAT, GL_FALSE, sizeof(Vertex), (void*) (3 * sizeof(float)));

// Unbind
glBindVertexArray (0);
glBindBuffer (GL_ARRAY_BUFFER, 0);

// Later, in renderOpenGL():
glBindVertexArray (vao);
glDrawArrays (GL_TRIANGLES, 0, 3);
glBindVertexArray (0);

// Cleanup in openGLContextClosing():
glDeleteVertexArrays (1, &vao);
glDeleteBuffers (1, &vbo);
```

**Element Buffer Objects (EBO) — Indexed Drawing:**

Reuse vertices for efficiency (e.g., cube has 8 vertices but 36 indices):

```cpp
GLuint ebo;
glGenBuffers (1, &ebo);
glBindBuffer (GL_ELEMENT_ARRAY_BUFFER, ebo);

unsigned int indices[] = { 0, 1, 2,  2, 3, 0 };  // Two triangles forming a quad
glBufferData (GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);

// Draw with indices
glDrawElements (GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
```

### 9.10 Advanced Shader Techniques

**Uniform Buffer Objects (UBO) — Share uniforms across shaders:**

```cpp
// Define uniform block in shader
const char* vertexShader = R"(
    #version 330 core
    layout(std140) uniform Matrices {
        mat4 model;
        mat4 view;
        mat4 projection;
    };
    // ... rest of shader
)";

// Create UBO
GLuint ubo;
glGenBuffers (1, &ubo);
glBindBuffer (GL_UNIFORM_BUFFER, ubo);
glBufferData (GL_UNIFORM_BUFFER, 3 * sizeof(glm::mat4), nullptr, GL_DYNAMIC_DRAW);

// Bind to binding point
GLuint blockIndex = glGetUniformBlockIndex (shaderProgram, "Matrices");
glUniformBlockBinding (shaderProgram, blockIndex, 0);
glBindBufferBase (GL_UNIFORM_BUFFER, 0, ubo);

// Update matrices
glm::mat4 matrices[3] = { model, view, projection };
glBindBuffer (GL_UNIFORM_BUFFER, ubo);
glBufferSubData (GL_UNIFORM_BUFFER, 0, sizeof(matrices), matrices);
```

**Geometry Shaders — Generate geometry on the GPU:**

```glsl
#version 330 core
layout(points) in;
layout(triangle_strip, max_vertices = 4) out;

void main() {
    // Expand each point into a quad
    vec4 pos = gl_in[0].gl_Position;
    float size = 0.1;
    
    gl_Position = pos + vec4(-size, -size, 0.0, 0.0); EmitVertex();
    gl_Position = pos + vec4( size, -size, 0.0, 0.0); EmitVertex();
    gl_Position = pos + vec4(-size,  size, 0.0, 0.0); EmitVertex();
    gl_Position = pos + vec4( size,  size, 0.0, 0.0); EmitVertex();
    EndPrimitive();
}
```

**Instanced Rendering — Draw many objects efficiently:**

```cpp
// Draw 1000 instances of the same mesh
glDrawArraysInstanced (GL_TRIANGLES, 0, vertexCount, 1000);

// In vertex shader, use gl_InstanceID:
// mat4 instanceMatrix = instanceMatrices[gl_InstanceID];
```

### 9.11 Framebuffer Objects (FBO) — Advanced Techniques

**Multiple Render Targets (MRT):**

```cpp
// Create FBO with multiple color attachments
GLuint fbo;
glGenFramebuffers (1, &fbo);
glBindFramebuffer (GL_FRAMEBUFFER, fbo);

GLuint colorTextures[2];
glGenTextures (2, colorTextures);

for (int i = 0; i < 2; ++i) {
    glBindTexture (GL_TEXTURE_2D, colorTextures[i]);
    glTexImage2D (GL_TEXTURE_2D, 0, GL_RGBA16F, width, height, 0, GL_RGBA, GL_FLOAT, nullptr);
    glFramebufferTexture2D (GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0 + i, GL_TEXTURE_2D, colorTextures[i], 0);
}

GLuint attachments[] = { GL_COLOR_ATTACHMENT0, GL_COLOR_ATTACHMENT1 };
glDrawBuffers (2, attachments);

// In fragment shader, write to multiple outputs:
// layout(location = 0) out vec4 color;
// layout(location = 1) out vec4 normals;
```

**Depth Textures for Shadow Mapping:**

```cpp
GLuint depthTexture;
glGenTextures (1, &depthTexture);
glBindTexture (GL_TEXTURE_2D, depthTexture);
glTexImage2D (GL_TEXTURE_2D, 0, GL_DEPTH_COMPONENT32, shadowMapSize, shadowMapSize, 0, 
              GL_DEPTH_COMPONENT, GL_FLOAT, nullptr);

glFramebufferTexture2D (GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_TEXTURE_2D, depthTexture, 0);
```

### 9.12 OpenGL Performance Best Practices

**Do:**
- **Batch draw calls**: Minimize state changes and draw calls per frame
- **Use VAOs**: Required in Core Profile, improves performance
- **Use VBOs with appropriate usage hints**: `GL_STATIC_DRAW` for unchanging geometry, `GL_DYNAMIC_DRAW` for frequently updated
- **Minimize uniform updates**: Use UBOs for shared data
- **Use instancing**: Draw many similar objects in one call
- **Profile with GPU tools**: RenderDoc, NVIDIA Nsight, AMD GPU PerfStudio

**Don't:**
- **Don't use immediate mode**: `glBegin/glEnd` is deprecated and slow
- **Don't create/destroy GL objects in render loop**: Create once in `newOpenGLContextCreated()`, destroy in `openGLContextClosing()`
- **Don't read back from GPU**: `glReadPixels` stalls the pipeline
- **Don't use deprecated functions**: Fixed-function pipeline, display lists, etc.

**Common performance patterns for audio visualization:**

```cpp
// Waveform display: Update VBO with audio samples
void updateWaveform (const float* samples, int numSamples) {
    glBindBuffer (GL_ARRAY_BUFFER, waveformVBO);
    glBufferSubData (GL_ARRAY_BUFFER, 0, numSamples * sizeof(float), samples);
}

// Spectrum analyzer: Use instancing for bars
void renderSpectrum (const float* magnitudes, int numBins) {
    glBindVertexArray (barVAO);
    for (int i = 0; i < numBins; ++i) {
        glUniform1f (magnitudeUniform, magnitudes[i]);
        glUniform1i (binIndexUniform, i);
        glDrawArrays (GL_TRIANGLE_STRIP, 0, 4);
    }
}
```

### 9.13 Migrating from Legacy OpenGL to Modern OpenGL

If you have existing OpenGL code using deprecated functions, here's how to migrate:

**Legacy (deprecated):**
```cpp
glBegin (GL_TRIANGLES);
    glVertex3f (-0.5f, -0.5f, 0.0f);
    glVertex3f ( 0.5f, -0.5f, 0.0f);
    glVertex3f ( 0.0f,  0.5f, 0.0f);
glEnd ();
```

**Modern (Core Profile):**
```cpp
// One-time setup
float vertices[] = { -0.5f, -0.5f, 0.0f,  0.5f, -0.5f, 0.0f,  0.0f, 0.5f, 0.0f };
glGenBuffers (1, &vbo);
glBindBuffer (GL_ARRAY_BUFFER, vbo);
glBufferData (GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

glGenVertexArrays (1, &vao);
glBindVertexArray (vao);
glEnableVertexAttribArray (0);
glVertexAttribPointer (0, 3, GL_FLOAT, GL_FALSE, 0, 0);

// In render loop
glBindVertexArray (vao);
glDrawArrays (GL_TRIANGLES, 0, 3);
```

**Legacy lighting:**
```cpp
// Deprecated
glEnable (GL_LIGHTING);
glEnable (GL_LIGHT0);
glLightfv (GL_LIGHT0, GL_POSITION, lightPos);
```

**Modern lighting (in fragment shader):**
```glsl
uniform vec3 lightPos;
uniform vec3 viewPos;

void main() {
    vec3 normal = normalize(Normal);
    vec3 lightDir = normalize(lightPos - FragPos);
    float diff = max(dot(normal, lightDir), 0.0);
    vec3 result = diff * lightColor * objectColor;
    FragColor = vec4(result, 1.0);
}
```

### 9.14 Platform-Specific OpenGL Considerations

**macOS:**
- Only Core Profile supported (Compatibility Profile removed)
- Maximum OpenGL version: 4.1 (Apple deprecated OpenGL in favor of Metal)
- Use `NSOpenGLView` under the hood (JUCE handles this)
- Retina displays: Use `getRenderingScale()` for proper resolution

**Windows:**
- Supports both Core and Compatibility profiles
- Maximum version depends on GPU driver (typically 4.6 on modern hardware)
- WGL (Windows GL) context creation
- Multi-GPU systems: JUCE uses the default GPU

**Linux:**
- GLX or EGL context creation (JUCE handles this)
- Mesa drivers typically support up to 4.5-4.6
- NVIDIA proprietary drivers support full 4.6
- Wayland: OpenGL works through XWayland or native EGL

**Checking capabilities at runtime:**
```cpp
// Check OpenGL version
const char* version = (const char*) glGetString (GL_VERSION);
const char* renderer = (const char*) glGetString (GL_RENDERER);
const char* vendor = (const char*) glGetString (GL_VENDOR);

// Check extensions
int numExtensions;
glGetIntegerv (GL_NUM_EXTENSIONS, &numExtensions);
for (int i = 0; i < numExtensions; ++i) {
    const char* ext = (const char*) glGetStringi (GL_EXTENSIONS, i);
    // Check for specific extension
}
```

### 9.15 Debugging OpenGL in JUCE

**Enable debug output (OpenGL 4.3+ or with extension):**
```cpp
void newOpenGLContextCreated() override {
    // Enable debug output
    glEnable (GL_DEBUG_OUTPUT);
    glEnable (GL_DEBUG_OUTPUT_SYNCHRONOUS);
    glDebugMessageCallback ([](GLenum source, GLenum type, GLuint id, GLenum severity,
                                GLsizei length, const GLchar* message, const void* userParam) {
        if (severity == GL_DEBUG_SEVERITY_HIGH)
            juce::Logger::writeToLog ("GL ERROR: " + juce::String (message));
        else if (severity == GL_DEBUG_SEVERITY_MEDIUM)
            juce::Logger::writeToLog ("GL WARNING: " + juce::String (message));
    }, nullptr);
    
    // ... rest of setup
}
```

**Common debugging tools:**
- **RenderDoc**: Frame capture and analysis (https://renderdoc.org)
- **NVIDIA Nsight Graphics**: NVIDIA GPU profiling
- **AMD Radeon GPU Profiler**: AMD GPU profiling
- **apitrace**: API call tracing and replay
- **glslangValidator**: GLSL shader validation

**Common errors and solutions:**
- `GL_INVALID_OPERATION`: Wrong state (e.g., drawing without VAO in Core Profile)
- `GL_INVALID_VALUE`: Invalid parameter (e.g., negative texture size)
- `GL_INVALID_ENUM`: Invalid enum value
- `GL_OUT_OF_MEMORY`: GPU out of memory (reduce texture/buffer sizes)

Use `glGetError()` to check for errors after GL calls:
```cpp
GLenum error = glGetError();
if (error != GL_NO_ERROR)
    juce::Logger::writeToLog ("OpenGL error: " + juce::String ((int) error));
```

### 9.16 OpenGL Resources and References

**Official Documentation:**
- OpenGL Registry: https://www.khronos.org/registry/OpenGL/
- OpenGL 4.6 Reference Pages: https://docs.gl/gl4/
- GLSL Reference: https://www.khronos.org/opengl/wiki/Core_Language_(GLSL)

**Learning Resources:**
- Learn OpenGL (excellent tutorial): https://learnopengl.com/
- OpenGL SuperBible (book)
- Real-Time Rendering (book)

**Libraries commonly used with JUCE OpenGL:**
- **GLM** (OpenGL Mathematics): Header-only math library for vectors, matrices
- **stb_image**: Single-header image loading for textures
- **Dear ImGui**: Immediate-mode GUI for debug overlays (has JUCE backend)

**JUCE-Specific:**
- JUCE OpenGL examples: `JUCE/examples/GUI/OpenGLAppDemo`
- JUCE Forum OpenGL discussions: https://forum.juce.com/c/opengl/10

---
};
```

### 9.7 3D Geometry Helpers

```cpp
juce::Vector3D<float> v (1.0f, 2.0f, 3.0f);
juce::Matrix3D<float> projection = juce::Matrix3D<float>::fromFrustum (left, right, bottom, top, near, far);
juce::Matrix3D<float> rotation = juce::Matrix3D<float>::rotation ({ angleX, angleY, angleZ });
juce::Quaternion<float> q (axis, angle);
juce::Draggable3DOrientation dragOrientation;  // mouse-driven 3D rotation
```

---

## 10. Audio Device Management (Standalone Apps)

For standalone audio apps (not plugins), use `AudioDeviceManager`:

```cpp
class MyApp : public juce::JUCEApplication, private juce::AudioIODeviceCallback
{
public:
    void initialise (const juce::String&) override
    {
        deviceManager.initialise (0, 2, nullptr, true, {}, nullptr);
        deviceManager.addAudioCallback (this);
        mainWindow = std::make_unique<MainWindow>();
    }

    void audioDeviceIOCallbackWithContext (const float* const* inputChannelData,
                                            int numInputChannels,
                                            float* const* outputChannelData,
                                            int numOutputChannels,
                                            int numSamples,
                                            const juce::AudioIODeviceCallbackContext&) override
    {
        for (int ch = 0; ch < numOutputChannels; ++ch)
            juce::FloatVectorOperations::clear (outputChannelData[ch], numSamples);
        // Generate/process audio here
    }

    void audioDeviceAboutToStart (juce::AudioIODevice* device) override
    {
        auto sampleRate = device->getCurrentSampleRate();
        // prepare DSP
    }

    void audioDeviceStopped() override {}

private:
    juce::AudioDeviceManager deviceManager;
    std::unique_ptr<MainWindow> mainWindow;
};
```

### AudioDeviceSelectorComponent

A ready-made UI for audio device configuration:

```cpp
juce::AudioDeviceSelectorComponent deviceSelector (
    deviceManager,
    0,   // minInputChannels
    2,   // maxInputChannels
    0,   // minOutputChannels
    2,   // maxOutputChannels
    true, // showMidiInput
    true, // showMidiOutput
    false, // showMidiOutputSelector
    true   // treatInputsAndOutputsAsIndependent
);
addAndMakeVisible (deviceSelector);
```

---

## 11. Audio Recording & File I/O

### Reading audio files

```cpp
juce::AudioFormatManager formatManager;
formatManager.registerBasicFormats();  // WAV, AIFF

auto file = juce::File ("/path/to/audio.wav");
if (auto reader = formatManager.createReaderFor (file))
{
    auto numChannels = reader->numChannels;
    auto numSamples  = reader->lengthInSamples;
    auto sampleRate  = reader->sampleRate;

    juce::AudioBuffer<float> buffer ((int) numChannels, (int) numSamples);
    reader->read (&buffer, 0, (int) numSamples, 0, true, true);
}
```

### Writing audio files

```cpp
juce::WavAudioFormat wavFormat;
auto outputStream = std::make_unique<juce::FileOutputStream> (file);

if (auto writer = wavFormat.createWriterFor (
        outputStream.get(), sampleRate, numChannels, 16, {}, 0))
{
    outputStream.release();  // writer takes ownership
    writer->writeFromAudioSampleBuffer (buffer, 0, buffer.getNumSamples());
}
```

### AudioThumbnail (waveform display)

```cpp
class WaveformDisplay : public juce::Component, private juce::ChangeListener
{
public:
    WaveformDisplay()
        : thumbnailCache (5),
          thumbnail (512, formatManager, thumbnailCache)
    {
        formatManager.registerBasicFormats();
        thumbnail.addChangeListener (this);
    }

    void loadFile (const juce::File& file) { thumbnail.setSource (new juce::FileInputSource (file)); }

    void paint (juce::Graphics& g) override
    {
        g.setColour (juce::Colours::green);
        thumbnail.drawChannels (g, getLocalBounds(),
            0.0, thumbnail.getTotalLength(), 1.0f);
    }

    void changeListenerCallback (juce::ChangeBroadcaster*) override { repaint(); }

private:
    juce::AudioFormatManager formatManager;
    juce::AudioThumbnailCache thumbnailCache;
    juce::AudioThumbnail thumbnail;
};
```

---

## 12. MIDI Processing

```cpp
void processBlock (juce::AudioBuffer<float>& buffer, juce::MidiBuffer& midiMessages) override
{
    for (const auto metadata : midiMessages)
    {
        auto msg = metadata.getMessage();
        if (msg.isNoteOn())
        {
            int noteNumber = msg.getNoteNumber();
            float velocity = msg.getFloatVelocity();
            // trigger voice
        }
        else if (msg.isNoteOff())
        {
            // release voice
        }
        else if (msg.isController())
        {
            int cc = msg.getControllerNumber();
            int value = msg.getControllerValue();
        }
    }
}
```

### Synthesiser (polyphonic synth)

```cpp
class MyVoice : public juce::SynthesiserVoice
{
public:
    bool canPlaySound (juce::SynthesiserSound* sound) override
    {
        return dynamic_cast<juce::SynthesiserSound*> (sound) != nullptr;
    }

    void startNote (int midiNoteNumber, float velocity,
                    juce::SynthesiserSound*, int pitchWheel) override
    {
        currentAngle = 0.0;
        auto cyclesPerSecond = juce::MidiMessage::getMidiNoteInHertz (midiNoteNumber);
        angleDelta = cyclesPerSecond * 2.0 * juce::MathConstants<double>::pi / sampleRate;
        level = velocity * 0.5;
    }

    void stopNote (float velocity, bool allowTailOff) override
    {
        if (allowTailOff) { tailOff = level; }
        else { clearCurrentNote(); }
    }

    void renderNextBlock (juce::AudioBuffer<float>& buffer, int startSample, int numSamples) override
    {
        if (angleDelta != 0.0)
        {
            if (tailOff > 0.0)
            {
                // Fade out
                while (--numSamples >= 0)
                {
                    auto currentSample = (float) (std::sin (currentAngle) * tailOff);
                    for (auto i = buffer.getNumChannels(); --i >= 0;)
                        buffer.addSample (i, startSample, currentSample * level);
                    currentAngle += angleDelta;
                    ++startSample;
                    tailOff *= 0.99;
                    if (tailOff <= 0.005) { clearCurrentNote(); break; }
                }
            }
            else
            {
                while (--numSamples >= 0)
                {
                    auto currentSample = (float) (std::sin (currentAngle) * level);
                    for (auto i = buffer.getNumChannels(); --i >= 0;)
                        buffer.addSample (i, startSample, currentSample);
                    currentAngle += angleDelta;
                    ++startSample;
                }
            }
        }
    }

private:
    void clearCurrentNote() { angleDelta = 0.0; }
    double currentAngle = 0.0, angleDelta = 0.0, sampleRate = 44100.0;
    double level = 0.0, tailOff = 0.0;
};

// Setup
juce::Synthesiser synth;
synth.addSound (std::make_unique<juce::SynthesiserSound>());
for (int i = 0; i < 8; ++i)
    synth.addVoice (std::make_unique<MyVoice>());
```

---

## 13. Threading & Real-Time Safety

### Critical rules for processBlock

- **No allocations** — no `new`, `malloc`, `std::vector::push_back`, `String` creation
- **No locks** — no `ScopedLock`, `std::mutex`, `CriticalSection` (these can block)
- **No I/O** — no file reads, network calls, `Logger::writeToLog`
- **No GUI updates** — never call `repaint()` or `setSize()` from audio thread

### Safe cross-thread communication

```cpp
// Audio thread → GUI thread (use atomic or lock-free queue)
std::atomic<float> currentLevel { 0.0f };  // set in processBlock, read in Timer

// GUI thread → Audio thread (use atomic parameters)
std::atomic<bool> shouldReset { false };

// For complex data: use lock-free ring buffer
// juce::AbstractFifo or juce::dsp::FixedSizeFunction
```

### ScopedNoDenormals

Always use at the top of processBlock:

```cpp
void processBlock (AudioBuffer<float>& buffer, MidiBuffer& midi) override
{
    juce::ScopedNoDenormals noDenormals;  // prevent denormalized float performance hit
    // ...
}
```

---

## 14. Plugin Development Patterns

### 14.1 Editor with UI Size Persistence

```cpp
class MyEditor final : public juce::AudioProcessorEditor,
                       private juce::Value::Listener
{
public:
    MyEditor (MyProcessor& p) : AudioProcessorEditor (&p), processor (p)
    {
        lastUIWidth.referTo (p.apvts.state.getChildWithName ("uiState")
                              .getPropertyAsValue ("width", nullptr));
        lastUIHeight.referTo (p.apvts.state.getChildWithName ("uiState")
                              .getPropertyAsValue ("height", nullptr));
        setSize (lastUIWidth.getValue(), lastUIHeight.getValue());
        lastUIWidth.addListener (this);
        lastUIHeight.addListener (this);
        setResizable (true, true);
        setResizeLimits (300, 200, 1200, 800);
    }

    void resized() override
    {
        lastUIWidth = getWidth();
        lastUIHeight = getHeight();
        // layout children...
    }

    void valueChanged (juce::Value&) override
    {
        setSize (lastUIWidth.getValue(), lastUIHeight.getValue());
    }

private:
    MyProcessor& processor;
    juce::Value lastUIWidth, lastUIHeight;
};
```

### 14.2 Multi-Format ProcessBlock (float/double)

```cpp
void processBlock (juce::AudioBuffer<float>& buffer, juce::MidiBuffer& midi) override
{
    jassert (! isUsingDoublePrecision());
    process (buffer, midi, delayBufferFloat);
}

void processBlock (juce::AudioBuffer<double>& buffer, juce::MidiBuffer& midi) override
{
    jassert (isUsingDoublePrecision());
    process (buffer, midi, delayBufferDouble);
}

template <typename FloatType>
void process (juce::AudioBuffer<FloatType>& buffer, juce::MidiBuffer& midi,
              juce::AudioBuffer<FloatType>& delayBuffer)
{
    // Templated processing works for both float and double
}
```

### 14.3 Buses Configuration

```cpp
static juce::AudioProcessor::BusesProperties getBusesProperties()
{
    return BusesProperties()
        .withInput  ("Input",  juce::AudioChannelSet::stereo(), true)
        .withOutput ("Output", juce::AudioChannelSet::stereo(), true)
        .withInput  ("Sidechain", juce::AudioChannelSet::stereo(), false);
}

bool isBusesLayoutSupported (const BusesLayout& layouts) const override
{
    auto mainOutput = layouts.getMainOutputChannelSet();
    auto mainInput  = layouts.getMainInputChannelSet();
    if (mainInput != mainOutput)
        return false;
    if (mainOutput != juce::AudioChannelSet::mono()
        && mainOutput != juce::AudioChannelSet::stereo())
        return false;
    return true;
}
```

### 14.4 Convolution Reverb Pattern

```cpp
juce::dsp::Convolution convolution;

void prepareToPlay (double sr, int blockSize) override
{
    juce::dsp::ProcessSpec spec { sr, (juce::uint32) blockSize,
                                   (juce::uint32) getTotalNumOutputChannels() };
    convolution.prepare (spec);

    // Load IR from binary data
    convolution.loadImpulseResponse (
        BinaryData::hall_wav, BinaryData::hall_wavSize,
        juce::dsp::Convolution::Stereo::yes,
        juce::dsp::Convolution::Trim::yes,
        juce::dsp::Convolution::Normalise::yes);
}

void processBlock (juce::AudioBuffer<float>& buffer, juce::MidiBuffer&) override
{
    juce::dsp::AudioBlock<float> block (buffer);
    juce::dsp::ProcessContextReplacing<float> context (block);
    convolution.process (context);
}
```

### 14.5 Oversampling Pattern

```cpp
juce::dsp::Oversampling<float> oversampling (
    getTotalNumOutputChannels(),
    2,  // 2^2 = 4x oversampling
    juce::dsp::Oversampling<float>::filterHalfBandPolyphaseIIR,
    true);

void prepareToPlay (double sr, int blockSize) override
{
    oversampling.initProcessing ((size_t) blockSize);
    oversampling.reset();
}

void processBlock (juce::AudioBuffer<float>& buffer, juce::MidiBuffer&) override
{
    juce::dsp::AudioBlock<float> block (buffer);
    auto osBlock = oversampling.processSamplesUp (block);    // upsample
    // ... process at higher sample rate using osBlock ...
    oversampling.processSamplesDown (block);                  // downsample
}

double getLatencySamples() const override
{
    return oversampling.getLatencyInSamples();
}
```

---

## 15. Common Pitfalls

### Build & Configuration
- **Plugin codes must be 4 chars**: `PLUGIN_MANUFACTURER_CODE` and `PLUGIN_CODE` must be exactly 4 ASCII characters
- **VST3 on Linux requires additional packages**: `libx11-dev`, `libxrandr-dev`, `libxinerama-dev`, `libxcursor-dev`, `libfreetype6-dev`, `libasound2-dev`, `libcurl4-openssl-dev`, `webkit2gtk`
- **AudioUnit requires macOS**: AU format only builds on macOS regardless of CMake configuration
- **`juce_generate_juce_header` is legacy**: Modern JUCE uses `target_compile_definitions` for module config flags instead

### Audio Processing
- **Never allocate in processBlock**: Pre-allocate all buffers in `prepareToPlay`
- **Denormals kill performance**: Always use `ScopedNoDenormals` at the top of processBlock
- **Latency must be reported**: If your DSP adds latency (lookahead, oversampling), override `getLatencySamples()` and call `setLatencySamples()` in `prepareToPlay`
- **Clear unused output channels**: Always clear channels beyond input count to avoid garbage output
- **Convolution loads async**: `loadImpulseResponse` runs on a background thread — the IR won't be available immediately

### GUI & Threading
- **Never call GUI methods from audio thread**: `repaint()`, `setSize()`, `Label::setText()` etc. must only be called on the message thread
- **Use `MessageManager::callAsync`**: To trigger GUI updates from non-GUI threads
- **Slider attachments must outlive the slider**: Store them as member variables in the editor, not as locals
- **LookAndFeel must be set before components are created**: Or call `lookAndFeelChanged()` on existing components

### State & Parameters
- **ParameterID version hints**: Always provide a version hint (int >= 1) — hosts use this to match parameters across plugin versions
- **Don't read parameters with `getValue()` for audio**: Use `AudioParameterFloat::get()` which returns the actual float value, not the normalized 0-1 range
- **APVTS state child nodes**: Store non-parameter state (UI size, file paths) as child ValueTree nodes in the APVTS state
- **Thread-safe parameter access**: Use `AudioProcessorParameter::getValue()` atomically; for complex state, use `SpinLock` or lock-free queues

### OpenGL
- **Always call `detach()` in destructor**: Before the Component is destroyed, call `openGLContext.detach()`
- **GL calls only on GL thread**: Only make GL calls inside `renderOpenGL()` or `newOpenGLContextCreated()`, or after `openGLContext.makeActive()`
- **Check context active**: Use `OpenGLHelpers::isContextActive()` before GL calls
- **Scale for HiDPI**: Multiply viewport dimensions by `openGLContext.getRenderingScale()`

---

## 16. Application Entry Points

### Standalone GUI App

```cpp
class MyApplication : public juce::JUCEApplication
{
public:
    const juce::String getApplicationName() override { return "My App"; }
    const juce::String getApplicationVersion() override { return "1.0.0"; }
    bool moreThanOneInstanceAllowed() override { return true; }

    void initialise (const juce::String&) override
    {
        mainWindow = std::make_unique<MainWindow> (getApplicationName());
    }

    void shutdown() override { mainWindow.reset(); }

private:
    class MainWindow : public juce::DocumentWindow
    {
    public:
        MainWindow (const juce::String& name)
            : DocumentWindow (name, juce::Colours::lightgrey,
                              DocumentWindow::allButtons)
        {
            setUsingNativeTitleBar (true);
            setContentOwned (new MainComponent(), true);
            centreWithSize (getWidth(), getHeight());
            setVisible (true);
        }

        void closeButtonPressed() override
        {
            juce::JUCEApplication::getInstance()->systemRequestedQuit();
        }
    };

    std::unique_ptr<MainWindow> mainWindow;
};

START_JUCE_APPLICATION (MyApplication)
```

### Audio App (with AudioAppComponent)

```cpp
class MainComponent : public juce::AudioAppComponent
{
public:
    MainComponent()
    {
        setAudioChannels (0, 2);  // 0 inputs, 2 outputs
        setSize (400, 300);
    }

    ~MainComponent() override { shutdownAudio(); }

    void prepareToPlay (int samplesPerBlockExpected, double sampleRate) override {}
    void releaseResources() override {}

    void getNextAudioBlock (const juce::AudioSourceChannelInfo& bufferToFill) override
    {
        bufferToFill.clearActiveBufferRegion();
        auto* leftBuffer = bufferToFill.buffer->getWritePointer (0, bufferToFill.startSample);
        for (int i = 0; i < bufferToFill.numSamples; ++i)
            leftBuffer[i] = (float) std::sin (currentPhase) * 0.2f;
        // ... update phase
    }

    void paint (juce::Graphics& g) override { /* ... */ }
    void resized() override { /* ... */ }

private:
    double currentPhase = 0.0;
};
```

---

## 17. WebView UIs (JUCE 8+)

JUCE 8 introduces first-class WebView support, allowing you to build plugin and app UIs with React, Vue, Svelte, or plain HTML/CSS/JavaScript instead of native JUCE Components.

### 17.1 Why WebView?

- **Rapid iteration**: Hot reloading during development (like normal web dev)
- **Mature ecosystems**: Use React, Vue, Svelte, and their component libraries
- **Frontend developers can contribute**: No C++ required for UI work
- **Hardware-accelerated graphics**: WebGL for complex visualizations
- **Smaller binaries**: WebView is provided by the OS, not bundled

**Platform WebViews:**
- macOS: WebKit
- Windows: Edge (Chromium-based) — pre-installed on Win11, most Win10 machines
- Linux: GTK WebKit2

### 17.2 CMake Configuration

Add WebView support to your project:

```cmake
juce_add_plugin(MyPlugin
    FORMATS AU VST3 Standalone
    NEEDS_WEBVIEW2 TRUE  # Required for Windows
    # ... other options
)

target_compile_definitions(MyPlugin
    PUBLIC
        JUCE_WEB_BROWSER=1  # Enabled by default
        JUCE_USE_WIN_WEBVIEW2_WITH_STATIC_LINKING=1  # Windows: static link WebView2 loader
)

# Link juce_gui_extra (contains WebView)
target_link_libraries(MyPlugin
    PRIVATE
        juce::juce_gui_extra
)
```

**Important**: The `juce_gui_extra` module contains WebView functionality. On Windows, `NEEDS_WEBVIEW2 TRUE` searches for the WebView2 Nuget package. If installed in a non-standard location, use:

```cmake
set(JUCE_WEBVIEW2_PACKAGE_LOCATION "/path/to/webview2/nuget")
```

### 17.3 WebBrowserComponent — The Foundation

`WebBrowserComponent` embeds a native WebView in your JUCE application:

```cpp
class MyWebViewEditor : public juce::AudioProcessorEditor
{
public:
    MyWebViewEditor (MyProcessor& p)
        : AudioProcessorEditor (&p), processor (p)
    {
        // Configure WebView options
        juce::WebBrowserComponent::Options options;
        
        options.withUserAgent ("MyPlugin/1.0");
        options.withResourceProvider ([this] (const juce::String& path)
            -> std::optional<juce::WebBrowserComponent::Resource>
        {
            // Serve files from BinaryData or filesystem
            return getResource (path);
        });
        
        // Backend: allows JS to call C++ functions
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
        
        // Load from local dev server (Debug builds)
        // webBrowser.goToURL ("http://localhost:3000");
        
        // Load from embedded resources (Release builds)
        webBrowser.goToURL ("https://plugin-app/index.html");
    }

    void resized() override
    {
        webBrowser.setBounds (getLocalBounds());
    }

private:
    std::optional<juce::WebBrowserComponent::Resource> getResource (const juce::String& path)
    {
        // Map URL paths to BinaryData resources
        if (path == "/index.html")
            return juce::WebBrowserComponent::Resource {
                BinaryData::index_html,
                BinaryData::index_htmlSize,
                "text/html"
            };
        if (path == "/bundle.js")
            return juce::WebBrowserComponent::Resource {
                BinaryData::bundle_js,
                BinaryData::bundle_jsSize,
                "application/javascript"
            };
        return std::nullopt;
    }

    MyProcessor& processor;
    juce::WebBrowserComponent webBrowser;
};
```

### 17.4 Resource Providers — Serving Local Files

The `withResourceProvider` callback intercepts WebView requests and serves local content. This is how you embed your built React/Vue app:

```cpp
options.withResourceProvider ([this] (const juce::String& path)
    -> std::optional<juce::WebBrowserComponent::Resource>
{
    // Strip leading slash
    auto cleanPath = path.startsWith ("/") ? path.dropFirstCharacters (1) : path;
    
    // Try BinaryData first (for Release builds with embedded resources)
    int dataSize = 0;
    if (auto* data = BinaryData::getNamedResource (cleanPath.replaceCharacter ('/', '_').toRawUTF8(), dataSize))
    {
        auto mimeType = getMimeType (cleanPath);
        return juce::WebBrowserComponent::Resource { data, (size_t) dataSize, mimeType };
    }
    
    // Fallback to filesystem (for Debug builds with dev server)
    auto file = juce::File::getCurrentWorkingDirectory().getChildFile ("frontend/dist").getChildFile (cleanPath);
    if (file.existsAsFile())
    {
        auto data = file.loadFileAsData();
        auto mimeType = getMimeType (cleanPath);
        return juce::WebBrowserComponent::Resource {
            data.release(),
            (size_t) data.getSize(),
            mimeType
        };
    }
    
    return std::nullopt;
});
```

### 17.5 C++ ↔ JavaScript Communication

#### JavaScript → C++ (Native Integration)

From JavaScript, call C++ functions:

```javascript
// In your React/Vue/JS frontend
async function getGain() {
    const value = await window.juce.nativeIntegration.getParameterValue("gain");
    return value;
}

async function setGain(newValue) {
    await window.juce.nativeIntegration.setParameterValue("gain", newValue);
}
```

The C++ handler receives these calls:

```cpp
options.withNativeIntegration (
    [this] (const juce::String& name, const juce::var& args) -> juce::var
    {
        if (name == "getParameterValue")
        {
            auto paramId = args.toString();
            return processor.apvts.getRawParameterValue (paramId)->load();
        }
        
        if (name == "setParameterValue")
        {
            auto paramId = args[0].toString();
            auto value = (float) args[1];
            auto* param = processor.apvts.getParameter (paramId);
            param->setValueNotifyingHost (value);
            return {};
        }
        
        if (name == "getState")
        {
            auto xml = processor.apvts.copyState().createXml();
            return xml->toString();
        }
        
        return {};
    });
```

#### C++ → JavaScript (Evaluate Script)

From C++, call JavaScript functions or update the UI:

```cpp
// Call a JavaScript function
webBrowser.evaluateJavascript ("window.updateGainValue(0.75)");

// Or inject data
auto json = juce::JSON::toString (myData);
webBrowser.evaluateJavascript ("window.receiveData(" + json + ")");
```

### 17.6 Parameter Binding

For automatic parameter sync, bind APVTS parameters to JavaScript:

```cpp
// In C++, expose parameter values via native integration
options.withNativeIntegration (
    [this] (const juce::String& name, const juce::var& args) -> juce::var
    {
        if (name == "getAllParameters")
        {
            juce::DynamicObject::Ptr params = new juce::DynamicObject();
            for (auto* param : processor.apvts.processor.getParameters())
            {
                if (auto* p = dynamic_cast<juce::RangedAudioParameter*> (param))
                {
                    params->setProperty (p->getParameterID(), p->getValue());
                }
            }
            return juce::var (params.get());
        }
        return {};
    });
```

In JavaScript, poll or listen for changes:

```javascript
// Poll for parameter updates
setInterval(async () => {
    const params = await window.juce.nativeIntegration.getAllParameters();
    updateUI(params);
}, 50);

// Or use C++ → JS push (preferred for performance)
window.receiveParameterUpdate = (params) => {
    updateUI(params);
};
```

### 17.7 Development Workflow

#### Debug Mode (Hot Reloading)

1. Run your React/Vue dev server: `npm run dev` (typically on `localhost:3000`)
2. In C++, load from the dev server:

```cpp
#ifdef DEBUG
    webBrowser.goToURL ("http://localhost:3000");
#else
    webBrowser.goToURL ("https://plugin-app/index.html");
#endif
```

#### Release Mode (Embedded Resources)

1. Build your frontend: `npm run build` → outputs to `frontend/dist/`
2. Embed files as BinaryData in CMake:

```cmake
juce_add_binary_data(FrontendData
    SOURCES
        frontend/dist/index.html
        frontend/dist/bundle.js
        frontend/dist/styles.css
)
target_link_libraries(MyPlugin PRIVATE FrontendData)
```

3. Serve from BinaryData via the resource provider (see §17.4)

### 17.8 WebView Plugin Demo Structure

JUCE 8 includes `WebViewPluginDemo` showing a React frontend:

```
WebViewPluginDemo/
├── Source/
│   ├── PluginProcessor.h/.cpp    # Standard AudioProcessor
│   └── PluginEditor.h/.cpp       # WebView-based editor
└── Frontend/
    ├── package.json              # React app dependencies
    ├── src/
    │   ├── App.tsx               # React components
    │   └── index.tsx             # Entry point
    └── public/
        └── index.html            # HTML shell
```

**Key patterns from the demo:**

- Processor uses standard APVTS for parameter management
- Editor creates `WebBrowserComponent` with resource provider
- React app calls `window.juce.nativeIntegration` to get/set parameters
- C++ evaluates JavaScript to push parameter updates to the UI

### 17.9 WebView Best Practices

**Do:**
- Use `NEEDS_WEBVIEW2 TRUE` in CMake for Windows compatibility
- Statically link WebView2 loader with `JUCE_USE_WIN_WEBVIEW2_WITH_STATIC_LINKING=1`
- Specify a User Data Folder for WebView state persistence
- Use resource providers to embed built frontend assets in Release builds
- Load from `localhost` dev server during development for hot reloading
- Keep C++ ↔ JS communication minimal and asynchronous
- Use TypeScript for type safety in your frontend code

**Don't:**
- Bundle WebView binaries (they're provided by the OS)
- Block the message thread with synchronous JS evaluation
- Assume all WebView features work identically across platforms (test on all three)
- Forget to handle WebView unavailability gracefully (older OS versions)

### 17.10 Limitations & Considerations

- **No built-in widgets**: JUCE doesn't provide UI controls for WebView — you choose your own framework (React, Vue, etc.)
- **Platform differences**: WebView capabilities vary between WebKit, Edge, and GTK WebKit2
- **Parameter labels**: `convertTo0To1`, `convertFrom0To1`, `stringFromValue` must be manually exposed to JavaScript
- **Accessibility**: WebView accessibility support is less mature than native JUCE Components
- **Plugin certification**: Some plugin hosts may have stricter requirements for WebView-based UIs
- **Startup time**: WebView initialization adds a small delay on first launch

### 17.11 Example: Complete WebView Editor

```cpp
class WebViewEditor final : public juce::AudioProcessorEditor
{
public:
    WebViewEditor (MyProcessor& p)
        : AudioProcessorEditor (&p), processor (p)
    {
        juce::WebBrowserComponent::Options options;
        
        // User agent
        options.withUserAgent (JucePlugin_Name "/" JucePlugin_VersionString);
        
        // Resource provider
        options.withResourceProvider ([this] (const juce::String& path)
            -> std::optional<juce::WebBrowserComponent::Resource>
        {
            return serveResource (path);
        });
        
        // Native integration (JS → C++)
        options.withNativeIntegration ([this] (const juce::String& name, const juce::var& args) -> juce::var
        {
            if (name == "getParam")
                return processor.apvts.getRawParameterValue (args.toString())->load();
            
            if (name == "setParam")
            {
                processor.apvts.getParameter (args[0].toString())
                    ->setValueNotifyingHost ((float) args[1]);
                return {};
            }
            
            return {};
        });
        
        webBrowser.setOptions (options);
        addAndMakeVisible (webBrowser);
        
        setSize (800, 600);
        setResizable (true, true);
        
        // Load UI
    #ifdef DEBUG
        webBrowser.goToURL ("http://localhost:3000");
    #else
        webBrowser.goToURL ("https://plugin-app/index.html");
    #endif
        
        // Listen for parameter changes (C++ → JS)
        processor.apvts.state.addListener (this);
    }

    ~WebViewEditor() override
    {
        processor.apvts.state.removeListener (this);
    }

    void resized() override
    {
        webBrowser.setBounds (getLocalBounds());
    }

private:
    void valueTreePropertyChanged (juce::ValueTree&, const juce::Identifier& property) override
    {
        // Push parameter updates to JavaScript
        auto* param = processor.apvts.getParameter (property.toString());
        if (param != nullptr)
        {
            auto value = param->getValue();
            webBrowser.evaluateJavascript (
                "window.dispatchEvent(new CustomEvent('paramUpdate', {detail: {'" 
                + property.toString() + "': " + juce::String (value) + "}}))");
        }
    }

    std::optional<juce::WebBrowserComponent::Resource> serveResource (const juce::String& path)
    {
        auto cleanPath = path.startsWith ("/") ? path.dropFirstCharacters (1) : path;
        auto resourceName = cleanPath.replaceCharacter ('/', '_').toRawUTF8();
        
        int size = 0;
        if (auto* data = BinaryData::getNamedResource (resourceName, size))
        {
            return juce::WebBrowserComponent::Resource {
                data, (size_t) size, getMimeType (cleanPath)
            };
        }
        
        return std::nullopt;
    }

    juce::String getMimeType (const juce::String& path)
    {
        if (path.endsWith (".html")) return "text/html";
        if (path.endsWith (".js"))   return "application/javascript";
        if (path.endsWith (".css"))  return "text/css";
        if (path.endsWith (".json")) return "application/json";
        if (path.endsWith (".png"))  return "image/png";
        if (path.endsWith (".svg"))  return "image/svg+xml";
        return "application/octet-stream";
    }

    MyProcessor& processor;
    juce::WebBrowserComponent webBrowser;
};
```

---

## References

- JUCE Documentation: https://juce.com/learn/documentation
- JUCE Tutorials: https://juce.com/learn/tutorials
- JUCE API Reference: https://docs.juce.com/master/
- JUCE GitHub: https://github.com/juce-framework/JUCE
- JUCE Forum: https://forum.juce.com/
- CMake documentation for JUCE: https://github.com/juce-framework/JUCE/blob/master/docs/CMake%20API.md
- JUCE 8 WebView Overview: https://juce.com/blog/juce-8-feature-overview-webview-uis/
