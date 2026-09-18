from __future__ import annotations

import re


class SecretMasker:
    _patterns = (re.compile(r"(?i)(password|token|secret|api[_-]?key)(\s*[:=]\s*)[^\s,]+"),)

    def mask(self, value: str) -> str:
        masked = value
        for pattern in self._patterns:
            masked = pattern.sub(r"\1\2***", masked)
        return masked
