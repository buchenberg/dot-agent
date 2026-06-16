# JUCE Standalone `window_size` Config — Pitfall & Recovery

## What it is

JUCE standalone apps persist their window scale to a JSON config in the platform user-data dir:

- **Windows**: `%APPDATA%\<AppName>\<AppName>.config` (e.g. `C:\Users\<user>\AppData\Roaming\vial\Vial.config`)
- **macOS**: `~/Library/Application Support/<AppName>/<AppName>.config`
- **Linux**: `~/.config/<AppName>/<AppName>.config`

File shape:

```json
{"window_size":1.8285714387893677}
```

This is JUCE's saved DPI scale multiplier, NOT a physical pixel size. It is read on app startup and applied to the base window resolution.

## Why this is a JUCE 6→8 migration pitfall

If you applied the `int pixel_scale` → `float pixel_scale` fix in `open_gl_image_component.cpp::redrawImage` (required for correct fractional DPI scaling on Windows / hi-DPI macOS):

- **Before the fix:** `pixel_scale` was truncated — a 1.5× monitor effectively rendered at 1×. The user compensated by manually resizing the window larger, and JUCE saved that compensated multiplier (e.g. `1.83`).
- **After the fix:** `pixel_scale` honors the real fractional DPI. The saved `1.83` now composes with the actual 1.5× DPI, producing a window ~2.75× the intended size — title bar above the top of the screen, controls off the right edge.

The user will report "the app opens too big / I can't see the menu / the title bar is gone" right after a successful rebuild and incorrectly attribute it to the most recent code change, when the actual culprit is stale persisted state.

## Recovery (Windows; adapt paths for macOS/Linux)

JUCE rewrites the config on **clean exit**, so order matters:

```bash
# 1. Confirm the process is running and get its PID
tasklist //FI "IMAGENAME eq <AppName>.exe"

# 2. FORCE-KILL it — don't let the user close it cleanly, that would overwrite our fix
taskkill //F //PID <pid>

# 3. Back up the config
cp "$APPDATA/<AppName>/<AppName>.config" "$APPDATA/<AppName>/<AppName>.config.bak-$(date +%Y%m%d)"

# 4. Reset to 1.0 (base scale; smallest possible window for the layout)
echo '{"window_size":1.0}' > "$APPDATA/<AppName>/<AppName>.config"
```

After relaunch, the user can resize the window to taste; JUCE will persist the new value on next clean exit.

## Why 1.0 and not the user's previous "comfortable" value

If you guess at a comfortable multiplier (e.g. 1.5×) you might still open off-screen on the user's specific monitor. `1.0` guarantees the smallest possible footprint, after which the user always has a visible resize handle to drag.

## Diagnostic check — was this actually the cause?

After resetting to `1.0`:

- **App opens visible at a small size** → confirmed: stale config was the cause. Done.
- **App still opens off-screen / too large** → the saved config was NOT the cause. The `pixel_scale` fix itself is misinterpreting the display DPI (likely passing a multiplier in the wrong unit). Revert `int → float` and apply a different fractional-scaling approach.

## Vial-specific notes

- Config: `C:\Users\gbuch\AppData\Roaming\vial\Vial.config`
- Standalone binary: `build/VialPlugin_artefacts/Release/Standalone/Vial.exe`
- The user runs Vial on a high-DPI Windows monitor; `1.8285714387893677` was the bad post-fix value observed 2026-06-12.

## When to add this check to the workflow

- Any time you touch `open_gl_image_component.cpp::redrawImage` `pixel_scale`
- After a JUCE major version bump (6 → 7 → 8)
- When a user reports "the app opens too big / off-screen / no title bar" immediately following any rendering or DPI-related code change
