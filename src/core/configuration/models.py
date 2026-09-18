from __future__ import annotations

import os
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, field_validator

BrowserName = Literal["chromium", "firefox", "webkit"]
SuiteName = Literal["smoke", "sanity", "regression"]


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class ExecutionConfig(StrictModel):
    parallel: bool = False
    workers: int = Field(default=1, ge=1)


class RetryConfig(StrictModel):
    count: int = Field(default=0, ge=0, le=5)


class TimeoutConfig(StrictModel):
    action: int = Field(default=10_000, gt=0)
    expect: int = Field(default=10_000, gt=0)
    page_load: int = Field(default=30_000, gt=0)
    navigation: int = Field(default=30_000, gt=0)
    test: int = Field(default=120_000, gt=0)


class FrameworkConfig(StrictModel):
    application: str = Field(min_length=1, pattern=r"^[a-z0-9_-]+$")
    environment: str = Field(min_length=1)
    browser: BrowserName = "chromium"
    suite: SuiteName = "regression"
    execution: ExecutionConfig = ExecutionConfig()
    retry: RetryConfig = RetryConfig()
    timeouts: TimeoutConfig = TimeoutConfig()

    @field_validator("environment")
    @classmethod
    def normalize_environment(cls, value: str) -> str:
        return value.upper()


def load_yaml(path: Path) -> dict[str, object]:
    with path.open(encoding="utf-8") as stream:
        value = yaml.safe_load(stream) or {}
    if not isinstance(value, dict):
        raise ValueError(f"Configuration root must be a mapping: {path}")
    return value


def load_framework_config(path: Path) -> FrameworkConfig:
    return FrameworkConfig.model_validate(load_yaml(path))


def load_runtime_config(path: Path) -> FrameworkConfig:
    values = load_yaml(path)
    execution = dict(values.get("execution", {}))
    retry = dict(values.get("retry", {}))
    overrides: dict[str, object] = {}
    for field, environment_name in (
        ("application", "APP"),
        ("environment", "ENVIRONMENT"),
        ("browser", "BROWSER"),
        ("suite", "SUITE"),
    ):
        if value := os.getenv(environment_name):
            overrides[field] = value
    if workers := os.getenv("WORKERS"):
        execution["workers"] = int(workers)
    if retry_count := os.getenv("RETRY_COUNT"):
        retry["count"] = int(retry_count)
    if execution:
        overrides["execution"] = execution
    if retry:
        overrides["retry"] = retry
    return FrameworkConfig.model_validate({**values, **overrides})
