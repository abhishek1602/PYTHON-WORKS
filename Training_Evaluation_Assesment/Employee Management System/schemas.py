from pydantic import BaseModel
from typing import Optional
from datetime import date

class EmployeeCreate(BaseModel):
    emp_id: int
    emp_firstname: str
    emp_lastname: str
    emp_dob: Optional[date]
    emp_doj: Optional[date]
    emp_grade: Optional[str]

    class Config:
        from_attributes = True

class EmployeeUpdate(BaseModel):
    emp_firstname: Optional[str]
    emp_lastname: Optional[str]
    emp_dob: Optional[date]
    emp_doj: Optional[date]
    emp_grade: Optional[str]

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True
