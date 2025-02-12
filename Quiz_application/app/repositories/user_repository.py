from sqlalchemy.orm import Session
from app.models.quiz_model import User
from app.schemas.user_schema import UserCreate, UserResponse


# User Repository
class UserRepository:

    def get_user_by_id(self, db: Session, user_id: int) -> UserResponse:
        return db.query(User).filter(User.id == user_id).first()

    def create_user(self, db: Session, user: UserCreate) -> User:
        db_user = User(
            username=user.username,
            hashed_password=user.password,
            is_admin=user.is_admin,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update_user(self, db: Session, user_id: int, updated_data: UserCreate) -> User:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return None

        user.username = updated_data.username
        user.hashed_password = updated_data.password
        user.is_admin = updated_data.is_admin

        db.commit()
        db.refresh(user)
        return user

    def delete_user(self, db: Session, user_id: int) -> bool:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return False

        db.delete(user)
        db.commit()
        return True

    def get_all_users(self, db: Session) -> list[UserResponse]:
        return db.query(User).all()