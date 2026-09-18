from __future__ import annotations

from datetime import UTC, datetime, timedelta


class DateTimeUtilities:
    @staticmethod
    def now_utc() -> datetime:
        return datetime.now(UTC)

    @staticmethod
    def iso_now() -> str:
        return DateTimeUtilities.now_utc().isoformat()

    @staticmethod
    def parse_iso(value: str) -> datetime:
        parsed = datetime.fromisoformat(value)
        return parsed if parsed.tzinfo else parsed.replace(tzinfo=UTC)

    @staticmethod
    def add_seconds(value: datetime, seconds: float) -> datetime:
        return value + timedelta(seconds=seconds)

    @staticmethod
    def is_expired(value: datetime, validity_seconds: float) -> bool:
        return DateTimeUtilities.now_utc() >= DateTimeUtilities.add_seconds(value, validity_seconds)
