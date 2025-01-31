from sqlalchemy.orm import Session
from app.db.models.mcq import MCQ
from app.schemas.mcq import MCQCreate, MCQUpdate
from typing import List, Optional
import random

class MCQCRUD:
    def __init__(self, db: Session):
        self.db = db

    def create_mcq(self, mcq: MCQCreate) -> MCQ:
        db_mcq = MCQ(**mcq.dict())
        self.db.add(db_mcq)
        self.db.commit()
        self.db.refresh(db_mcq)
        return db_mcq

    def get_mcq(self, mcq_id: int) -> Optional[MCQ]:
        return self.db.query(MCQ).filter(MCQ.id == mcq_id).first()

    def get_mcqs(self, skip: int = 0, limit: int = 20, category: Optional[str] = None, difficulty: Optional[str] = None) -> List[MCQ]:
        query = self.db.query(MCQ)
        if category:
            query = query.filter(MCQ.category == category)
        if difficulty:
            query = query.filter(MCQ.difficulty == difficulty)
        return query.offset(skip).limit(limit).all()

    def update_mcq(self, mcq_id: int, mcq: MCQUpdate) -> Optional[MCQ]:
        db_mcq = self.get_mcq(mcq_id)
        if db_mcq:
            for key, value in mcq.dict(exclude_unset=True).items():
                setattr(db_mcq, key, value)
            self.db.commit()
            self.db.refresh(db_mcq)
            return db_mcq
        return None

    def delete_mcq(self, mcq_id: int) -> Optional[MCQ]:
        db_mcq = self.get_mcq(mcq_id)
        if db_mcq:
            self.db.delete(db_mcq)
            self.db.commit()
            return db_mcq
        return None

    def get_random_mcqs(self, category: Optional[str] = None, difficulty: Optional[str] = None, count: int = 20) -> List[MCQ]:
        query = self.db.query(MCQ)
        if category:
            query = query.filter(MCQ.category == category)
        if difficulty:
            query = query.filter(MCQ.difficulty == difficulty)
        mcqs = query.all()
        return random.sample(mcqs, min(count, len(mcqs))) if mcqs else []