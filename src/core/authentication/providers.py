from __future__ import annotations

import os

from playwright.sync_api import BrowserContext

DEFAULT_AUTH_HEADER = "Authorization"


class BearerTokenProvider:
    def __init__(self, token: str, header: str = DEFAULT_AUTH_HEADER) -> None:
        if not token:
            raise ValueError("Authentication token cannot be empty")
        self._token = token
        self._header = header

    @classmethod
    def from_environment(cls, variable: str = "AUTH_TOKEN") -> BearerTokenProvider:
        token = os.getenv(variable)
        if not token:
            raise RuntimeError(f"{variable} is required for token authentication")
        return cls(token)

    def authenticate(self, context: BrowserContext) -> None:
        context.set_extra_http_headers({self._header: f"Bearer {self._token}"})


class CookieAuthenticationProvider:
    def __init__(self, name: str, value: str, domain: str, path: str = "/") -> None:
        if not name or not value or not domain:
            raise ValueError("Cookie name, value, and domain are required")
        self._cookie = {"name": name, "value": value, "domain": domain, "path": path}

    def authenticate(self, context: BrowserContext) -> None:
        context.add_cookies([self._cookie])
