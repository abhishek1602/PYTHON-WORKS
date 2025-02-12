from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum
from typing import List, Optional

class Role(str, Enum):
    admin = "admin"
    user = "user"

class Category(str, Enum):
    science = "science"
    technical = "technical"
    sports = "sports"
    mixed = "mixed"

class Difficulty(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    role: Role

    class Config:
        from_attributes = True

class QuestionBase(BaseModel):
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str
    category: Category
    difficulty: Difficulty
    hint: Optional[str] = None
    explanation: Optional[str] = None
    image_url: Optional[str] = None
    audio_url: Optional[str] = None

    class Config:
        from_attributes = True

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int
    quiz_id: int

    class Config:
        orm_mode = True

class QuizBase(BaseModel):
    title: str
    description: str

class QuizCreate(QuizBase):
    questions: List[QuestionCreate]

class Quiz(QuizBase):
    id: int
    user_id: int
    questions: List[Question]

    class Config:
        orm_mode = True

class QuizUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class AttemptedBase(BaseModel):
    score: int
    attempted_at: datetime
    user_responses: str

    class Config:
        from_attributes = True

class AttemptedCreate(AttemptedBase):
    pass

class Attempted(AttemptedBase):
    id: int
    user_id: int
    quiz_id: int

    class Config:
        from_attributes = True