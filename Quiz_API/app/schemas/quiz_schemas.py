from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class Difficulty(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"

class QuizBase(BaseModel):
    question: str
    options: List[str]
    answer: str
    explanation: Optional[str] = None
    image_url: Optional[str] = None
    difficulty: Optional[Difficulty] = None

class SportsQuizCreate(QuizBase):
    pass

class SportsQuizUpdate(BaseModel):
    question: Optional[str] = None
    options: Optional[List[str]] = None
    answer: Optional[str] = None
    explanation: Optional[str] = None
    image_url: Optional[str] = None
    difficulty: Optional[Difficulty] = None

class SportsQuizResponse(QuizBase):
    id: int

    class Config:
        from_attributes: True

class TechQuizCreate(QuizBase):
    pass

class TechQuizUpdate(BaseModel):
    question: Optional[str] = None
    options: Optional[List[str]] = None
    answer: Optional[str] = None
    explanation: Optional[str] = None
    image_url: Optional[str] = None
    difficulty: Optional[Difficulty] = None

class TechQuizResponse(QuizBase):
    id: int

    class Config:
        from_attributes: True

class ScienceQuizCreate(QuizBase):
    pass

class ScienceQuizUpdate(BaseModel):
    question: Optional[str] = None
    options: Optional[List[str]] = None
    answer: Optional[str] = None
    explanation: Optional[str] = None
    image_url: Optional[str] = None
    difficulty: Optional[Difficulty] = None

class ScienceQuizResponse(QuizBase):
    id: int

    class Config:
        from_attributes: True