from werkzeug.security import generate_password_hash, check_password_hash
from flask import session
from src.repositories.user_repository import UserRepository

class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, name: str, email: str, password: str):
        hashed_password = generate_password_hash(password)
        user = self.user_repository.create_user(name=name, email=email, hashed_password=hashed_password)
        return user

    def login_user(self, email: str, password: str):
        user = self.user_repository.get_user_by_email(email)
        if user and check_password_hash(user.hashed_password, password):
            session['user_id'] = user.id
            return user
        return None

    def logout_user(self):
        session.pop('user_id', None)

    def is_authenticated(self):
        return 'user_id' in session

    def get_current_user(self):
        user_id = session.get('user_id')
        if user_id:
            return self.user_repository.get_user_by_id(user_id)
        return None