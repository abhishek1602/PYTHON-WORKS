from sqlalchemy.orm import Session
from app.models.quiz_model import SportsQuiz, TechQuiz, ScienceQuiz
from app.schemas.quiz_schemas import (
    SportsQuizCreate, TechQuizCreate, ScienceQuizCreate, 
    SportsQuizUpdate, TechQuizUpdate, ScienceQuizUpdate)
from app.repositories.quiz_repository import (
    get_all_science_quiz, get_all_sports_quiz, get_all_tech_quiz, 
    get_science_quiz, get_sports_quiz, get_tech_quiz,
    get_science_quiz_by_difficulty, get_sports_quiz_by_difficulty, get_tech_quiz_by_difficulty, 
    science_quiz_create, sports_quiz_create, tech_quiz_create, 
    update_science_quiz, update_sports_quiz, update_tech_quiz, 
    delete_science_quiz, delete_sports_quiz, delete_tech_quiz)

#Sports Quiz

def create_sports_quiz(db: Session, quiz: SportsQuizCreate) -> SportsQuiz:
    return sports_quiz_create(db, quiz)

def get_sports_quiz_by_id(db: Session, quiz_id: int) -> SportsQuiz:
    return get_sports_quiz(db, quiz_id)

def get_all_sports_quizzes_by_difficulty(db: Session, difficulty: str) -> list[SportsQuiz]:
    return get_sports_quiz_by_difficulty(db, difficulty)

def get_all_sports_quizzes(db: Session) -> list[SportsQuiz]:
    return get_all_sports_quiz(db)

def update_sports_quiz_by_id(db: Session, quiz_id: int, quiz: SportsQuizUpdate) -> SportsQuiz:
    return update_sports_quiz(db, quiz_id, quiz)

def delete_sports_quiz_by_id(db: Session, quiz_id: int) -> SportsQuiz:
    return delete_sports_quiz(db, quiz_id)


#Tech Quiz

def create_tech_quiz(db: Session, quiz: TechQuizCreate) -> TechQuiz:
    return tech_quiz_create(db, quiz)

def get_tech_quiz_by_id(db: Session, quiz_id: int) -> TechQuiz:
    return get_tech_quiz(db, quiz_id)

def get_all_tech_quizzes_by_difficulty(db: Session, difficulty: str) -> list[TechQuiz]:
    return get_tech_quiz_by_difficulty(db, difficulty)

def get_all_tech_quizzes(db: Session) -> list[TechQuiz]:
    return get_all_tech_quiz(db)

def update_tech_quiz_by_id(db: Session, quiz_id: int, quiz: TechQuizUpdate) -> TechQuiz:
    return update_tech_quiz(db, quiz_id, quiz)

def delete_tech_quiz_by_id(db: Session, quiz_id: int) -> TechQuiz:
    return delete_tech_quiz(db, quiz_id)


#Science Quiz

def create_science_quiz(db: Session, quiz: ScienceQuizCreate) -> ScienceQuiz:
    return science_quiz_create(db, quiz)

def get_science_quiz_by_id(db: Session, quiz_id: int) -> ScienceQuiz:
    return get_science_quiz(db, quiz_id)

def get_all_science_quizzes_by_difficulty(db: Session, difficulty: str) -> list[ScienceQuiz]:
    return get_science_quiz_by_difficulty(db, difficulty)

def get_all_science_quizzes(db: Session) -> list[ScienceQuiz]:
    return get_all_science_quiz(db)

def update_science_quiz_by_id(db: Session, quiz_id: int, quiz: ScienceQuizUpdate) -> ScienceQuiz:
    return update_science_quiz(db, quiz_id, quiz)

def delete_science_quiz_by_id(db: Session, quiz_id: int) -> ScienceQuiz:
    return delete_science_quiz(db, quiz_id)

