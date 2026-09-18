from pathlib import Path

import pytest

from core.data.repository import TestDataRepository

ROOT = Path(__file__).resolve().parents[2]


def test_data_repository_merges_common_application_suite_and_runtime_data():
    data = TestDataRepository(ROOT / "automation" / "testData").load_case(
        "app2", "smoke", runtime_override={"searchQuery": "runtime query"}
    )
    assert data["locale"] == "en-US"
    assert data["applicationName"] == "Google"
    assert data["suite"] == "smoke"
    assert data["searchQuery"] == "runtime query"


def test_data_repository_rejects_path_traversal():
    with pytest.raises(ValueError, match="Unsafe"):
        TestDataRepository(ROOT / "automation" / "testData").load_case("../app1", "smoke")
