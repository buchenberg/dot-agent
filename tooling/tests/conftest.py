"""Shared fixtures for the dot-agent test suite.

Puts `tooling/` on sys.path so tests can import the sibling `sync` and
`validate` modules, and exposes the repo root.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLING = REPO_ROOT / "tooling"
if str(TOOLING) not in sys.path:
    sys.path.insert(0, str(TOOLING))

import sync  # noqa: E402  (tooling/sync.py)
import validate  # noqa: E402  (tooling/validate.py)


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture(scope="session")
def sync_module():
    return sync


@pytest.fixture(scope="session")
def validate_module():
    return validate
