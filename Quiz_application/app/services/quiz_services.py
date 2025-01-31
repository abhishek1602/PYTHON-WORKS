from sqlalchemy.orm import Session
from app.model.model import MCQ
from app.schemas.mcq_schemas import QuestionCreate, QuestionUpdate, MCQBase, MCQUpdate
from app.repositories.quiz_repository import Question, Quiz

def add_mcq(db: Session, mcq: QuestionCreate):
    return Question.add_mcq(db, mcq)

def update_mcq(db: Session, mcq: MCQ, mcq_update: QuestionUpdate):
    return Question.update_mcq(db, mcq, mcq_update)

def get_mcq(db: Session, mcq_id: int):
    return Question.get_mcq(db, mcq_id)

def get_mcqs(db: Session, skip: int = 0, limit: int = 10):
    return Question.get_mcqs(db, skip, limit)

def add_quiz(db: Session, quiz: MCQBase):
    return Quiz.add_quiz(db, quiz)

def update_quiz(db: Session, quiz: MCQ, quiz_update: MCQUpdate):
    return Quiz.update_quiz(db, quiz, quiz_update)

def get_quiz(db: Session, quiz_id: int):
    return Quiz.get_quiz(db, quiz_id)

def get_quiz_by_heading(db: Session, heading: str):
    return Quiz.get_quiz_by_heading(db, heading)

