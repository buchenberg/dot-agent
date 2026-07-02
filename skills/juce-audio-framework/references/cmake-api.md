# The JUCE CMake API

Verbatin reference from https://github.com/juce-framework/JUCE/blob/master/docs/CMake%20API.md (updated Feb 2026).

## System Requirements

- All project types require CMake 3.22 or higher.
- Android targets are not currently supported.

Most system package managers have packages for CMake, but we recommend using the most recent release
from https://cmake.org/download. You should always use a CMake that's newer than your build
toolchain, so that CMake can identify your build tools and understand how to invoke them.

In addition to CMake you'll need a build toolchain for your platform, such as Xcode or MSVC.

## Getting Started

### Using `add_subdirectory`

The simplest way to include JUCE in your project is to add JUCE as a
subdirectory of your project, and to include the line `add_subdirectory(JUCE)`
in your project CMakeLists.txt. This will make the JUCE targets and helper
functions available for use by your custom targets.

### Using `find_package`

To install JUCE globally on your system, you'll need to tell CMake where to
place the installed files.

    # Go to JUCE directory
    cd /path/to/clone/JUCE
    # Configure build with library components only
    cmake -B cmake-build-install -DCMAKE_INSTALL_PREFIX=/path/to/JUCE/install
    # Run the installation
    cmake --build cmake-build-install --target install

In your project which consumes JUCE, make sure the project CMakeLists.txt contains the line
`find_package(JUCE CONFIG REQUIRED)`. This will make the JUCE modules and CMake helper functions
available for use in the rest of your build. Then, run the build like so:

    # Go to project directory
    cd /path/to/my/project
    # Configure build, passing the JUCE install path you used earlier
    cmake -B cmake-build -DCMAKE_PREFIX_PATH=/path/to/JUCE/install
    # Build the project
    cmake --build cmake-build

### Example projects

In the JUCE/examples/CMake directory, you'll find example projects for a GUI app, a console app,
and an audio plugin.

    cmake -Bbuild (-GgeneratorName) (-DJUCE_BUILD_EXTRAS=ON) (-DJUCE_BUILD_EXAMPLES=ON)

Then, to build the project:

    cmake --build build (--target targetNameFromCMakeLists) (--config Release/Debug/...)

### Building for iOS

    cmake -Bbuild-ios -GXcode -DCMAKE_SYSTEM_NAME=iOS -DCMAKE_OSX_DEPLOYMENT_TARGET=12.0

Build for simulator:

    cmake --build build-ios --target <targetName> -- -sdk iphonesimulator

Build for device (requires signing):

    cmake -Bbuild-ios -GXcode -DCMAKE_SYSTEM_NAME=iOS -DCMAKE_OSX_DEPLOYMENT_TARGET=12.0 \
        -DCMAKE_XCODE_ATTRIBUTE_CODE_SIGN_IDENTITY="iPhone Developer"
        -DCMAKE_XCODE_ATTRIBUTE_DEVELOPMENT_TEAM=<10 character id>

With provisioning updates:

    cmake --build build-ios --target <targetName> -- -allowProvisioningUpdates

#### Archiving for iOS

If "Product -> Archive" fails due to missing staticlibs:

    set_target_properties(my_static_lib_target PROPERTIES ARCHIVE_OUTPUT_DIRECTORY "./")

Note that `juce_add_binary_data` automatically sets this property.

### Building universal binaries for macOS

    -DCMAKE_OSX_ARCHITECTURES="arm64;x86_64"

### Building with Clang on Windows

Clang-cl with Visual Studio: pass `-T ClangCL` on configuration.

Clang with GNU-like command-line: pass `-DCMAKE_CXX_COMPILER=clang++` and `-DCMAKE_C_COMPILER=clang`.
May need `MSVC_RUNTIME_LIBRARY` property set.

### A note about compile definitions

Module options that would have been set in the Projucer can be set via `target_compile_definitions`.
Find module config options in module headers using the pattern:

    /** Config: NAME_OF_KEY
        Docs go here...
    */
    #ifndef NAME_OF_KEY
     #define NAME_OF_KEY ...
    #endif

Set via:

    target_compile_definitions(my_target PUBLIC NAME_OF_KEY=<value>)

> **Important:** Avoid `JucePlugin_PreferredChannelConfigurations` — its curly-brace syntax breaks on
> Ninja/Makefile generators. Use the newer buses API instead.

## API Reference

### CMake Options

Configure via `-DNAME=ON/OFF` or `set(NAME ON/OFF)` before including JUCE.

| Option | Default | Description |
|--------|---------|-------------|
| `JUCE_BUILD_EXTRAS` | OFF | Build Projucer, AudioPluginHost, etc. |
| `JUCE_BUILD_EXAMPLES` | OFF | Build DemoRunner, PIPs |
| `JUCE_ENABLE_MODULE_SOURCE_GROUPS` | OFF | Make module source files browsable in IDEs |
| `JUCE_COPY_PLUGIN_AFTER_BUILD` | OFF | Install plugins to system after building |
| `JUCE_MODULES_ONLY` | OFF | Only build modules (no apps/plugins). Disables juceaide. |
| `JUCE_WEBVIEW2_PACKAGE_LOCATION` | (default path) | Override WebView2 NuGet package location on Windows |

### Target Creation Functions

#### `juce_add_plugin` — Audio Plugin

```cmake
juce_add_plugin(<target> [KEY value]...)
```

Creates a shared-code static library `<target>` plus per-format wrapper targets.
All arguments set `JUCE_<paramName>` properties on the target.

**Identity & Versioning:**

| Key | Description |
|-----|-------------|
| `PRODUCT_NAME` | Output name (defaults to target name) |
| `VERSION` | "major.minor.bugfix" — CFBundleShortVersionString on Apple |
| `BUILD_VERSION` | Private version for App Store — CFBundleVersion |
| `BUNDLE_ID` | `com.company.product` — auto-generated from COMPANY_NAME if omitted |
| `COMPANY_NAME` | Author name (inherits from `JUCE_COMPANY_NAME` directory property) |
| `COMPANY_COPYRIGHT` | Copyright text (inherits from `JUCE_COMPANY_COPYRIGHT` directory property) |
| `COMPANY_WEBSITE` | Website URL (inherits from `JUCE_COMPANY_WEBSITE` directory property) |
| `COMPANY_EMAIL` | Contact email (inherits from `JUCE_COMPANY_EMAIL` directory property) |
| `DESCRIPTION` | Short plugin description |

**Plugin Identity:**

| Key | Default | Description |
|-----|---------|-------------|
| `PLUGIN_NAME` | `PRODUCT_NAME` | Display name in DAW |
| `PLUGIN_MANUFACTURER_CODE` | `Manu` | 4-char code; AU needs at least 1 uppercase. GarageBand: first uppercase, rest lowercase |
| `PLUGIN_CODE` | Random | 4-char code; AU needs exactly 1 uppercase. GarageBand: first uppercase, rest lowercase |

**Plugin Type Flags:**

| Key | Default | Description |
|-----|---------|-------------|
| `IS_SYNTH` | FALSE | Sets categories appropriately |
| `IS_MIDI_EFFECT` | FALSE | MIDI effect strip placement |
| `IS_ARA_EFFECT` | FALSE | Enable ARA support (adds `JucePlugin_Enable_ARA=1`) |
| `NEEDS_MIDI_INPUT` | FALSE | Provide MIDI input |
| `NEEDS_MIDI_OUTPUT` | FALSE | Provide MIDI output |
| `EDITOR_WANTS_KEYBOARD_FOCUS` | FALSE | Plugin wants keyboard focus |
| `DISABLE_AAX_BYPASS` | FALSE | Disable AAX bypass |
| `DISABLE_AAX_MULTI_MONO` | FALSE | Disable AAX multi-mono |

**Plugin Formats:**

| Key | Description |
|-----|-------------|
| `FORMATS` | Space-separated list: `Standalone Unity VST3 AU AUv3 AAX VST LV2`. VST requires `juce_set_vst2_sdk_path`. AU/AUv3 only on macOS; AUv3 only with Xcode. |

**VST2/VST3:**

| Key | Default | Description |
|-----|---------|-------------|
| `VST_NUM_MIDI_INS` | 16 | Number of MIDI inputs |
| `VST_NUM_MIDI_OUTS` | 16 | Number of MIDI outputs |
| `VST2_CATEGORY` | `kPlugCategSynth` or `kPlugCategEffect` | One of the `kPlugCateg*` constants |
| `VST3_CATEGORIES` | `Instrument Synth` or `Fx` | Space-separated: `Fx`, `Instrument`, `Delay`, `Distortion`, `EQ`, `Reverb`, `Spatial`, etc. |
| `VST3_AUTO_MANIFEST` | TRUE | POST_BUILD moduleinfo.json generation. Set FALSE if plugin needs post-build signing first. Use `juce_enable_vst3_manifest_step` later. |

**AU:**

| Key | Default | Description |
|-----|---------|-------------|
| `AU_MAIN_TYPE` | — | `kAudioUnitType_Effect`, `_Generator`, `_MusicDevice`, `_MusicEffect`, `_MIDIProcessor`, etc. |
| `AU_EXPORT_PREFIX` | Plugin name + `AU` | C++ token prefix for entry points |
| `AU_SANDBOX_SAFE` | FALSE | Add sandbox-safe plist entries |
| `SUPPRESS_AU_PLIST_RESOURCE_USAGE` | FALSE | Suppress resourceUsage key (needed for PACE-protected plugins in GarageBand) |

**AAX:**

| Key | Default | Description |
|-----|---------|-------------|
| `AAX_IDENTIFIER` | `BUNDLE_ID` | AAX bundle ID |
| `AAX_CATEGORY` | Context-dependent | Space-separated: `EQ`, `Dynamics`, `Reverb`, `Delay`, `Modulation`, `Harmonic`, `Effect`, `MIDIEffect`, etc. |

**LV2:**

| Key | Default | Description |
|-----|---------|-------------|
| `LV2URI` | Generated from COMPANY_WEBSITE and PLUGIN_NAME | Unique URI. Change on incompatible parameter/preset changes. |

**ARA:**

| Key | Default | Description |
|-----|---------|-------------|
| `ARA_FACTORY_ID` | Generated from BUNDLE_ID + VERSION | Globally unique, versioned |
| `ARA_DOCUMENT_ARCHIVE_ID` | Generated | Change on incompatible archive format changes |
| `ARA_ANALYSIS_TYPES` | None | `kARAContentTypeNotes`, `kARAContentTypeTempoEntries`, `kARAContentTypeBarSignatures`, etc. |
| `ARA_TRANSFORMATION_FLAGS` | `kARAPlaybackTransformationNoChanges` | `kARAPlaybackTransformationTimestretch`, `kARAPlaybackTransformationContentBasedFadeAtTail`, etc. |

**Install/Location:**

| Key | Default | Description |
|-----|---------|-------------|
| `COPY_PLUGIN_AFTER_BUILD` | FALSE | Install plugin to system after build. Set `JUCE_COPY_PLUGIN_AFTER_BUILD` as directory property to apply globally. |
| `VST_COPY_DIR` | System default | Custom VST2 install path |
| `VST3_COPY_DIR` | System default | Custom VST3 install path |
| `AAX_COPY_DIR` | System default | Custom AAX install path |
| `AU_COPY_DIR` | System default | Custom AU install path |
| `UNITY_COPY_DIR` | No default (must set explicitly) | Custom Unity plugin install path |

**Apple Platform Permissions & Settings:**

| Key | Default | Description |
|-----|---------|-------------|
| `MICROPHONE_PERMISSION_ENABLED` | FALSE | `NSMicrophoneUsageDescription` |
| `CAMERA_PERMISSION_ENABLED` | FALSE | `NSCameraUsageDescription` |
| `BLUETOOTH_PERMISSION_ENABLED` | FALSE | `NSBluetoothAlwaysUsageDescription` |
| `LOCAL_NETWORK_PERMISSION_ENABLED` | FALSE | `NSLocalNetworkUsageDescription` |
| `SEND_APPLE_EVENTS_PERMISSION_ENABLED` | FALSE | Allow sending Apple events |
| `PUSH_NOTIFICATIONS_ENABLED` | FALSE | App entitlements for push |
| `NETWORK_MULTICAST_ENABLED` | FALSE | IP multicast/broadcast on macOS/iOS |
| `HARDENED_RUNTIME_ENABLED` | FALSE | macOS hardened runtime (required for notarisation) |
| `HARDENED_RUNTIME_OPTIONS` | — | Space-separated `com.apple.security.*` entitlements |
| `APP_SANDBOX_ENABLED` | FALSE | macOS app sandbox |
| `APP_SANDBOX_INHERIT` | FALSE | Child processes inherit parent entitlements |
| `APP_SANDBOX_OPTIONS` | — | Space-separated `com.apple.security.*` entitlements |
| `APP_SANDBOX_FILE_ACCESS_HOME_RO` | — | Read-only paths relative to home |
| `APP_SANDBOX_FILE_ACCESS_HOME_RW` | — | Read/write paths relative to home |
| `APP_SANDBOX_FILE_ACCESS_ABS_RO` | — | Read-only absolute paths |
| `APP_SANDBOX_FILE_ACCESS_ABS_RW` | — | Read/write absolute paths |
| `APP_SANDBOX_EXCEPTION_IOKIT` | — | IOUserClient subclass access |
| `PLIST_TO_MERGE` | — | XML string to merge into Info.plist |

**iOS-Specific:**

| Key | Default | Description |
|-----|---------|-------------|
| `FILE_SHARING_ENABLED` | FALSE | iOS file sharing |
| `DOCUMENT_BROWSER_ENABLED` | FALSE | iOS document browser |
| `STATUS_BAR_HIDDEN` | FALSE | Hide status bar |
| `REQUIRES_FULL_SCREEN` | FALSE | Full screen requirement |
| `BACKGROUND_AUDIO_ENABLED` | FALSE | Background audio |
| `BACKGROUND_BLE_ENABLED` | FALSE | Background BLE |
| `APP_GROUPS_ENABLED` | FALSE | App groups entitlement |
| `APP_GROUP_IDS` | — | App group identifiers |
| `ICLOUD_PERMISSIONS_ENABLED` | FALSE | iCloud entitlement |
| `IPHONE_SCREEN_ORIENTATIONS` | Portrait, landscape left/right | `UIInterfaceOrientation*` values |
| `IPAD_SCREEN_ORIENTATIONS` | Portrait, landscape left/right | `UIInterfaceOrientation*` values |
| `TARGETED_DEVICE_FAMILY` | `1,2` | 1=iPhone, 2=iPad |
| `LAUNCH_STORYBOARD_FILE` | Default storyboard | Custom launch storyboard |
| `CUSTOM_XCASSETS_FOLDER` | — | Path to xcassets with icons/launch images |

**App/Plugin Icons:**

| Key | Description |
|-----|-------------|
| `ICON_BIG` | Path to icon image |
| `ICON_SMALL` | Path to small icon image (if only one given, used for all) |
| `ICON_COMPOSER_BUNDLE` | Apple Icon Composer bundle (Xcode 26+, takes precedence over ICON_BIG/SMALL) |

**Other:**

| Key | Default | Description |
|-----|---------|-------------|
| `NEEDS_CURL` | — | Link Curl on Linux |
| `NEEDS_WEB_BROWSER` | — | Link Webkit on Linux |
| `NEEDS_WEBVIEW2` | — | Link WebView2 on Windows |
| `NEEDS_STORE_KIT` | — | Link StoreKit on macOS |
| `NEEDS_WINDOWS_MIDI_SERVICES` | — | Enable MIDI 2.0 on Windows |
| `DOCUMENT_EXTENSIONS` | — | File associations (e.g. `wav mp3 aif`) |
| `PLUGINHOST_AU` | FALSE | Add JUCE_PLUGINHOST_AU and link macOS frameworks |
| `USE_LEGACY_COMPATIBILITY_PLUGIN_CODE` | FALSE | Compatibility with old buggy manufacturer code handling |

#### `juce_add_gui_app` / `juce_add_console_app`

```cmake
juce_add_gui_app(<target> [KEY value]...)
juce_add_console_app(<target> [KEY value]...)
```

Creates an executable target. Accepts the same KEY/value arguments as `juce_add_plugin` (minus
plugin-format-specific keys like `FORMATS`, `IS_SYNTH`, etc.).

### Binary Data & Resources

#### `juce_add_binary_data`

```cmake
juce_add_binary_data(<name>
    [HEADER_NAME ...]
    [NAMESPACE ...]
    SOURCES ...)
```

Creates a static library embedding file contents. Link with `target_link_libraries(<other> PRIVATE <name>)`.
Include via `#include <BinaryData.h>` or custom HEADER_NAME. Default NAMESPACE is `BinaryData`.

#### `juce_add_bundle_resources_directory`

```cmake
juce_add_bundle_resources_directory(<target> <folder>)
```

Copies entire directory into Apple bundle Resources directory.

### Module Management

#### `juce_add_module` / `juce_add_modules`

```cmake
juce_add_module(<path to module>)
juce_add_modules(<names of module>...)
```

Adds interface library for a JUCE module. Link with **PRIVATE visibility only** — PUBLIC causes ODR
violations.

Optional args: `INSTALL_PATH` (rel install path), `ALIAS_NAMESPACE` (e.g. `company::module_name`).

#### `juce_generate_juce_header`

```cmake
juce_generate_juce_header(<target>)
```

Generates `JuceHeader.h` with `#include` for each linked module. Disable `using namespace juce` with
`DONT_SET_USING_JUCE_NAMESPACE`. Disable ProjectInfo with `JUCE_DONT_DECLARE_PROJECTINFO`.
Optional in plain CMake projects — modules can be included directly.

### Post-Build Steps

#### `juce_enable_copy_plugin_step`

```cmake
juce_enable_copy_plugin_step(<target>)
```

Manually enable post-build copy for a plugin (alternative to `JUCE_COPY_PLUGIN_AFTER_BUILD`).
Use when extra build steps (signing, modification) must run before install. The plugin artefact
location can be queried via `JUCE_PLUGIN_ARTEFACT_FILE` on the per-format target.

#### `juce_enable_vst3_manifest_step`

```cmake
juce_enable_vst3_manifest_step(<target>)
```

Manually enable VST3 moduleinfo.json manifest generation. Use when `VST3_AUTO_MANIFEST FALSE`
and extra post-build steps must run first.

### SDK Path Configuration

```cmake
juce_set_aax_sdk_path(<absolute path>)
juce_set_vst2_sdk_path(<absolute path>)
juce_set_vst3_sdk_path(<absolute path>)
juce_set_ara_sdk_path(<absolute path>)
```

Must be called *before* adding targets that depend on these SDKs.

### PIP Support

```cmake
juce_add_pip(<header>)
```

Parses a PIP metadata block and adds build targets. Mainly for building example projects and
quick demos. Prefer `juce_add_plugin`/`juce_add_gui_app` for real projects.

### Utility Functions

```cmake
juce_disable_default_flags()
```

Sets `CMAKE_<LANG>_FLAGS_<MODE>` to empty in current directory and below. Allows custom
optimisation/debug flags without clashing with CMake defaults.

```cmake
juce_link_with_embedded_linux_subprocess(<target>)
```

Links a barebones standalone executable embedded as binary resource. Only used by `juce_gui_extra`
when `JUCE_WEB_BROWSER` is enabled. Automatically called for targets created by `juce_add_gui_app`
etc. — you don't need to call this manually.

### Recommended Targets

```cmake
target_link_libraries(myTarget PUBLIC juce::juce_recommended_warning_flags)
target_link_libraries(myTarget PUBLIC juce::juce_recommended_config_flags)
target_link_libraries(myTarget PUBLIC juce::juce_recommended_lto_flags)
```

- `juce_recommended_warning_flags` — Recommended compiler/linker warnings
- `juce_recommended_config_flags` — Optimisation and debug flags
- `juce_recommended_lto_flags` — Link-time optimisation settings

For plugins, link these with PUBLIC visibility on the shared code target so all plugin wrappers
inherit them.
