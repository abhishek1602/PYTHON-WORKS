import sqlite3
from user import User
 
class Database:

    def __init__(self):
        self.connection = sqlite3.connect('MYdatabase.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT
    )
    ''')
    
    def insert(self,user):
        insertQuery = 'INSERT INTO users (name, age, email, id) VALUES (?, ?, ?, ?)'
        self.cursor.execute(insertQuery, (user.userName, user.userAge, user.userEmail, user.userId))
        self.connection.commit()
        return True

    def getData(self):
        self.cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        users = []

        for row in rows:
            user = User(row[1],row[2],row[3],row[4])
            users.append(user)
        return users

    def cleanUp(self):
        self.cursor.close()
        self.connection.close()

    
    


