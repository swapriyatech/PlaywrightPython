from __future__ import annotations

import os
import smtplib
from email.message import EmailMessage


class EmailReporter:
    def __init__(self, host: str, port: int, sender: str, recipients: tuple[str, ...]) -> None:
        if not recipients:
            raise ValueError("At least one email recipient is required")
        self._host = host
        self._port = port
        self._sender = sender
        self._recipients = recipients

    @classmethod
    def from_environment(cls) -> EmailReporter:
        host = os.getenv("SMTP_HOST")
        sender = os.getenv("SMTP_SENDER")
        recipients = tuple(filter(None, os.getenv("SMTP_RECIPIENTS", "").split(",")))
        if not host or not sender:
            raise RuntimeError("SMTP_HOST and SMTP_SENDER are required for email reporting")
        return cls(host, int(os.getenv("SMTP_PORT", "587")), sender, recipients)

    def send(self, subject: str, body: str) -> None:
        message = EmailMessage()
        message["Subject"] = subject
        message["From"] = self._sender
        message["To"] = ", ".join(self._recipients)
        message.set_content(body)
        with smtplib.SMTP(self._host, self._port, timeout=30) as smtp:
            smtp.starttls()
            smtp.send_message(message)
