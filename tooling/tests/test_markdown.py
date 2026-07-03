"""Markdown content validation (rules/commands/context/hooks)."""
from __future__ import annotations

import pytest

from conftest import REPO_ROOT, validate

CASES = []
for cat in validate.MD_CATEGORIES:
    for path, fm, body in validate.load_md(cat):
        CASES.append((cat, path, fm, body))

IDS = [f"{c}:{p.relative_to(REPO_ROOT).as_posix()}" for c, p, _, _ in CASES]


@pytest.mark.parametrize("cat,path,fm,body", CASES, ids=IDS)
def test_md_valid(cat, path, fm, body):
    errors, _ = validate.check_md(path, fm, body)
    assert not errors, f"{path}:\n  " + "\n  ".join(errors)


@pytest.mark.parametrize("cat", validate.MD_CATEGORIES, ids=validate.MD_CATEGORIES)
def test_content_dir_has_readme(cat):
    assert (REPO_ROOT / "content" / cat / "README.md").exists(), (
        f"content/{cat}/ must contain a README.md placeholder"
    )
