class Guest:

    def __init__(self, guestId, guestName, guestNumber, guestStatus):
        self.guestId = guestId
        self.guestName = guestName
        self.guestNumber = guestNumber
        self.guestStatus = guestStatus

    def __repr__(self):
        return f"Guest({self.guestId},{self.guestName},{self.guestNumber},{self.guestStatus})"
    
    def toDict(self):
        return {
            "guestId" : self.guestId,
            "guestName" : self.guestName,
            "guestNumber" : self.guestNumber,
            "guestStatus" : self.guestStatus
        }