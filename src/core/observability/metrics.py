from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ExecutionMetrics:
    total: int = 0
    passed: int = 0
    failed: int = 0
    skipped: int = 0
    retries: int = 0
    duration_seconds: float = 0.0

    @property
    def pass_rate(self) -> float:
        return self.passed / self.total if self.total else 0.0

    @property
    def failure_rate(self) -> float:
        return self.failed / self.total if self.total else 0.0
