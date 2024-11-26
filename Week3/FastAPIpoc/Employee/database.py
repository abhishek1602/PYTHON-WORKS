import sqlite3
from emp import Employee

class Database:

    def __init__(self):
        self.connection = sqlite3.connect('MyDatabase.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                number INTEGER NOT NULL,
                location TEXT NOT NULL
                )
            ''')

    
    def updateEmp(self, empId, newName=None, newNumber=None, newLocation=None):
        self.cursor.execute('SELECT * FROM employees WHERE id = ?', (empId,))
        row = self.cursor.fetchone()

        if not row:
            return f"No employee found with ID {empId}"

        if newName:
            self.cursor.execute('UPDATE employees SET name = ? WHERE id = ?', (newName, empId))
        if newNumber:
            self.cursor.execute('UPDATE employees SET number = ? WHERE id = ?', (newNumber, empId))
        if newLocation:
            self.cursor.execute('UPDATE employees SET location = ? WHERE id = ?', (newLocation, empId))

        self.connection.commit()
        return True
    

    def viewAll(self):
        self.cursor.execute('SELECT * FROM employees')
        rows = self.cursor.fetchall()

        employees = []

        for row in rows:
            emp = Employee(row[0],row[1],row[2],row[3])
            employees.append(emp)
        return employees
    

    def searchById(self, empId):
        self.cursor.execute('SELECT * FROM employees WHERE id = ?', (empId,))
        row = self.cursor.fetchone()
        if row:
            return Employee(row[0], row[1], row[2], row[3])
        return None


    def searchByLocation(self, empLocation):
            self.cursor.execute('SELECT * FROM employees WHERE location = ?', (empLocation,))
            rows = self.cursor.fetchall()   
            employees = []
            for row in rows:
                emp = Employee(row[0],row[1],row[2],row[3])
                employees.append(emp)
            return employees
            
        

    def cleanUp(self):
        self.cursor.close()
        self.connection.close()

        

if __name__ == "__main__":
    Database()
            