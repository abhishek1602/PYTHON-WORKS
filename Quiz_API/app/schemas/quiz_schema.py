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
        from_attributes: True

class QuestionBase(BaseModel):
    question_id : int
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    answer: str
    category: Category
    difficulty: Difficulty

class QuestionUpdate(BaseModel):
    question: Optional[str] = None
    option_a: Optional[str] = None
    option_b: Optional[str] = None
    option_c: Optional[str] = None
    option_d: Optional[str] = None
    correct_answer: Optional[str] = None
    category: Optional[Category] = None
    difficulty: Optional[Difficulty] = None

class QuestionCreate(QuestionBase):
    pass

    class Config:
        from_attributes: True

class Question(QuestionBase):
    id: int
    quiz_id: int
    role: Role

    class Config:
        from_attributes: True   

class QuizBase(BaseModel):
    title: str
    description: str

class QuizCreate(QuizBase):
    questions: List[QuestionCreate]

class Quiz(QuizBase):
    id: int
    user_id: int
    questions: List[Question]

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