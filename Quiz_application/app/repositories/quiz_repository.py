from sqlalchemy.orm import Session
from app.models.quiz_model import Quiz, Question
from app.schemas.quiz_schema import QuizCreateRequest, QuizResponse, QuestionSchema
from app.models.quiz_model import Category, DifficultyLevel
import random

# Quiz Repository
class QuizRepository:

    def get_quiz_by_id(self, db: Session, quiz_id: int) -> QuizResponse:
        return db.query(Quiz).filter(Quiz.id == quiz_id).first()

    def create_quiz(self, db: Session, quiz: QuizCreateRequest) -> Quiz:
        db_quiz = Quiz(
            title=quiz.title,
            category=quiz.category,
            description=quiz.description,
            difficulty=quiz.difficulty,
            questions=[
                Question(
                    question_text=q.question_text,
                    options=q.options,
                    correct_option=q.correct_option,
                    category=q.category,
                    difficulty=q.difficulty,
                )
                for q in quiz.question_data
            ],
        )
        db.add(db_quiz)
        db.commit()
        db.refresh(db_quiz)
        return db_quiz

    def update_quiz(self, db: Session, quiz_id: int, updated_data: QuizCreateRequest) -> Quiz:
        quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
        if not quiz:
            return None

        quiz.title = updated_data.title
        quiz.category = updated_data.category
        quiz.description = updated_data.description
        quiz.difficulty = updated_data.difficulty
        quiz.questions = [
            Question(
                question_text=q.question_text,
                options=q.options,
                correct_option=q.correct_option,
                category=q.category,
                difficulty_level=q.difficulty,
            )
            for q in updated_data.question_data
        ]

        db.commit()
        db.refresh(quiz)
        return quiz

    def delete_quiz(self, db: Session, quiz_id: int) -> bool:
        quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
        if not quiz:
            return False

        db.delete(quiz)
        db.commit()
        return True

    def get_all_quizzes(self, db: Session) -> list[QuizResponse]:
        return db.query(Quiz).all()

    def get_quiz_questions_by_category_and_difficulty(self, db: Session, category: Category, difficulty: DifficultyLevel) -> list[QuestionSchema]:
        return db.query(Question).filter(Question.category == category, Question.difficulty == difficulty).all()

    def get_random_questions(self, db: Session, count: int) -> list[QuestionSchema]:
        questions = db.query(Question).all()
        return random.sample(questions, min(len(questions), count))

    def get_paginated_quizzes(self, db: Session, page: int, page_size: int) -> list[QuizResponse]:
        offset = (page - 1) * page_size
        return db.query(Quiz).offset(offset).limit(page_size).all()

