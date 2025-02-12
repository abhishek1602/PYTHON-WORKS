from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.quiz_schema import QuizAttempt, QuizAttemptCreate
from app.services.quiz_attempt_service import attempt_quiz, retrieve_quiz_attempts
from app.config.database import get_db
from typing import List
from app.utils.auth import get_current_user_id

router = APIRouter()

@router.post("/quiz_attempts/", response_model=QuizAttempt)
def create_quiz_attempt(quiz_attempt: QuizAttemptCreate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    return attempt_quiz(db, quiz_attempt, user_id)

@router.get("/quiz_attempts/", response_model=List[QuizAttempt])
def read_quiz_attempts(db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    return retrieve_quiz_attempts(db, user_id)