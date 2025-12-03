from utils.api_client import api_get

def test_endpoint_3_warmup_optional(token):
    """
    Optional test:
    First call should fail with 503.
    Second call should return success.
    """

    first = api_get("/api/test/3", token)
    second = api_get("/api/test/3", token)

    assert first.status_code == 503
    assert second.status_code == 200
