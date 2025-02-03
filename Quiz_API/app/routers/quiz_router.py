from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.quiz_schemas import (
    Difficulty, ScienceQuizCreate, ScienceQuizResponse, ScienceQuizUpdate, 
    SportsQuizCreate, SportsQuizResponse, SportsQuizUpdate, 
    TechQuizCreate, TechQuizResponse, TechQuizUpdate)
from app.models.quiz_model import ScienceQuiz, SportsQuiz, TechQuiz
from app.services.quiz_services import (
    get_all_science_quiz, get_all_sports_quiz, get_all_tech_quiz,
    get_science_quiz, get_sports_quiz, get_tech_quiz,
    get_science_quiz_by_difficulty, get_sports_quiz_by_difficulty, get_tech_quiz_by_difficulty,
    create_science_quiz, create_sports_quiz, create_tech_quiz,
    update_science_quiz, update_sports_quiz, update_tech_quiz,
    delete_science_quiz, delete_sports_quiz, delete_tech_quiz)

from app.config.database import get_db

router = APIRouter()

#Science Quiz

@router.get('/science_quiz', response_model=list[ScienceQuizResponse])
def get_all_science_quizzes(db: Session = Depends(get_db)):
    return get_all_science_quiz(db)

@router.get('/science_quiz/{quiz_id}', response_model=ScienceQuizResponse)
def get_science_quiz_by_id(quiz_id: int, db: Session = Depends(get_db)):
    quiz = get_science_quiz(db, quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail='Quiz not found')
    return quiz

@router.get('/science_quiz/difficulty/{difficulty}', response_model=list[ScienceQuizResponse])
def get_all_science_quizzes_by_difficulty(difficulty:Difficulty , db: Session = Depends(get_db)):
    return get_science_quiz_by_difficulty(db, difficulty)

@router.post('/science_quiz', response_model=ScienceQuiz)
def add_science_quiz(quiz: ScienceQuizCreate, db: Session = Depends(get_db)):
    return create_science_quiz(db, quiz)

@router.patch('/science_quiz/{quiz_id}', response_model= ScienceQuizResponse)
def modify_science_quiz(quiz_id: int, quiz_update = ScienceQuizUpdate, db: Session= Depends(get_db)):
    quiz = update_science_quiz(db, quiz_id, quiz_update)
    if not quiz:
        raise HTTPException(status_code=404, detail='Quiz not found')
    return quiz

@router.delete('science/{quiz_id}')