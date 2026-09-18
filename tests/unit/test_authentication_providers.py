import pytest

from core.authentication.providers import BearerTokenProvider, CookieAuthenticationProvider


def test_token_provider_requires_a_token():
    with pytest.raises(ValueError, match="token"):
        BearerTokenProvider("")


def test_cookie_provider_requires_scope():
    with pytest.raises(ValueError, match="domain"):
        CookieAuthenticationProvider("session", "value", "")
