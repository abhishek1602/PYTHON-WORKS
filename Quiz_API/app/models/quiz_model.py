from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()

class SportsQuiz(Base):
    __tablename__ = 'sports_quiz'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    quiz_id = Column(Integer, ForeignKey('quiz.id'))
    options = Column(JSONB)
    answer = Column(String)
    explanation = Column(String)
    image_url = Column(String)
    difficulty = Column(String)
    quiz = relationship('Quiz', back_populates='sports_quiz')

class TechQuiz(Base):
    __tablename__ = 'tech_quiz'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    quiz_id = Column(Integer, ForeignKey('quiz.id'))
    options = Column(JSONB)
    answer = Column(String)
    explanation = Column(String)
    image_url = Column(String)
    difficulty = Column(String)
    quiz = relationship('Quiz', back_populates='tech_quiz')

class ScienceQuiz(Base):
    __tablename__ = 'science_quiz'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    quiz_id = Column(Integer, ForeignKey('quiz.id'))
    options = Column(JSONB)
    answer = Column(String)
    explanation = Column(String)
    image_url = Column(String)
    difficulty = Column(String)
    quiz = relationship('Quiz', back_populates='science_quiz')