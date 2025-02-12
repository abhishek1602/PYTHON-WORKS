from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services.question_service import (
    add_question, fetch_question, fetch_questions_by_quiz, modify_question, remove_question
)
from app.schemas.quiz_schema import QuestionCreate, Question
from typing import List

router = APIRouter()

@router.post("/", response_model=Question)
def create_question(question_data: QuestionCreate, quiz_id: int, db: Session = Depends(get_db)):
    return add_question(db, question_data, quiz_id)

@router.get("/{question_id}", response_model=Question)
def get_question(question_id: int, db: Session = Depends(get_db)):
    question = fetch_question(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@router.get("/quiz/{quiz_id}", response_model=List[Question])
def get_questions_by_quiz(quiz_id: int, db: Session = Depends(get_db)):
    return fetch_questions_by_quiz(db, quiz_id)

@router.put("/{question_id}", response_model=Question)
def update_question(question_id: int, question_data: dict, db: Session = Depends(get_db)):
    question = modify_question(db, question_id, question_data)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@router.delete("/{question_id}")
def delete_question(question_id: int, db: Session = Depends(get_db)):
    question = remove_question(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return {"message": "Question deleted successfully"}
