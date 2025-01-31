from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import models, session
from app.schemas import mcq as mcq_schemas
from app.crud import mcq as mcq_crud
from app.core.security import get_current_user
from typing import List

router = APIRouter()

@router.get("/mcqs", response_model=List[mcq_schemas.MCQ])
def get_mcqs(skip: int = 0, limit: int = 20, db: Session = Depends(session.get_db)):
    return mcq_crud.get_mcqs(db=db, skip=skip, limit=limit)

@router.get("/mcqs/{mcq_id}", response_model=mcq_schemas.MCQ)
def get_mcq(mcq_id: int, db: Session = Depends(session.get_db)):
    mcq = mcq_crud.get_mcq(db=db, mcq_id=mcq_id)
    if mcq is None:
        raise HTTPException(status_code=404, detail="MCQ not found")
    return mcq

@router.post("/mcqs/submit", response_model=mcq_schemas.Score)
def submit_mcq_answers(answers: mcq_schemas.AnswerSubmission, db: Session = Depends(session.get_db), current_user: models.User = Depends(get_current_user)):
    score, percentage = mcq_crud.calculate_score(db=db, answers=answers, user_id=current_user.id)
    return {"score": score, "percentage": percentage}

@router.get("/mcqs/history", response_model=List[mcq_schemas.History])
def get_user_history(db: Session = Depends(session.get_db), current_user: models.User = Depends(get_current_user)):
    return mcq_crud.get_user_history(db=db, user_id=current_user.id)

@router.get("/mcqs/random/{category}", response_model=List[mcq_schemas.MCQ])
def get_random_mcqs(category: str, db: Session = Depends(session.get_db)):
    return mcq_crud.get_random_mcqs(db=db, category=category)

@router.post("/mcqs/bulk-upload", response_model=str)
def upload_mcqs(mcqs: List[mcq_schemas.MCQCreate], db: Session = Depends(session.get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to perform this action")
    mcq_crud.bulk_upload_mcqs(db=db, mcqs=mcqs)
    return "MCQs uploaded successfully"