from pathlib import Path

from core.data.data_engine import TestDataEngine
from core.retry.failure_classifier import FailureCategory, FailureClassifier
from core.security.secret_masker import SecretMasker


def test_data_merge_uses_runtime_values_last(tmp_path: Path):
    path = tmp_path / "data.json"
    path.write_text('{"name": "common", "nested": {"enabled": true}}', encoding="utf-8")
    engine = TestDataEngine()
    assert engine.merge(engine.load_json(path), {"name": "runtime"})["name"] == "runtime"


def test_assertions_are_not_retryable():
    classifier = FailureClassifier()
    category = classifier.classify(AssertionError("expected title"))
    assert category == FailureCategory.ASSERTION
    assert not classifier.is_retryable(category)


def test_secrets_are_masked():
    assert SecretMasker().mask("password=secret123 token=abc") == "password=*** token=***"
