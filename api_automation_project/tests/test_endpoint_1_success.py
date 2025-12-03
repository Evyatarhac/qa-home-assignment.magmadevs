from utils.api_client import api_get

def test_endpoint_1_success(token):
    response = api_get("/api/test/1", token)

    assert response.status_code == 200
    json = response.json()
    assert json["status"] == "success"
    assert json["message"] == "Request completed"
