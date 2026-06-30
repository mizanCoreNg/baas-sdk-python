"""mizancore-baas — Official Python SDK for the MizanCore BaaS API.

The wire-level client is generated from the BaaS OpenAPI spec (under
``sdks/python/generated``). This package is the hand-written value-add layer:
a configured client, typed errors, and webhook verification.
"""

from .client import MizanBaasClient, BASE_URLS
from .errors import (
    BaasApiError,
    BaasAuthError,
    BaasValidationError,
    BaasRateLimitError,
)
from .webhooks import MizanWebhooks

__all__ = [
    "MizanBaasClient",
    "BASE_URLS",
    "BaasApiError",
    "BaasAuthError",
    "BaasValidationError",
    "BaasRateLimitError",
    "MizanWebhooks",
]

__version__ = "0.1.0"
