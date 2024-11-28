from sqlalchemy.orm import Session
from models import Employee, User
from datetime import datetime, date
from schemas import EmployeeCreate, EmployeeUpdate

DATE_FORMAT = "%d/%m/%Y" 

class EmployeeLogic:
    def __init__(self, db: Session):
        self.db = db

    def create_employee(self, employee: EmployeeCreate):
        new_employee = Employee(
            emp_id=employee.emp_id,
            emp_firstname=employee.emp_firstname,
            emp_lastname=employee.emp_lastname,
            emp_dob=employee.emp_dob.strftime(DATE_FORMAT) if employee.emp_dob else None,  # Convert date to string in DD/MM/YYYY format
            emp_doj=employee.emp_doj.strftime(DATE_FORMAT) if employee.emp_doj else None,  # Convert date to string in DD/MM/YYYY format
            emp_grade=employee.emp_grade
        )
        self.db.add(new_employee)
        self.db.commit()
        self.db.refresh(new_employee)
        return new_employee

    def get_employee_by_id(self, emp_id: int):
        employee = self.db.query(Employee).filter(Employee.emp_id == emp_id).first()
        if employee:
            employee.emp_dob = datetime.strptime(employee.emp_dob, DATE_FORMAT).date() if employee.emp_dob else None  # Convert string to date
            employee.emp_doj = datetime.strptime(employee.emp_doj, DATE_FORMAT).date() if employee.emp_doj else None  # Convert string to date
        return employee
    

    def get_employees_by_grade(self, emp_grade: str):
        employees = self.db.query(Employee).filter(Employee.emp_grade == emp_grade).all()
        for employee in employees:
            employee.emp_dob = datetime.strptime(employee.emp_dob, DATE_FORMAT).date() if employee.emp_dob else None  # Convert string to date
            employee.emp_doj = datetime.strptime(employee.emp_doj, DATE_FORMAT).date() if employee.emp_doj else None  # Convert string to date
        return employees


    def update_employee(self, emp_id: int, employee_update: EmployeeUpdate):
        employee = self.db.query(Employee).filter(Employee.emp_id == emp_id).first()
        if not employee:
            return None

        if employee_update.emp_firstname:
            employee.emp_firstname = employee_update.emp_firstname
        if employee_update.emp_lastname:
            employee.emp_lastname = employee_update.emp_lastname
        if employee_update.emp_dob:
            employee.emp_dob = employee_update.emp_dob.strftime(DATE_FORMAT) if isinstance(employee_update.emp_dob, date) else datetime.strptime(employee_update.emp_dob, DATE_FORMAT).strftime(DATE_FORMAT)
        if employee_update.emp_doj:
            employee.emp_doj = employee_update.emp_doj.strftime(DATE_FORMAT) if isinstance(employee_update.emp_doj, date) else datetime.strptime(employee_update.emp_doj, DATE_FORMAT).strftime(DATE_FORMAT)
        if employee_update.emp_grade:
            employee.emp_grade = employee_update.emp_grade

        self.db.commit()
        self.db.refresh(employee)
        return employee

class UserLogic:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, username: str, password: str):
        existing_user = self.db.query(User).filter(User.username == username).first()
        if existing_user:
            return None  
        new_user = User(username=username, password=password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def authenticate_user(self, username: str, password: str) -> bool:
        user = self.db.query(User).filter(User.username == username).first()
        if user and user.password == password:
            return True
        return False
