# Commands

Canonical slash commands and reusable prompt templates for agent harnesses.

## Format

Each command is a markdown file with YAML frontmatter:

```markdown
---
description: What this command does
argument-hint: "[optional argument description]"
---

# Command instructions

$ARGUMENTS
```

## Harness Mapping

| Harness | Native Format | Location |
|---------|--------------|----------|
| Claude Code | `.claude/commands/<name>.md` | `~/.claude/commands/` or repo `.claude/commands/` |
| Copilot | `.github/prompts/<name>.md` | Repo `.github/prompts/` |
| Cursor | `.cursor/commands/<name>.md` | Repo `.cursor/commands/` |
| OpenCode | `.opencode/commands/<name>.md` | Repo `.opencode/commands/` |
