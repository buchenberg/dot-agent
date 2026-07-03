# JUCE Linux Dependencies

JUCE requires platform-specific packages on Linux. This covers Ubuntu 22.04/24.04; package names may differ on other distributions.

## Compiler

```bash
# Clang (recommended)
sudo apt update && sudo apt install clang

# or GCC
sudo apt update && sudo apt install g++
```

## Per-Module Dependencies

### juce_audio_devices
- `libasound2-dev` — ALSA audio I/O
- `libjack-jackd2-dev` — JACK audio (disable with `JUCE_JACK=0`)

### juce_audio_processors
- `ladspa-sdk` — LADSPA plugin hosting (disable with `JUCE_PLUGINHOST_LADSPA=0`)

### juce_core
- `libcurl4-openssl-dev` — HTTP/network (disable with `JUCE_USE_CURL=0`)

### juce_graphics
- `libfontconfig1-dev` — Font discovery (disable with `JUCE_USE_FONTCONFIG=0`)
- `libfreetype-dev` — Font rendering (disable with `JUCE_USE_FREETYPE=0`)

On older systems where `libfreetype-dev` is unavailable, try `libfreetype6-dev`.

### juce_gui_basics
- `libx11-dev` — X11 display
- `libxcomposite-dev` — X11 compositing
- `libxcursor-dev` — Cursor shapes (disable with `JUCE_USE_XCURSOR=0`)
- `libxext-dev` — X11 extensions
- `libxinerama-dev` — Multi-monitor (disable with `JUCE_USE_XINERAMA=0`)
- `libxrandr-dev` — Display modes (disable with `JUCE_USE_XRANDR=0`)
- `libxrender-dev` — X11 rendering (disable with `JUCE_USE_XRENDER=0`)

### juce_gui_extra
- `libwebkit2gtk-4.1-dev` — WebView/browser (disable with `JUCE_WEB_BROWSER=0`)

On older systems, `libwebkit2gtk-4.0-dev` also works. JUCE dynamically loads whichever version is available at runtime.

### juce_opengl
- `libglu1-mesa-dev` — GLU library
- `mesa-common-dev` — OpenGL headers

## Full Install Command (Ubuntu 22/24)

```bash
sudo apt update
sudo apt install libasound2-dev libjack-jackd2-dev \
    ladspa-sdk \
    libcurl4-openssl-dev \
    libfreetype-dev libfontconfig1-dev \
    libx11-dev libxcomposite-dev libxcursor-dev libxext-dev \
    libxinerama-dev libxrandr-dev libxrender-dev \
    libwebkit2gtk-4.1-dev \
    libglu1-mesa-dev mesa-common-dev
```

## VST3 on Linux

Building VST3 plugins requires the same X11/freetype packages above, plus:

```bash
sudo apt install libx11-dev libxrandr-dev libxinerama-dev \
    libxcursor-dev libfreetype6-dev libasound2-dev \
    libcurl4-openssl-dev
```

## Headless / CI Builds

For CI environments without a display server, you can disable GUI-dependent modules:

```cmake
target_compile_definitions(MyTarget
    PUBLIC
        JUCE_WEB_BROWSER=0
        JUCE_USE_CURL=0
        JUCE_USE_FONTCONFIG=0
)
```

Or use `xvfb-run` to provide a virtual framebuffer:

```bash
xvfb-run cmake --build build
```

## Wayland

JUCE uses X11 by default. On Wayland sessions, JUCE runs through XWayland (automatic). Native Wayland support is not yet available in JUCE 8.

## References

- JUCE Linux Dependencies doc: `JUCE/docs/Linux Dependencies.md`
- JUCE Forum Linux discussions: https://forum.juce.com/c/platform-specific/linux/
