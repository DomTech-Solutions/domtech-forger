from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)

def test_full_auth_flow():
    unique_email = f"test.user.flow.{uuid.uuid4()}@example.com"
    password = "password123"

    response = client.post(
        "/auth/register",
        json={"full_name": "Test Flow User", "email": unique_email, "password": password},
    )
    assert response.status_code == 201, response.text

    response = client.post(
        "/auth/login",
        data={"username": unique_email, "password": password},
    )
    assert response.status_code == 200, response.text
    token_data = response.json()
    access_token = token_data["access_token"]

    response = client.get(
        "/auth/users/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 200, response.text
    user_data = response.json()
    assert user_data["email"] == unique_email