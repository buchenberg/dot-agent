# dot-agent

A curated, **harness-agnostic** collection of reusable content for AI coding agents — skills, agent personas, rules, commands, context docs, and hooks — with adapters that compile everything to native formats for Claude Code, GitHub Copilot, Kilo Code, OpenCode, Hermes, and Cursor.

## Content Types

| Type | Directory | What it defines |
|------|-----------|-----------------|
| **Skills** | `skills/` | Procedural knowledge — patterns, pitfalls, step-by-step workflows (what the agent knows) |
| **Agents** | `agents/` | Persona definitions — system prompt, tool permissions, model preferences (who the agent is) |
| **Rules** | `rules/` | Coding guidelines and repo conventions (how the agent should behave) |
| **Commands** | `commands/` | Slash commands and reusable prompt templates |
| **Context** | `context/` | Reference docs, architecture context, domain glossaries |
| **Hooks** | `hooks/` | Lifecycle hooks — pre-commit, post-tool-use, session start |

Each content type lives in a canonical format at the repo root. The `adapters/sync.py` script compiles everything to native harness formats in `dist/`, or installs directly to the right locations.

## Supported Harnesses

| Harness | Agents | Skills | Rules | Commands |
|---------|--------|--------|-------|----------|
| Claude Code | `.claude/agents/*.md` | `.claude/skills/` | `.claude/rules/*.md` | `.claude/commands/*.md` |
| GitHub Copilot | `.github/agents/*.agent.md` | `.agents/skills/` | `.github/copilot-instructions.md` | `.github/prompts/*.md` |
| Kilo Code | `~/.agents/*.agent.json` | `.agent/skills/` | `.kilo/rules/*.md` | — |
| OpenCode | JSON entries | `.opencode/skills/` | `.opencode/instructions.md` | `.opencode/commands/` |
| Hermes | Subagent refs | `~/.agents/skills/` | `AGENTS.md` | — |
| Cursor | `.cursor/rules/*.mdc` | `.cursor/rules/*.mdc` | `.cursor/rules/*.mdc` | `.cursor/commands/` |

## Quick Start

```bash
# See what content exists
python adapters/sync.py --list

# Emit everything to dist/
python adapters/sync.py

# Emit one content type or harness
python adapters/sync.py --content agents
python adapters/sync.py --harness claude_code

# Install to native locations (~/.claude/, ~/.agents/, etc.)
python adapters/sync.py --install

# Validate all definitions without writing
python adapters/sync.py --validate
```

## Philosophy

All content is **domain-agnostic** and sanitized. No company-specific class names, internal project references, or sensitive data. If content was originally born from a real project, it has been sanitized so the *technique* survives but the *domain dressing* is replaced with vanilla examples.

## Structure

```
dot-agent/
├── skills/                    # Procedural knowledge packs
│   ├── <skill-name>/
│   │   ├── SKILL.md          #   frontmatter + markdown
│   │   └── references/       #   optional supporting docs
│   └── <category>/<skill>/   #   categorized skills (graphics/, mlops/)
├── agents/                    # Canonical agent personas
│   ├── _schema.yaml          # Schema reference
│   └── <name>.agent.yaml     # One YAML file per agent
├── rules/                     # Coding conventions and guidelines
├── commands/                  # Slash commands / prompt templates
├── context/                   # Architecture and domain reference docs
├── hooks/                     # Lifecycle hooks
├── adapters/                  # Sync engine
│   ├── sync.py               #   compiles all content → native formats
│   └── README.md             #   adapter docs + tool mapping
├── templates/                 # Templates for new content
├── .agent/
│   └── skills/
│       └── sanitize-skill/   # Meta-skill: generic-ify before sharing
└── README.md
```

## Skills

| Skill | Description |
|-------|-------------|
| [autofixture-xunit-dotnet](skills/autofixture-xunit-dotnet/) | AutoFixture + xUnit patterns — specimen builders, customizations, and AutoData extensions for .NET tests. |
| [conventional-commits](skills/conventional-commits/) | Conventional Commits 1.0.0 reference — commit message format, breaking-change signaling, SemVer mapping, and commitlint-ready conventions. |
| [cpp-coding-standards](skills/cpp-coding-standards/) | C++ coding standards based on the C++ Core Guidelines (isocpp.github.io). |
| [cpp-testing](skills/cpp-testing/) | GoogleTest patterns, test structure, coverage, and sanitizer configuration for C++. |
| [graphics/opengl-reference](skills/graphics/opengl-reference/) | OpenGL 4.x API and GLSL reference backed by the Khronos repository. |
| [juce-audio-framework](skills/juce-audio-framework/) | JUCE C++ audio framework — plugin development (VST/AU/AAX), DSP chains, GUI/LookAndFeel, font rendering, OpenGL, MIDI, state management. |
| [juce-changelog](skills/juce-changelog/) | JUCE framework changelog reference — breaking changes, new features, and deprecations across JUCE versions. |
| [mlops/vllm-ubuntu-setup](skills/mlops/vllm-ubuntu-setup/) | vLLM installation and configuration on Ubuntu for local LLM inference. |
| [typespec](skills/typespec/) | TypeSpec API definition language — models, operations, decorators, HTTP bindings, OpenAPI emission, server/client code generation. |

## Agents

Agent definitions live in `agents/<name>.agent.yaml` (canonical YAML) and are compiled to native harness formats via `adapters/sync.py`.

| Agent | Description |
|-------|-------------|
| [architect](agents/architect.agent.yaml) | Stress-test technical designs and produce implementation-ready plans. |
| [juce-developer](agents/juce-developer.agent.yaml) | Expert C++ DSP and JUCE developer — builds audio plugins, standalone apps, and DSP chains with modern C++ and solid testing practices. |
| [typespec-developer](agents/typespec-developer.agent.yaml) | Expert TypeSpec API designer — authors .tsp definitions, models, operations, interfaces, templates, and decorators for OpenAPI, JSON Schema, Protobuf, and HTTP client/server code generation. |

See `agents/_schema.yaml` for the full schema and `templates/agent-template.yaml` for a blank template.

## Sanitization

Before a skill is added here, it must be **sanitized** — stripped of anything domain-specific or sensitive. The [.agent/skills/sanitize-skill](.agent/skills/sanitize-skill/SKILL.md) meta-skill instructs agents on how to do this. Key rules:

- **Class names** → vanilla placeholders (`RouteDispositionBuilder` → `WidgetBuilder`, `RoutingSession` → `Order`)
- **Parameter/property names** → generic equivalents (`matchUri` → `itemUri`, `routeCode` → `itemCode`)
- **Descriptions & comments** → no internal project names, company jargon, or proprietary terminology
- **Sensitive data** → no connection strings, API keys, internal URLs, tenant IDs, or PII
- **External references** → keep public blog posts, docs, and package references intact

## Using these skills

Copy a skill folder into your agent's skill directory, or reference it from your agent's configuration. Each skill's `description` frontmatter tells the agent **when** to load it — the agent matches keywords and context to decide relevance.

## CI and Releases

This repository uses GitHub Actions plus Conventional Commits to automate versioning, tagging, releases, and dist packaging.

- Workflow: [.github/workflows/auto-release.yml](.github/workflows/auto-release.yml)
- Trigger: push to `main`
- Versioning: Conventional Commits (`feat`, `fix`, and `!` / `BREAKING CHANGE`)
- Release automation: Release Please opens/updates a release PR, then creates tag + GitHub Release when merged
- Release asset: `dot-agent-dist-<tag>.zip` — the full `dist/` output of `adapters/sync.py` (skills, rules, commands, context, hooks, and per-harness agents), built and uploaded by [auto-release.yml](.github/workflows/auto-release.yml) when a release is created

### Changelog Automation

`CHANGELOG.md` is updated by CI via Release Please during the release PR flow.

- Config: [release-please-config.json](release-please-config.json)
- Changelog path: `CHANGELOG.md`
- Initial version source: [.release-please-manifest.json](.release-please-manifest.json)

If Actions in your repo/org cannot create PRs with `GITHUB_TOKEN`, add a PAT secret named `RELEASE_PLEASE_TOKEN` and the workflow will use it automatically.

## Contributing

1. Fork and branch.
2. Add content under the appropriate directory (`skills/`, `agents/`, `rules/`, `commands/`, `context/`, or `hooks/`).
3. If adding skills or agents, run the sanitization skill against them first (or ask your agent to).
4. Validate: `python adapters/sync.py --validate`
5. Test emission: `python adapters/sync.py`
6. Submit a PR.
