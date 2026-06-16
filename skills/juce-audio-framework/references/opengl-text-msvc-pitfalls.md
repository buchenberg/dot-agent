# OpenGL Text & MSVC Build Pitfalls

Discovered during Vial synth text rendering fixes (2026-06).

## OpenGL pixel_scale Integer Truncation

When `OpenGLImageComponent` (or any custom OpenGL-rendered text component)
calculates `pixel_scale` via integer division (e.g. `width / imageWidth`),
sub-1.0 DPI scaling values truncate to **zero**, producing pixelated/blank
framebuffers.

**Always use float division:**

```cpp
// BAD — truncates to 0 when image is larger than display
int pixel_scale = jmin(getWidth() / imageWidth, getHeight() / imageHeight);

// GOOD — preserves fractional scaling
float pixel_scale = (float)jmin(getWidth(), getHeight()) / (float)std::max(imageWidth, imageHeight);
```

**Symptom:** text looks crisp on a 1:1 scale but pixelated/blurry at other DPI
settings or window sizes. The OpenGL framebuffer was being rendered at 0x0
effective scale because the int truncated.

**File:** `src/interface/look_and_feel/open_gl_image_component.cpp` in Vial.

## Root-Cause Fixes Require Removing Offset Hacks

When you fix a rendering root cause (like pixel_scale above), **search the
codebase for offset/position compensation hacks** that were added to work
around the original bug. These will now misalign text in the correct rendering
path.

**Where to look:**
- Skin/layout JSON files: hardcoded pixel offsets (e.g. `"Text Component Offset": -8.0`)
- `drawText()` calls: `+offset`, `+1`, `std::round(offset)` adjustments
- `setBounds()` centering math: `+1` padding in vertical centering

**Grep patterns after a root-cause fix:**
```
\+offset
\+ 1
std::round
y_offset
pixel_scale.*int
```

**Vial example:** After fixing pixel_scale → float, we removed:
- `default.vialskin`: `"Text Component Offset": -8.0` → `0.0`
- `text_look_and_feel.cpp`: `std::round(offset)` → `offset`
- `synth_slider.cpp`: `(getHeight() - text_height + 1) / 2` → `(getHeight() - text_height) / 2`

## MSVC x64 Doesn't Auto-Define `__SSE2__`

MSVC on x64 always supports SSE2 but doesn't define the `__SSE2__` macro
(unlike GCC/Clang). Code that `#ifdef __SSE2__` silently falls back to scalar
paths or fails to compile.

**Fix in top-level CMakeLists.txt:**
```cmake
# MSVC x64 always supports SSE2 but doesn't define __SSE2__ like GCC/Clang
if(MSVC AND CMAKE_SIZEOF_VOID_P EQUAL 8)
  add_compile_definitions(__SSE2__)
endif()
```

**Symptom:** `fatal error C1083: Cannot open include file: 'cassert'` or
similar — the build is actually failing earlier in SIMD-guarded headers
that don't compile without the SSE2 path enabled.

## `cmake --build --clean-first` Wipes MSVC Environment on Windows

On Windows, `--clean-first` can destroy the CMake cache along with build
artifacts, losing the MSVC toolchain configuration. The next build fails
with missing standard headers.

**Workaround:** reconfigure CMake from a VS developer command prompt via a
batch file:

```batch
@echo off
call "C:\Program Files\Microsoft Visual Studio\2022\Enterprise\VC\Auxiliary\Build\vcvars64.bat" >nul 2>&1
cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build build --target YourPlugin_Standalone --parallel
```

**Tip:** Build a specific target (e.g. `VialPlugin_Standalone`) to skip test
targets that may have unrelated include path issues.
