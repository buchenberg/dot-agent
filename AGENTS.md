# dot-agent

Harness-agnostic content library for AI coding agents — skills, agent personas, rules, commands, context docs, and hooks. Canonical content lives under `content/`; `tooling/` holds the compiler, validator, and tests that turn it into native harness formats in `dist/`.

## Directories

The repo is split into two top-level concerns: **`content/`** (the shipped library) and **`tooling/`** (everything that compiles, validates, and tests it).

| Path | Purpose |
|------|---------|
| `content/skills/<name>/SKILL.md` | Procedural knowledge — frontmatter `description` field is the trigger hint |
| `content/agents/*.agent.yaml` | Agent persona definitions (see `content/agents/_schema.yaml`) |
| `content/rules/*.md` | Coding guidelines and repo conventions |
| `content/commands/*.md` | Slash commands and prompt templates |
| `content/context/*.md` | Reference docs and architecture context |
| `content/hooks/*` | Lifecycle hook scripts/configs |
| `tooling/sync.py` | Compiler — canonical content → per-harness `dist/` |
| `tooling/validate.py` | Single content validator (agents, skills, markdown) |
| `tooling/templates/agent-template.yaml` | Template for new agent definitions |
| `tooling/tests/` | pytest suite — thin wrappers around `validate.py` |

## Commands

```bash
# Validate all content (single source of truth)
python tooling/validate.py

# Auto-repair missing skill 'name' fields
python tooling/validate.py --fix

# Emit everything to dist/
python tooling/sync.py

# Emit one content type or harness
python tooling/sync.py --content agents
python tooling/sync.py --harness claude_code

# Emit + install to native locations (~/.claude/, ~/.agents/, etc.)
python tooling/sync.py --install

# List all content with descriptions
python tooling/sync.py --list

# Wipe dist/ before emitting
python tooling/sync.py --clean
```

## Testing

A pytest suite under `tooling/tests/` validates every canonical content file. Each file is a separate parametrized case; the tests are thin wrappers around `tooling/validate.py`'s `check_*` functions, so validation logic lives in exactly one place.

```bash
# Install dev deps
pip install pytest pyyaml

# Run the full suite
python -m pytest

# Run one category
python -m pytest tooling/tests/test_agents.py
python -m pytest tooling/tests/test_skills.py
```

CI runs `tooling/validate.py` then the pytest suite on every push/PR (`.github/workflows/tests.yml`).

Requires PyYAML: `pip install pyyaml`

## Architecture

- All content is **domain-agnostic and sanitized**. No company-specific names, internal project references, or sensitive data.
- Content compiled from canonical to native per-harness: skills/rules/context/hooks are **shared** (identical output, written once to `dist/shared/`); agents are **per-harness** (unique output per harness).
- `dist/` is gitignored — it is generated output only.
- CI: GitHub Actions on push to `main`. Release Please (Conventional Commits) opens release PRs. Tags and GitHub Releases are created on merge. Release asset: `dot-agent-dist-<tag>.zip` packaging the full `dist/` output of `tooling/sync.py`.
- Canonical tool names: `read_file`, `search_files`, `write_file`, `patch`, `terminal`, `web_search`, `web_fetch`, `mcp`, `task`, `question`, `plan`, `todo`. Mapped per-harness by `tooling/sync.py`.

## Adding or editing content

- **New skill**: create `content/skills/<name>/SKILL.md` with YAML `description` frontmatter (triggers are comma-separated keywords after `WHEN:`) plus the markdown body. Optionally add `references/` files.
- **New agent**: create `content/agents/<name>.agent.yaml` following `content/agents/_schema.yaml` and `tooling/templates/agent-template.yaml`.
- **Rules/commands/context/hooks**: add markdown files under the matching `content/` subdirectory.
- **Sanitization required**: any content derived from a real project must be generic-ified first. Run `.agent/skills/sanitize-skill/SKILL.md` for the procedure.
- Always validate before committing: `python tooling/validate.py`

## Existing skills

- `autofixture-xunit-dotnet` — AutoFixture + xUnit patterns for .NET tests
- `conventional-commits` — Conventional Commits 1.0.0 reference
- `cpp-coding-standards` — C++ coding standards based on the C++ Core Guidelines
- `cpp-testing` — GoogleTest patterns, coverage, and sanitizer configuration
- `graphics/opengl-reference` — OpenGL 4.x API and GLSL reference
- `juce-audio-framework` — JUCE C++ audio plugin development
- `juce-changelog` — JUCE framework changelog reference
- `mlops/vllm-ubuntu-setup` — vLLM installation and configuration on Ubuntu for local LLM inference
- `typespec` — TypeSpec API definition language — models, operations, decorators, HTTP bindings, OpenAPI emission

## Existing agents

- `architect` — plan-focused agent (read-only: read/search/plan/todo/question only, no write/patch/terminal)
- `juce-developer` — expert C++ DSP and JUCE developer for audio plugins and standalone apps
- `typespec-developer` — expert TypeSpec API designer for OpenAPI, JSON Schema, and HTTP client/server generation
