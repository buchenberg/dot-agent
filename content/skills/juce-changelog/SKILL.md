---
name: juce-changelog
description: "JUCE framework changelog from 6.0.0 through 8.0.14 — major features, breaking changes, migration notes, and module evolution. Use when writing or reviewing JUCE code to ensure API compatibility, understanding version requirements, or planning upgrades. WHEN: JUCE, API changes, breaking changes, upgrade, migration, what version added, when was X introduced, deprecation, removed API, changelog."
---

# JUCE Changelog — 6.0.0 through 8.0.14

Comprehensive version history sourced from the official [JUCE GitHub releases](https://github.com/juce-framework/JUCE/releases) and [BREAKING_CHANGES.md](https://github.com/juce-framework/JUCE/blob/master/BREAKING_CHANGES.md).

## Version Timeline at a Glance

| Version | Date | Key Theme |
|---------|------|-----------|
| 6.0.0 | Jun 2020 | CMake, revamped DSP, VST3 Linux, WebView, Oboe Android |
| 6.0.2 | Oct 2020 | **macOS 11 / Apple Silicon arm64**, IAudioClient3 |
| 6.1.0 | Aug 2021 | **Accessibility framework**, C++14 baseline, macOS Monterey |
| 6.1.3 | Dec 2021 | VS 2022, threadsafe Font/TypefaceCache, FlexBox CSS compat |
| 6.1.5 | Jan 2022 | MPEKeyboardComponent, accessibility improvements |
| 7.0.0 | Jun 2022 | **ARA SDK**, **LV2 support**, Metal default renderer, revamped AudioPlayHead |
| 7.0.3 | Nov 2022 | AudioProcessorGraph refactor, new threading classes |
| 7.0.8 | Oct 2023 | macOS/iOS AudioWorkgroup, Xcode 15, Sonoma |
| 7.0.9 | Nov 2023 | MIDI-CI support |
| 8.0.0 | Jun 2024 | **Direct2D renderer**, **WebView UIs**, **bundled AAX SDK**, Unicode, Animation module |
| 8.0.2 | Sep 2024 | C++20 and C++23 support, VST3 3.7.12 |
| 8.0.5 | Jan 2025 | Windows ARM, VST3 parameter migrations, Ranges |
| 8.0.7 | Apr 2025 | MessageManager::callSync |
| 8.0.9 | Sep 2025 | Font features (ligatures/kerning), macOS/iOS 26, 32-bit WAV |
| 8.0.13 | May 2026 | Component painting perf, min Windows target 1607, reduced stack sizes |
| 8.0.14 | Jun 2026 | Latest stable |

---

## 6.0.x Series (June 2020 – March 2021)

### 6.0.0 — "The CMake & DSP Release" (June 29, 2020)

**Major features:**
- **CMake support**: `juce_add_plugin()`, `juce_add_gui_app()`, etc. Projucer no longer the only build system.
- **Revamped DSP module**: `juce::dsp::ProcessorChain`, `AudioBlock`, `ProcessContextReplacing`, new DSP processor classes
- **VST3 on Linux**: Full VST3 plugin support on Linux
- **WebView support**: `juce_webview` for macOS/iOS and Windows
- **Projucer freed**: Removed sign-in requirement, app reporting, and analytics
- **Oboe on Android**: Bundled Oboe source, now default Android audio device
- **HWNDComponent**: Embed native Windows HWNDs
- **IPP FFT implementation**: Intel Performance Primitives FFT option
- **C++11 range-for**: `MidiBuffer::Iterator`, `RangedDirectoryIterator`, `String` range-for compatibility
- Preallocated `MidiMessageCollector` storage
- `AudioProcessorGraph::extractNode()`
- Refactored APVTS parameter attachments; added `ParameterAttachment`
- Windows/Linux hiDPI scaling improvements
- Removed JuceHeader.h requirement from Projucer projects

### 6.0.1 (July 7, 2020)
- Projucer GUI editor fix (code overwrite bug)
- Android Oboe 1.4.2, Gradle/plugin version bumps
- VST3 MIDI bus enablement fix
- Windows Clang compatibility
- GCC 4.8/5.0 fix
- Projucer CLion exporter fix
- DPI-aware drag-and-drop fix

### 6.0.2 — **"Apple Silicon"** (Oct 5, 2020)
- **macOS 11 and Apple Silicon arm64 support**
- **Windows IAudioClient3** for low-latency audio drivers
- Precompiled header support in Projucer (Windows and macOS)
- macOS menu bar accessibility
- VST3 hosting for persistent DLL loads
- macOS camera capture API update
- Projucer diff improvements
- Linux JACK fixes

### 6.0.3 (Oct 5, 2020)
- Version number fix in project files

### 6.0.4 (Oct 14, 2020)
- Projucer update mechanism improvement
- AUv3 parameter normalisation fix
- WASAPI exclusive mode sample rate fix
- Linux ALSA build fix

### 6.0.5 (Dec 1, 2020)
- PopupMenu styling support
- IPC/named pipe race condition fixes
- FileChooser improvements
- Latest Android SDK compatibility
- CoreAudio glitch prevention (before mic permission)
- Robust MIDI and audio file reading

### 6.0.6 (Jan 13, 2021)
- **New CoreMIDI API** on supported platforms
- **Xcode "New Build System"** support
- Audio format readers made more robust
- HiResTimer improvements
- VST3 program parameter fix
- Android Oboe 1.5

### 6.0.8 (Mar 22, 2021)
- macOS graphics invalidation region fix
- Modal dialog dismissal improvements
- CoreAudio glitch fix before microphone permission
- AUv3 resizing and initialisation
- String-to-double conversion fixes
- iOS split view behaviour
- `Display::safeAreaInsets` added
- macOS ARM assertion behaviour
- Display scaling and resizing fixes
- `audioProcessorChanged` callback with more info
- DSP convolution issues fixed
- macOS ARM host detection

---

## 6.1.x Series (August 2021 – February 2022)

### 6.1.0 — **"Accessibility & C++14"** (Aug 23, 2021)
- **Accessibility support** added to the framework
- VST3 plugin extensions enabled
- OpenGL function loading improvements
- **C++14 baseline** (minimum standard)
- macOS Monterey and iOS 15 support
- **Async versions of all modal functions**
- VST3 threading fixes
- **Cross-platform-compatible VST3 UID hash**
- MinGW compatibility improvements
- `BufferingAudioReader` fixes
- TextEditor repainting improvements
- Larger ASIO buffer support
- Android Oboe 1.6.1
- Modal dismissing improvements
- macOS ARM assertion handling improvements

### 6.1.1 (Sep 9, 2021)
- CMake installation fix
- Parameter value loading after plugin restarts
- Multi-line text layout problems fixed
- Modal native message box fallback on Windows
- OpenGL repaint events fix
- Accessibility improvements

### 6.1.2 (Sep 20, 2021)
- OpenGL display refresh rate fix (macOS)
- VST3 plugin scaling behaviour improvement
- Accessibility improvements

### 6.1.3 — **"VS 2022 & Threadsafe Fonts"** (Dec 8, 2021)
- **Visual Studio 2022** support in Projucer
- **OpenGL 3.2 context creation on Windows**
- Stable parameter ID retrieval for plugin hosts
- High-resolution images in DragAndDropContainer
- Wider range of frame-rates in plugins and hosts
- **Threadsafe Font and TypefaceCache** — background thread font rendering
- FlexBox CSS specification compatibility
- macOS 12 (Monterey) compatibility: OpenGL and FileChooser fixes
- Accessibility improvements

### 6.1.4 (Dec 20, 2021)
- Projucer project saving behaviour restored
- CGImage memory access violation on Monterey
- macOS thread priority management

### 6.1.5 (Jan 28, 2022)
- Accessibility framework improvements
- Non-Latin virtual key codes on macOS
- X11 compatibility
- iOS in-app purchases workflow update
- macOS windowing behaviour improvements
- MinGW-w64 compatibility
- **MPEKeyboardComponent** class added

### 6.1.6 (Feb 28, 2022)
- AU multichannel layout handling
- `JUCE_NODISCARD` on builder-pattern functions
- `DirectoryIterator` recursion options
- OpenGL 3.2 core profile unified loading
- macOS full-screen behaviour with non-native titlebars

---

## 7.0.x Series (June 2022 – April 2024)

### 7.0.0 — **"ARA, LV2 & Metal"** (Jun 21, 2022)
- **ARA SDK** support (Audio Random Access)
- **LV2 plugin support** (authoring and hosting)
- **Metal default renderer** for macOS and iOS
- New macOS/iOS rendering options
- **Hardware synchronized drawing** on Windows, macOS, and iOS
- Updated Android billing and file access APIs
- **Revamped AudioPlayHead** functionality
- Accessibility improvements

### 7.0.1 (Jul 4, 2022)
- Xcode and MSVC compiler warnings fixed
- VST3 bus configuration and channel handling improvements
- Metal layer rendering bug fixes

### 7.0.2 (Aug 15, 2022)
- Accessibility table navigation fix
- Android file access on older APIs
- Linux VST3 threading improvements
- ARA integration improvements

### 7.0.3 — **"New Threading & Graph Refactor"** (Nov 29, 2022)
- Unique machine ID added
- **New threading classes**
- Multiple OpenGL context performance
- **AudioProcessorGraph refactored**
- AudioDeviceManager sample rate handling
- Studio One drawing performance fix
- FLAC library update

### 7.0.4 (Jan 5, 2023)
- Metal device handling improvements
- **More C++17 features adopted**
- macOS and iOS input handling improvements
- Linux GUI display fix

### 7.0.5 (Jan 26, 2023)
- Windows 7 compatibility restored
- macOS dark mode notifications fix
- AudioProcessorGraph performance improvements

### 7.0.6 — **"VST3 Bundles"** (Aug 3, 2023)
- **VST3 bundles and moduleinfo.json support**
- Message box dismissal improvements
- WebView support improvements
- Updated VST3 and AAX SDKs
- Metal layer rendering fixes
- Ambisonic support improvements
- Machine ID improvements
- HighResolutionTimer implementation improvements

### 7.0.7 (Aug 23, 2023)
- macOS 14.0 deprecation fixes
- VST3 manifest generation fixes
- Metal layer rendering issue fix
- Realtime thread priority fix
- VirtualDesktopWatcher crash fix
- AUv3 bundling fix

### 7.0.8 — **"AudioWorkgroup & Xcode 15"** (Oct 19, 2023)
- **macOS/iOS AudioWorkgroup support**
- Xcode 15, macOS Sonoma, LLVM 17 compatibility
- Serialisation tools added
- VST3 manifest generation fixes
- MessageManager locking bug fix
- GCC 7 VST3 support
- SVG scaling issues fixed

### 7.0.9 — **"MIDI-CI"** (Nov 20, 2023)
- **MIDI-CI support** (Capability Inquiry)
- `enumerate` utility function
- macOS/iOS CMake signing fix

### 7.0.10 (Feb 12, 2024)
- AudioDeviceSelector device selection fixes
- Bundled Oboe version update
- Timer fixes
- Bundled FLAC update
- Socket configuration options
- **JSON::Formatter** class added
- Xcode 15.1 support
- OpenGL compatibility headers update
- **ChildProcessManager** added
- MIDI-CI fixes

### 7.0.11 (Mar 26, 2024)
- Xcode tilde path fix
- Plugin deployment and code signing fixes (Xcode)
- Empty `RectangleList` painting fix
- TreeView rendering performance

### 7.0.12 (Apr 15, 2024)
- Pro Tools timer fix
- Projucer Xcode code signing fix

---

## 8.0.x Series (June 2024 – present)

### 8.0.0 — **"Direct2D, WebView & Bundled AAX"** (Jun 12, 2024)

**Major features:**
- **Direct2D renderer** — new Windows rendering backend replacing the legacy GDI-based path
- **WebView UIs** — `juce_webview` module for embedding web content in plugins
- **Consistent Unicode support** across all platforms
- **Animation module** — `juce_animation` added
- **Bundled AAX SDK** — no longer need a separate Avid license to build AAX plugins

### 8.0.1 (Jul 29, 2024)
- Text layout fixes
- Removed source code for unsupported platforms
- Direct2D fixes
- Embedded harfbuzz update
- **More surround formats** added

### 8.0.2 — **"C++20/23"** (Sep 26, 2024)
- Direct2D large image handling fixes
- **Windows 11 rounded window corners**
- Xcode 16 compiler warning fixes
- macOS and Android GUI rendering performance
- **C++20 and C++23 support** enabled
- Windows mouse response fix
- Updated VST3 SDK to 3.7.12

### 8.0.3 (Oct 16, 2024)
- AAX SDK updated to 2.8.0
- Multiple Direct2D drawing fixes
- iOS 18 buffer size and sample rate fixes

### 8.0.4 — **"JavaScript Module Separation"** (Nov 18, 2024)
- **Simplified singleton creation**
- JavaScript and C++ interoperability fixes
- **Exact passthrough of MIDI CC timestamps**
- Runtime MIDI plugin property retrieval
- Windows ARM CMake support
- **ShapedText** improvements
- Windows DLL build fixes
- System-provided timestamps to VBlankAttachment and animations
- iOS deprecation warning fixes
- Embedded CHOC version update
- Embedded Oboe version update
- **JavaScript implementation moved to separate module**

### 8.0.5 — **"Windows ARM & VST3 Migrations"** (Jan 8, 2025)
- **Windows ARM support**
- Local notifications support
- Passthrough compiler options to juceaide
- **VST3 parameter migrations** — migrate parameter IDs across plugin versions
- Windows mouse events and window dragging fixes
- **Ranges functionality** added
- **VST2 and VST3 MIDI note names**

### 8.0.6 (Jan 10, 2025)
- Visual Studio toolchain error downgraded to warning

### 8.0.7 — **"MessageManager::callSync"** (Apr 8, 2025)
- Unicode handling and performance in TextEditor
- iOS 18 external device sample rate fix
- Many Direct2D bug fixes and performance improvements
- **`MessageManager::callSync`** — synchronous counterpart to `callAsync`
- Ableton crash fix when closing plugin window
- sscache compatibility improvements
- PopupMenu bug fixes
- Zlib update

### 8.0.8 (Jun 2, 2025)
- TextEditor layout behaviour improvements
- Text line spacing options
- Direct2D bug fixes and performance improvements
- iOS simulator buffer size fix
- MIDI CapabilityInquiry Demo moved into DemoRunner
- Default Android toolchain version update

### 8.0.9 — **"Font Features & OS 26"** (Sep 1, 2025)
- **Configurable font features** (ligatures, kerning, etc.)
- Android windowing improvements
- Text shaping improvements
- WASAPI audio buffer clearing fix
- AU hosting fix for plugins with poorly implemented parameters
- **macOS/iOS 26 support**
- iOS UIScene lifecycle on iOS 13+
- **32-bit int WAV file support**
- Linux WebView improvements
- MIDI FX AAX plugin fix for any audio channel layout
- **Accessibility navigation enabled by default for disabled components**

### 8.0.10 (Sep 15, 2025)
- Android Activity restart on theme change avoided
- PopupMenu item visibility fix
- iOS screen size detection in plugins
- LLVM 21 compiler warning fixes
- Direct2D drawing fixes
- XEmbedComponent fix

### 8.0.11 (Dec 1, 2025)
- Same fixes as 8.0.10

### 8.0.12 (Dec 16, 2025)
- **Visual Studio 2026 default** in Projucer
- Android In-App Purchases compilation fix
- MIDI device name fixes

### 8.0.13 — **"GUI Performance"** (May 19, 2026)
- **`juce_gui_basics` compile time reduced**
- Apple Icon Composer support
- **Component painting performance improvements**
- **ComponentDiagnosticsDemo** added
- **Reduced stack size of Component and ListenerList**
- macOS image tiling improvements
- **Bumped minimum Windows target version to 1607** (Anniversary Update)
- Windows rendering performance
- Windows resizing behaviour
- iOS input support (touch, mouse, pencil)
- **Linux FreeDesktop.org Trash support**

### 8.0.14 — Current (Jun 22, 2026)
- Reduced build tree depth for Windows path limits
- MIDI fixes
- Projucer macOS code signing fixes
- iOS sample rate testing fix

---

## Breaking Changes Summary

### 8.0.13 Breaking Changes

| Change | Migration |
|--------|-----------|
| `AudioProcessor::createEditor()` made private | Use `createEditorAndMakeActive()` instead |
| `AlertWindow::show()` return values changed | Update code to respect new return codes; native and non-native now consistent |
| `AudioPluginInstance::getPlatformSpecificData()` removed | Use `getVSTClient()`, `getVST3Client()`, `getAudioUnitClient()`, `getARAClient()` |
| `ExtensionsVisitor` type removed | Use `getVSTClient()`, `getVST3Client()`, etc. on AudioPluginInstance |
| `Typeface::getStringWidth()`, `getGlyphPositions()`, `getEdgeTableForGlyph()` removed | Use `GlyphArrangement::getStringWidth()` or `TextLayout::getStringWidth()`; use `getLayersForGlyph()` for glyph rendering |
| `Font::getStringWidth()`, `getStringWidthFloat()` removed | Use `GlyphArrangement::getStringWidth()` or `TextLayout::getStringWidth()` |
| `Typeface::getOutlineForGlyph()`, `getGlyphBounds()`, `getLayersForGlyph()` signatures changed (no TypefaceMetricsKind arg) | Functions now normalise to point size 1.0; use `Typeface::getMetrics()` for legacy scaling |
| `Displays::logicalToPhysical()`/`physicalToLogical()` Point overloads deprecated | Use new `Point<float>` overloads |
| `Displays::Display` — `totalArea`, `userArea`, `topLeftPhysical` deprecated | Use `logicalBounds`, `userBounds`, `physicalBounds` |
| ARA SDK updated to 2.3.0; `ARA::ChannelArrangement` replaced by `ARA::ChannelFormat` | Update ARA SDK; rename `ChannelArrangement` → `ChannelFormat` |

### 8.0.11 Breaking Changes

| Change | Migration |
|--------|-----------|
| `var::equals()` / `operator==` now deep-compares `DynamicObject` | No workaround — was previously comparing object addresses, now compares contents |
| `JUCE_ASIO` now defaults to bundled ASIO sources | Set `JUCE_ASIO_USE_EXTERNAL_SDK` to use external SDK |

### 8.0.9 Breaking Changes

| Change | Migration |
|--------|-----------|
| `TrackProperties::colour` removed | Use `colourARGB` (uint32); construct Colour with the packed ARGB value |
| `AudioPluginFormatManager::addDefaultFormats()` removed | Use non-member function `addDefaultFormatsToManager()` |
| `OpenGLFrameBuffer::readPixels()`/`writePixels()` — new `RowOrder` parameter | Pass `RowOrder` to specify top/bottom-first pixel ordering |
| Default `FocusTraverser` now navigates onto disabled components | Override `Component::createFocusTraverser()` with `SkipDisabledComponents::yes` to restore old behaviour |
| Visual Studio debug info format /Zi default | Override with `CMAKE_MSVC_DEBUG_INFORMATION_FORMAT` or Projucer settings |
| `AudioFormat::createWriterFor` — old overloads deprecated, single virtual using `AudioFormatWriterOptions` | Override new `createWriterFor(OutputStream&, AudioFormatWriterOptions)` |
| VST3ClientExtensions refactored into `VST3Interface` struct | Use `VST3Interface` types or define `JUCE_VST3_COMPATIBLE_CLASSES` |

### 8.0.7 Breaking Changes

| Change | Migration |
|--------|-----------|
| Visual Studio debug info format `/Z7` default in Projucer | Adjust debug format settings per VS configuration |

---

## Module Evolution

### New Modules

| Module | Introduced | Purpose |
|--------|-----------|---------|
| `juce_animation` | 8.0.0 | Animation framework |
| `juce_webview` | 6.0.0 (expanded in 8.0.0) | Embed web content in plugins |
| `juce_midi_ci` | 7.0.9 | MIDI Capability Inquiry |

### Major Module Changes

| Module | Version | Change |
|--------|---------|--------|
| `juce_dsp` | 6.0.0 | Complete revamp: ProcessorChain, AudioBlock, ProcessContext, new processors |
| `juce_gui_basics` | 8.0.13 | Significant compile-time and runtime performance improvements |
| `juce_opengl` | 8.0.9 | `readPixels`/`writePixels` RowOrder parameter added |

### SDK Bundles Updated

| SDK | Version Introduced | Release |
|-----|-------------------|---------|
| VST3 SDK | 3.7.12 | 8.0.2 |
| AAX SDK | 2.8.0 (bundled from 8.0.0) | 8.0.3 |
| Oboe (Android) | 1.6.1 → updated through 8.x | Various |
| Harfbuzz | Updated in 8.0.1 | 8.0.1 |
| FLAC | Updated in 7.0.10, 7.0.3 | Various |

---

## Platform Support Timeline

| Platform | Introduced | Release |
|----------|-----------|---------|
| macOS 11 / Apple Silicon arm64 | 6.0.2 | Oct 2020 |
| Windows ARM | 8.0.5 | Jan 2025 |
| macOS Monterey (12) | 6.1.0 | Aug 2021 |
| macOS Sonoma (14) | 7.0.8 | Oct 2023 |
| macOS/iOS 26 | 8.0.9 | Sep 2025 |
| iOS UIScene lifecycle | 8.0.9 | Sep 2025 |
| Windows minimum target 1607 | 8.0.13 | May 2026 |
| Linux VST3 | 6.0.0 | Jun 2020 |
| Visual Studio 2022 | 6.1.3 | Dec 2021 |
| Visual Studio 2026 | 8.0.12 | Dec 2025 |
| Xcode 15 | 7.0.8 | Oct 2023 |

---

## Language Standard Timeline

| Standard | Baseline Since | Release |
|----------|---------------|---------|
| C++11 | Pre-6.0 | — |
| C++14 | 6.1.0 | Aug 2021 |
| C++17 | 7.0.4+ | Jan 2023 |
| C++20 (supported) | 8.0.2 | Sep 2024 |
| C++23 (supported) | 8.0.2 | Sep 2024 |

---

## Quick Migration Guide: 7.x → 8.x

1. **`createEditor()` is now private** → use `createEditorAndMakeActive()`
2. **ExtensionsVisitor API removed** → use typed client accessors on AudioPluginInstance
3. **Font/Typeface width and glyph APIs removed** → use GlyphArrangement or TextLayout
4. **AAX SDK is now bundled** → remove external AAX SDK paths from build config
5. **New Direct2D renderer on Windows** → test Windows rendering; min target is now 1607
6. **ASIO defaults to bundled** → set `JUCE_ASIO_USE_EXTERNAL_SDK` if needed
7. **C++20/23 available** → can now use modern language features
8. **`AudioPluginFormatManager::addDefaultFormats()`** → use `addDefaultFormatsToManager()`
9. **`TrackProperties::colour`** → use `colourARGB` (uint32 packed ARGB)
