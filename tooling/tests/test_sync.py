"""Integration tests for tooling/sync.py + tooling/validate.py."""
from __future__ import annotations

import subprocess
import sys

import pytest

from conftest import REPO_ROOT, sync, validate


@pytest.mark.parametrize("content_type", list(sync.CONTENT_TYPES))
def test_load_content_succeeds(content_type):
    assert isinstance(sync.load_content(content_type), list)


def test_validate_cli_exits_zero():
    result = subprocess.run(
        [sys.executable, "tooling/validate.py"],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"validate.py failed:\n{result.stdout}\n{result.stderr}"
    )


def test_full_emit_to_tmp(tmp_path):
    original = sync.DIST_DIR
    sync.DIST_DIR = tmp_path / "dist"
    try:
        old_argv = sys.argv
        sys.argv = ["sync.py", "--clean"]
        try:
            sync.main()
        finally:
            sys.argv = old_argv
    finally:
        sync.DIST_DIR = original

    emitted = list((tmp_path / "dist").rglob("*"))
    assert any(p.is_file() for p in emitted), "full emit produced no files"


def test_canonical_tools_map_to_known_harnesses():
    for tool, mapping in sync.CANONICAL_TOOLS.items():
        assert isinstance(mapping, dict), f"CANONICAL_TOOLS['{tool}'] must be a dict"
        for harness in mapping:
            assert harness in sync.HARNESSES, (
                f"CANONICAL_TOOLS['{tool}'] references unknown harness '{harness}'"
            )


def test_shared_harnesses_subset_of_all_harnesses():
    for ct, harnesses in sync.SHARED_HARNESSES.items():
        for h in harnesses:
            assert h in sync.HARNESSES, (
                f"SHARED_HARNESSES['{ct}'] references unknown harness '{h}'"
            )


def test_validate_covers_all_content_types():
    # Sanity: validate exposes loaders for every content category.
    assert validate.load_agents()
    assert validate.load_skills()
    for cat in validate.MD_CATEGORIES:
        assert isinstance(validate.load_md(cat), list)
