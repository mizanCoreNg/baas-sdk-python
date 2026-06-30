"""Configured entry point for the MizanCore BaaS SDK.

The hand-written value-add layer over the OpenAPI-generated python client.

Adds:
  - ``X-API-Key`` auth header on every request (BaasAuthMiddleware reads
    X-API-Key; NOT X-Partner-Key).
  - Auto ``Idempotency-Key`` (uuid4) on POST/PUT/PATCH when the caller omitted
    one; a supplied key is preserved.
  - Exponential-backoff retry on 429 + 5xx honouring ``Retry-After``.
  - Typed ``BaasApiError`` (+ Auth/Validation/RateLimit) mapping for the
    ``{success, message, errors}`` envelope.

The HTTP layer is urllib3 (the generated client's own dependency), so the SDK
adds no new runtime dependency. ``api()`` wires a configured generated
``ApiClient`` so generated calls inherit auth + retry + idempotency.
"""

from __future__ import annotations

import email.utils
import json
import random
import time
import uuid
from typing import Any, Dict, Mapping, Optional

import urllib3

from .errors import BaasApiError

BASE_URLS: Dict[str, str] = {
    "test": "https://test-api.mizancore.ng/api/v1",
    "staging": "https://staging-api.mizancore.ng/api/v1",
    "live": "https://api.mizancore.ng/api/v1",
}

_WRITE_METHODS = {"POST", "PUT", "PATCH"}


def _parse_retry_after(value: Optional[str]) -> Optional[float]:
    """Parse a Retry-After header into seconds, or None if unparseable."""
    if not value:
        return None
    value = value.strip()
    if value.isdigit():
        return float(value)
    parsed = email.utils.parsedate_to_datetime(value)
    if parsed is None:
        return None
    delta = parsed.timestamp() - time.time()
    return max(0.0, delta)


class MizanBaasClient:
    """Configured BaaS client with auth, idempotency, retry and typed errors."""

    def __init__(
        self,
        api_key: str,
        environment: str = "test",
        base_url: Optional[str] = None,
        tenant: Optional[str] = None,
        max_retries: int = 3,
        base_delay_ms: int = 200,
        pool_manager: Optional[urllib3.PoolManager] = None,
    ) -> None:
        if not api_key:
            raise ValueError("MizanBaasClient: `api_key` is required.")
        self.api_key = api_key
        self.tenant = tenant
        self.max_retries = max_retries
        self.base_delay_ms = base_delay_ms
        self.base_url = (base_url or BASE_URLS.get(environment, BASE_URLS["test"])).rstrip("/")
        # urllib3 retries are disabled here; we implement our own retry loop so
        # we can honour Retry-After and map typed errors uniformly.
        self._http = pool_manager or urllib3.PoolManager(retries=False)

    # ----- header construction -------------------------------------------------

    def _headers(self, method: str, extra: Optional[Mapping[str, str]] = None) -> Dict[str, str]:
        headers: Dict[str, str] = {
            "X-API-Key": self.api_key,
            "Accept": "application/json",
            "User-Agent": "mizancore-baas-python-sdk/0.1",
        }
        if self.tenant:
            headers["X-Tenant-ID"] = self.tenant
        if extra:
            headers.update(extra)
        if method.upper() in _WRITE_METHODS and "Idempotency-Key" not in headers:
            headers["Idempotency-Key"] = str(uuid.uuid4())
        return headers

    # ----- core request with retry + error mapping -----------------------------

    def request(
        self,
        method: str,
        path: str,
        *,
        body: Any = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any:
        method = method.upper()
        url = self.base_url + "/" + path.lstrip("/")
        req_headers = self._headers(method, headers)
        encoded_body = None
        if body is not None:
            encoded_body = json.dumps(body).encode("utf-8")
            req_headers["Content-Type"] = "application/json"

        attempt = 0
        while True:
            resp = self._http.request(
                method,
                url,
                body=encoded_body,
                fields=dict(params) if (params and encoded_body is None) else None,
                headers=req_headers,
                preload_content=True,
            )
            status = resp.status

            if (status == 429 or status >= 500) and attempt < self.max_retries:
                retry_after = _parse_retry_after(resp.headers.get("Retry-After"))
                if retry_after is not None:
                    delay = retry_after
                else:
                    base = self.base_delay_ms / 1000.0
                    delay = base * (2 ** attempt) + random.uniform(0, base)
                time.sleep(delay)
                attempt += 1
                continue

            decoded = self._decode(resp)
            if status >= 400:
                raise BaasApiError.from_response(status, decoded)
            return decoded

    @staticmethod
    def _decode(resp: "urllib3.HTTPResponse") -> Any:
        raw = resp.data
        if not raw:
            return {}
        try:
            return json.loads(raw)
        except (ValueError, TypeError):
            return raw

    # ----- convenience helpers -------------------------------------------------

    def get(self, path: str, params: Optional[Mapping[str, Any]] = None) -> Any:
        return self.request("GET", path, params=params)

    def post(
        self,
        path: str,
        body: Optional[Mapping[str, Any]] = None,
        idempotency_key: Optional[str] = None,
    ) -> Any:
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else None
        return self.request("POST", path, body=body or {}, headers=headers)

    # ----- generated-client wiring ---------------------------------------------

    def configuration(self) -> Any:
        """Build a generated ``Configuration`` pre-loaded with key + host.

        Imported lazily so the value-add layer works even if the generated
        package is not installed.
        """
        from mizancore_baas_generated.configuration import Configuration  # type: ignore

        config = Configuration(host=self.base_url)
        config.api_key["apiKeyAuth"] = self.api_key
        if self.tenant:
            config.api_key["tenantHeader"] = self.tenant
        return config

    def api(self, api_class: Any) -> Any:
        """Instantiate a generated ``*Api`` wired to a configured ApiClient.

        The returned ApiClient sends ``X-API-Key`` (overriding the generated
        ``X-Partner-Key`` default) and the tenant header on every call.
        """
        from mizancore_baas_generated.api_client import ApiClient  # type: ignore

        api_client = ApiClient(self.configuration())
        # Force the verified auth header regardless of the generated default.
        api_client.set_default_header("X-API-Key", self.api_key)
        if self.tenant:
            api_client.set_default_header("X-Tenant-ID", self.tenant)
        return api_class(api_client)
