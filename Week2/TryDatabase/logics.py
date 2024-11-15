from user import User
from db import Database

class Logic:

    def __init__(self):
        self.db = Database

    def insert(self, name, age, email, id):        
        user = User(name, age, email, id)
        success = self.db.insert(user)
        return success
    
    def getLogics(self):
        getData = self.db.getData()
        return getData
    
    def cleanUp(self):
        getClean = self.db.cleanUp()
        return getClean




        
    


        
