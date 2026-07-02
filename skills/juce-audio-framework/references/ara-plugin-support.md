# ARA Plugin Support in JUCE

ARA (Audio Random Access) is an extension protocol by Celemony that allows plugins to access audio data directly from the host, enabling features like waveform display, pitch analysis, and time-stretching without real-time transfer.

## Prerequisites

- **ARA SDK 2.3.0** — download from Celemony's GitHub:

```bash
git clone --recursive --branch releases/2.3.0 https://github.com/Celemony/ARA_SDK
```

## Enabling ARA in CMake

```cmake
# Option 1: Set SDK path before adding targets
juce_set_ara_sdk_path(/path/to/ARA_SDK)

# Option 2: Global path (when building JUCE examples/extras)
# cmake -DJUCE_GLOBAL_ARA_SDK_PATH=/path/to/ARA_SDK

# Mark plugin as ARA-capable
juce_add_plugin(MyPlugin
    IS_ARA_EFFECT TRUE
    FORMATS AU VST3  # ARA extends AU and VST3 only
    # ... other options
)
```

## Adding ARA to an Existing Plugin

1. Set `IS_ARA_EFFECT TRUE` in `juce_add_plugin`
2. Implement `createARAFactory()` alongside the existing `createPluginFilter()`:

```cpp
// In your PluginProcessor.cpp
#include <juce_audio_processors/juce_audio_processors.h>

// Subclass ARADocumentControllerSpecialisation
class MyARADocumentController : public juce::ARADocumentControllerSpecialisation
{
public:
    using ARADocumentControllerSpecialisation::ARADocumentControllerSpecialisation;

    // Override ARA callbacks for audio source analysis, playback, etc.
    // See ARA SDK documentation for full API
};

// Provide the ARA factory
juce::ARAFactory* createARAFactory()
{
    return juce::ARADocumentControllerSpecialisation::createARAFactory<
        MyARADocumentController>();
}
```

## ARA Plugin Properties (CMake)

| Property | Description | Default |
|----------|-------------|---------|
| `IS_ARA_EFFECT` | Enable ARA codepaths in VST3/AU wrappers | `FALSE` |
| `ARA_FACTORY_ID` | Globally unique versioned identifier | Auto-generated from BUNDLE_ID + VERSION |
| `ARA_DOCUMENT_ARCHIVE_ID` | ID for document archives (must change if format changes) | Auto-generated |
| `ARA_ANALYSIS_TYPES` | What the plugin can analyze | None |
| `ARA_TRANSFORMATION_FLAGS` | Playback transformation capabilities | `kARAPlaybackTransformationNoChanges` |

### Analysis Types

```
kARAContentTypeNotes
kARAContentTypeTempoEntries
kARAContentTypeBarSignatures
kARAContentTypeStaticTuning
kARAContentTypeKeySignatures
kARAContentTypeSheetChords
```

### Transformation Flags

```
kARAPlaybackTransformationTimestretch
kARAPlaybackTransformationTimestretchReflectingTempo
kARAPlaybackTransformationContentBasedFadeAtTail
kARAPlaybackTransformationContentBasedFadeAtHead
```

## Building AudioPluginHost with ARA

The JUCE AudioPluginHost has basic ARA hosting support. Enable it:

```cmake
# In AudioPluginHost/CMakeLists.txt
target_compile_definitions(AudioPluginHost PRIVATE JUCE_PLUGINHOST_ARA=1)
```

ARA-capable plugins appear with an "(ARA)" suffix in the Create plugin menu. Right-click the plugin in the graph and select "Show ARA host control" to assign audio files for ARA-based access.

## Key ARA Concepts

- **Document Controller**: Manages the plugin's ARA document model (audio sources, regions, musical context)
- **Audio Source**: A reference to an audio file in the host's timeline
- **Region**: A segment of an audio source placed on the timeline
- **Musical Context**: Tempo, time signature, bar positions
- **Editor Renderer**: Reads audio data from the host for display/analysis
- **Playback Renderer**: Processes audio during playback with access to ARA data

## References

- ARA SDK documentation: `ARA_SDK/ARA_Library/html_docs/index.html`
- ARA SDK GitHub: https://github.com/Celemony/ARA_SDK
- ARAPluginDemo in JUCE examples
