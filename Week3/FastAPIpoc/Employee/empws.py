from fastapi import FastAPI
from logics import Logics

app = FastAPI()
lgk = Logics()

@app.get("/viewall")
def viewEmp():
    view = lgk.getEmp()
    return view

@app.put("/update/{empId}")
def updateEmp(empId: int, newName: str = None, newNumber: int = None, newLocation: str = None):
    result = lgk.updateEmployee(empId, newName, newNumber, newLocation)
    if isinstance(result, str) and "No employee found" in result:
        return {"error": result}
    return {"success": "Employee updated successfully"}



@app.get("/searchbyid/{empId}")
def searchById(empId: int):
    employee = lgk.searchById(empId)
    if employee:
        return employee.to_dict()
    return {"error": f"Employee with ID {empId} not found"}


@app.get("/searchbylocation/{empLocation}")
def searchByLocation(empLocation: str):
    employee = lgk.searchByLocation(empLocation)
    if employee:
        return employee
    return {"error": f"No employees found in location {empLocation}"}



