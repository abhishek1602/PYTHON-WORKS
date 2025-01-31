from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default='user')
    attempts = relationship('AttemptedQuiz', backref='user')

class MCQ(Base):
    __tablename__ = 'mcqs'
    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    option1 = Column(String, nullable=False)
    option2 = Column(String, nullable=False)
    option3 = Column(String, nullable=False)
    option4 = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)
    category = Column(String, nullable=False)
    explanation = Column(Text, nullable=True)
    image_url = Column(String, nullable=True)
    audio_url = Column(String, nullable=True)

class AttemptedQuiz(Base):
    __tablename__ = 'attempted_quizzes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    mcq_id = Column(Integer, ForeignKey('mcqs.id'), nullable=False)
    score = Column(Float, nullable=False)
    timestamp = Column(Integer, nullable=False)  # Store timestamp for quiz attempt

class Leaderboard(Base):
    __tablename__ = 'leaderboard'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    score = Column(Float, nullable=False)