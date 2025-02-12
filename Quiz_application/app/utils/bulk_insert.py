import json
from sqlalchemy.orm import Session
from app.models.quiz_model import Question, Category, DifficultyLevel
from app.config.database import get_db
from app.schemas.quiz_schema import QuestionCreate

def load_questions_from_json(file_path: str) -> list[QuestionCreate]:
    with open(file_path, 'r') as f:
        questions_data = json.load(f)
    questions = []
    for data in questions_data:
        question = QuestionCreate(
            question_text=data['question_text'],
            options=data['options'],
            correct_option=data['correct_option'],
            category=Category(data['category']),
            difficulty=DifficultyLevel(data['difficulty'])
        )
        questions.append(question)
    return questions

def bulk_insert_questions(db: Session, questions: list[QuestionCreate]):
    for question in questions:
        db_question = Question(
            question_text=question.question_text,
            options=question.options,
            correct_option=question.correct_option,
            category=question.category,
            difficulty_level=question.difficulty
        )
        db.add(db_question)
    db.commit()

def bulk_insert():
    file_path = "quiz_questions.json"  
    db = next(get_db())
    questions = load_questions_from_json(file_path)
    bulk_insert_questions(db, questions)
    print(f"Successfully inserted {len(questions)} questions into the database.")
