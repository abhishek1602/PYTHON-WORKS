from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import admin, auth, mcq, user
from app.db.init_db import init_db

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the database
init_db()

# Include routers
app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(mcq.router, prefix="/mcq", tags=["mcq"])
app.include_router(user.router, prefix="/user", tags=["user"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the MCQ Application!"}