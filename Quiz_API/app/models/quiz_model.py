from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime
from enum import Enum as PyEnum

Base = declarative_base()

class Role(PyEnum):
    admin = "admin"
    user = "user"

class Category(PyEnum):
    science = "science"
    technical = "technical"
    sports = "sports"
    mixed = "mixed"

class Difficulty(PyEnum):
    easy = "easy"
    medium = "medium"
    hard = "hard"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(Enum(Role), default=Role.user)
    quizzes = relationship("Quiz", back_populates="user")
    attempts = relationship("Attempted", back_populates="user")

class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="quizzes")
    questions = relationship("Question", back_populates="quiz")
    attempts = relationship("Attempted", back_populates="quiz")

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)
    option_a = Column(String)
    option_b = Column(String)
    option_c = Column(String)
    option_d = Column(String)
    correct_answer = Column(String)
    category = Column(Enum(Category), default=Category.mixed)
    difficulty = Column(Enum(Difficulty), default=Difficulty.easy)
    hint = Column(String, nullable=True)
    explanation = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    audio_url = Column(String, nullable=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    quiz = relationship("Quiz", back_populates="questions")

class Attempted(Base):
    __tablename__ = "attempted"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    score = Column(Integer)
    attempted_at = Column(DateTime, default=datetime.utcnow)
    user_responses = Column(String)  
    user = relationship("User", back_populates="attempts")
    quiz = relationship("Quiz", back_populates="attempts")