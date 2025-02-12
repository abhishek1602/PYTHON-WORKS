from sqlalchemy.orm import Session
from app.repositories.quiz_repository import (
    create_quiz, get_quiz, get_all_quizzes, update_quiz, delete_quiz
)
from app.schemas.quiz_schema import QuizCreate, QuizUpdate

def create_new_quiz(db: Session, quiz_data: QuizCreate, user_id: int):
    return create_quiz(db, quiz_data, user_id)

def fetch_quiz(db: Session, quiz_id: int):
    return get_quiz(db, quiz_id)

def fetch_all_quizzes(db: Session):
    return get_all_quizzes(db)

def modify_quiz(db: Session, quiz_id: int, quiz_data: QuizUpdate):
    return update_quiz(db, quiz_id, quiz_data.model_dump(exclude_unset=True))

def remove_quiz(db: Session, quiz_id: int):
    return delete_quiz(db, quiz_id)
