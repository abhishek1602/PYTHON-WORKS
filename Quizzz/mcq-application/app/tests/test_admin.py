from fastapi.testclient import TestClient
from app.main import app
from app.db.models.user import User
from app.db.models.mcq import MCQ
from app.db.session import get_db
from sqlalchemy.orm import Session

client = TestClient(app)

def test_admin_upload_mcq():
    # Simulate admin login
    response = client.post("/auth/login", json={"username": "admin", "password": "admin_password"})
    assert response.status_code == 200
    token = response.json().get("access_token")

    # Admin uploads MCQs in bulk
    headers = {"Authorization": f"Bearer {token}"}
    mcq_data = [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "correct_answer": "Paris", "category": "Geography", "difficulty": "Easy"},
        {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "correct_answer": "4", "category": "Math", "difficulty": "Easy"},
    ]
    response = client.post("/admin/upload_mcq", json={"mcqs": mcq_data}, headers=headers)
    assert response.status_code == 201
    assert response.json().get("message") == "MCQs uploaded successfully"

def test_admin_manage_users():
    # Simulate admin login
    response = client.post("/auth/login", json={"username": "admin", "password": "admin_password"})
    assert response.status_code == 200
    token = response.json().get("access_token")

    # Admin retrieves user list
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/admin/users", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    # Admin can delete a user
    user_id = response.json()[0]["id"]
    response = client.delete(f"/admin/users/{user_id}", headers=headers)
    assert response.status_code == 204

def test_admin_role_required():
    # Attempt to access admin route without admin privileges
    response = client.get("/admin/users")
    assert response.status_code == 403

def test_admin_upload_mcq_unauthorized():
    # Attempt to upload MCQs without authorization
    mcq_data = [{"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "correct_answer": "Paris", "category": "Geography", "difficulty": "Easy"}]
    response = client.post("/admin/upload_mcq", json={"mcqs": mcq_data})
    assert response.status_code == 403

def test_admin_upload_mcq_invalid_data():
    # Simulate admin login
    response = client.post("/auth/login", json={"username": "admin", "password": "admin_password"})
    assert response.status_code == 200
    token = response.json().get("access_token")

    # Admin uploads MCQs with invalid data
    headers = {"Authorization": f"Bearer {token}"}
    mcq_data = [{"question": "", "options": [], "correct_answer": "", "category": "", "difficulty": ""}]
    response = client.post("/admin/upload_mcq", json={"mcqs": mcq_data}, headers=headers)
    assert response.status_code == 422  # Unprocessable Entity for validation errors