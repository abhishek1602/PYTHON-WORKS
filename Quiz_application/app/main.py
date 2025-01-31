from fastapi import FastAPI
from app.utils.init_db import init_db
from app.router import quiz_router

app = FastAPI()

app.include_router(quiz_router.router)
