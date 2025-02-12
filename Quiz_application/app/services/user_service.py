from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserResponse


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, db: Session, user: UserCreate) -> UserResponse:
        return self.user_repository.create_user(db, user)

    def get_user_by_id(self, db: Session, user_id: int) -> UserResponse:
        return self.user_repository.get_user_by_id(db, user_id)

    def update_user(self, db: Session, user_id: int, user: UserCreate) -> UserResponse:
        return self.user_repository.update_user(db, user_id, user)

    def delete_user(self, db: Session, user_id: int) -> bool:
        return self.user_repository.delete_user(db, user_id)

    def get_all_users(self, db: Session) -> list[UserResponse]:
        return self.user_repository.get_all_users(db)