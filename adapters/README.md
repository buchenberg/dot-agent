# Adapters

Convert canonical agent definitions (`agents/*.agent.yaml`) into native formats for each supported harness.

## Quick Start

```bash
# Emit all formats to dist/
python adapters/sync.py

# Emit one harness only
python adapters/sync.py --target claude_code

# Emit to dist/ AND install to native locations
python adapters/sync.py --install

# Emit one harness and install
python adapters/sync.py --target kilo --install

# Validate all agent definitions without writing
python adapters/sync.py --validate
```

## Supported Harnesses

| Adapter | Output Format | Native Install Location |
|---------|--------------|------------------------|
| `to_claude_code.py` | `.claude/agents/*.md` | `~/.claude/agents/` or repo `.claude/agents/` |
| `to_copilot.py` | `.github/agents/*.agent.md` | Repo `.github/agents/` |
| `to_kilo.py` | `~/.agents/*.agent.json` | `~/.agents/` |
| `to_opencode.py` | Agent entries in `opencode.json` | `~/.config/opencode/` |
| `to_hermes.py` | Hermes subagent context docs | `dist/hermes/<name>.md` (reference only) |

## Canonical Tool Name Mapping

Adapters translate canonical tool names to harness-specific equivalents:

| Canonical | Claude Code | Copilot | Kilo Code |
|-----------|------------|---------|-----------|
| `read_file` | `Read` | `read` | `read` |
| `search_files` | `Glob`/`Grep` | `search` | `glob`/`grep` |
| `write_file` | `Write` | `edit` | `edit` |
| `patch` | `Edit` | `edit` | `edit` |
| `terminal` | `Bash` | `bash` | `bash` |
| `web_search` | `WebSearch` | `websearch` | `websearch` |
| `web_fetch` | `WebFetch` | `webfetch` | `webfetch` |
| `mcp` | `mcp__*` | `mcp` | `mcp` |
| `task` | `Task` | `task` | `task` |
| `question` | n/a (always available) | `question` | `question` |
| `plan` | `Plan` | `plan` | `plan`/`plan_exit` |
| `todo` | `TodoWrite`/`TodoRead` | n/a | `todowrite`/`todoread` |

## Adding a New Harness Adapter

1. Create `to_<harness>.py` with a `convert(agent: dict, output_dir: str) -> str` function.
2. Register it in `sync.py`'s `ADAPTERS` dict.
3. Test with `python adapters/sync.py --target <harness> --validate`.
