from sqlalchemy.orm import Session
from models import MCQ

class MCQRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_mcq(self, mcq_data):
        mcq = MCQ(**mcq_data)
        self.session.add(mcq)
        self.session.commit()
        return mcq

    def get_mcq(self, mcq_id):
        return self.session.query(MCQ).filter(MCQ.id == mcq_id).first()

    def update_mcq(self, mcq_id, mcq_data):
        mcq = self.get_mcq(mcq_id)
        if mcq:
            for key, value in mcq_data.items():
                setattr(mcq, key, value)
            self.session.commit()
        return mcq

    def delete_mcq(self, mcq_id):
        mcq = self.get_mcq(mcq_id)
        if mcq:
            self.session.delete(mcq)
            self.session.commit()
            return True
        return False

    def get_all_mcqs(self):
        return self.session.query(MCQ).all()

    def get_mcqs_by_category(self, category):
        return self.session.query(MCQ).filter(MCQ.category == category).all()

    def get_mcqs_by_difficulty(self, difficulty):
        return self.session.query(MCQ).filter(MCQ.difficulty == difficulty).all()