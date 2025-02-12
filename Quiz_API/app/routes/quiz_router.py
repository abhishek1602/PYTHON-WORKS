from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services.quiz_service import (
    create_new_quiz, fetch_quiz, fetch_all_quizzes, modify_quiz, remove_quiz
)
from app.schemas.quiz_schema import QuizCreate, QuizUpdate, Quiz
from typing import List

router = APIRouter()

@router.post("/", response_model=Quiz)
def create_quiz(quiz_data: QuizCreate, user_id: int, db: Session = Depends(get_db)):
    return create_new_quiz(db, quiz_data, user_id)

@router.get("/{quiz_id}", response_model=Quiz)
def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    quiz = fetch_quiz(db, quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz

@router.get("/", response_model=List[Quiz])
def get_all_quizzes(db: Session = Depends(get_db)):
    return fetch_all_quizzes(db)

@router.put("/{quiz_id}", response_model=Quiz)
def update_quiz(quiz_id: int, quiz_data: QuizUpdate, db: Session = Depends(get_db)):
    quiz = modify_quiz(db, quiz_id, quiz_data)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz

@router.delete("/{quiz_id}")
def delete_quiz(quiz_id: int, db: Session = Depends(get_db)):
    quiz = remove_quiz(db, quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return {"message": "Quiz deleted successfully"}
