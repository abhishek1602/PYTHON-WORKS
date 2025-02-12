from sqlalchemy.orm import Session
from app.repositories.question_repository import (
    create_question, get_question, get_questions_by_quiz, update_question, delete_question
)
from app.schemas.quiz_schema import QuestionCreate

def add_question(db: Session, question_data: QuestionCreate, quiz_id: int):
    return create_question(db, question_data, quiz_id)

def fetch_question(db: Session, question_id: int):
    return get_question(db, question_id)

def fetch_questions_by_quiz(db: Session, quiz_id: int):
    return get_questions_by_quiz(db, quiz_id)

def modify_question(db: Session, question_id: int, question_data: dict):
    return update_question(db, question_id, question_data)

def remove_question(db: Session, question_id: int):
    return delete_question(db, question_id)
