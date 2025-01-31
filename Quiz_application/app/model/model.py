from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    role = Column(String, default='user')   
    history = relationship('AttempetedQuiz', backref='user')


class MCQ(Base):
    __tablename__ = 'mcqs'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    options = Column(JSONB)
    answer = Column(String)
    difficulty = Column(String)
    category = Column(String)
    explanation = Column(Text)
    image_url = Column(String, nullable=True)


class AttemptedQuiz(Base):
    __tablename__ = 'quiz_histories'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    score = Column(Integer)
    percecntage = Column(Integer)
    questions_answered = Column(Integer)
    correct_answers = Column(Integer)  

    user = relationship('User', backref='quiz_histories')