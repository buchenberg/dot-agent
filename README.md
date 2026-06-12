# dot-agent

A curated collection of **generic, reusable agent skills** — procedural knowledge packs that any AI coding agent (Copilot, Claude Code, Codex, Hermes, etc.) can load to work smarter on common tasks.

## Philosophy

Skills in this repo are **domain-agnostic**. They contain the patterns, pitfalls, and step-by-step workflows that agents need — without any company-specific class names, internal project references, or sensitive data. If a skill was originally born from a real project, it has been sanitized so the *technique* survives but the *domain dressing* is replaced with vanilla examples.

## Structure

```
dot-agent/
├── skills/
│   ├── <skill-name>/
│   │   ├── SKILL.md          # The skill definition (frontmatter + markdown)
│   │   └── references/       # Optional supporting docs, templates, scripts
│   └── ...
├── .agent/
│   └── skills/
│       └── sanitize-skill/   # Meta-skill: instructions for generic-ifying skills
│           └── SKILL.md
└── README.md
```

Each skill lives in its own folder under `skills/` with a `SKILL.md` file that follows the standard frontmatter format:

```yaml
---
description: Short description and WHEN triggers for the skill.
---
```

## Skills

| Skill | Description |
|-------|-------------|
| [autofixture-xunit-dotnet](skills/autofixture-xunit-dotnet/) | AutoFixture + xUnit patterns — specimen builders, customizations, and AutoData extensions for .NET tests. |
| [conventional-commits](skills/conventional-commits/) | Conventional Commits 1.0.0 reference — commit message format, breaking-change signaling, SemVer mapping, and commitlint-ready conventions. |
| [juce-audio-framework](skills/juce-audio-framework/) | JUCE C++ audio framework — plugin development (VST/AU/AAX), DSP chains, GUI/LookAndFeel, font rendering, OpenGL, MIDI, state management. |

## Sanitization

Before a skill is added here, it must be **sanitized** — stripped of anything domain-specific or sensitive. The [.agent/skills/sanitize-skill](.agent/skills/sanitize-skill/SKILL.md) meta-skill instructs agents on how to do this. Key rules:

- **Class names** → vanilla placeholders (`RouteDispositionBuilder` → `WidgetBuilder`, `RoutingSession` → `Order`)
- **Parameter/property names** → generic equivalents (`matchUri` → `itemUri`, `routeCode` → `itemCode`)
- **Descriptions & comments** → no internal project names, company jargon, or proprietary terminology
- **Sensitive data** → no connection strings, API keys, internal URLs, tenant IDs, or PII
- **External references** → keep public blog posts, docs, and package references intact

## Using these skills

Copy a skill folder into your agent's skill directory, or reference it from your agent's configuration. Each skill's `description` frontmatter tells the agent **when** to load it — the agent matches keywords and context to decide relevance.

## Contributing

1. Fork and branch.
2. Add your skill under `skills/<skill-name>/`.
3. Run the sanitization skill against it (or ask your agent to).
4. Submit a PR.
