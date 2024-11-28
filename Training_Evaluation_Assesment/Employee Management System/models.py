from sqlalchemy import Integer, Column, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True, index=True)
    emp_firstname = Column(String, nullable=False)
    emp_lastname = Column(String, nullable=False)
    emp_dob = Column(String, nullable=True)  
    emp_doj = Column(String, nullable=True)  
    emp_grade = Column(String, nullable=True)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
