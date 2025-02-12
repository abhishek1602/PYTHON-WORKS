from sqlalchemy.orm import Session
from app.models.quiz_model import QuizAttempt, Question
from app.schemas.quiz_schema import QuizAttemptCreate, UserAnswer

from app.models.quiz_model import QuizAttempt, UserAnswer, Question

def create_quiz_attempt(db: Session, quiz_attempt: QuizAttemptCreate, user_id: int):
    # Calculate score as a percentage
    correct_answers = db.query(Question).filter(Question.id.in_([answer.question_id for answer in quiz_attempt.user_answers])).all()
    total_questions = len(correct_answers)
    correct_count = sum(1 for answer in quiz_attempt.user_answers if answer.selected_option in [q.correct_option for q in correct_answers if q.id == answer.question_id])
    score_percentage = (correct_count / total_questions) * 100 if total_questions > 0 else 0

    db_quiz_attempt = QuizAttempt(
        user_id=user_id,
        quiz_id=quiz_attempt.quiz_id,
        score=score_percentage
    )
    db.add(db_quiz_attempt)
    db.commit()
    db.refresh(db_quiz_attempt)

    for answer in quiz_attempt.user_answers:
        db_user_answer = UserAnswer(
            quiz_attempt_id=db_quiz_attempt.id,
            question_id=answer.question_id,
            selected_option=answer.selected_option
        )
        db.add(db_user_answer)
    
    db.commit()
    db.refresh(db_quiz_attempt)
    return db_quiz_attempt


def get_quiz_attempts(db: Session, user_id: int):
    return db.query(QuizAttempt).filter(QuizAttempt.user_id == user_id).all()
