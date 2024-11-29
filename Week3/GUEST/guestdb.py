import sqlite3
from guest import Guest

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('GuestDatabase.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS guests(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                number INTEGER NOT NULL,
                status TEXT NOT NULL
                            )''')

    def updateGuest(self, guestId, newName, newNumber, newStatus):
        self.cursor.execute('SELECT * FROM guests WHERE id=?', (guestId,))
        guest = self.cursor.fetchone()

        if not guest:
            return f"No Guest found with ID {guestId}"
        
        if newName:
            self.cursor.execute('UPDATE guests SET name = ? WHERE id =?', (newName, guestId))

        if newNumber:
            self.cursor.execute('UPDATE guests SET number = ? WHERE id =?', (newNumber, guestId))

        if newStatus:
            self.cursor.execute('UPDATE guests SET status = ? WHERE id =?', (newStatus, guestId))

        self.connection.commit()
        return f"Guest {guestId} updated successfully"
    
    
    def deleteGuest(self, guestId):
        self.cursor.execute('SELECT * FROM guests WHERE id=?', (guestId,))
        guest = self.cursor.fetchone

        if not guest:
            return f"No Guest found with ID {guestId}"
        
        if guest:
            self.cursor.execute('DELETE FROM guests WHERE id=?', (guestId,))

        self.connection.commit()
        return f"Guest {guestId} deleted successfully"
    
    
    def viewGuests(self):
        self.cursor.execute('SELECT * FROM guests')
        rows = self.cursor.fetchall()

        guests = []

        for row in rows:
            gst = Guest(row[0],row[1],row[2],row[3])
            guests.append(gst.toDict())

        return guests
        

    def searchByName(self, geustName):
        self.cursor.execute('SELECT * FROM guests WHERE name = ?', (geustName,))
        rows = self.cursor.fetchall()

        guests = []

        for row in rows:
            gst = Guest(row[0],row[1],row[2],row[3])
            guests.append(gst)

        return guests
        
    def searchById(self, guestId):
        self.cursor.execute('SELECT * FROM guests WHERE id = ?', (guestId,))
        row = self.cursor.fetchone()

        if row:
            return Guest(row[0],row[1],row[2],row[3])
        return f"{guestId} Not Valid"
    

    def cleanUp(self):
        self.cursor.close()
        self.connection.close()


        
if __name__ == "__main__":
    Database() 