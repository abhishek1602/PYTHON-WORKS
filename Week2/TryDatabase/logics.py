from user import User
from db import Database

class Logic:

    def __init__(self):
        self.db = Database()

    def insert(self, userName, userAge, userEmail):        
        user = User(userName, userAge, userEmail)
        return self.db.insertUser(user)
    
    def getLogics(self):
        return self.db.getData()
    
    def cleanUp(self):
        self.db.cleanUp()




        
    


        
