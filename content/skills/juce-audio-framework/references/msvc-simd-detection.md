# Cross-Platform SIMD Detection for MSVC

## Problem

MSVC x64 does not define `__SSE2__` (a GCC/Clang macro), causing preprocessor checks like `#elif __SSE2__` to fail with "invalid integer constant expression" on Windows builds, even though SSE2 is always available on x64.

## Fix Option 1: CMake-Level (Preferred)

The cleanest approach — no C++ source changes needed. Add to your `CMakeLists.txt`:

```cmake
# MSVC x64 always supports SSE2 but doesn't define __SSE2__ like GCC/Clang
if(MSVC AND CMAKE_SIZEOF_VOID_P EQUAL 8)
  add_compile_definitions(__SSE2__)
endif()
```

This works because:
- `add_compile_definitions()` applies to all targets in the current directory and below
- `CMAKE_SIZEOF_VOID_P EQUAL 8` ensures we only add it for 64-bit builds
- MSVC's `<immintrin.h>` already includes SSE2 intrinsics, so the macro just needs to be defined

**Advantages:**
- No C++ source code changes
- Centralized fix in one place
- Doesn't clutter platform-specific headers

## Fix Option 2: C++ Preprocessor Pattern

When you need per-file control or can't modify CMake:

```cpp
// Detect SSE2 support across GCC/Clang and MSVC
#if defined(__SSE2__) || (defined(_MSC_VER) && (defined(_M_X64) || (defined(_M_IX86_FP) && _M_IX86_FP >= 2)))
  #define MY_PROJECT_SSE2 1
  #include <immintrin.h>
#elif defined(__ARM_NEON__) || defined(__ARM_NEON)
  #define MY_PROJECT_NEON 1
  #include <arm_neon.h>
#else
  static_assert(false, "No SIMD support detected");
#endif
```

## MSVC-Specific Macros

- `_M_X64` or `_M_AMD64` — Defined for 64-bit x86 builds (always has SSE2)
- `_M_IX86_FP` — For 32-bit x86 builds:
  - `0` = No SIMD
  - `1` = SSE
  - `2` = SSE2 or higher

## AVX/AVX2 Detection

```cpp
#if defined(__AVX2__) || (defined(_MSC_VER) && defined(__AVX2__))
  #define MY_PROJECT_AVX2 1
#elif defined(__AVX__) || (defined(_MSC_VER) && defined(__AVX__))
  #define MY_PROJECT_AVX 1
#endif
```

## Common Pitfalls

- **`--clean-first` wipes MSVC environment**: Running `cmake --build --clean-first` can destroy the cached MSVC toolchain state in the build directory. Always reconfigure from a VS developer prompt first:
  ```bat
  @echo off
  call "C:\Program Files\Microsoft Visual Studio\2022\Enterprise\VC\Auxiliary\Build\vcvars64.bat" >nul 2>&1
  cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
  cmake --build build --parallel
  ```

- **Tests target may fail independently**: Use `--target <specific_target>` (e.g., `VialPlugin_Standalone`) to build just what you need without blocking on unrelated test targets.

- **Don't use `#if VITAL_SSE2`** when `VITAL_SSE2` is undefined — preprocessor evaluates undefined macros as 0, causing the `#elif __SSE2__` to be checked
- **Always use `defined(MACRO)`** for existence checks before value checks

## Real-World Example

From `poly_values.h` in the Vial synthesizer — the original code failed on MSVC:

```cpp
// BROKEN (fails on MSVC x64)
#if VITAL_AVX2
  #define VITAL_AVX2 1
  static_assert(false, "AVX2 is not supported yet.");
#elif __SSE2__  // MSVC doesn't define this!
  #define VITAL_SSE2 1

// FIXED via CMake (preferred)
// Add to CMakeLists.txt: add_compile_definitions(__SSE2__)

// FIXED via C++ preprocessor (alternative)
#if defined(VITAL_AVX2) && VITAL_AVX2
  #undef VITAL_AVX2
  #define VITAL_AVX2 1
  static_assert(false, "AVX2 is not supported yet.");
#elif defined(__SSE2__) || (defined(_MSC_VER) && (defined(_M_X64) || (defined(_M_IX86_FP) && _M_IX86_FP >= 2)))
  #define VITAL_SSE2 1
```

## Related

- MSVC predefined macros: https://docs.microsoft.com/en-us/cpp/preprocessor/predefined-macros
- SIMD intrinsics header: `<immintrin.h>` (Intel), `<arm_neon.h>` (ARM)
