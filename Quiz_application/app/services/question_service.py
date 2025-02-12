from sqlalchemy.orm import Session
from app.repositories.question_repository import QuestionRepository
from app.schemas.quiz_schema import QuestionCreate, QuestionSchema


class QuestionService:
    def __init__(self):
        self.question_repository = QuestionRepository()

    def create_question(self, db: Session, question: QuestionCreate) -> QuestionSchema:
        return self.question_repository.create_question(db, question)

    def get_question_by_id(self, db: Session, question_id: int) -> QuestionSchema:
        return self.question_repository.get_question_by_id(db, question_id)

    def update_question(self, db: Session, question_id: int, question: QuestionCreate) -> QuestionSchema:
        return self.question_repository.update_question(db, question_id, question)

    def delete_question(self, db: Session, question_id: int) -> bool:
        return self.question_repository.delete_question(db, question_id)

    def get_all_questions(self, db: Session) -> list[QuestionSchema]:
        return self.question_repository.get_all_questions(db)