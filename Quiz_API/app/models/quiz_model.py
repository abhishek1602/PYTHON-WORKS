from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PyEnum

Base = declarative_base()

class Category(PyEnum):
    science = "science"
    technical = "technical"
    sports = "sports"
    mixed = "mixed"

class Difficulty(PyEnum):
    easy = "easy"
    medium = "medium"
    hard = "hard"

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    question = Column(String)
    option_a = Column(String)
    option_b = Column(String)
    option_c = Column(String)
    option_d = Column(String)
    correct_answer = Column(String)
    category = Column(Enum(Category), default=Category.mixed)
    difficulty = Column(Enum(Difficulty), default=Difficulty.easy)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    quiz = relationship("Quiz", back_populates="questions")

class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="quizzes")
    questions = relationship("Question", back_populates="quiz")

class Attempted(Base):
    __tablename__ = "attempted"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    score = Column(Integer)
    attempted_at = Column(DateTime, default=datetime.utcnow)
    user_responses = Column(String) 
    user = relationship("User", back_populates="attempts")
    quiz = relationship("Quiz", back_populates="attempts")

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    quizzes = relationship("Quiz", back_populates="user")
    attempts = relationship("Attempted", back_populates="user")

Quiz.attempts = relationship("Attempted", back_populates="quiz")