from __future__ import annotations

from typing import Any

import httpx


class ApiClient:
    def __init__(self, base_url: str, timeout_seconds: float = 30.0) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout_seconds)

    def get(self, path: str, **params: str) -> httpx.Response:
        response = self._client.get(path, params=params)
        response.raise_for_status()
        return response

    def post(self, path: str, payload: dict[str, Any]) -> httpx.Response:
        response = self._client.post(path, json=payload)
        response.raise_for_status()
        return response

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> ApiClient:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
