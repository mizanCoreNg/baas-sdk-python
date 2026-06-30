"""Webhook signature verification for MizanCore BaaS partner webhooks.

Backend signer — source of truth:
    server/app/Domains/BaaS/Services/WebhookDispatchService.php:165-184
        hash_hmac('sha256', json_encode($payload, JSON_UNESCAPED_SLASHES), $secret)
    -> lowercase hex, delivered in the ``X-Webhook-Signature`` header,
       verified with hash_equals() (timing-safe).

RAW-BYTES CONTRACT (cross-language correctness)
-----------------------------------------------
The string the backend signs IS the exact byte sequence it writes to the HTTP
response body. So the robust, language-agnostic way to verify is to HMAC the
RAW RECEIVED REQUEST BODY BYTES — never a re-encode of the parsed object.
Re-encoding is fragile across languages: PHP ``json_encode`` with only
JSON_UNESCAPED_SLASHES still escapes non-ASCII as ``\\uXXXX`` and emits compact
separators; Python ``json.dumps`` adds spaces and does not escape slashes by
default. Any difference flips a valid signature to invalid. So: pass the raw
body exactly as received.

In FastAPI/Starlette use ``await request.body()``; in Flask use
``request.get_data()`` (NOT ``request.json`` re-serialized); in Django use
``request.body``. Never pass ``json.dumps(parsed)``.
"""

from __future__ import annotations

import hashlib
import hmac
from typing import Union


class MizanWebhooks:
    """Verify and sign MizanCore BaaS partner webhook payloads."""

    @staticmethod
    def verify(
        raw_body: Union[bytes, str],
        signature_header: str,
        secret: Union[bytes, str],
    ) -> bool:
        """Verify an inbound webhook's ``X-Webhook-Signature``.

        :param raw_body:         The RAW request body, exactly as received.
        :param signature_header: The ``X-Webhook-Signature`` value (lowercase hex).
        :param secret:           The partner webhook signing secret.
        """
        if not signature_header or not secret:
            return False

        expected = MizanWebhooks.sign(raw_body, secret)
        # compare_digest is timing-safe; it accepts str (ASCII) or bytes.
        return hmac.compare_digest(expected, signature_header)

    @staticmethod
    def sign(raw_body: Union[bytes, str], secret: Union[bytes, str]) -> str:
        """Compute the lowercase-hex HMAC-SHA256 of the raw body bytes."""
        key = secret.encode("utf-8") if isinstance(secret, str) else secret
        msg = raw_body.encode("utf-8") if isinstance(raw_body, str) else raw_body
        return hmac.new(key, msg, hashlib.sha256).hexdigest()
