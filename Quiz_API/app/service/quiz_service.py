from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi import HTTPException
from app.repository.quiz_repository import (
    get_quiz, get_quizzes, create_quiz, update_quiz, delete_quiz,
    create_question, get_questions, get_question, get_filtered_questions,
    create_attempted, get_attempted, get_quiz_selection
)
from app.schemas.quiz_schema import QuizCreate, QuizUpdate, QuestionCreate, AttemptedCreate, Category, Difficulty

# Quiz Services

def get_quiz_service(db: Session, quiz_id: int):
    quiz = get_quiz(db, quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz

def get_quizzes_service(db: Session, skip: int = 0, limit: int = 10):
    quizzes = get_quizzes(db, skip, limit)
    if not quizzes:
        raise HTTPException(status_code=404, detail="No quizzes found")
    return quizzes

def create_quiz_service(db: Session, quiz: QuizCreate, user_id: int):
    return create_quiz(db, quiz, user_id)

def update_quiz_service(db: Session, quiz_id: int, quiz: QuizUpdate):
    updated_quiz = update_quiz(db, quiz_id, quiz)
    if not updated_quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return updated_quiz

def delete_quiz_service(db: Session, quiz_id: int):
    deleted_quiz = delete_quiz(db, quiz_id)
    if not deleted_quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return deleted_quiz

def get_quiz_by_selecting(db: Session, category: Category, difficulty: Difficulty):
    quizzes = get_quiz_selection(db, category, difficulty)
    if not quizzes:
        raise HTTPException(status_code=404, detail="No quizzes found with the specified parameters")
    return quizzes

# Question Services

def create_question_service(db: Session, question: QuestionCreate, quiz_id: int):
    return create_question(db, question, quiz_id)

def get_question_service(db: Session, quiz_id: int):
    questions = get_question(db, quiz_id)
    if not questions:
        raise HTTPException(status_code=404, detail="No questions found for the specified quiz")
    return questions

def get_questions(db: Session, skip: int = 0, limit: int = 10):
    questions = get_questions(db, skip, limit)
    if not questions:
        raise HTTPException(status_code=404, detail="No questions found")
    return questions

def get_selected_questions(db: Session, category: Optional[str] = None, difficulty: Optional[str] = None):
    questions = get_filtered_questions(db, category, difficulty)
    if not questions:
        raise HTTPException(status_code=404, detail="No questions found with the specified parameters")
    return questions

# Attempted Services

def create_attempted_service(db: Session, attempted: AttemptedCreate, user_id: int, quiz_id: int):
    return create_attempted(db, attempted, user_id, quiz_id)

def get_attempted_service(db: Session, user_id: int, quiz_id: int):
    attempted = get_attempted(db, user_id, quiz_id)
    if not attempted:
        raise HTTPException(status_code=404, detail="No attempted records found for the specified user and quiz")
    return attempted