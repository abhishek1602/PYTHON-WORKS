class Employees:

    def __init__(self, emp_id, emp_name, emp_age, emp_number, emp_location, emp_grade):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_age = emp_age
        self.emp_number = emp_number
        self.emp_location = emp_location
        self.emp_grade = emp_grade

    def __repr__(self):
        return f"Employees('{self.emp_id}', '{self.emp_name}', '{self.emp_age}', '{self.emp_number}', '{self.emp_location}, '{self.emp_grade}')"
    

        