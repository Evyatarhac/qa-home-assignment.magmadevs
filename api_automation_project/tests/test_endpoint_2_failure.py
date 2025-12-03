from utils.api_client import api_get

def test_endpoint_2_failure(token):
    response = api_get("/api/test/2", token)

    # Expecting intentional server-side failure
    assert response.status_code == 500
    json = response.json()
    assert json["message"] == "Request failed"

