# dot-agent

Harness-agnostic content library for AI coding agents — skills, agent personas, rules, commands, context docs, and hooks. All content lives in canonical formats under repo root directories; `adapters/sync.py` compiles everything to native harness formats in `dist/`.

## Directories

| Path | Purpose |
|------|---------|
| `skills/<name>/SKILL.md` | Procedural knowledge — frontmatter `description` field is the trigger hint |
| `agents/*.agent.yaml` | Agent persona definitions (see `agents/_schema.yaml`) |
| `rules/*.md` | Coding guidelines and repo conventions |
| `commands/*.md` | Slash commands and prompt templates |
| `context/*.md` | Reference docs and architecture context |
| `hooks/*` | Lifecycle hook scripts/configs |
| `templates/agent-template.yaml` | Template for new agent definitions |

## Commands

```bash
# Validate definitions only (no output)
python adapters/sync.py --validate

# Emit everything to dist/
python adapters/sync.py

# Emit one content type or harness
python adapters/sync.py --content agents
python adapters/sync.py --harness claude_code

# Emit + install to native locations (~/.claude/, ~/.agents/, etc.)
python adapters/sync.py --install

# List all content with descriptions
python adapters/sync.py --list

# Wipe dist/ before emitting
python adapters/sync.py --clean
```

Requires PyYAML: `pip install pyyaml`

## Architecture

- All content is **domain-agnostic and sanitized**. No company-specific names, internal project references, or sensitive data.
- Content compiled from canonical to native per-harness: skills/rules/context/hooks are **shared** (identical output, written once to `dist/shared/`); agents are **per-harness** (unique output per harness).
- `dist/` is gitignored — it is generated output only.
- CI: GitHub Actions on push to `main`. Release Please (Conventional Commits) opens release PRs. Tags and GitHub Releases are created on merge. Release asset: `dot-agent-skills-<tag>.zip` mapping `skills/` → `.agent/skills/`.
- Canonical tool names: `read_file`, `search_files`, `write_file`, `patch`, `terminal`, `web_search`, `web_fetch`, `mcp`, `task`, `question`, `plan`, `todo`. Mapped per-harness by `adapters/sync.py`.

## Adding or editing content

- **New skill**: create `skills/<name>/SKILL.md` with YAML `description` frontmatter (triggers are comma-separated keywords after `WHEN:`) plus the markdown body. Optionally add `references/` files.
- **New agent**: create `agents/<name>.agent.yaml` following `agents/_schema.yaml` and `templates/agent-template.yaml`.
- **Rules/commands/context/hooks**: add markdown files under the matching directory.
- **Sanitization required**: any content derived from a real project must be generic-ified first. Run `.agent/skills/sanitize-skill/SKILL.md` for the procedure.
- Always validate before committing: `python adapters/sync.py --validate`

## Existing skills

- `autofixture-xunit-dotnet` — AutoFixture + xUnit patterns for .NET tests
- `conventional-commits` — Conventional Commits 1.0.0 reference
- `cpp-coding-standards` — C++ coding standards based on the C++ Core Guidelines
- `cpp-testing` — GoogleTest patterns, coverage, and sanitizer configuration
- `juce-audio-framework` — JUCE C++ audio plugin development
- `juce-changelog` — JUCE framework changelog reference
- `typespec` — TypeSpec API definition language — models, operations, decorators, HTTP bindings, OpenAPI emission

## Existing agents

- `architect` — plan-focused agent (read-only: read/search/plan/todo/question only, no write/patch/terminal)
- `juce-developer` — expert C++ DSP and JUCE developer for audio plugins and standalone apps
- `typespec-developer` — expert TypeSpec API designer for OpenAPI, JSON Schema, and HTTP client/server generation
