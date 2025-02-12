from sqlalchemy.orm import Session
from app.repositories.quiz_attempt_repository import create_quiz_attempt, get_quiz_attempts
from app.schemas.quiz_schema import QuizAttemptCreate, QuizAttempt
from typing import List

def attempt_quiz(db: Session, quiz_attempt: QuizAttemptCreate, user_id: int) -> QuizAttempt:
    return create_quiz_attempt(db, quiz_attempt, user_id)

def retrieve_quiz_attempts(db: Session, user_id: int) -> List[QuizAttempt]:
    return get_quiz_attempts(db, user_id)
