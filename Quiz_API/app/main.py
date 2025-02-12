from fastapi import FastAPI
from app.routes import quiz_router, question_router

app = FastAPI()


app.include_router(quiz_router.router, prefix="/api", tags=["Quiz API"])
app.include_router(question_router.router, prefix="/api", tags=["Question API"])
