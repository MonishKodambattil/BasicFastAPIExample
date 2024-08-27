def test_create_item(client):
    user_response = client.post("/users/", json={"email": "owner@example.com", "password": "password123"})
    assert user_response.status_code == 200
    user_data = user_response.json()

    item_response = client.post("/items/", json={"title": "Test Item", "description": "A test item description", "owner_id": user_data["id"]})
    assert item_response.status_code == 200
    item_data = item_response.json()
    assert item_data["title"] == "Test Item"
    assert item_data["description"] == "A test item description"
    assert item_data["owner_id"] == user_data["id"]


def test_create_item_with_invalid_user(client):
    item_response = client.post("/items/", json={"title": "Test Item", "description": "A test item description", "owner_id": 9999})
    assert item_response.status_code == 400
