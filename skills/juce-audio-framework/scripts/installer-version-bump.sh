#!/bin/bash
# Conventional commits version bump for GitHub Actions
# Usage: source this in a GHA step, or embed the logic directly.
# Assumes CMakeLists.txt has: project(ProjectName VERSION X.Y.Z)

# Determine bump type from PR title
TITLE="${{ github.event.pull_request.title }}"
if echo "$TITLE" | grep -qiE 'BREAKING[ -]CHANGE|!:'; then
  BUMP="major"
elif echo "$TITLE" | grep -qiE '^feat[\(:]'; then
  BUMP="minor"
else
  BUMP="patch"
fi

# Calculate new version
OLD=$(grep -oP 'project\(ProjectName VERSION \K[0-9.]+' CMakeLists.txt)
IFS='.' read -r MAJOR MINOR PATCH <<< "$OLD"
case "$BUMP" in
  major) MAJOR=$((MAJOR + 1)); MINOR=0; PATCH=0 ;;
  minor) MINOR=$((MINOR + 1)); PATCH=0 ;;
  patch) PATCH=$((PATCH + 1)) ;;
esac
NEW="${MAJOR}.${MINOR}.${PATCH}"
TAG="v${NEW}"

# Output for downstream jobs
echo "old_version=${OLD}" >> "$GITHUB_OUTPUT"
echo "new_version=${NEW}" >> "$GITHUB_OUTPUT"
echo "tag=${TAG}" >> "$GITHUB_OUTPUT"
echo "bump=${BUMP}" >> "$GITHUB_OUTPUT"

# Bump in source files (only on merge — gate with if:)
sed -i "s/project(ProjectName VERSION ${OLD}/project(ProjectName VERSION ${NEW}/" CMakeLists.txt
sed -i "s/\"version\": \"${OLD}\"/\"version\": \"${NEW}\"/" ui/package.json

# Commit and tag
git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"
git add CMakeLists.txt ui/package.json
git commit -m "chore(release): bump version to ${NEW} [skip ci]"
git tag "${TAG}"
git push origin main --tags
