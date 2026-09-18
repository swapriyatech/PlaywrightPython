import pytest

from core.reporting.email import EmailReporter


def test_email_requires_recipients():
    with pytest.raises(ValueError, match="recipient"):
        EmailReporter("smtp.example.test", 587, "qa@example.test", ())


def test_email_requires_environment(monkeypatch):
    monkeypatch.delenv("SMTP_HOST", raising=False)
    monkeypatch.delenv("SMTP_SENDER", raising=False)
    monkeypatch.delenv("SMTP_RECIPIENTS", raising=False)
    with pytest.raises(RuntimeError, match="SMTP_HOST"):
        EmailReporter.from_environment()
