from sqlalchemy.orm import Session
from src.repositories.user_repository import UserRepository
from src.unit_of_work import UnitOfWork

class UserService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        self.user_repository = UserRepository(uow.session)

    def get_user_by_id(self, user_id: int):
        return self.user_repository.get_by_id(user_id)

    def get_leaderboard(self, limit: int = 10):
        return self.user_repository.get_leaderboard(limit)

    def update_user(self, user_id: int, **kwargs):
        user = self.user_repository.get_by_id(user_id)
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            self.uow.commit()
            return user
        return None

    def delete_user(self, user_id: int):
        user = self.user_repository.get_by_id(user_id)
        if user:
            self.user_repository.delete(user)
            self.uow.commit()
            return True
        return False

    def create_user(self, name: str, email: str, hashed_password: str):
        user = self.user_repository.create(name=name, email=email, hashed_password=hashed_password)
        self.uow.commit()
        return user