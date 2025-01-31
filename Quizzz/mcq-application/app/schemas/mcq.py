from pydantic import BaseModel
from typing import List, Optional

class MCQBase(BaseModel):
    question: str
    options: List[str]
    correct_answer: str
    category: str
    difficulty: str
    tags: Optional[List[str]] = None

class MCQCreate(MCQBase):
    pass

class MCQUpdate(MCQBase):
    pass

class MCQ(MCQBase):
    id: int

    class Config:
        orm_mode = True

class MCQResponse(BaseModel):
    question: str
    options: List[str]
    correct_answer: str
    user_answer: Optional[str] = None
    is_correct: Optional[bool] = None
    explanation: Optional[str] = None

class MCQAttempt(BaseModel):
    mcqs: List[MCQResponse]
    score: float
    percentage: float

class MCQHistory(BaseModel):
    user_id: int
    attempted_mcqs: List[MCQResponse]
    total_score: float
    total_percentage: float
    timestamp: str