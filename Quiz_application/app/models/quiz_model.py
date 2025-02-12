from sqlalchemy import Column, Integer, String, JSON, Table, ForeignKey, TIMESTAMP, Float, Enum as SQLAEnum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func
from enum import Enum

Base = declarative_base()

#Quiz

class Category(str, Enum):
    SCIENCE = "SCIENCE"
    TECHNOLOGY = "TECHNOLOGY"
    SPORTS = "SPORTS"

class DifficultyLevel(str, Enum):
    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"

quiz_union = Table(
    'quiz_union',
    Base.metadata,
    Column('quiz_id', Integer, ForeignKey('quizzes.id'), primary_key=True),
    Column('question_id', Integer, ForeignKey('questions.id'), primary_key=True)
)

class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    category = Column(SQLAEnum(Category, name="category_enum"), nullable=False)
    difficulty = Column(SQLAEnum(DifficultyLevel, name="difficulty_enum"), nullable=False)
    questions = relationship("Question", secondary=quiz_union, back_populates="quizzes")

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    question_text = Column(String, nullable=False)
    options = Column(JSON, nullable=False)
    category = Column(SQLAEnum(Category, name="category_enum"), nullable=False)
    correct_option = Column(String, nullable=False)
    difficulty = Column(SQLAEnum(DifficultyLevel, name="difficulty_enum"), nullable=False)
    quizzes = relationship("Quiz", secondary=quiz_union, back_populates="questions")


#Users

class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(SQLAEnum(UserRole), default=UserRole.USER)

#Attempt

class UserAnswer(Base):
    __tablename__ = "user_answers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    quiz_attempt_id = Column(Integer, ForeignKey('quiz_attempts.id'), nullable=False)
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=False)
    selected_option = Column(String, nullable=False)

    quiz_attempt = relationship("QuizAttempt", back_populates="user_answers")
    question = relationship("Question")


class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'), nullable=False)
    score = Column(Float, nullable=False)
    attempted_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    user = relationship("User", back_populates="quiz_attempts")
    quiz = relationship("Quiz", back_populates="quiz_attempts")
    user_answers = relationship("UserAnswer", back_populates="quiz_attempt", cascade="all, delete-orphan")

User.quiz_attempts = relationship("QuizAttempt", back_populates="user")
Quiz.quiz_attempts = relationship("QuizAttempt", back_populates="quiz")