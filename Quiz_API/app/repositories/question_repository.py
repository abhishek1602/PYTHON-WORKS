from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from app.models.quiz_model import Question, Attempted
from app.schemas.quiz_schema import QuestionCreate
from app.models.quiz_model import Category, Difficulty

def create_question(db: Session, question_data: QuestionCreate, quiz_id: int):
    question = Question(**question_data.model_dump(), quiz_id=quiz_id)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

def get_question(db: Session, question_id: int):
    return db.query(Question).filter(Question.id == question_id).first()

def get_questions_by_quiz(db: Session, quiz_id: int):
    return db.query(Question).filter(Question.quiz_id == quiz_id).all()

def get_questions_by_category(db: Session, category: Category):
    return db.query(Question).filter(Question.category == category).all()

def get_questions_by_difficulty(db: Session, difficulty: Difficulty):
    return db.query(Question).filter(Question.difficulty == difficulty).all()

def get_random_questions(db: Session, quiz_id: int, limit: int = 5):
    return db.query(Question).filter(Question.quiz_id == quiz_id).order_by(func.random()).limit(limit).all()

def update_question(db: Session, question_id: int, question_data: dict):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        return None
    for key, value in question_data.items():
        setattr(question, key, value)
    db.commit()
    db.refresh(question)
    return question

def delete_question(db: Session, question_id: int):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        return None
    db.delete(question)
    db.commit()
    return question

def get_hint(db: Session, question_id: int):
    question = db.query(Question).filter(Question.id == question_id).first()
    return question.hint if question else None
