from sqlalchemy import Column, Integer, String, Enum, Text, JSON
from sqlalchemy.orm import relationship
from app.db.base import Base
from enum import Enum as PyEnum

class UserRole(PyEnum):
    ADMIN = "admin"
    USER = "user"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(Enum(UserRole), default=UserRole.USER)
    history = Column(JSON, default=list)

    mcqs = relationship("MCQ", back_populates="owner")