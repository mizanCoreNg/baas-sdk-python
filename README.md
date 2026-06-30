# mizancore-baas

Official Python SDK for the **MizanCore Banking-as-a-Service (BaaS) API**. A
hand-written value-add layer (auth, idempotency, retry, typed errors, webhook
verification) over an OpenAPI-generated client (under [`generated/`](./generated)).

## Quickstart

```python
from mizancore_baas import MizanBaasClient

client = MizanBaasClient(api_key="pk_test_...", environment="test")
account = client.request("POST", "/baas/virtual-accounts", json={"customer_id": "c_123"})
# X-API-Key + an auto Idempotency-Key are attached; 429/5xx are retried.
```

## What the SDK adds

| Concern | Behaviour |
|---|---|
| **Auth** | `X-API-Key` header on every request (resolves test/staging/live base URL by `environment`). |
| **Idempotency** | Auto `Idempotency-Key` (`uuid.uuid4()`) on POST/PUT/PATCH; a caller-supplied key is preserved; never added on GET. |
| **Retries** | Exponential backoff with jitter on `429` + `5xx`, honouring `Retry-After`. |
| **Typed errors** | Non-2xx `{success, message, errors}` → `BaasApiError` (+ `BaasAuthError`/`BaasValidationError`/`BaasRateLimitError`) with `http_status`, `error_code`, `errors`. |
| **Webhooks** | `MizanWebhooks.verify(raw_body, signature_header, secret)` — HMAC-SHA256 over the **raw body bytes**, timing-safe compare. |

## Webhook verification (raw bytes — important)

```python
from mizancore_baas import MizanWebhooks

# Pass the RAW request body bytes exactly as received — do NOT re-serialize the
# parsed dict (json formatting differences flip a valid signature to invalid).
ok = MizanWebhooks.verify(
    raw_body=request.body,                       # bytes, exactly as received
    signature_header=request.headers["X-Webhook-Signature"],
    secret=webhook_secret,
)
if not ok:
    return Response(status_code=401)
```

## Install

```bash
pip install mizancore-baas
```

## Source of truth

The `generated/` client is produced from the BaaS OpenAPI spec — do not hand-edit
it. The value-add layer in `src/mizancore_baas/` is what you import.
