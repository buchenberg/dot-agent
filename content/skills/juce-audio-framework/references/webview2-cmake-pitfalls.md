# JUCE WebView2 CMake Pitfalls

## JUCE_WEBVIEW2_PACKAGE_LOCATION path gotcha

When configuring CMake with `JUCE_WEBVIEW2_PACKAGE_LOCATION`, point to the **parent directory** that *contains* the `Microsoft.Web.WebView2.*` package directory — NOT the package directory itself.

### Why
JUCE's `FindWebView2.cmake` does:
```cmake
file(GLOB subdirs "${JUCE_WEBVIEW2_PACKAGE_LOCATION}/*Microsoft.Web.WebView2*")
list(GET subdirs 0 search_dir)
find_path(WebView2_root_dir build/native/include/WebView2.h HINTS ${search_dir})
```

If you point to the package directory itself, the glob matches internal files (like `*.dll` or `*.winmd` files containing "Microsoft.Web.WebView2" in their name), and `search_dir` ends up pointing to a subdirectory with no `build/native/include/` structure.

### Correct
```bash
# Package lives at:  third_party/webview2/Microsoft.Web.WebView2.1.0.4022.49/
# Point to its PARENT:
cmake -G Ninja -DJUCE_WEBVIEW2_PACKAGE_LOCATION=third_party/webview2 ..
```

### Wrong
```bash
# DO NOT point to the package directory itself:
cmake -G Ninja -DJUCE_WEBVIEW2_PACKAGE_LOCATION=third_party/webview2/Microsoft.Web.WebView2.1.0.4022.49 ..
```

### Symptom
- Configure output: `Found WebView2: WebView2_root_dir-NOTFOUND/build/native/include`
- Build failure: `fatal error C1083: Cannot open include file: 'WebView2.h': No such file or directory`

## Windows build environment (VS 2026)

For JUCE projects on Windows with Visual Studio 2026:
```powershell
# Activate DevShell, configure with Ninja, build:
powershell -NoProfile -Command "
  & 'C:\Program Files\Microsoft Visual Studio\18\Enterprise\Common7\Tools\Launch-VsDevShell.ps1' -Arch amd64
  Set-Location $buildDir
  cmake -G Ninja $cmakeFlags .. 
  ninja
"
```

Use `vswhere` to find the VS installation path:
```bash
"C:/Program Files (x86)/Microsoft Visual Studio/Installer/vswhere.exe" -latest -property installationPath
```
