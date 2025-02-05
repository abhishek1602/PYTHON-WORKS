from sqlalchemy.orm import Session
from app.models.quiz_model import Quiz, Question, Attempted
from app.schemas.quiz_schema import (QuizCreate, QuizUpdate, 
    QuestionCreate, QuestionUpdate, 
    AttemptedCreate, Category, Difficulty)

#Quiz

def create_quiz(db:Session, quiz: QuizCreate, user_id: int):
    quiz_obj = Quiz(user_id=user_id, **quiz.model_dump())
    db.add(quiz_obj)
    db.commit()
    db.refresh(quiz_obj)    
    return quiz_obj

def get_quiz(db: Session, quiz_id: int):
    return db.query(Quiz).filter(Quiz.id == quiz_id).first()

def get_quiz_selection(db: Session, category: Category, difficulty: Difficulty):
    return db.query(Quiz).filter(Quiz.category == category, Quiz.difficulty == difficulty).all()

def get_quizzes(db:Session, skip: int = 0 , limit: int = 10):
    return db.query(Quiz).offset(skip).limit(limit).all()

def update_quiz(db: Session, quiz_id: int, quiz = QuizUpdate):
    quiz_obj = db.query(Quiz).filter(Quiz.id == quiz_id).first()
    if quiz_obj:
        for key,value in quiz.model_dump(exclude_none=True).items():
            setattr(quiz_obj, key, value)
        db.commit
        db.refresh(quiz_obj)
    return quiz_obj

def delete_quiz(db: Session, quiz_id: int):
    quiz_obj = db.query(Quiz).filter(Quiz.id == quiz_id).first()
    if quiz_obj:
        db.delete(quiz_obj)
        db.commit()
    return quiz_obj


#Question

def create_question(db: Session, question: QuestionCreate, quiz_id: int):
    question_obj = Question(quiz_id=quiz_id, **question.model_dump())
    db.add(question_obj)
    db.commit()
    db.refresh(question_obj)
    return question_obj

def get_question(db:Session, Quiz_id:int):
    return db.query(Question).filter(Question.quiz_id == Quiz_id).all()

def get_questions(db:Session, skip: int = 0, limit: int = 10):
    return db.query(Question).offset(skip).limit(limit).all()

def update_question(db: Session, question_id: int, question = QuestionUpdate):
    question_obj = db.query(Question).filter(Question.id == question_id).first()
    if question_obj:
        for key,value in question.model_dump(exclude_none=True).items():
            setattr(question_obj, key, value)
        db.commit()
        db.refresh(question_obj)
    return question_obj

def get_filtered_questions(db:Session, category: str = None, difficulty: str = None):
    query = db.query(Question)
    if category:
        query = query.filter(Question.category == category)
    if difficulty:
        query = query.filter(Question.difficulty == difficulty)
    return query.all()

def delete_questions(db: Session, quiz_id: int):
    questions = db.query(Question).filter(Question.quiz_id == quiz_id).all()
    for question in questions:
        db.delete(question)
        db.commit()
    return questions


#Attempted

def create_attempted(db: Session, attempted: AttemptedCreate, quiz_id: int):
    attempted_obj = Attempted(quiz_id=quiz_id, **attempted.model_dump())
    db.add(attempted_obj)
    db.commit()
    db.refresh(attempted_obj)
    return attempted_obj

def get_attempted(db:Session, user_id: int, quiz_id: int):
    return db.query(Attempted).filter(Attempted.user_id == user_id, Attempted.quiz_id == quiz_id).all()

