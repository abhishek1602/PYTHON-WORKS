from fastapi import FastAPI
from guestlogic import Logic

app = FastAPI()
lgk = Logic()


@app.get("/viewGuest")
def viewGuest():
    view = lgk.ViewAllGuest()
    return view

@app.put("/updateGuest/{guestId}")
def updateGuest(guestId:int , newName:str=None , newNumber:int=None, newStatus:str=None):
    update = lgk.UpdateDetails(guestId, newName, newNumber, newStatus)
    
    if isinstance(update, str) and "No Guest found" in update:
        return f"Cannot make chnages to Guest Id : {guestId}"
    
    return f"Guest updated with Id: {guestId}"


@app.get("/searchById/{guestId}") 
def searchById(guestId:int):
    guest = lgk.SearchById(guestId)
    if guest:
        return guest.toDict()
    return f"No guest found with id {guestId}"


@app.get("/searchByName/{guestName}")
def searchByName(guestName:str):
    guest = lgk.SearchByName(guestName)
    if guest:
        return guest
    return f"No guest found with name {guestName}"

@app.delete("/deleteGuest/{guestId}")
def deleteGuest(guestId:int):
    delete = lgk.DeleteGuest(guestId)
    if delete:
        return f"Guest with id {guestId} deleted"
    return f"No guest found with id {guestId}"

