def test_create_item(client):
    item_response = client.post("/items/", json={"name": "Test Item", "description": "A test item description"})
    assert item_response.status_code == 200
    item_data = item_response.json()
    assert item_data["name"] == "Test Name"
    assert item_data["description"] == "A test item description"
