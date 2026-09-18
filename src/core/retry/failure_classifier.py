from __future__ import annotations

from enum import StrEnum

from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


class FailureCategory(StrEnum):
    ASSERTION = "AssertionFailure"
    BUSINESS = "BusinessValidationFailure"
    TIMEOUT = "TimeoutFailure"
    NETWORK = "NetworkFailure"
    BROWSER = "BrowserCrash"
    INFRASTRUCTURE = "InfrastructureFailure"
    CONFIGURATION = "ConfigurationFailure"
    AUTHENTICATION = "AuthenticationFailure"
    DATA = "DataFailure"
    FRAMEWORK = "FrameworkFailure"
    UNKNOWN = "UnknownFailure"


class FailureClassifier:
    def classify(self, error: BaseException) -> FailureCategory:
        if isinstance(error, AssertionError):
            return FailureCategory.ASSERTION
        if isinstance(error, PlaywrightTimeoutError):
            return FailureCategory.TIMEOUT
        if isinstance(error, PlaywrightError):
            message = str(error).lower()
            if "network" in message or "connection" in message:
                return FailureCategory.NETWORK
            return FailureCategory.BROWSER
        return FailureCategory.UNKNOWN

    def is_retryable(self, category: FailureCategory) -> bool:
        return category in {
            FailureCategory.TIMEOUT,
            FailureCategory.NETWORK,
            FailureCategory.BROWSER,
            FailureCategory.INFRASTRUCTURE,
        }
