from fastapi.testclient import TestClient
from app.main import app
from app.db.models.user import User
from app.db.session import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

client = TestClient(app)

def override_get_db():
    db = get_db()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

def test_create_user():
    response = client.post("/api/auth/register", json={"username": "testuser", "password": "testpass", "role": "user"})
    assert response.status_code == 201
    assert response.json()["username"] == "testuser"

def test_get_user():
    response = client.get("/api/user/testuser")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_update_user():
    response = client.put("/api/user/testuser", json={"password": "newpass"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_delete_user():
    response = client.delete("/api/user/testuser")
    assert response.status_code == 204

def test_user_history():
    response = client.get("/api/user/testuser/history")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Assuming history is a list of attempts