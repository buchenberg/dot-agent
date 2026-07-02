# Rules

Canonical coding guidelines, repo conventions, and guardrails that apply across all agent harnesses.

## Format

Each rule file is a markdown file with optional YAML frontmatter:

```markdown
---
description: Brief description of when this rule applies
globs: ["*.ts", "*.tsx"]          # Optional: file patterns this rule targets
---

# Rule Title

Rule content...
```

## Harness Mapping

| Harness | Native Format | Location |
|---------|--------------|----------|
| Claude Code | `.claude/rules/<name>.md` or `CLAUDE.md` | Repo root or `~/.claude/` |
| Copilot | `.github/copilot-instructions.md` (concatenated) | Repo `.github/` |
| Cursor | `.cursor/rules/<name>.mdc` | Repo `.cursor/rules/` |
| Hermes | `AGENTS.md` (concatenated) | Repo root |
| OpenCode | `.opencode/instructions.md` | Repo `.opencode/` |
| Kilo Code | `.kilo/rules/<name>.md` | Repo `.kilo/rules/` |
