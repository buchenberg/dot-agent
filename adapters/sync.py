#!/usr/bin/env python3
"""
sync.py - Master sync script for dot-agent.

Reads canonical content from top-level directories and emits native formats.
Identical output across harnesses goes to dist/shared/ (written once).
Harness-specific output goes to dist/<harness>/ (agents for everyone, .mdc for cursor).

Usage:
    python adapters/sync.py                              # Emit everything
    python adapters/sync.py --content agents             # Only agents
    python adapters/sync.py --harness claude_code        # Only Claude Code
    python adapters/sync.py --install                    # Install natively
    python adapters/sync.py --validate                   # Validate only
    python adapters/sync.py --list                       # List all content
    python adapters/sync.py --clean                      # Wipe dist/ first
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. pip install pyyaml", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
DIST_DIR = REPO_ROOT / "dist"

# ═══ CONFIGURATION ════════════════════════════════════════════════════

CONTENT_TYPES = {
    "agents":   {"dir": "agents",   "glob": "*.agent.yaml"},
    "skills":   {"dir": "skills",   "glob": "**/SKILL.md"},
    "rules":    {"dir": "rules",    "glob": "*.md"},
    "commands": {"dir": "commands", "glob": "*.md"},
    "context":  {"dir": "context",  "glob": "*.md"},
    "hooks":    {"dir": "hooks",    "glob": "*"},
}

HARNESSES = ["claude_code", "copilot", "kilo", "opencode", "hermes", "cursor"]

# For these (content_type, harness) combos, the output is identical — emitted
# once to dist/shared/ and installed from there. Everything else is per-harness.
SHARED_HARNESSES = {
    "skills":   ["claude_code", "copilot", "kilo", "opencode", "hermes"],
    "rules":    ["claude_code", "copilot", "kilo", "opencode", "hermes"],
    "commands": ["claude_code", "copilot", "kilo", "opencode", "hermes"],
    "context":  ["claude_code", "copilot", "kilo", "opencode", "hermes", "cursor"],
    "hooks":    ["claude_code", "copilot", "kilo", "opencode", "hermes", "cursor"],
}
# agents: NOT listed — every harness gets unique output

INSTALL_BASES = {
    "claude_code": Path.home() / ".claude",
    "copilot":     None,
    "kilo":        Path.home() / ".agents",
    "opencode":    Path.home() / ".config" / "opencode",
    "hermes":      Path.home() / ".agents",
    "cursor":      Path.home() / ".cursor",
}

INSTALL_SUBDIRS = {
    "agents": "", "skills": "skills", "rules": "rules",
    "commands": "commands", "context": "context", "hooks": "hooks",
}

CANONICAL_TOOLS = {
    "read_file":    {"claude_code": "Read",      "copilot": "read",      "kilo": "read"},
    "search_files": {"claude_code": "Glob",      "copilot": "search",    "kilo": "glob"},
    "write_file":   {"claude_code": "Write",     "copilot": "edit",      "kilo": "edit"},
    "patch":        {"claude_code": "Edit",      "copilot": "edit",      "kilo": "edit"},
    "terminal":     {"claude_code": "Bash",      "copilot": "bash",      "kilo": "bash"},
    "web_search":   {"claude_code": "WebSearch", "copilot": "websearch", "kilo": "websearch"},
    "web_fetch":    {"claude_code": "WebFetch",  "copilot": "webfetch",  "kilo": "webfetch"},
    "mcp":          {"claude_code": "mcp__*",    "copilot": "mcp",       "kilo": "mcp"},
    "task":         {"claude_code": "Task",      "copilot": "task",      "kilo": "task"},
    "question":     {"claude_code": None,        "copilot": "question",  "kilo": "question"},
    "plan":         {"claude_code": "Plan",      "copilot": "plan",      "kilo": "plan"},
    "todo":         {"claude_code": "TodoWrite", "copilot": None,        "kilo": "todowrite"},
}

# ═══ HELPERS ══════════════════════════════════════════════════════════

def map_tools(tools_cfg, harness):
    result = {"allow": [], "deny": []}
    for t in tools_cfg.get("allow", []):
        m = CANONICAL_TOOLS.get(t, {}).get(harness)
        if m and m not in result["allow"]:
            result["allow"].append(m)
    for t in tools_cfg.get("deny", []):
        m = CANONICAL_TOOLS.get(t, {}).get(harness)
        if m and m not in result["deny"]:
            result["deny"].append(m)
    return result

def merge_overrides(agent, harness):
    ov = agent.get("harness_overrides", {}).get(harness, {})
    merged = dict(agent)
    for k, v in ov.items():
        if k == "tools":
            mt = dict(merged.get("tools", {}))
            mt.update(v)
            merged["tools"] = mt
        else:
            merged[k] = v
    return merged

def parse_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    try:
        fm = yaml.safe_load(parts[1])
        return (fm if isinstance(fm, dict) else {}), parts[2].lstrip("\n")
    except yaml.YAMLError:
        return None, text

def wf(path, content):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return str(p)

def is_shared(ct, harness):
    """True if this content type produces identical output for this harness."""
    return harness in SHARED_HARNESSES.get(ct, [])

# ═══ LOADING ══════════════════════════════════════════════════════════

def load_content(ct):
    spec = CONTENT_TYPES[ct]
    src = REPO_ROOT / spec["dir"]
    if not src.exists():
        return []
    items = []
    for p in sorted(src.glob(spec["glob"])):
        name = p.parent.name if ct == "skills" else p.stem
        if ct == "skills" and p.parent.parent != src:
            name = str(p.parent.relative_to(src)).replace("\\", "/")
        if name == "README":
            continue
        if ct == "agents":
            with open(p, encoding="utf-8") as f:
                d = yaml.safe_load(f)
            d["_src"] = p
            items.append(d)
        elif ct == "skills":
            items.append({"name": name, "_path": p, "_dir": p.parent})
        else:
            fm, body = parse_frontmatter(p.read_text(encoding="utf-8"))
            items.append({"name": name, "frontmatter": fm or {}, "body": body, "_path": p})
    return items

# ═══ AGENT EMITTERS (each harness is genuinely different) ═════════════

def emit_agent_claude_code(agent, out):
    a = merge_overrides(agent, "claude_code")
    tools = map_tools(a.get("tools", {}), "claude_code")
    deny = f'\ndeny: "{",".join(tools["deny"])}"' if tools["deny"] else ""
    model = (a.get("model", {}).get("preference") or ["sonnet"])[0]
    content = f"---\nname: {a['name']}\ndescription: {a['description']}\nmodel: {model}{deny}\n---\n\n# {a['name']}\n\n{a['system_prompt']}\n"
    if a.get("voice"):
        content += f"\n## Voice\n\n{a['voice']}\n"
    return wf(out / f"{a['name']}.md", content)

def emit_agent_copilot(agent, out):
    a = merge_overrides(agent, "copilot")
    title = a["name"].replace("-", " ").title()
    cat = a.get("category", "general").title()
    content = f"---\nname: {cat} {title}\ndescription: {a['description']}\ndisable-model-invocation: false\n---\n\n# {title}\n\n{a['system_prompt']}\n"
    if a.get("voice"):
        content += f"\n## Voice\n\n{a['voice']}\n"
    tools = a.get("tools", {})
    if tools.get("deny"):
        content += "\n## Restrictions\n\nDo not use: " + ", ".join(f"`{t}`" for t in tools["deny"]) + ".\n"
    return wf(out / f"{a['name']}.agent.md", content)

def emit_agent_kilo(agent, out):
    a = merge_overrides(agent, "kilo")
    tools = map_tools(a.get("tools", {}), "kilo")
    modes = a.get("modes", {})
    perm = {
        "read": "allow",
        "bash": "deny" if "bash" in tools["deny"] else "allow",
        "edit": {"*": "allow"},
        "mcp": "deny" if "mcp" in tools["deny"] else "allow",
        "question": "allow" if modes.get("interactive", True) else "deny",
        "webfetch": "allow" if "webfetch" in tools["allow"] else "deny",
        "websearch": "allow" if "websearch" in tools["allow"] else "deny",
        "glob": "allow", "grep": "allow",
        "task": "allow" if modes.get("subagent", True) else "deny",
    }
    for t in tools["deny"]:
        perm["edit"][f"*{t}*"] = "deny"
    doc = {
        "name": a["name"], "prompt": a["system_prompt"],
        "description": a["description"],
        "mode": a.get("mode", "subagent" if modes.get("subagent") else "primary"),
        "options": {"displayName": a["name"].replace("-", " ").title(), "id": a["name"]},
        "permission": perm,
    }
    return wf(out / f"{a['name']}.agent.json", json.dumps(doc, indent=2))

def emit_agent_opencode(agent, out):
    a = merge_overrides(agent, "opencode")
    modes = a.get("modes", {})
    prefs = a.get("model", {}).get("preference") or ["default"]
    doc = {
        "name": a["name"], "description": a["description"],
        "prompt": a["system_prompt"],
        "mode": "subagent" if modes.get("subagent") else "primary",
        "model": prefs[0] if prefs else "default",
    }
    return wf(out / f"{a['name']}.json", json.dumps(doc, indent=2))

def emit_agent_hermes(agent, out):
    a = agent
    modes = a.get("modes", {})
    tools = a.get("tools", {})
    denied = ""
    if tools.get("deny"):
        denied = "\n**Tools denied:** " + ", ".join(f"`{t}`" for t in tools["deny"])
    content = f"# Agent: {a['name']}\n\n> {a['description']}\n\n## Persona\n\n{a['system_prompt']}\n"
    if a.get("voice"):
        content += f"\n## Voice\n\n{a['voice']}\n"
    content += f"\n## Delegation\n\nUse with `delegate_task`:\n- **role**: `leaf`\n- **context**: Include this agent's system prompt.\n\n## Capabilities\n\n- **Primary**: {modes.get('primary', False)}\n- **Subagent**: {modes.get('subagent', True)}\n- **Interactive**: {modes.get('interactive', True)}{denied}\n"
    return wf(out / f"{a['name']}.md", content)

def emit_agent_cursor(agent, out):
    a = merge_overrides(agent, "cursor")
    content = f"---\ndescription: {a['description']}\nalwaysApply: false\n---\n\n# Agent: {a['name']}\n\n{a['system_prompt']}\n"
    if a.get("voice"):
        content += f"\n## Voice\n\n{a['voice']}\n"
    return wf(out / f"{a['name']}.mdc", content)

# ═══ SHARED EMITTERS (identical output, written once) ═════════════════

def _copy_skill_dir(src_dir, dest_dir):
    dest_dir.mkdir(parents=True, exist_ok=True)
    for f in Path(src_dir).rglob("*"):
        if f.is_file():
            rel = f.relative_to(src_dir)
            tgt = dest_dir / rel
            tgt.parent.mkdir(parents=True, exist_ok=True)
            tgt.write_bytes(f.read_bytes())

def emit_skill_shared(skill, out):
    dest = out / skill["name"]
    _copy_skill_dir(skill["_dir"], dest)
    return str(dest)

def emit_md_shared(item, out, ext=".md"):
    fm = item.get("frontmatter", {})
    body = item.get("body", "")
    desc = fm.get("description", "")
    content = f"---\ndescription: {desc}\n---\n\n{body}" if desc else body
    return wf(out / f"{item['name']}{ext}", content)

# ═══ CURSOR-SPECIFIC EMITTERS ═════════════════════════════════════════

def emit_skill_cursor(skill, out):
    skill_text = skill["_path"].read_text(encoding="utf-8")
    fm, body = parse_frontmatter(skill_text)
    desc = (fm or {}).get("description", skill["name"])
    content = f"---\ndescription: {desc}\nalwaysApply: false\n---\n\n{body}"
    return wf(out / f"{skill['name']}.mdc", content)

def emit_cursor_mdc(item, out):
    fm = item.get("frontmatter", {})
    body = item.get("body", "")
    globs = fm.get("globs", [])
    glob_line = f'\nglobs: {json.dumps(globs)}' if globs else ""
    content = f"---\ndescription: {fm.get('description', item['name'])}{glob_line}\nalwaysApply: false\n---\n\n{body}"
    return wf(out / f"{item['name']}.mdc", content)

# ═══ EMITTER REGISTRY ═════════════════════════════════════════════════
# Key is (content_type, harness_or_"shared").
# "shared" emitters write once to dist/shared/<ct>/ for all shared harnesses.

EMITTERS = {
    # Agents — every harness is unique
    ("agents", "claude_code"): emit_agent_claude_code,
    ("agents", "copilot"):     emit_agent_copilot,
    ("agents", "kilo"):        emit_agent_kilo,
    ("agents", "opencode"):    emit_agent_opencode,
    ("agents", "hermes"):      emit_agent_hermes,
    ("agents", "cursor"):      emit_agent_cursor,
    # Skills — shared for 5 harnesses, .mdc for cursor
    ("skills", "shared"):      emit_skill_shared,
    ("skills", "cursor"):      emit_skill_cursor,
    # Rules — shared for 5, .mdc for cursor
    ("rules", "shared"):       lambda i, o: emit_md_shared(i, o),
    ("rules", "cursor"):       emit_cursor_mdc,
    # Commands — shared for 5, plain .md for cursor
    ("commands", "shared"):    lambda i, o: emit_md_shared(i, o),
    ("commands", "cursor"):    lambda i, o: emit_md_shared(i, o),
    # Context — shared for all 6 (identical everywhere)
    ("context", "shared"):     lambda i, o: emit_md_shared(i, o),
    # Hooks — shared for all 6
    ("hooks", "shared"):       lambda i, o: emit_md_shared(i, o),
}

# ═══ INSTALL ══════════════════════════════════════════════════════════

def _install_from(src_dir, harness, ct):
    base = INSTALL_BASES.get(harness)
    if base is None:
        return
    subdir = INSTALL_SUBDIRS.get(ct, "")
    dest = base / subdir if subdir else base
    dest.mkdir(parents=True, exist_ok=True)
    for item in Path(src_dir).rglob("*"):
        if item.is_file():
            rel = item.relative_to(src_dir)
            tgt = dest / rel
            tgt.parent.mkdir(parents=True, exist_ok=True)
            tgt.write_bytes(item.read_bytes())

def install_content(ct, harness):
    if is_shared(ct, harness):
        src = DIST_DIR / "shared" / ct
    else:
        src = DIST_DIR / harness / ct
    if not src.exists() or not any(Path(src).rglob("*")):
        return
    _install_from(src, harness, ct)

# ═══ MAIN ════════════════════════════════════════════════════════════

def main():
    p = argparse.ArgumentParser(description="Sync dot-agent content to harness formats")
    p.add_argument("--content", choices=list(CONTENT_TYPES))
    p.add_argument("--harness", choices=HARNESSES)
    p.add_argument("--install", action="store_true")
    p.add_argument("--validate", action="store_true")
    p.add_argument("--list", action="store_true")
    p.add_argument("--clean", action="store_true")
    args = p.parse_args()

    cts = [args.content] if args.content else list(CONTENT_TYPES)
    harnesses = [args.harness] if args.harness else HARNESSES

    # --list
    if args.list:
        for ct in cts:
            items = load_content(ct)
            shared = SHARED_HARNESSES.get(ct, [])
            tag = f" (shared: {', '.join(shared)})" if shared else " (per-harness)"
            print(f"{ct}/ ({len(items)} items){tag}")
            for it in items:
                d = it.get("description", it.get("frontmatter", {}).get("description", ""))
                print(f"  {it['name']:30s} {str(d)[:60]}")
        return

    # Load + validate
    print("Loading content...")
    all_loaded = {}
    errors = 0
    for ct in cts:
        items = load_content(ct)
        all_loaded[ct] = items
        if items:
            print(f"  {ct}: {len(items)} item(s)")
        for it in items:
            if ct == "agents":
                missing = [f for f in ("name", "description", "system_prompt") if not it.get(f)]
                if missing:
                    print(f"    ERROR: {it.get('name', '?')}: missing {missing}", file=sys.stderr)
                    errors += 1
    if errors:
        print(f"\n{errors} validation error(s).", file=sys.stderr)
        sys.exit(1)

    if args.validate:
        print("\nValidation complete.")
        return

    if args.clean and DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
        print("Cleaned dist/")

    # ═══ EMIT ═══
    # For each content type, figure out which harnesses need output.
    # Shared content is emitted once to dist/shared/<ct>/.
    # Per-harness content goes to dist/<harness>/<ct>/.
    print("\nEmitting...")
    for ct in cts:
        items = all_loaded.get(ct, [])
        if not items:
            continue

        shared_hs = [h for h in harnesses if is_shared(ct, h)]
        specific_hs = [h for h in harnesses if not is_shared(ct, h)]

        # Emit shared (once)
        if shared_hs:
            fn = EMITTERS.get((ct, "shared"))
            if fn:
                out_dir = DIST_DIR / "shared" / ct
                out_dir.mkdir(parents=True, exist_ok=True)
                for it in items:
                    try:
                        r = fn(it, out_dir)
                        if r:
                            print(f"  [shared:{','.join(shared_hs)}] {ct}/{it['name']}")
                    except Exception as e:
                        print(f"  [shared] {ct}/{it['name']} ERROR: {e}", file=sys.stderr)

        # Emit per-harness
        for h in specific_hs:
            fn = EMITTERS.get((ct, h))
            if not fn:
                continue
            out_dir = DIST_DIR / h / ct
            out_dir.mkdir(parents=True, exist_ok=True)
            for it in items:
                try:
                    r = fn(it, out_dir)
                    if r:
                        print(f"  [{h}] {ct}/{it['name']}")
                except Exception as e:
                    print(f"  [{h}] {ct}/{it['name']} ERROR: {e}", file=sys.stderr)

    # Install
    if args.install:
        print("\nInstalling...")
        for ct in cts:
            for h in harnesses:
                install_content(ct, h)

    print("\nDone.")

if __name__ == "__main__":
    main()
