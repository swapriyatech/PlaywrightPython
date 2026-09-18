from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ExecutionSummary:
    execution_id: str
    application: str
    environment: str
    browser: str
    suite: str
    total: int
    passed: int
    failed: int
    skipped: int
    duration_seconds: float


class ExecutionHistory:
    def __init__(self, database_path: Path) -> None:
        self._database_path = database_path
        self._database_path.parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(self._database_path) as connection:
            connection.execute("""CREATE TABLE IF NOT EXISTS executions (
                execution_id TEXT PRIMARY KEY, application TEXT NOT NULL,
                environment TEXT NOT NULL, browser TEXT NOT NULL, suite TEXT NOT NULL,
                total INTEGER NOT NULL, passed INTEGER NOT NULL, failed INTEGER NOT NULL,
                skipped INTEGER NOT NULL, duration_seconds REAL NOT NULL
            )""")

    def record(self, summary: ExecutionSummary) -> None:
        with sqlite3.connect(self._database_path) as connection:
            connection.execute(
                "INSERT OR REPLACE INTO executions VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                tuple(summary.__dict__.values()),
            )

    def latest(self, limit: int = 20) -> list[ExecutionSummary]:
        with sqlite3.connect(self._database_path) as connection:
            rows = connection.execute(
                "SELECT execution_id, application, environment, browser, suite, total, "
                "passed, failed, skipped, duration_seconds FROM executions "
                "ORDER BY rowid DESC LIMIT ?",
                (limit,),
            ).fetchall()
        return [ExecutionSummary(*row) for row in rows]
