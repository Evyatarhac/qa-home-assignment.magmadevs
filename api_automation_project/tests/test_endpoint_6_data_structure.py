from utils.api_client import api_get

def test_endpoint_6_data_structure(token):
    response = api_get("/api/test/6", token)

    assert response.status_code == 200
    json = response.json()

    assert "data" in json
    assert json["status"] == "success"

    data = json["data"]

    # Validate structure
    assert "count" in data
    assert "id" in data
    assert "value" in data

    # Validate types
    assert isinstance(data["count"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["value"], int)

