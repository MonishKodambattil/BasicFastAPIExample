def test_create_user(client):
    response = client.post("/users/", json={"email": "user@example.com", "password": "password123"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "user@example.com"
    assert "id" in data
    assert data["is_active"] is True

def test_create_user_with_existing_email(client):
    response = client.post("/users/", json={"email": "user@example.com", "password": "password123"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already registered"}
