from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserInDB(UserBase):
    id: int

class User(UserInDB):
    pass

class UserHistory(BaseModel):
    user_id: int
    mcq_attempts: List[int]  # List of MCQ IDs attempted by the user
    scores: List[float]  # List of scores for each attempt
    timestamps: List[str]  # List of timestamps for each attempt

class UserResponse(BaseModel):
    user: User
    history: UserHistory