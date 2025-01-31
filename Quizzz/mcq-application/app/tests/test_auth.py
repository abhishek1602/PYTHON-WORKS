from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient
from app.api.auth import get_current_user
from app.db.models.user import User
from app.db.session import get_db
from sqlalchemy.orm import Session
import pytest

app = FastAPI()

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture
def db_session():
    db = get_db()
    yield db
    db.close()

def test_login(client, db_session):
    response = client.post("/auth/login", json={"username": "admin", "password": "admin123"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_invalid_user(client):
    response = client.post("/auth/login", json={"username": "invalid", "password": "wrong"})
    assert response.status_code == 401

def test_get_current_user(client, db_session):
    response = client.post("/auth/login", json={"username": "admin", "password": "admin123"})
    token = response.json()["access_token"]
    response = client.get("/auth/users/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["username"] == "admin"

def test_get_current_user_unauthorized(client):
    response = client.get("/auth/users/me")
    assert response.status_code == 401

def test_admin_access(client, db_session):
    response = client.post("/auth/login", json={"username": "admin", "password": "admin123"})
    token = response.json()["access_token"]
    response = client.get("/admin/users", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

def test_user_access(client, db_session):
    response = client.post("/auth/login", json={"username": "user", "password": "user123"})
    token = response.json()["access_token"]
    response = client.get("/admin/users", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 403  # User should not have access to admin routes