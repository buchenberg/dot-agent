# WiX Build Commands (PowerShell)

# WiX v3.14 is pre-installed on GitHub Actions Windows runners at:
# C:\Program Files (x86)\WiX Toolset v3.14\bin

$WIX = "C:\Program Files (x86)\WiX Toolset v3.14\bin"
$VERSION = "0.1.0"  # or from needs.version.outputs.new_version in GHA
$ErrorActionPreference = "Stop"

New-Item -ItemType Directory -Force -Path build\installer | Out-Null

# 1. Harvest VST3 directory tree (generates vst3.wxs fragment)
Write-Host "=== heat.exe ==="
& "$WIX\heat.exe" dir "build\VialEffects_artefacts\Release\VST3\PLUGIN_NAME.vst3" `
  -out build\installer\vst3.wxs -gg -sfrag -dr VST3DIR -cg VST3Components `
  -var var.VST3SourceDir -template fragment
if ($LASTEXITCODE -ne 0) { throw "heat failed" }

# 2. Compile .wxs -> .wixobj
Write-Host "=== candle.exe ==="
& "$WIX\candle.exe" -arch x64 -ext WixUIExtension `
  -dVST3SourceDir="build\VialEffects_artefacts\Release\VST3\PLUGIN_NAME.vst3" `
  installer\PLUGIN_NAME.wxs build\installer\vst3.wxs `
  -out build\installer\
if ($LASTEXITCODE -ne 0) { throw "candle failed" }

# 3. Link .wixobj -> .msi
Write-Host "=== light.exe ==="
& "$WIX\light.exe" -ext WixUIExtension -sval `
  build\installer\PLUGIN_NAME.wixobj build\installer\vst3.wixobj `
  -out "build\installer\PLUGIN_NAME-$VERSION-win64.msi"
if ($LASTEXITCODE -ne 0) { throw "light failed" }

Write-Host "=== Done: build\installer\PLUGIN_NAME-$VERSION-win64.msi ==="
ls build\installer\*.msi
