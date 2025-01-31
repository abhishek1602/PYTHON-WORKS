from pydantic import BaseModel
from typing import Optional, List
from enum import Enum


class Category(str, Enum):
    science = "science"
    sports = "sports"
    technology = "technology"

class Difficulty(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"

class QuestionCreate(BaseModel):
    question: str
    options: List[str]
    answer: str
    difficulty: Difficulty
    category: Category
    hint: Optional[str] = None
    image_url: Optional[str] = None
    audio_url: Optional[str] = None

    class Config:
        from_attributes = True

class QuestionUpdate(BaseModel):
    question: Optional[str] = None
    options: Optional[List[str]] = None
    answer: Optional[str] = None
    difficulty: Optional[Difficulty] = None
    category: Optional[Category] = None
    hint: Optional[str] = None
    image_url: Optional[str] = None
    audio_url: Optional[str] = None

    class Config:
        from_attributes = True

class MCQBase(BaseModel):
    heading : str
    description : Optional[str]
    category : Category
    difficulty : Difficulty

    class Config:
        from_attributes = True

class MCQUpdate(BaseModel):
    heading : Optional[str] = None
    description : Optional[str] = None
    category : Optional[Category] = None
    difficulty : Optional[Difficulty] = None

    class Config:
        from_attributes = True

class MCQResponse(MCQBase):
    questions : List[QuestionCreate] = []

    class Config:
        from_attributes = True
