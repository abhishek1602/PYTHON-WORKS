from emp import Employee
from database import Database

class Logics:

    def __init__(self):
        self.db = Database()

        
    def getEmp(self):
        view = self.db.viewAll()
        return view

    
    def updateEmployee(self, empId, newName=None, newNumber=None, newLocation=None):
        return self.db.updateEmp(empId, newName, newNumber, newLocation)
    
    
    def searchById(self, empId):
        result = self.db.searchById(empId)
        return result


    def searchByLocation(self, empLocation):
        return self.db.searchByLocation(empLocation)
            
    
    def closeEmp(self):
        close =  self.db.cleanUp()
        return close
        

        