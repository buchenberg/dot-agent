#!/usr/bin/env python3
"""
validate_skills.py - Validates SKILL.md files in the skills/ directory.

Checks:
  1. File has YAML frontmatter (--- ... ---)
  2. 'name' field is present and non-empty
  3. 'name' matches the skill's directory name
  4. 'description' field is present and non-empty
  5. 'description' contains a WHEN: trigger section (warning, not error)
  6. File has a body (content after frontmatter)

Exit code 0 = all checks passed (or only warnings).
Exit code 1 = one or more errors.

Usage:
    python scripts/validate_skills.py
    python scripts/validate_skills.py --warn-as-error
    python scripts/validate_skills.py --fix          # auto-add missing 'name' field
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required.  pip install pyyaml", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"

ANSI = {
    "red":    "\033[31m",
    "yellow": "\033[33m",
    "green":  "\033[32m",
    "bold":   "\033[1m",
    "reset":  "\033[0m",
}


def color(text: str, *codes: str) -> str:
    if not sys.stdout.isatty():
        return text
    prefix = "".join(ANSI[c] for c in codes)
    return f"{prefix}{text}{ANSI['reset']}"


def parse_frontmatter(text: str):
    """Return (dict | None, body_str).  dict is None if frontmatter is missing/broken."""
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    try:
        fm = yaml.safe_load(parts[1])
        body = parts[2].lstrip("\n")
        return (fm if isinstance(fm, dict) else {}), body
    except yaml.YAMLError as exc:
        return None, text


def skill_name_from_path(skill_md: Path) -> str:
    """Derive the canonical skill name from its directory path relative to skills/."""
    rel = skill_md.parent.relative_to(SKILLS_DIR)
    # Use forward slashes for nested skills (e.g. graphics/opengl-reference)
    return str(rel).replace("\\", "/")


def validate_skill(path: Path, warn_as_error: bool, fix: bool) -> tuple[int, int]:
    """Validate a single SKILL.md. Returns (error_count, warning_count)."""
    errors: list[str] = []
    warnings: list[str] = []

    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    expected_name = skill_name_from_path(path)

    # ── Check 1: frontmatter present ──────────────────────────────────
    if fm is None:
        errors.append("missing or malformed YAML frontmatter (--- ... ---)")
        _report(path, errors, warnings, warn_as_error)
        return len(errors), len(warnings)

    # ── Check 2: 'name' present ────────────────────────────────────────
    name_val = fm.get("name", "")
    if not name_val:
        if fix:
            _apply_fix(path, text, expected_name)
            warnings.append(f"'name' was missing — auto-set to '{expected_name}'")
        else:
            errors.append(f"'name' field missing; expected '{expected_name}'")

    # ── Check 3: 'name' matches directory ─────────────────────────────
    elif str(name_val) != expected_name:
        errors.append(
            f"'name' mismatch: frontmatter has '{name_val}', "
            f"directory implies '{expected_name}'"
        )

    # ── Check 4: 'description' present ────────────────────────────────
    desc_val = fm.get("description", "")
    if not desc_val:
        errors.append("'description' field missing or empty")
    else:
        # ── Check 5: WHEN: trigger keywords ───────────────────────────
        if "WHEN:" not in str(desc_val):
            msg = "'description' has no WHEN: trigger keywords (aids routing)"
            if warn_as_error:
                errors.append(msg)
            else:
                warnings.append(msg)

    # ── Check 6: body content ─────────────────────────────────────────
    if not body.strip():
        errors.append("file has no body content after frontmatter")

    _report(path, errors, warnings, warn_as_error)
    return len(errors), len(warnings)


def _report(path: Path, errors: list[str], warnings: list[str], warn_as_error: bool) -> None:
    rel = path.relative_to(REPO_ROOT)
    if not errors and not warnings:
        print(f"  {color('OK', 'green')}  {rel}")
        return

    print(f"  {color('FAIL', 'red') if errors else color('WARN', 'yellow')}  {rel}")
    for msg in errors:
        print(f"       {color('error:', 'red', 'bold')} {msg}")
    for msg in warnings:
        print(f"       {color('warn: ', 'yellow')} {msg}")


def _apply_fix(path: Path, original_text: str, name: str) -> None:
    """Insert 'name: <name>' as the first key in the frontmatter block."""
    # Replace the opening --- with --- + name line
    fixed = re.sub(
        r"^---\n",
        f"---\nname: {name}\n",
        original_text,
        count=1,
    )
    path.write_text(fixed, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate SKILL.md files.")
    ap.add_argument(
        "--warn-as-error",
        action="store_true",
        help="Treat warnings (e.g. missing WHEN:) as errors.",
    )
    ap.add_argument(
        "--fix",
        action="store_true",
        help="Auto-insert missing 'name' field derived from directory name.",
    )
    args = ap.parse_args()

    skill_files = sorted(SKILLS_DIR.glob("**/SKILL.md"))
    if not skill_files:
        print(f"No SKILL.md files found under {SKILLS_DIR}")
        return 0

    print(f"{color('Validating', 'bold')} {len(skill_files)} skill file(s)...\n")

    total_errors = 0
    total_warnings = 0
    for sf in skill_files:
        e, w = validate_skill(sf, args.warn_as_error, args.fix)
        total_errors += e
        total_warnings += w

    print()
    if total_errors == 0 and total_warnings == 0:
        print(color("All skills are valid.", "green", "bold"))
    elif total_errors == 0:
        print(color(f"{total_warnings} warning(s), 0 errors.", "yellow", "bold"))
    else:
        print(
            color(
                f"{total_errors} error(s), {total_warnings} warning(s). "
                "Run with --fix to auto-repair missing 'name' fields.",
                "red",
                "bold",
            )
        )

    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main())
