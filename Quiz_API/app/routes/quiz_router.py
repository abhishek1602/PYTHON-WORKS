from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.quiz_schema import QuizCreate, QuizUpdate, QuestionCreate, AttemptedCreate, Category, Difficulty
from app.service.quiz_service import (
    get_quiz_service, get_quizzes_service, create_quiz_service, update_quiz_service, delete_quiz_service,
    create_question_service, get_question_service, get_questions, get_selected_questions,
    create_attempted_service, get_attempted_service, get_quiz_by_selecting
)

router = APIRouter()

# Quiz Endpoints

@router.get("/quizzes/{quiz_id}", tags=["quizzes"])
def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    return get_quiz_service(db, quiz_id)

@router.get("/quizzes", tags=["quizzes"])
def get_quizzes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_quizzes_service(db, skip, limit)

@router.post("/quizzes", tags=["quizzes"])
def create_quiz(quiz: QuizCreate, user_id: int, db: Session = Depends(get_db)):
    return create_quiz_service(db, quiz, user_id)

@router.put("/quizzes/{quiz_id}", tags=["quizzes"])
def update_quiz(quiz_id: int, quiz: QuizUpdate, db: Session = Depends(get_db)):
    return update_quiz_service(db, quiz_id, quiz)

@router.delete("/quizzes/{quiz_id}", tags=["quizzes"])
def delete_quiz(quiz_id: int, db: Session = Depends(get_db)):
    return delete_quiz_service(db, quiz_id)

@router.get("/quizzes/select", tags=["quizzes"])
def get_quizzes_by_selection(category: Category, difficulty: Difficulty, db: Session = Depends(get_db)):
    return get_quiz_by_selecting(db, category, difficulty)

# Question Endpoints

@router.post("/questions", tags=["questions"])
def create_question(question: QuestionCreate, quiz_id: int, db: Session = Depends(get_db)):
    return create_question_service(db, question, quiz_id)

@router.get("/questions/{quiz_id}", tags=["questions"])
def get_questions_by_quiz(quiz_id: int, db: Session = Depends(get_db)):
    return get_question_service(db, quiz_id)

@router.get("/questions", tags=["questions"])
def get_all_questions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_questions(db, skip, limit)

@router.get("/questions/filter", tags=["questions"])
def get_filtered_questions(category: str = None, difficulty: str = None, db: Session = Depends(get_db)):
    return get_selected_questions(db, category, difficulty)

# Attempted Endpoints

@router.post("/attempted", tags=["attempted"])
def create_attempted_attempt(attempted: AttemptedCreate, user_id: int, quiz_id: int, db: Session = Depends(get_db)):
    return create_attempted_service(db, attempted, user_id, quiz_id)

@router.get("/attempted/{user_id}/{quiz_id}", tags=["attempted"])
def get_attempted(user_id: int, quiz_id: int, db: Session = Depends(get_db)):
    return get_attempted_service(db, user_id, quiz_id)
