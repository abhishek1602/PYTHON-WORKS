from sqlalchemy.orm import Session
from app.models.quiz_model import Quiz, Question, Attempted
from app.schemas.quiz_schema import QuizCreate, QuizUpdate, AttemptedCreate

def create_quiz(db: Session, quiz_data: QuizCreate, user_id: int):
    quiz = Quiz(title=quiz_data.title, description=quiz_data.description, user_id=user_id)
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    for question_data in quiz_data.questions:
        question = Question(**question_data.model_dump(), quiz_id=quiz.id)
        db.add(question)
    db.commit()
    return quiz

def get_quiz(db: Session, quiz_id: int):
    return db.query(Quiz).filter(Quiz.id == quiz_id).first()

def get_all_quizzes(db: Session):
    return db.query(Quiz).all()

def update_quiz(db: Session, quiz_id: int, quiz_data: QuizUpdate):
    quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
    if not quiz:
        return None
    for key, value in quiz_data.model_dump(exclude_unset=True).items():
        setattr(quiz, key, value)
    db.commit()
    db.refresh(quiz)
    return quiz

def delete_quiz(db: Session, quiz_id: int):
    quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
    if not quiz:
        return None
    db.delete(quiz)
    db.commit()
    return quiz

def create_attempt(db: Session, attempt_data: AttemptedCreate, user_id: int, quiz_id: int):
    attempt = Attempted(**attempt_data.model_dump(), user_id=user_id, quiz_id=quiz_id)
    db.add(attempt)
    db.commit()
    db.refresh(attempt)
    return attempt

def get_attempts_by_user(db: Session, user_id: int):
    return db.query(Attempted).filter(Attempted.user_id == user_id).all()

def get_attempts_by_quiz(db: Session, quiz_id: int):
    return db.query(Attempted).filter(Attempted.quiz_id == quiz_id).all()
