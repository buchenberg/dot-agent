"""Agent validation — thin wrappers around tooling/validate.check_agent.

Each agent file is a separate parametrized case; failure names the exact file
and the specific check that failed.
"""
from __future__ import annotations

import pytest

from conftest import validate

CASES = validate.load_agents()
IDS = [p.name.removesuffix(".agent.yaml") for p, _ in CASES]


@pytest.mark.parametrize("path,agent", CASES, ids=IDS)
def test_agent_valid(path, agent):
    errors, _ = validate.check_agent(path, agent)
    assert not errors, f"{path.name}:\n  " + "\n  ".join(errors)
