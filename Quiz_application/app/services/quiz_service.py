from sqlalchemy.orm import Session
from app.repositories.quiz_repository import QuizRepository
from app.schemas.quiz_schema import QuizCreateRequest, QuizResponse, QuestionSchema
from app.models.quiz_model import Category, DifficultyLevel

class QuizService:
    def __init__(self):
        self.quiz_repository = QuizRepository()

    def create_quiz(self, db: Session, quiz: QuizCreateRequest) -> QuizResponse:
        return self.quiz_repository.create_quiz(db, quiz)

    def get_quiz_by_id(self, db: Session, quiz_id: int) -> QuizResponse:
        return self.quiz_repository.get_quiz_by_id(db, quiz_id)

    def update_quiz(self, db: Session, quiz_id: int, quiz: QuizCreateRequest) -> QuizResponse:
        return self.quiz_repository.update_quiz(db, quiz_id, quiz)

    def delete_quiz(self, db: Session, quiz_id: int) -> bool:
        return self.quiz_repository.delete_quiz(db, quiz_id)

    def get_all_quizzes(self, db: Session) -> list[QuizResponse]:
        return self.quiz_repository.get_all_quizzes(db)

    def get_quiz_questions_by_category_and_difficulty(self, db: Session, category: Category, difficulty: DifficultyLevel) -> list[QuestionSchema]:
        return self.quiz_repository.get_quiz_questions_by_category_and_difficulty(db, category, difficulty)

    def get_random_questions(self, db: Session, count: int) -> list[QuestionSchema]:
        return self.quiz_repository.get_random_questions(db, count)

    def get_paginated_quizzes(self, db: Session, page: int, page_size: int) -> list[QuizResponse]:
        return self.quiz_repository.get_paginated_quizzes(db, page, page_size)




