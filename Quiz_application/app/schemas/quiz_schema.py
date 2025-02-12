from pydantic import BaseModel
from typing import List, Dict, Optional
from app.models.quiz_model import DifficultyLevel, Category
from datetime import datetime

class QuestionCreate(BaseModel):
    question_text: str
    options: Dict[str, str]
    correct_option: str
    difficulty: DifficultyLevel
    category: Category

class QuestionUpdate(BaseModel):
    question_text: Optional[str] = None
    options: Optional[Dict[str, str]] = None
    correct_option: Optional[str] = None
    difficulty: Optional[DifficultyLevel] = None
    category: Optional[Category] = None

class QuestionSchema(BaseModel):
    id: int
    question_text: str
    options: dict
    correct_option: str
    category: Category
    difficulty: DifficultyLevel

    class Config:
        from_attributes = True

class QuestionUpdateSchema(BaseModel):
    question_text: Optional[str] = None
    options: Optional[dict] = None
    correct_option: Optional[str] = None
    category: Optional[Category] = None
    difficulty: Optional[DifficultyLevel] = None

    class Config:
        from_attributes = True

class QuestionResponse(BaseModel):
    id: int  
    question_text: str
    options: dict
    correct_option: str
    difficulty: DifficultyLevel
    category: Category

    class Config:
        from_attributes = True

class QuizResponse(BaseModel):
    id: int
    title: str
    category: Category
    description: str
    difficulty: DifficultyLevel
    questions: List[QuestionResponse]

    class Config:
        from_attributes = True


class QuizCreateRequest(BaseModel):
    title: str
    category: Category
    difficulty: DifficultyLevel
    description: str
    question_data: List[QuestionCreate]


class UserAnswer(BaseModel):
    question_id: int
    selected_option: str

class QuizAttemptCreate(BaseModel):
    quiz_id: int
    user_answers: List[UserAnswer]

class QuizAttempt(BaseModel):
    id: int
    user_id: int
    quiz_id: int
    score: float
    attempted_at: datetime
    user_answers: List[UserAnswer]

    class Config:
        from_attributes = True











