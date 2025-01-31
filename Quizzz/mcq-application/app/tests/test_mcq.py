from fastapi.testclient import TestClient
from app.main import app
from app.db.models.user import User
from app.db.models.mcq import MCQ
from app.schemas.user import UserCreate
from app.schemas.mcq import MCQCreate
from app.db.session import get_db
from sqlalchemy.orm import Session

client = TestClient(app)

def test_create_mcq(db: Session):
    mcq_data = {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct_answer": "Paris",
        "category": "Geography",
        "difficulty": "Easy"
    }
    response = client.post("/api/mcq/", json=mcq_data)
    assert response.status_code == 201
    assert response.json()["question"] == mcq_data["question"]

def test_get_mcqs():
    response = client.get("/api/mcq/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_user_registration():
    user_data = {
        "username": "testuser",
        "password": "testpassword"
    }
    response = client.post("/api/auth/register", json=user_data)
    assert response.status_code == 201
    assert response.json()["username"] == user_data["username"]

def test_user_login():
    user_data = {
        "username": "testuser",
        "password": "testpassword"
    }
    response = client.post("/api/auth/login", json=user_data)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_submit_mcq_answers():
    answers = {
        "mcq_id": 1,
        "selected_options": ["Paris"]
    }
    response = client.post("/api/mcq/submit", json=answers)
    assert response.status_code == 200
    assert "score" in response.json()

def test_get_user_history():
    response = client.get("/api/user/history/testuser")
    assert response.status_code == 200
    assert isinstance(response.json(), list)