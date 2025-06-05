
def test_logo_endpoint(test_client):
    print("test_logo_endpoint called")
    response = test_client.get("/logo/logoIcons")
    assert response.status_code == 200
    data = response.json()

    print("Response data:", data)

    assert isinstance(data, list)
    assert "name" in data[0]
