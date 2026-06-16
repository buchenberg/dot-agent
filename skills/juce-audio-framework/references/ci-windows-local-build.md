# Local Windows Build (git-bash + VS + cmake + ninja)

How to build JUCE projects from git-bash on Windows when the MSVC toolchain
is not in the default PATH.

## VS detection

Use `vswhere.exe` to find the installed VS version:

```bash
"$PROGRAMFILES_X86/Microsoft Visual Studio/Installer/vswhere.exe" -latest -property installationPath
```

Common paths:
- VS 2022: `C:\Program Files\Microsoft Visual Studio\2022\Enterprise\`
- VS 2026: `C:\Program Files\Microsoft Visual Studio\18\Enterprise\`

## Build invocation

### Reliable method: PowerShell + Launch-VsDevShell.ps1

This is the most reliable method across bash/MSYS environments:

```powershell
powershell -NoProfile -Command "& '<VS_INSTALL>\Common7\Tools\Launch-VsDevShell.ps1' -Arch amd64; Set-Location <build_dir>; cmake -G Ninja <args> ..; ninja"
```

Example for VS 2026:
```bash
powershell -NoProfile -Command \
  "& 'C:\Program Files\Microsoft Visual Studio\18\Enterprise\Common7\Tools\Launch-VsDevShell.ps1' -Arch amd64; \
   Set-Location C:\Code\Personal\vial-effects\build; \
   cmake -G Ninja ..; \
   ninja"
```

To capture full build output:
```bash
powershell -NoProfile -Command "..." > build_output.txt 2>&1
```

### Alternative: cmd + vcvars64.bat

```bash
# MUST set MSYS_NO_PATHCONV to prevent bash from mangling Windows paths
MSYS_NO_PATHCONV=1 MSYS2_ARG_CONV_EXCL="*" \
  cmd //c "call \"<VS_INSTALL>\VC\Auxiliary\Build\vcvars64.bat\" > nul && cd /d <build_dir> && ninja"
```

This method is more fragile — PowerShell is preferred.

## JUCE 8 WebView2

`JUCE_WEBVIEW2_PACKAGE_LOCATION` must point to the PARENT directory containing
the `Microsoft.Web.WebView2.*` subdirectory, NOT to the package directory itself.
JUCE internally `file(GLOB)` for `*Microsoft.Web.WebView2*` inside the path.

```bash
# CORRECT:
cmake ... -DJUCE_WEBVIEW2_PACKAGE_LOCATION=C:/path/to/third_party/webview2

# WRONG:
cmake ... -DJUCE_WEBVIEW2_PACKAGE_LOCATION=C:/path/to/third_party/webview2/Microsoft.Web.WebView2.1.0.4022.49
```
