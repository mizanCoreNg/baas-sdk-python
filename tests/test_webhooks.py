"""Cross-language webhook verification tests.

Reproduce the BACKEND signature exactly the way PHP does it
(server/app/Domains/BaaS/Services/WebhookDispatchService.php:165-184):
    hash_hmac('sha256', <exact body bytes>, $secret) -> lowercase hex.

The body string used here IS the exact byte sequence the backend writes to the
HTTP response. Verifying by HMAC-ing the raw received bytes reproduces it
without re-encoding (the robust cross-language pattern)."""

import hashlib
import hmac

from mizancore_baas import MizanWebhooks

SECRET = "whsec_partner_shared_secret"
BACKEND_BODY = '{"event":"va.credited","amount":150050}'


def backend_signature(body: str, secret: str) -> str:
    return hmac.new(secret.encode(), body.encode(), hashlib.sha256).hexdigest()


def test_accepts_backend_signature():
    sig = backend_signature(BACKEND_BODY, SECRET)
    assert MizanWebhooks.verify(BACKEND_BODY, sig, SECRET) is True


def test_accepts_bytes_raw_body():
    sig = backend_signature(BACKEND_BODY, SECRET)
    assert MizanWebhooks.verify(BACKEND_BODY.encode(), sig, SECRET) is True


def test_rejects_tampered_body():
    sig = backend_signature(BACKEND_BODY, SECRET)
    tampered = '{"event":"va.credited","amount":999999}'
    assert MizanWebhooks.verify(tampered, sig, SECRET) is False


def test_rejects_wrong_secret():
    sig = backend_signature(BACKEND_BODY, SECRET)
    assert MizanWebhooks.verify(BACKEND_BODY, sig, "wrong_secret") is False


def test_rejects_empty_signature_or_secret():
    assert MizanWebhooks.verify(BACKEND_BODY, "", SECRET) is False
    assert MizanWebhooks.verify(BACKEND_BODY, "abc", "") is False


def test_non_ascii_payload_via_raw_bytes():
    body = '{"name":"Olúwaséun","city":"Lagos"}'
    sig = backend_signature(body, SECRET)
    assert MizanWebhooks.verify(body, sig, SECRET) is True


def test_sign_produces_lowercase_hex_matching_backend():
    sig = MizanWebhooks.sign(BACKEND_BODY, SECRET)
    assert len(sig) == 64
    assert sig == sig.lower()
    assert sig == backend_signature(BACKEND_BODY, SECRET)
