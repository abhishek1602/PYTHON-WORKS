from sqlalchemy.orm import Session
from models import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, name: str, email: str, hashed_password: str, role: str = 'user') -> User:
        new_user = User(name=name, email=email, hashed_password=hashed_password, role=role)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def get_user_by_id(self, user_id: int) -> User:
        return self.session.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str) -> User:
        return self.session.query(User).filter(User.email == email).first()

    def update_user(self, user: User) -> User:
        self.session.commit()
        return user

    def delete_user(self, user_id: int) -> None:
        user = self.get_user_by_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()