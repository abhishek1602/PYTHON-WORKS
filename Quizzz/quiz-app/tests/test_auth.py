from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import pytest
from src.app import app
from src.models import User
from src.repositories.user_repository import UserRepository

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/test_db'
    with app.test_client() as client:
        yield client

@pytest.fixture
def init_database():
    db.create_all()
    yield db
    db.drop_all()

def test_register(client, init_database):
    response = client.post('/register', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 201
    assert b'Registration successful' in response.data

def test_login(client, init_database):
    client.post('/register', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    response = client.post('/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert b'Login successful' in response.data

def test_login_invalid(client, init_database):
    response = client.post('/login', json={
        'email': 'invalid@example.com',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert b'Invalid credentials' in response.data

def test_register_existing_user(client, init_database):
    client.post('/register', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    response = client.post('/register', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 400
    assert b'User already exists' in response.data