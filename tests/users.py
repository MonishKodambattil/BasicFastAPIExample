from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"email": "test@test.com", "password": "test"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@test.com"