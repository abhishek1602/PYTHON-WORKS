import sqlite3
from user import User

class Database:

    def __init__(self):
        self.connection = sqlite3.connect('myDatabase.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTERGER NOT NULL,
                email TEXT
            )
        ''' )
        
    def insertUser(self, user):
        insert_query = 'INSERT INTO users (name, age, email) VALUES(?,?,?)'
        self.cursor.execute(insert_query, (user.userName, user.userAge, user.userEmail))
        self.connection.commit()
        return True
    
    def getData(self):
        self.cursor.execute('SELECT * FROM users')
        rows = self.cursor.fetchall()

        users = []

        for row in rows:
            user = User(row[1], row[2], row[3],)
            users.append(user)
        return users
        
    def cleanUp(self):
        self.cursor.close()
        self.connection.close()

    