from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserCreate, UserUpdate

class UserCRUD:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserCreate) -> User:
        db_user = User(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_username(self, username: str) -> User:
        return self.db.query(User).filter(User.username == username).first()

    def update_user(self, user_id: int, user: UserUpdate) -> User:
        db_user = self.get_user(user_id)
        if db_user:
            for key, value in user.dict(exclude_unset=True).items():
                setattr(db_user, key, value)
            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int) -> None:
        db_user = self.get_user(user_id)
        if db_user:
            self.db.delete(db_user)
            self.db.commit()