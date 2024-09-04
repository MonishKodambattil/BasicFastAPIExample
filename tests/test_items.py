from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"name": "Test Item", "description": "This is a test item"})
    assert response.status_code == 200
    assert response.json() == {"name": "Test Item", "description": "This is a test item"}

def test_read_item():
    response = client.post("/items/", json={"name": "Test Item", "description": "This is a test item"})
    item_id = response.json()["id"]

    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"id": item_id, "name": "Test Item", "description": "This is a test item"}

def test_read_items():
    client.post("/items/", json={"name": "Test Item 1", "description": "This is a test item"})
    client.post("/items/", json={"name": "Test Item 2", "description": "This is another test item"})
    response = client.get("/items/")
    assert response.status_code == 200
    items = response.json()
    assert len(items) >= 2

def test_update_item():
    response = client.post("/items/", json={"name": "Test Item", "description": "This is a test item"})
    item_id = response.json()["id"]

    response = client.put(f"/items/{item_id}", json={"name": "Updated Item", "description": "Updated description"})
    assert response.status_code == 200
    assert response.json() == {"id": item_id, "name": "Updated Item", "description": "Updated description"}

def test_delete_item():
    response = client.post("/items/", json={"name": "Test Item", "description": "This is a test item"})
    item_id = response.json()["id"]

    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"detail": "Item deleted"}

    response = client.get(f"/items/{item_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
