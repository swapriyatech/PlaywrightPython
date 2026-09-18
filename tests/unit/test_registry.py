from pathlib import Path

import pytest

from core.registry.application_registry import ApplicationRegistry

ROOT = Path(__file__).resolve().parents[2]


def test_registry_discovers_applications_without_core_branches():
    registry = ApplicationRegistry(ROOT / "src" / "applications")
    assert registry.names() == ("app1", "app2")
    assert registry.get("app1").display_name == "Cricbuzz"
    assert registry.get("app2").display_name == "Google"


def test_registry_rejects_unknown_application():
    registry = ApplicationRegistry(ROOT / "src" / "applications")
    with pytest.raises(ValueError, match="Unknown application"):
        registry.get("app3")
