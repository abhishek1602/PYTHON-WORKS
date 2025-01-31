from sqlalchemy.orm import Session
from models import MCQ, User
from repositories.mcq_repository import MCQRepository
from repositories.user_repository import UserRepository

class QuizService:
    def __init__(self, session: Session):
        self.session = session
        self.mcq_repository = MCQRepository(session)
        self.user_repository = UserRepository(session)

    def get_random_questions(self, subject: str, difficulty: str, limit: int):
        return self.mcq_repository.get_random_questions(subject, difficulty, limit)

    def submit_quiz(self, user_id: int, answers: dict):
        score = 0
        total_questions = len(answers)
        for question_id, user_answer in answers.items():
            question = self.mcq_repository.get_by_id(question_id)
            if question and question.answer == user_answer:
                score += 1
        percentage_score = (score / total_questions) * 100 if total_questions > 0 else 0
        self.user_repository.update_user_score(user_id, percentage_score)
        return percentage_score

    def get_leaderboard(self):
        return self.user_repository.get_leaderboard()

    def get_question_by_id(self, question_id: int):
        return self.mcq_repository.get_by_id(question_id)

    def add_question(self, question_data: dict):
        new_question = MCQ(**question_data)
        self.mcq_repository.add(new_question)
        self.session.commit()

    def update_question(self, question_id: int, question_data: dict):
        question = self.mcq_repository.get_by_id(question_id)
        if question:
            for key, value in question_data.items():
                setattr(question, key, value)
            self.session.commit()

    def delete_question(self, question_id: int):
        self.mcq_repository.delete(question_id)
        self.session.commit()