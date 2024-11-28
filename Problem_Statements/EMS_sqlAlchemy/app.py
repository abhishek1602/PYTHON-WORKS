from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from logic import Logic



app = FastAPI()
lgk = Logic()

class EmployeeIn(BaseModel):
    emp_id : int
    emp_name : str
    emp_age : int
    emp_number : int
    emp_location : str



@app.post("/employee",status_code=status.HTTP_201_CREATED)
def new_employee(new_employee : EmployeeIn):
    added = lgk.insert_emp(new_employee)
    if not added:
        raise HTTPException(status_code=400, detail="Employee Already Exists")
    return f"Employee Added {new_employee.emp_name}"


@app.put("/employee",status_code=status.HTTP_200_OK)
def update_employee(emp_id: int, new_empname: str, new_empage: int, new_empnumber: int, new_emplocation: str, new_empgrade: str):
    updated = lgk.update_emp(emp_id, new_empname, new_empage, new_empnumber, new_emplocation, new_empgrade)
    if "Not Found" in updated:
        raise HTTPException(status_code=400, detail="Employee Not Found")
    return f"Employee Updated: {new_empname}"


@app.get("/employee", status_code=status.HTTP_200_OK)
def get_all_employees():
    employee = lgk.view_employee()
    if not employee:
        raise HTTPException(status_code=404, detail="No Employee Found")
    return employee


@app.get("/employee/by_id", status_code=status.HTTP_202_ACCEPTED)
def get_employee_by_id(emp_id: int):
    employee = lgk.view_employee_by_id(emp_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee Not Found")
    return employee


@app.get("/employee/by_location", status_code=status.HTTP_202_ACCEPTED)
def get_employee_by_location(emp_location: str):
    employee = lgk.view_employee_by_location(emp_location)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee Not Found")
    return employee


@app.get("/employee/by_grade", status_code=status.HTTP_202_ACCEPTED)
def get_employee_by_grade(emp_grade: str):
    employee = lgk.view_employee_by_location(emp_grade)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee Not Found")
    return employee
        


    

