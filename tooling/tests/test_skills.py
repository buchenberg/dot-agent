"""Skill validation — thin wrappers around tooling/validate.check_skill."""
from __future__ import annotations

import pytest

from conftest import validate

CASES = validate.load_skills()
IDS = [c[0] for c in CASES]


@pytest.mark.parametrize("rel,path,fm,body", CASES, ids=IDS)
def test_skill_valid(rel, path, fm, body):
    errors, _ = validate.check_skill(rel, path, fm, body)
    assert not errors, f"{rel}:\n  " + "\n  ".join(errors)
