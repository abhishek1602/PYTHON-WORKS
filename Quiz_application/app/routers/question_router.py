from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.quiz_schema import QuestionCreate, QuestionSchema, QuestionUpdateSchema
from app.services.question_service import QuestionService
from app.config.database import get_db

router = APIRouter()

question_service = QuestionService()

@router.post("/", response_model=QuestionSchema)
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    return question_service.create_question(db, question)

@router.get("/{question_id}", response_model=QuestionSchema)
def get_question_by_id(question_id: int, db: Session = Depends(get_db)):
    question = question_service.get_question_by_id(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@router.get("/", response_model=list[QuestionSchema])
def get_all_questions(db: Session = Depends(get_db)):
    return question_service.get_all_questions(db)

@router.patch("/{question_id}", response_model=QuestionSchema)
def update_question(question_id: int, question: QuestionUpdateSchema, db: Session = Depends(get_db)):
    return question_service.update_question(db, question_id, question)

@router.delete("/{question_id}", response_model=bool)
def delete_question(question_id: int, db: Session = Depends(get_db)):
    return question_service.delete_question(db, question_id)
