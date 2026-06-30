"""Tests for the MizanBaasClient value-add layer (auth, idempotency, retry,
error mapping). Uses a fake PoolManager so nothing hits the network."""

import re

import pytest

from mizancore_baas import (
    MizanBaasClient,
    BaasApiError,
    BaasAuthError,
    BaasValidationError,
    BaasRateLimitError,
)


class FakeResponse:
    def __init__(self, status, data=b"{}", headers=None):
        self.status = status
        self.data = data if isinstance(data, bytes) else data.encode("utf-8")
        self.headers = headers or {}


class FakePoolManager:
    """Records each request and replays a scripted response queue."""

    def __init__(self, responses):
        self._responses = responses
        self._i = 0
        self.calls = []

    def request(self, method, url, body=None, fields=None, headers=None, preload_content=True):
        self.calls.append(
            {"method": method, "url": url, "body": body, "headers": dict(headers or {})}
        )
        resp = self._responses[min(self._i, len(self._responses) - 1)]
        self._i += 1
        return resp


def make_client(responses, **kwargs):
    pm = FakePoolManager(responses)
    client = MizanBaasClient(
        api_key="pk_test_123", pool_manager=pm, base_delay_ms=1, **kwargs
    )
    return client, pm


# --- auth header -------------------------------------------------------------


def test_sends_x_api_key_not_x_partner_key():
    client, pm = make_client([FakeResponse(200, b'{"ok":true}')])
    client.get("/baas/virtual-accounts")
    h = pm.calls[0]["headers"]
    assert h["X-API-Key"] == "pk_test_123"
    assert "X-Partner-Key" not in h


def test_sends_tenant_header_when_provided():
    client, pm = make_client([FakeResponse(200)], tenant="world.test.localhost")
    client.get("/baas/ping")
    assert pm.calls[0]["headers"]["X-Tenant-ID"] == "world.test.localhost"


# --- idempotency -------------------------------------------------------------

_UUID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.I)


def test_auto_idempotency_key_on_post():
    client, pm = make_client([FakeResponse(201, b'{"id":"va_1"}')])
    client.post("/baas/virtual-accounts", {"customer_id": "c1"})
    key = pm.calls[0]["headers"]["Idempotency-Key"]
    assert _UUID_RE.match(key)


def test_preserves_supplied_idempotency_key():
    client, pm = make_client([FakeResponse(201)])
    client.post("/baas/virtual-accounts", {"customer_id": "c1"}, idempotency_key="my-key-abc")
    assert pm.calls[0]["headers"]["Idempotency-Key"] == "my-key-abc"


def test_no_idempotency_key_on_get():
    client, pm = make_client([FakeResponse(200)])
    client.get("/baas/virtual-accounts")
    assert "Idempotency-Key" not in pm.calls[0]["headers"]


# --- error mapping -----------------------------------------------------------


def test_maps_401_to_auth_error():
    client, _ = make_client(
        [FakeResponse(401, b'{"success":false,"message":"Unauthenticated."}')]
    )
    with pytest.raises(BaasAuthError) as exc:
        client.get("/x")
    assert exc.value.http_status == 401
    assert exc.value.message == "Unauthenticated."


def test_maps_422_to_validation_error_with_fields():
    body = b'{"success":false,"message":"Validation failed.","errors":{"customer_id":["required"]}}'
    client, _ = make_client([FakeResponse(422, body)])
    with pytest.raises(BaasValidationError) as exc:
        client.post("/x", {})
    assert exc.value.http_status == 422
    assert exc.value.errors == {"customer_id": ["required"]}


def test_maps_generic_400_to_base_error():
    client, _ = make_client([FakeResponse(400, b'{"success":false,"message":"Bad."}')])
    with pytest.raises(BaasApiError):
        client.get("/x")


# --- retry / backoff ---------------------------------------------------------


def test_retries_on_429_then_succeeds():
    client, pm = make_client(
        [
            FakeResponse(429, b'{"message":"slow"}', {"Retry-After": "0"}),
            FakeResponse(200, b'{"ok":true}'),
        ]
    )
    out = client.get("/x")
    assert out == {"ok": True}
    assert len(pm.calls) == 2


def test_gives_up_after_max_retries_on_persistent_429():
    client, pm = make_client(
        [FakeResponse(429, b'{"message":"nope"}', {"Retry-After": "0"})],
        max_retries=2,
    )
    with pytest.raises(BaasRateLimitError):
        client.get("/x")
    assert len(pm.calls) == 3  # 1 initial + 2 retries


def test_retries_on_503_then_succeeds():
    client, pm = make_client(
        [FakeResponse(503, b"{}"), FakeResponse(200, b'{"ok":true}')]
    )
    client.get("/x")
    assert len(pm.calls) == 2


# --- config ------------------------------------------------------------------


def test_resolves_base_url_by_environment():
    live = MizanBaasClient(api_key="k", environment="live")
    assert live.base_url == "https://api.mizancore.ng/api/v1"
    test = MizanBaasClient(api_key="k")
    assert test.base_url == "https://test-api.mizancore.ng/api/v1"


def test_requires_api_key():
    with pytest.raises(ValueError):
        MizanBaasClient(api_key="")
