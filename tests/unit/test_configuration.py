from pathlib import Path

import pytest
from pydantic import ValidationError

from core.configuration.models import FrameworkConfig, load_framework_config

ROOT = Path(__file__).resolve().parents[2]


def test_framework_yaml_loads_as_immutable_configuration():
    config = load_framework_config(ROOT / "config" / "framework.yaml")
    assert config.application == "app1"
    assert config.environment == "UAT"
    with pytest.raises(ValidationError):
        config.application = "app2"


def test_invalid_application_is_rejected():
    with pytest.raises(ValidationError):
        FrameworkConfig(application="bad app", environment="UAT")
