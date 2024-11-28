from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from logic import EmployeeLogic, UserLogic
from schemas import EmployeeCreate, EmployeeUpdate, UserCreate


app = FastAPI()

@app.post("/register/", status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    user_logic = UserLogic(db)
    created_user = user_logic.create_user(user.username, user.password)
    if not created_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return {"username": created_user.username}

@app.post("/login/", status_code=status.HTTP_200_OK)
def login(username: str, password: str, db: Session = Depends(get_db)):
    user_logic = UserLogic(db)
    if not user_logic.authenticate_user(username, password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}

@app.post("/employee/", status_code=status.HTTP_201_CREATED)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    employee_logic = EmployeeLogic(db)
    new_employee = employee_logic.create_employee(employee)
    return new_employee

@app.get("/employee/{emp_id}", status_code=status.HTTP_200_OK)
def get_employee_by_id(emp_id: int, db: Session = Depends(get_db)):
    employee_logic = EmployeeLogic(db)
    employee = employee_logic.get_employee_by_id(emp_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.get("/employee/grade/{emp_grade}", status_code=status.HTTP_200_OK)
def get_employees_by_grade(emp_grade: str, db: Session = Depends(get_db)):
    employee_logic = EmployeeLogic(db)
    return employee_logic.get_employees_by_grade(emp_grade)

@app.put("/employee/{emp_id}", status_code=status.HTTP_200_OK)
def update_employee(emp_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    employee_logic = EmployeeLogic(db)
    updated_employee = employee_logic.update_employee(emp_id, employee)
    if not updated_employee:
        raise HTTPException(status_code=404, detail="Employee not found or not updated")
    return {"message": "Employee updated successfully"}
