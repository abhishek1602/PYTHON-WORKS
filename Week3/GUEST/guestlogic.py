from guest import Guest
from guestdb import Database


class Logic:

    def __init__(self):
        self.db = Database()


    def UpdateDetails(self, guestId, newName=None, newNumber=None, newStatus=None):
        return self.db.updateGuest(guestId, newName, newNumber, newStatus)
    
    def DeleteGuest(self, guestId):
        return self.db.deleteGuest(guestId)
    
    def ViewAllGuest(self):
        view = self.db.viewGuests()
        return view
    
    def SearchByName(self, guestName):
        return self.db.searchByName(guestName)
    
    def SearchById(self, guestId):
        return self.db.searchById(guestId)
    
    def close(self):
        return self.db.close()


