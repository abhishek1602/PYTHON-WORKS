class User:

    def __init__(self, userName, userAge, userEmail, userId = 0):
        self.userName = userName
        self.userAge = userAge
        self.userEmail = userEmail
        self.userId = userId
        

    def __repr__(self):
        return f"UserName: {self.userName}, UserAge: {self.userAge}, UserEmail: {self.userEmail}"
    
    
    

