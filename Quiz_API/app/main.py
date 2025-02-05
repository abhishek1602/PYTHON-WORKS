from fastapi import FastAPI
from app.routes.quiz_router import router

app = FastAPI()


app.include_router(router, prefix="/api", tags=["Quiz API"])
