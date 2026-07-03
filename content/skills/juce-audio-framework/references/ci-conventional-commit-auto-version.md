# Conventional Commit → Semver Auto-Bump (CI)

Pattern for parsing a PR title to determine semver bump type and auto-bumping
version in source files during CI.

## Bump-type determination

```bash
# Input: PR title (from github.event.pull_request.title)
# Output: major | minor | patch

if echo "$TITLE" | grep -qiE 'BREAKING[ -]CHANGE|!:'; then
  BUMP="major"
elif echo "$TITLE" | grep -qiE '^feat[\(:]'; then
  BUMP="minor"
elif echo "$TITLE" | grep -qiE '^fix[\(:]'; then
  BUMP="patch"
else
  BUMP="patch"   # default for unrecognized types
fi
```

Pattern notes:
- `^feat[\(:]` matches `feat:`, `feat(scope):` — case-insensitive
- `^fix[\(:]` matches `fix:`, `fix(scope):`
- `BREAKING[ -]CHANGE` matches `BREAKING CHANGE` or `BREAKING-CHANGE` anywhere in title
- `!:` matches the `!` before `:` in conventional commit breaking syntax (`feat!: ...`)

## Full version bump script

```bash
# Extract current version from CMakeLists.txt
OLD=$(grep -oP 'project\(PluginName VERSION \K[0-9.]+' CMakeLists.txt)

# Determine bump type (see above)
# BUMP = "major" | "minor" | "patch"

# Calculate new version
IFS='.' read -r MAJOR MINOR PATCH <<< "$OLD"
case "$BUMP" in
  major) MAJOR=$((MAJOR + 1)); MINOR=0; PATCH=0 ;;
  minor) MINOR=$((MINOR + 1)); PATCH=0 ;;
  patch) PATCH=$((PATCH + 1)) ;;
esac
NEW="${MAJOR}.${MINOR}.${PATCH}"
TAG="v${NEW}"

# Bump in source files
sed -i "s/project(PluginName VERSION ${OLD}/project(PluginName VERSION ${NEW}/" CMakeLists.txt
sed -i "s/\"version\": \"${OLD}\"/\"version\": \"${NEW}\"/" ui/package.json

# Note: on macOS, use sed -i '' instead of sed -i, or use the pattern above
# which works in bash on both platforms.

# Commit with [skip ci] to prevent workflow re-trigger
git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"
git add CMakeLists.txt ui/package.json
git commit -m "chore(release): bump version to ${NEW} [skip ci]"
git tag "${TAG}"
git push origin main --tags
```

## GitHub Actions job outputs

```yaml
version:
  runs-on: ubuntu-latest
  outputs:
    old_version: ${{ steps.ver.outputs.old_version }}
    new_version: ${{ steps.ver.outputs.new_version }}
    tag: ${{ steps.ver.outputs.tag }}
    bump: ${{ steps.ver.outputs.bump }}
  steps:
    - uses: actions/checkout@v4
    - id: bump
      run: |
        # ... bump type determination (above)
        echo "type=${BUMP}" >> "$GITHUB_OUTPUT"
    - id: ver
      run: |
        # ... version calculation (above)
        echo "old_version=${OLD}" >> "$GITHUB_OUTPUT"
        echo "new_version=${NEW}" >> "$GITHUB_OUTPUT"
        echo "tag=${TAG}" >> "$GITHUB_OUTPUT"
        echo "bump=${BUMP}" >> "$GITHUB_OUTPUT"

  # Downstream jobs reference: ${{ needs.version.outputs.new_version }}
```

## Gating

- The version-bump-and-commit step: `if: github.event.pull_request.merged == true || github.event_name == 'workflow_dispatch'`
- The release job: same gate
- Build jobs: always run (they `needs: version`; version job always runs but skips bump steps on non-merge)
- On PR open/sync: version is calculated and output, but files are not modified and no tag is created

## Manual override

For `workflow_dispatch`, provide a bump-type input:

```yaml
workflow_dispatch:
  inputs:
    bump:
      description: 'Version bump type'
      required: true
      type: choice
      options: [patch, minor, major]
      default: 'patch'
```

In the bump determination step:
```bash
if [ "${{ github.event_name }}" = "workflow_dispatch" ]; then
  echo "type=${{ inputs.bump }}" >> "$GITHUB_OUTPUT"
else
  # parse PR title...
fi
```
