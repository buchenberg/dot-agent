# dot-agent

A curated, **harness-agnostic** collection of reusable content for AI coding agents — skills, agent personas, rules, commands, context docs, and hooks — with a compiler (`tooling/sync.py`) that turns it into native formats for Claude Code, GitHub Copilot, Kilo Code, OpenCode, Hermes, and Cursor.

The repo has two top-level concerns: **`content/`** (the shipped library, harness-agnostic) and **`tooling/`** (the compiler, validator, and tests that act on it).

## Content Types

| Type | Directory | What it defines |
|------|-----------|-----------------|
| **Skills** | `content/skills/` | Procedural knowledge — patterns, pitfalls, step-by-step workflows (what the agent knows) |
| **Agents** | `content/agents/` | Persona definitions — system prompt, tool permissions, model preferences (who the agent is) |
| **Rules** | `content/rules/` | Coding guidelines and repo conventions (how the agent should behave) |
| **Commands** | `content/commands/` | Slash commands and reusable prompt templates |
| **Context** | `content/context/` | Reference docs, architecture context, domain glossaries |
| **Hooks** | `content/hooks/` | Lifecycle hooks — pre-commit, post-tool-use, session start |

Each content type lives in a canonical format under `content/`. The `tooling/sync.py` script compiles everything to native harness formats in `dist/`, or installs directly to the right locations.

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
python tooling/sync.py --list

# Emit everything to dist/
python tooling/sync.py

# Emit one content type or harness
python tooling/sync.py --content agents
python tooling/sync.py --harness claude_code

# Install to native locations (~/.claude/, ~/.agents/, etc.)
python tooling/sync.py --install

# Validate all content without writing
python tooling/validate.py
```

## Philosophy

All content is **domain-agnostic** and sanitized. No company-specific class names, internal project references, or sensitive data. If content was originally born from a real project, it has been sanitized so the *technique* survives but the *domain dressing* is replaced with vanilla examples.

## Structure

```
dot-agent/
├── content/                    # The shipped library (harness-agnostic)
│   ├── skills/                 #   procedural knowledge packs
│   │   ├── <skill-name>/
│   │   │   ├── SKILL.md        #     frontmatter + markdown
│   │   │   └── references/     #     optional supporting docs
│   │   └── <category>/<skill>/ #     categorized skills (graphics/, mlops/)
│   ├── agents/                 #   canonical agent personas
│   │   ├── _schema.yaml        #     schema reference
│   │   └── <name>.agent.yaml   #     one YAML file per agent
│   ├── rules/                  #   coding conventions and guidelines
│   ├── commands/               #   slash commands / prompt templates
│   ├── context/                #   architecture and domain reference docs
│   └── hooks/                  #   lifecycle hooks
│
├── tooling/                    # Compile + validate + test (not shipped)
│   ├── sync.py                 #   compiles all content → native formats
│   ├── validate.py             #   single content validator
│   ├── templates/
│   │   └── agent-template.yaml #   blank agent template
│   └── tests/                  #   pytest suite (wrappers around validate.py)
│
├── .agent/
│   └── skills/
│       └── sanitize-skill/     # Meta-skill: generic-ify before sharing
└── README.md
```

## Skills

| Skill | Description |
|-------|-------------|
| [autofixture-xunit-dotnet](content/skills/autofixture-xunit-dotnet/) | AutoFixture + xUnit patterns — specimen builders, customizations, and AutoData extensions for .NET tests. |
| [conventional-commits](content/skills/conventional-commits/) | Conventional Commits 1.0.0 reference — commit message format, breaking-change signaling, SemVer mapping, and commitlint-ready conventions. |
| [cpp-coding-standards](content/skills/cpp-coding-standards/) | C++ coding standards based on the C++ Core Guidelines (isocpp.github.io). |
| [cpp-testing](content/skills/cpp-testing/) | GoogleTest patterns, test structure, coverage, and sanitizer configuration for C++. |
| [graphics/opengl-reference](content/skills/graphics/opengl-reference/) | OpenGL 4.x API and GLSL reference backed by the Khronos repository. |
| [juce-audio-framework](content/skills/juce-audio-framework/) | JUCE C++ audio framework — plugin development (VST/AU/AAX), DSP chains, GUI/LookAndFeel, font rendering, OpenGL, MIDI, state management. |
| [juce-changelog](content/skills/juce-changelog/) | JUCE framework changelog reference — breaking changes, new features, and deprecations across JUCE versions. |
| [mlops/vllm-ubuntu-setup](content/skills/mlops/vllm-ubuntu-setup/) | vLLM installation and configuration on Ubuntu for local LLM inference. |
| [typespec](content/skills/typespec/) | TypeSpec API definition language — models, operations, decorators, HTTP bindings, OpenAPI emission, server/client code generation. |

## Agents

Agent definitions live in `content/agents/<name>.agent.yaml` (canonical YAML) and are compiled to native harness formats via `tooling/sync.py`.

| Agent | Description |
|-------|-------------|
| [architect](content/agents/architect.agent.yaml) | Stress-test technical designs and produce implementation-ready plans. |
| [juce-developer](content/agents/juce-developer.agent.yaml) | Expert C++ DSP and JUCE developer — builds audio plugins, standalone apps, and DSP chains with modern C++ and solid testing practices. |
| [typespec-developer](content/agents/typespec-developer.agent.yaml) | Expert TypeSpec API designer — authors .tsp definitions, models, operations, interfaces, templates, and decorators for OpenAPI, JSON Schema, Protobuf, and HTTP client/server code generation. |

See `content/agents/_schema.yaml` for the full schema and `tooling/templates/agent-template.yaml` for a blank template.

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
- Release asset: `dot-agent-dist-<tag>.zip` — the full `dist/` output of `tooling/sync.py` (skills, rules, commands, context, hooks, and per-harness agents), built and uploaded by [auto-release.yml](.github/workflows/auto-release.yml) when a release is created

### Validation Tests

A pytest suite under `tooling/tests/` validates every content file. Each file is a separate parametrized case; the tests are thin wrappers around `tooling/validate.py`'s `check_*` functions, so validation logic lives in exactly one place.

```bash
pip install pytest pyyaml
python tooling/validate.py   # CLI validator
python -m pytest             # test suite
```

CI runs `tooling/validate.py` then the suite on every push/PR ([tests.yml](.github/workflows/tests.yml)).

### Changelog Automation

`CHANGELOG.md` is updated by CI via Release Please during the release PR flow.

- Config: [release-please-config.json](release-please-config.json)
- Changelog path: `CHANGELOG.md`
- Initial version source: [.release-please-manifest.json](.release-please-manifest.json)

If Actions in your repo/org cannot create PRs with `GITHUB_TOKEN`, add a PAT secret named `RELEASE_PLEASE_TOKEN` and the workflow will use it automatically.

## Contributing

1. Fork and branch.
2. Add content under the appropriate `content/` subdirectory (`skills/`, `agents/`, `rules/`, `commands/`, `context/`, or `hooks/`).
3. If adding skills or agents, run the sanitization skill against them first (or ask your agent to).
4. Validate: `python tooling/validate.py`
5. Test emission: `python tooling/sync.py`
6. Submit a PR.
