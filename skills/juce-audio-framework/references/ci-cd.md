# CI/CD for JUCE Plugins (GitHub Actions)

Cross-platform build + release pipeline for JUCE audio plugins.

## Trigger Pattern

Two equivalent options — pick one, never combine:

**Option 1: PR merge gate**
```yaml
on:
  pull_request:
    types: [closed]

jobs:
  build:
    if: github.event.pull_request.merged == true || github.event_name == 'workflow_dispatch'
```

**Option 2: Push to main**
```yaml
on:
  push:
    branches: [main]
```

## Conventional-Commit Version Bump

Parse merged PR title for prefix:
- `fix:` → patch
- `feat:` → minor
- `BREAKING CHANGE` or `!:` → major
- Fall back to `workflow_dispatch` with manual `choice` input

Bump `CMakeLists.txt` VERSION + tag + GitHub Release in the same job.

See `references/ci-conventional-commit-auto-version.md` for full details.

## Per-Platform Installers

| Platform | Tool | Output |
|----------|------|--------|
| Windows | WiX 4 (`wix build -arch x64`) | `.msi` |
| macOS | `pkgbuild` + `productbuild` | `.pkg` |
| Linux | `tar czf` | `.tar.gz` |

## Key Pitfalls

- **WiX 4 ≠ WiX 3**: Use `<Wix xmlns="http://wixtoolset.org/schemas/v4/wxs">` and `<Package>` (not `<Product>`)
- **Code-signing**: Install cert in runner's cert store before `signtool`. Use `azure/azure-key-vault` or `Azure/trusted-signing-action`. Never check cert into repo.
- **`COPY_PLUGIN_AFTER_BUILD`**: Set `FALSE` in CI — runner doesn't have user plugin dirs

## Files in This Skill

- `scripts/installer-version-bump.sh` — derives version from conventional-commit PR title
- `scripts/installer-wix-build.ps1` — Windows `wix build` with signing fallback
- `templates/ci-build-and-release.yml` — full GitHub Actions workflow (matrix build)
- `templates/installer-wix-template.wxs` — minimal WiX 4 template for JUCE plugin
- `templates/installer-example-VialEffects.wxs` — fully populated example

## References

- `references/ci-conventional-commit-auto-version.md` — title parsing rules, edge cases
- `references/ci-windows-local-build.md` — reproducing Windows CI locally
- WiX 4 docs: https://wixtoolset.org/docs/intro/
- Conventional Commits: https://www.conventionalcommits.org/
