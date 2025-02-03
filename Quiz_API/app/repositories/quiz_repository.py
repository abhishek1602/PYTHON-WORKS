from sqlalchemy.orm import Session
from app.models.quiz_model import SportsQuiz, TechQuiz, ScienceQuiz
from app.schemas.quiz_schemas import (
    SportsQuizCreate, TechQuizCreate, ScienceQuizCreate, 
    SportsQuizUpdate, TechQuizUpdate, ScienceQuizUpdate)

#Sports Quiz

def sports_quiz_create(db: Session, quiz: SportsQuizCreate) -> SportsQuiz:
    new_quiz = SportsQuiz(**quiz.model_dump())
    db.add(new_quiz)
    db.commit()
    db.refresh(new_quiz)
    return new_quiz

def get_sports_quiz(db: Session, quiz_id: int) -> SportsQuiz:
    return db.query(SportsQuiz).filter(SportsQuiz.id == quiz_id).first()

def get_sports_quiz_by_difficulty(db: Session, difficulty: str) -> list[SportsQuiz]:
    return db.query(SportsQuiz).filter(SportsQuiz.difficulty == difficulty).all()

def get_all_sports_quiz(db: Session) -> list[SportsQuiz]:
    return db.query(SportsQuiz).all()

def update_sports_quiz(db: Session, quiz_id: int, quiz: SportsQuizUpdate) -> SportsQuiz:
    quiz_to_update = db.query(SportsQuiz).filter(SportsQuiz.id == quiz_id).first()
    for key, value in quiz.model_dump(exclude_none= True).items():
        setattr(quiz_to_update, key, value)
    db.commit()
    db.refresh(quiz_to_update)
    return quiz_to_update

def delete_sports_quiz(db: Session, quiz_id: int) -> SportsQuiz:
    quiz_to_delete = db.query(SportsQuiz).filter(SportsQuiz.id == quiz_id).first()
    db.delete(quiz_to_delete)
    db.commit()
    return quiz_to_delete


#Tech Quiz

def tech_quiz_create(db: Session, quiz: TechQuizCreate) -> TechQuiz:
    new_quiz = TechQuiz(**quiz.model_dump())
    db.add(new_quiz)
    db.commit()
    db.refresh(new_quiz)
    return new_quiz

def get_tech_quiz(db: Session, quiz_id: int) -> TechQuiz:
    return db.query(TechQuiz).filter(TechQuiz.id == quiz_id).first()

def get_tech_quiz_by_difficulty(db: Session, difficulty: str) -> list[TechQuiz]:
    return db.query(TechQuiz).filter(TechQuiz.difficulty == difficulty).all()

def get_all_tech_quiz(db: Session) -> list[TechQuiz]:
    return db.query(TechQuiz).all()

def update_tech_quiz(db: Session, quiz_id: int, quiz: TechQuizUpdate) -> TechQuiz:
    quiz_to_update = db.query(TechQuiz).filter(TechQuiz.id == quiz_id).first()
    for key, value in quiz.model_dump(exclude_none= True).items():
        setattr(quiz_to_update, key, value)
    db.commit()
    db.refresh(quiz_to_update)
    return quiz_to_update

def delete_tech_quiz(db: Session, quiz_id: int) -> TechQuiz:
    quiz_to_delete = db.query(TechQuiz).filter(TechQuiz.id == quiz_id).first()
    db.delete(quiz_to_delete)
    db.commit()
    return quiz_to_delete


#Science Quiz

def science_quiz_create(db: Session, quiz: ScienceQuizCreate) -> ScienceQuiz:
    new_quiz = ScienceQuiz(**quiz.model_dump())
    db.add(new_quiz)
    db.commit()
    db.refresh(new_quiz)
    return new_quiz

def get_science_quiz(db: Session, quiz_id: int) -> ScienceQuiz:
    return db.query(ScienceQuiz).filter(ScienceQuiz.id == quiz_id).first()

def get_science_quiz_by_difficulty(db: Session, difficulty: str) -> list[ScienceQuiz]:
    return db.query(ScienceQuiz).filter(ScienceQuiz.difficulty == difficulty).all()

def get_all_science_quiz(db: Session) -> list[ScienceQuiz]:
    return db.query(ScienceQuiz).all()

def update_science_quiz(db: Session, quiz_id: int, quiz: ScienceQuizUpdate) -> ScienceQuiz:
    quiz_to_update = db.query(ScienceQuiz).filter(ScienceQuiz.id == quiz_id).first()
    for key, value in quiz.model_dump(exclude_none= True).items():
        setattr(quiz_to_update, key, value)
    db.commit()
    db.refresh(quiz_to_update)
    return quiz_to_update

def delete_science_quiz(db: Session, quiz_id: int) -> ScienceQuiz:
    quiz_to_delete = db.query(ScienceQuiz).filter(ScienceQuiz.id == quiz_id).first()
    db.delete(quiz_to_delete)
    db.commit()
    return quiz_to_delete