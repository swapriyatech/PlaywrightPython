from __future__ import annotations

import os
import secrets
import time
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


class PythonUtilities:
    @staticmethod
    def required_env(name: str) -> str:
        value = os.getenv(name)
        if not value:
            raise RuntimeError(f"Environment variable {name} is required")
        return value

    @staticmethod
    def optional_env(name: str, default: str | None = None) -> str | None:
        return os.getenv(name, default)

    @staticmethod
    def parse_bool(value: str) -> bool:
        normalized = value.strip().lower()
        if normalized in {"1", "true", "yes", "y", "on"}:
            return True
        if normalized in {"0", "false", "no", "n", "off"}:
            return False
        raise ValueError(f"Invalid boolean value: {value!r}")

    @staticmethod
    def parse_int(value: str, minimum: int | None = None, maximum: int | None = None) -> int:
        result = int(value)
        if minimum is not None and result < minimum:
            raise ValueError(f"Value must be >= {minimum}: {result}")
        if maximum is not None and result > maximum:
            raise ValueError(f"Value must be <= {maximum}: {result}")
        return result

    @staticmethod
    def unique_id(prefix: str = "run") -> str:
        return f"{prefix}-{secrets.token_hex(8)}"

    @staticmethod
    def retry(operation: Callable[[], T], attempts: int = 3, delay_seconds: float = 0.5) -> T:
        if attempts < 1:
            raise ValueError("attempts must be at least 1")
        last_error: Exception | None = None
        for attempt in range(attempts):
            try:
                return operation()
            except Exception as error:
                last_error = error
                if attempt < attempts - 1:
                    time.sleep(delay_seconds)
        assert last_error is not None
        raise last_error
