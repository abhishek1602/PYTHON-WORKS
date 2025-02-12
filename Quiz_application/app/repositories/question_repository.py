from sqlalchemy.orm import Session
from app.models.quiz_model import Question
from app.schemas.quiz_schema import QuestionCreate, QuestionSchema, QuestionUpdate

# Question Repository
class QuestionRepository:

    def get_question_by_id(self, db: Session, question_id: int) -> QuestionSchema:
        return db.query(Question).filter(Question.id == question_id).first()

    def create_question(self, db: Session, question: QuestionCreate) -> Question:
        db_question = Question(
            question_text=question.question_text,
            options=question.options,
            correct_option= question.correct_option,
            category=question.category,
            difficulty=question.difficulty,
        )
        db.add(db_question)
        db.commit()
        db.refresh(db_question)
        return db_question

    def update_question(self, db: Session, question_id: int, updated_data: QuestionUpdate) -> Question:
        question = db.query(Question).filter(Question.id == question_id).first()
        if not question:
            return None

        question_data = updated_data.model_dump(exclude_unset=True)
        for key, value in question_data.items():
            setattr(question, key, value)

        db.commit()
        db.refresh(question)
        return question

    def delete_question(self, db: Session, question_id: int) -> bool:
        question = db.query(Question).filter(Question.id == question_id).first()
        if not question:
            return False

        db.delete(question)
        db.commit()
        return True

    def get_all_questions(self, db: Session) -> list[QuestionSchema]:
        return db.query(Question).all()