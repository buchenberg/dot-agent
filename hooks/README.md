# Hooks

Canonical lifecycle hooks — scripts or configs that run automatically at specific points in an agent's workflow (pre-commit, post-tool-use, session start, etc.).

## What Belongs Here

- Pre/post commit checks
- Lint/format triggers
- Notification hooks
- Guard rails that execute as code, not as prompt instructions

## Format

Each hook is a self-contained script or config file. YAML frontmatter describes when it fires:

```yaml
---
event: pre_commit          # pre_commit, post_tool_use, session_start, etc.
harnesses: [all]           # or specific: [claude_code, kilo]
description: "Run markdownlint on all .md files"
---

# Hook implementation (script body or config JSON)
```
