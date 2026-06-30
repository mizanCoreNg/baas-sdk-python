"""Typed exception hierarchy for the MizanCore BaaS SDK.

Maps the standard error envelope ``{"success": false, "message", "errors"}``
onto structured exceptions carrying the HTTP status, a machine error code, the
human message, and the field-level validation errors.

Mirrors the PHP/JS SDK error layer (BaasApiError + Auth/Validation/RateLimit).
"""

from __future__ import annotations

from typing import Any, Mapping, Optional


class BaasApiError(Exception):
    """Base typed error for non-2xx MizanCore BaaS API responses."""

    def __init__(
        self,
        message: str,
        http_status: int,
        error_code: Optional[str] = None,
        errors: Optional[Mapping[str, Any]] = None,
        body: Any = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.http_status = http_status
        self.error_code = error_code
        self.errors: Mapping[str, Any] = errors or {}
        self.body = body

    @classmethod
    def from_response(cls, status: int, body: Any) -> "BaasApiError":
        """Build the correct typed error from an HTTP status + decoded body."""
        message = "MizanCore BaaS API request failed."
        error_code: Optional[str] = None
        errors: Mapping[str, Any] = {}

        if isinstance(body, Mapping):
            msg = body.get("message")
            if isinstance(msg, str):
                message = msg
            raw_code = body.get("code", body.get("error_code"))
            if isinstance(raw_code, (str, int)):
                error_code = str(raw_code)
            raw_errors = body.get("errors")
            if isinstance(raw_errors, Mapping):
                errors = raw_errors

        if status in (401, 403):
            return BaasAuthError(message, status, error_code, errors, body)
        if status == 422:
            return BaasValidationError(message, status, error_code, errors, body)
        if status == 429:
            return BaasRateLimitError(message, status, error_code, errors, body)
        return cls(message, status, error_code, errors, body)


class BaasAuthError(BaasApiError):
    """Raised on 401/403 — invalid/missing X-API-Key, or insufficient scope."""


class BaasValidationError(BaasApiError):
    """Raised on 422 — request failed FormRequest validation; see ``.errors``."""


class BaasRateLimitError(BaasApiError):
    """Raised on 429 — rate limit exceeded after the SDK exhausted its retries."""
