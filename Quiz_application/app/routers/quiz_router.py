from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.auth import get_current_user, get_current_admin
from app.schemas.quiz_schema import QuizCreateRequest, QuizResponse, QuestionSchema, Category, DifficultyLevel
from app.services.quiz_service import QuizService
from app.config.database import get_db
from app.models.quiz_model import User

router = APIRouter()

quiz_service = QuizService()

@router.post("/", response_model=QuizResponse)
def create_quiz(quiz: QuizCreateRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin)):
    return quiz_service.create_quiz(db, quiz)

@router.get("/page", response_model=list[QuizResponse])
def get_paginated_quizzes(page: int, page_size: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return quiz_service.get_paginated_quizzes(db, page, page_size)

@router.get("/random", response_model=list[QuestionSchema])
def get_random_questions(count: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return quiz_service.get_random_questions(db, count)

@router.get("/{quiz_id}", response_model=QuizResponse)
def get_quiz_by_id(quiz_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    quiz = quiz_service.get_quiz_by_id(db, quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz

@router.get("/", response_model=list[QuizResponse])
def get_all_quizzes(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return quiz_service.get_all_quizzes(db)

@router.put("/{quiz_id}", response_model=QuizResponse)
def update_quiz(quiz_id: int, quiz: QuizCreateRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin)):
    return quiz_service.update_quiz(db, quiz_id, quiz)

@router.delete("/{quiz_id}", response_model=bool)
def delete_quiz(quiz_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin)):
    return quiz_service.delete_quiz(db, quiz_id)

@router.get("/category/{category}/difficulty/{difficulty}", response_model=list[QuestionSchema])
def get_quiz_questions_by_category_and_difficulty(category: Category, difficulty: DifficultyLevel, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return quiz_service.get_quiz_questions_by_category_and_difficulty(db, category, difficulty)



