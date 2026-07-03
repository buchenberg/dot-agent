#!/usr/bin/env python3
"""
validate.py - Single source of truth for content validation.

Validates every canonical content file:
  - content/agents/*.agent.yaml   (schema, tools, harness overrides, ...)
  - content/skills/**/SKILL.md    (frontmatter, name, description, body)
  - content/{rules,commands,context,hooks}/*.md  (frontmatter, body)

Exposes per-file check_* functions returning (errors, warnings) so the pytest
suite can assert without duplicating logic.

Usage:
    python tooling/validate.py                # validate everything
    python tooling/validate.py --warn-as-error
    python tooling/validate.py --fix          # auto-repair missing skill 'name'
    python tooling/validate.py --content skills
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

# Reuse the compiler's parser + config so there is one definition of truth.
_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))
import sync  # noqa: E402  (sibling module: tooling/sync.py)

REPO_ROOT = _HERE.parent
CONTENT_ROOT = REPO_ROOT / "content"

VALID_TOOLS = set(sync.CANONICAL_TOOLS) | {"skill", "lsp"}
VALID_HARNESSES = set(sync.HARNESSES)
REQUIRED_AGENT_FIELDS = ("name", "description", "system_prompt")
KEBAB_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+")

MD_CATEGORIES = ("rules", "commands", "context", "hooks")


# ═══════════════════════════════════════════════════════════════════════
# Loaders — each returns a list of lightweight records.
# ═══════════════════════════════════════════════════════════════════════

def load_agents():
    out = []
    d = CONTENT_ROOT / "agents"
    for p in sorted(d.glob("*.agent.yaml")):
        if p.name == "_schema.yaml":
            continue
        with open(p, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        out.append((p, data if isinstance(data, dict) else {}))
    return out


def load_skills():
    out = []
    d = CONTENT_ROOT / "skills"
    for p in sorted(d.rglob("SKILL.md")):
        rel = p.parent.relative_to(d).as_posix()
        fm, body = sync.parse_frontmatter(p.read_text(encoding="utf-8"))
        out.append((rel, p, fm or {}, body))
    return out


def load_md(category):
    out = []
    d = CONTENT_ROOT / category
    if not d.exists():
        return out
    for p in sorted(d.rglob("*.md")):
        if p.stem == "README":
            continue
        fm, body = sync.parse_frontmatter(p.read_text(encoding="utf-8"))
        out.append((p, fm or {}, body))
    return out


# ═══════════════════════════════════════════════════════════════════════
# Checkers — return (errors: list[str], warnings: list[str]).
# ═══════════════════════════════════════════════════════════════════════

def check_agent(path: Path, agent: dict, warn_as_error: bool = False):
    errors, warnings = [], []
    name = path.name.removesuffix(".agent.yaml")

    missing = [f for f in REQUIRED_AGENT_FIELDS if not agent.get(f)]
    if missing:
        errors.append(f"missing required fields {missing}")

    if agent.get("name") and not KEBAB_RE.match(str(agent["name"])):
        errors.append(f"name '{agent['name']}' must be kebab-case")
    if agent.get("name") and agent["name"] != name:
        errors.append(f"name '{agent.get('name')}' should match filename '{name}'")

    for f in REQUIRED_AGENT_FIELDS:
        v = agent.get(f)
        if v is not None and not (isinstance(v, str) and v.strip()):
            errors.append(f"field '{f}' must be a non-empty string")

    tools = agent.get("tools") or {}
    for key in ("allow", "deny"):
        for t in (tools.get(key) or []):
            if t not in VALID_TOOLS:
                errors.append(f"unknown tool '{t}' in tools.{key}; valid: {sorted(VALID_TOOLS)}")

    for h in (agent.get("harness_overrides") or {}):
        if h not in VALID_HARNESSES:
            errors.append(f"unknown harness '{h}' in harness_overrides; valid: {sorted(VALID_HARNESSES)}")

    model = agent.get("model") or {}
    prefs = model.get("preference")
    if prefs is not None and not (isinstance(prefs, list) and prefs):
        errors.append("model.preference must be a non-empty list")

    for k, v in (agent.get("modes") or {}).items():
        if not isinstance(v, bool):
            errors.append(f"modes.{k} must be boolean, got {v!r}")

    version = agent.get("version")
    if version and not SEMVER_RE.match(str(version)):
        errors.append(f"version '{version}' should look like semver (x.y.z)")

    return errors, warnings


def check_skill(rel: str, path: Path, fm: dict, body: str, warn_as_error: bool = False, fix: bool = False):
    errors, warnings = [], []

    if not fm:
        errors.append("missing or malformed YAML frontmatter (--- ... ---)")
        return errors, warnings

    name_val = fm.get("name", "")
    if not name_val:
        if fix:
            _fix_skill_name(path, rel)
            warnings.append(f"'name' was missing — auto-set to '{rel}'")
        else:
            errors.append(f"'name' field missing; expected '{rel}'")
    elif str(name_val) != rel:
        errors.append(f"'name' mismatch: frontmatter has '{name_val}', directory implies '{rel}'")

    desc = fm.get("description", "")
    if not desc:
        errors.append("'description' field missing or empty")
    elif "WHEN:" not in str(desc):
        msg = "'description' has no WHEN: trigger keywords (aids routing)"
        (errors if warn_as_error else warnings).append(msg)

    if not body.strip():
        errors.append("file has no body content after frontmatter")
    elif not any(ln.lstrip().startswith("#") for ln in body.splitlines()):
        warnings.append("body has no Markdown heading")

    return errors, warnings


def check_md(path: Path, fm: dict, body: str, warn_as_error: bool = False):
    errors, warnings = [], []
    text = path.read_text(encoding="utf-8")
    if text.startswith("---") and not isinstance(fm, dict):
        errors.append("frontmatter must parse as a YAML mapping")
    if not body.strip():
        errors.append("file body must not be empty")
    return errors, warnings


def _fix_skill_name(path: Path, name: str) -> None:
    fixed = re.sub(r"^---\n", f"---\nname: {name}\n", path.read_text(encoding="utf-8"), count=1)
    path.write_text(fixed, encoding="utf-8")


# ═══════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════

def _run(warn_as_error: bool, fix: bool, only: str | None) -> int:
    total_e = total_w = 0

    if only in (None, "agents"):
        for path, agent in load_agents():
            e, w = check_agent(path, agent, warn_as_error)
            total_e += len(e); total_w += len(w)
            _report(path, e, w)

    if only in (None, "skills"):
        for rel, path, fm, body in load_skills():
            e, w = check_skill(rel, path, fm, body, warn_as_error, fix)
            total_e += len(e); total_w += len(w)
            _report(path, e, w)

    if only in (None, "md"):
        for cat in MD_CATEGORIES:
            for path, fm, body in load_md(cat):
                e, w = check_md(path, fm, body, warn_as_error)
                total_e += len(e); total_w += len(w)
                _report(path, e, w)

    if total_e == 0 and total_w == 0:
        print("All content is valid.")
    elif total_e == 0:
        print(f"{total_w} warning(s), 0 errors.")
    else:
        print(f"{total_e} error(s), {total_w} warning(s).", file=sys.stderr)
    return 1 if total_e else 0


def _report(path: Path, errors, warnings) -> None:
    rel = path.relative_to(REPO_ROOT)
    if not errors and not warnings:
        return
    tag = "FAIL" if errors else "WARN"
    print(f"  {tag}  {rel}")
    for m in errors:
        print(f"       error: {m}")
    for m in warnings:
        print(f"       warn:  {m}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate dot-agent content.")
    ap.add_argument("--warn-as-error", action="store_true")
    ap.add_argument("--fix", action="store_true", help="Auto-insert missing skill 'name' fields.")
    ap.add_argument("--content", choices=["agents", "skills", "md"])
    args = ap.parse_args()
    return _run(args.warn_as_error, args.fix, args.content)


if __name__ == "__main__":
    sys.exit(main())
