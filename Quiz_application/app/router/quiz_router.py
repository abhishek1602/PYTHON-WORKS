from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.mcq_schemas import QuestionCreate, QuestionUpdate, MCQBase, MCQUpdate
from app.services.quiz_services import add_mcq, update_mcq, get_mcq, get_mcqs, add_quiz, update_quiz, get_quiz, get_quiz_by_heading

router = APIRouter()

@router.post("/mcq/", response_model=MCQBase)
def create_mcq(mcq: QuestionCreate, db: Session = Depends(get_db)):
    return add_mcq(db, mcq)

@router.put("/mcq/{mcq_id}", response_model=MCQBase)
def update_mcq(mcq_id: int, mcq_update: QuestionUpdate, db: Session = Depends(get_db)):
    mcq = get_mcq(db, mcq_id)
    if mcq is None:
        raise HTTPException(status_code=404, detail="MCQ not found")
    return update_mcq(db, mcq, mcq_update)

@router.get("/mcq/{mcq_id}", response_model=MCQBase)
def read_mcq(mcq_id: int, db: Session = Depends(get_db)):
    mcq = get_mcq(db, mcq_id)
    if mcq is None:
        raise HTTPException(status_code=404, detail="MCQ not found")
    return mcq

@router.get("/mcqs/", response_model=list[MCQBase])
def read_mcqs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_mcqs(db, skip, limit)

@router.post("/quiz/", response_model=MCQBase)
def create_quiz(quiz: MCQBase, db: Session = Depends(get_db)):
    return add_quiz(db, quiz)

