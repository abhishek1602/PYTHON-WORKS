from models import Employees
from db import sessionlocal, Employees


class Logic:

    def __init__(self):
        self.db = sessionlocal()

    
    def insert_emp(self, new_employee):      
        employee = Employees(emp_id = new_employee.emp_id, 
                                emp_name = new_employee.emp_name, 
                                emp_age = new_employee.emp_age, 
                                emp_number = new_employee.emp_number, 
                                emp_location = new_employee.emp_location,
                                emp_grade = new_employee.emp_grade)
            
        try:    
            self.db.add(employee)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False
        

    
    def update_emp(self, emp_id, new_empname, new_empnumber, new_empage, new_emplocataion, new_empgrade):
        employee = self.db.query(Employees).filter(Employees.emp_id == emp_id).first()

        if not employee:
            return f"Employee {emp_id} Not Found"
        
        employee.emp_name = new_empname
        employee.emp_age = new_empage
        employee.emp_number = new_empnumber
        employee.emp_location = new_emplocataion
        employee.emp_grade = new_empgrade
        try:
            self.db.commit()
            return f"Employee {emp_id} Details Updated, Name: {new_empage}, Age: {new_empage}, Number: {new_empnumber}, Location: {new_emplocataion}, Grade: {new_empgrade}"
        except:
            self.db.rollback()
        
    


    def view_employee(self):
        employee = self.db.query(Employees).all()
        return employee
    


    def view_employee_by_id(self, emp_id):
        employee = self.db.query(Employees).filter(Employees.emp_id == emp_id).first()
        if employee:
            return employee
        return f"No employee found with id: {emp_id}"
    


    def view_employee_by_location(self, emp_locataion):
        employee = self.db.query(Employees).filter(Employees.emp_location == emp_locataion).all()
        if employee:
            return employee
        return f"No employee found with location: {emp_locataion}"
    

    def view_employee_by_grade(self, emp_grade):
        employee = self.db.query(Employees).filter(Employees.emp_grade == emp_grade).all()
        if employee:
            return employee
        return f"No employee found with grade: {emp_grade}"
        
        


