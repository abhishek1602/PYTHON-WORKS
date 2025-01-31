from sqlalchemy.orm import Session
from app.model.model import MCQ
from app.schemas.mcq_schemas import QuestionCreate, QuestionUpdate, MCQBase, MCQUpdate

class Question:

    def add_mcq(db: Session, mcq: QuestionCreate):
        mcq = MCQ(**mcq.model_dump())
        db.add(mcq)
        db.commit()
        db.refresh(mcq)
        return mcq

    def update_mcq(db: Session, mcq: MCQ, mcq_update: QuestionUpdate):
        for key, value in mcq_update.model_dump(exclude_none=True).items():
            setattr(mcq, key, value)
        db.commit()
        db.refresh(mcq)
        return mcq
    
    def get_mcq(db: Session, mcq_id: int):
        return db.query(MCQ).filter(MCQ.id == mcq_id).first()

    def get_mcqs(db: Session, skip: int = 0, limit: int = 10):
        return db.query(MCQ).offset(skip).limit(limit).all()


class Quiz:

    def add_quiz(db: Session, quiz: MCQBase):
        quiz = MCQ(**quiz.model_dump())
        db.add(quiz)
        db.commit()
        db.refresh(quiz)
        return quiz
    
    def update_quiz(db: Session, quiz: MCQ, quiz_update: MCQUpdate):
        for key, value in quiz_update.model_dump(exclude_none=True).items():
            setattr(quiz, key, value)
        db.commit()
        db.refresh(quiz)
        return quiz
    
    def get_quiz(db: Session, quiz_id: int):
        return db.query(MCQ).filter(MCQ.id == quiz_id).first()
    
    def get_quiz_by_heading(db: Session, heading: str):
        return db.query(MCQ).filter(MCQ.heading == heading).first()
