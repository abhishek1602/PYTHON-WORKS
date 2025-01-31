from src.app import app
from src.repositories.mcq_repository import MCQRepository
from src.services.quiz_service import QuizService
from src.models import MCQ
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def quiz_service():
    return QuizService(MCQRepository())

def test_quiz_creation(quiz_service):
    mcq = MCQ(question="What is the capital of France?", option1="Berlin", option2="Madrid", option3="Paris", option4="Rome", answer="Paris", difficulty="easy", category="Geography")
    quiz_service.create_mcq(mcq)
    assert quiz_service.get_mcq(mcq.id).question == "What is the capital of France?"

def test_quiz_attempt(client):
    response = client.post('/quiz/attempt', data={'quiz_id': 1, 'answers': ['Paris']})
    assert response.status_code == 200
    assert b'Your score is' in response.data

def test_leaderboard(client):
    response = client.get('/leaderboard')
    assert response.status_code == 200
    assert b'Leaderboard' in response.data

def test_random_question_selection(quiz_service):
    questions = quiz_service.get_random_questions(category="Geography", difficulty="easy")
    assert len(questions) > 0
    assert all(q.category == "Geography" for q in questions)