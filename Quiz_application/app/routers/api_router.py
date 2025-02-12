from fastapi import APIRouter
from app.routers import quiz_router, question_router, user_router, auth_router, quiz_attempt_router

api_router = APIRouter()

api_router.include_router(auth_router.router, prefix="/auth", tags=["auth"])
api_router.include_router(quiz_router.router, prefix="/quizzes", tags=["quizzes"])
api_router.include_router(question_router.router, prefix="/questions", tags=["questions"])
api_router.include_router(user_router.router, prefix="/users", tags=["users"])
api_router.include_router(quiz_attempt_router.router, prefix="/quiz-attempts", tags=["quiz-attempts"])

