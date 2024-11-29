from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from logics import GuestLogic
from schemas import GuestSchema

app = FastAPI()
logic = GuestLogic()

@app.post("/guests/")
def create_guest(guest: GuestSchema, db: Session = Depends(get_db)):
    new_guest = logic.create_guest(db, guest.guest_name, guest.guest_number, guest.guest_status)
    return new_guest

@app.get("/guests/{guest_id}", response_model= GuestSchema)
def get_guest_by_id(guest_id: int, db: Session = Depends(get_db)):
    guest = logic.get_guest_by_id(db, guest_id)
    if not guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return guest

@app.get("/guests/", response_model=list[GuestSchema])
def get_all_guests(db: Session = Depends(get_db)):
    return logic.get_all_guests(db)

@app.get("/guests/search/", response_model=list[GuestSchema])
def get_guest_by_name(guest_name: str, db: Session = Depends(get_db)):
    guests = logic.get_guest_by_name(db, guest_name)
    if not guests:
        raise HTTPException(status_code=404, detail="No guests found with that name")
    return guests

@app.get("/guests/status/", response_model= list[GuestSchema])
def get_guest_by_status(guest_status: str, db: Session = Depends(get_db)):
    guests = logic.get_guest_by_status(db, guest_status)
    if not guests:
        raise HTTPException(status_code=404, detail="No guests found with this status")
    return guests

@app.put("/guests/{guest_id}")
def update_guest(guest_id: int, guest: GuestSchema, db: Session = Depends(get_db)):
    updated_guest = logic.update_guest(db, guest_id, guest.guest_name, guest.guest_number, guest.guest_status)
    if not updated_guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return updated_guest
