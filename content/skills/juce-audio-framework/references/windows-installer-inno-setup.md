# Windows Installer (Inno Setup) for JUCE Plugins

When distributing JUCE plugins on Windows, Inno Setup 6+ integrates cleanly with CMake.

## CMake Integration

Add an installer target that builds automatically when Inno Setup is detected:

```cmake
if(WIN32)
    find_program(ISCC_EXECUTABLE iscc
        HINTS "$ENV{ProgramFiles}/Inno Setup 6"
              "$ENV{ProgramFiles\(x86\)}/Inno Setup 6")
    
    if(ISCC_EXECUTABLE)
        set(ISS_FILE "${CMAKE_CURRENT_SOURCE_DIR}/installer/Plugin.iss")
        add_custom_target(installer ALL
            COMMENT "Building Windows installer..."
            COMMAND "${ISCC_EXECUTABLE}"
                    "/DConfiguration=$<CONFIG>"
                    "/O${CMAKE_BINARY_DIR}/installer/"
                    "${ISS_FILE}"
            DEPENDS MyPlugin
            SOURCES "${ISS_FILE}"
        )
    else()
        message(STATUS "Inno Setup not found — installer target disabled.")
    endif()
endif()
```

## WebView2 NuGet Packaging

JUCE's `NEEDS_WEBVIEW2 TRUE` requires the WebView2 NuGet package:

- Extract to a project-local `third_party/webview2/` folder (not a hardcoded external path).
- Pass to CMake: `-DJUCE_WEBVIEW2_PACKAGE_LOCATION=third_party/webview2`
- The folder must contain a `Microsoft.Web.WebView2.<version>/` subfolder.
- Document the default location in README so users know where to place it.

## Pitfalls

### BYPRODUCTS with globs
Do NOT use glob patterns in `BYPRODUCTS` (e.g., `VialEffects-*-win64.exe`). CMake requires literal file paths, and Ninja generator will fail. For custom targets, BYPRODUCTS is optional — omit it rather than use a wildcard.

### AppId GUID
Generate a **real GUID** for `AppId` (use `uuidgen` or online generator). Placeholder GUIDs like `A1B2C3D4-...` cause install/uninstall conflicts in Windows Add/Remove Programs when multiple products share the same ID.

### Hardcoded paths
Use environment variables (`$ENV{ProgramFiles}`) instead of hardcoded `C:/Program Files` in CMake hints. Inno Setup 6 on 64-bit Windows installs to `Program Files` (not x86), so the env var covers both cases.

### VST3 installation path
Use `{commoncf64}\VST3\` for system-wide 64-bit VST3 installation. This resolves to `C:\Program Files\Common Files\VST3\` on most systems.

### Architecture
Set `ArchitecturesInstallIn64BitMode=x64compatible` for 64-bit plugins. Required for proper installation on 64-bit Windows.

## Inno Setup Script Template

```iss
; Inno Setup script for JUCE plugin
; Build with: iscc installer\Plugin.iss
;   (or `iscc /DConfiguration=Release installer\Plugin.iss`)

#ifndef Configuration
  #define Configuration "Debug"
#endif

#define AppName        "Plugin Name"
#define AppPublisher   "Company"
#define AppURL         "https://example.com"
#define AppVersion     GetVersionNumbersString("..\build\*_artefacts\" + Configuration + "\Standalone\Plugin.exe")

[Setup]
AppId={{GENERATE-REAL-GUID-HERE}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher={#AppPublisher}
AppPublisherURL={#AppURL}
DefaultDirName={autopf}\{#AppPublisher}\{#AppName}
DefaultGroupName={#AppPublisher}\{#AppName}
DisableProgramGroupPage=auto
OutputDir=..\build\installer
OutputBaseFilename=Plugin-{#AppVersion}-win64
Compression=lzma2/ultra64
SolidCompression=yes
WizardStyle=modern
ArchitecturesInstallIn64BitMode=x64compatible
UninstallDisplayName={#AppName}
UninstallDisplayIcon={app}\Plugin.exe
LicenseFile=..\LICENSE

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Types]
Name: "full";       Description: "Full installation (VST3 + Standalone)"
Name: "vst3";       Description: "VST3 plugin only"
Name: "standalone"; Description: "Standalone application only"
Name: "custom";     Description: "Custom"; Flags: iscustom

[Components]
Name: "vst3";       Description: "VST3 Plugin (64-bit)"; Types: full vst3 custom; Flags: disablenouninstallwarning
Name: "standalone"; Description: "Standalone Application"; Types: full standalone custom

[Files]
; VST3 Plugin (folder bundle)
Source: "..\build\*_artefacts\{#Configuration}\VST3\Plugin.vst3\*"; \
    DestDir: "{commoncf64}\VST3\Plugin.vst3"; \
    Components: vst3; Flags: ignoreversion recursesubdirs createallsubdirs

; Standalone executable
Source: "..\build\*_artefacts\{#Configuration}\Standalone\Plugin.exe"; \
    DestDir: "{app}"; Components: standalone; Flags: ignoreversion

; License
Source: "..\LICENSE"; DestDir: "{app}"; Components: standalone; \
    Flags: ignoreversion; DestName: "LICENSE.txt"

[Icons]
Name: "{group}\{#AppName}"; Filename: "{app}\Plugin.exe"; Components: standalone
Name: "{group}\Uninstall {#AppName}"; Filename: "{uninstallexe}"; Components: standalone
Name: "{group}\License"; Filename: "{app}\LICENSE.txt"; Components: standalone

[Run]
Filename: "{app}\Plugin.exe"; Description: "Launch {#AppName}"; \
    Flags: nowait postinstall skipifsilent; Components: standalone
```

## Build Script (batch)

For users who prefer a one-click build:

```bat
@echo off
REM Run from "x64 Native Tools Command Prompt for VS 2022"
setlocal

REM Set WEBVIEW2_DIR via environment variable or use default
if "%WEBVIEW2_DIR%"=="" set "WEBVIEW2_DIR=%~dp0third_party\webview2"
set "BUILD_DIR=build"
set "BUILD_TYPE=Release"

echo ===== Building web UI =====
cd /d "%~dp0ui"
call npm install && call npm run build
if %ERRORLEVEL% NEQ 0 (echo ERROR: UI build failed && exit /b 1)

echo ===== Configuring CMake =====
cd /d "%~dp0"
cmake -B %BUILD_DIR% -G Ninja -DCMAKE_BUILD_TYPE=%BUILD_TYPE% ^
      -DJUCE_WEBVIEW2_PACKAGE_LOCATION=%WEBVIEW2_DIR%
if %ERRORLEVEL% NEQ 0 (echo ERROR: CMake configure failed && exit /b 1)

echo ===== Building plugin + installer =====
cmake --build %BUILD_DIR%
if %ERRORLEVEL% NEQ 0 (echo ERROR: Build failed && exit /b 1)

echo ===== Done! =====
echo Installer: %BUILD_DIR%\installer\Plugin-*-win64.exe
endlocal
```

## Verification

After building the installer:
1. Run the `.exe` and verify component selection works (VST3 only, Standalone only, Full).
2. Check VST3 installs to `C:\Program Files\Common Files\VST3\Plugin.vst3\`.
3. Check Standalone installs to `Program Files\Company\Plugin\`.
4. Verify uninstall removes all files and registry entries.
5. Test upgrade path: install v1, then install v2 over it — should replace files cleanly.
