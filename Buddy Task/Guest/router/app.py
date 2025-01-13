from fastapi import FastAPI, HTTPException, Depends
from contextlib import asynccontextmanager
from sqlalchemy import or_
from sqlalchemy.orm import Session
from Guest.config.init_db import SessionLocal, initialise_db
from Guest.schemas.guest_schemas import GuestBase, GuestStatus, GuestInfo, GuestUpdate
from Guest.services.guest_services import (
    create_guest, 
    read_guest_by_id, 
    read_guests, 
    read_guest_by_name, 
    read_guest_by_status, 
    update_guest_details, 
    remove_guest
    )

@asynccontextmanager
async def lifespan(app: FastAPI):
    initialise_db() 
    yield 

app = FastAPI(lifespan=lifespan)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/guests/", response_model=GuestInfo)
def create_guest_api(guest: GuestBase, db: Session = Depends(get_db)):
    return create_guest(db, guest)


@app.get("/guests/{guest_id}", response_model=GuestBase)
def read_guest_by_id_api(guest_id: int, db: Session = Depends(get_db)):
    return read_guest_by_id(db, guest_id)


@app.get("/guests/", response_model=list[GuestInfo])
def read_guests_api(page: int = 0, page_size: int = 10, db: Session = Depends(get_db)):
    return read_guests(db, page, page_size)


@app.get("/guests/name/{name}", response_model=GuestBase)
def read_guest_by_name_api(name: str, db: Session = Depends(get_db)):
    return read_guest_by_name(db, name)


@app.get("/guests/status/{status}", response_model=list[GuestInfo])
def read_guest_by_status_api(status: GuestStatus, db: Session = Depends(get_db)):
    return read_guest_by_status(db, status)


@app.patch("/guests/{guest_id}", response_model=GuestBase)
def update_guest_api(guest_id: int, guest: GuestUpdate, db: Session = Depends(get_db)):
    return update_guest_details(db, guest_id, guest)


@app.delete("/guests/{guest_id}")
def remove_guest_api(guest_id: int, db: Session = Depends(get_db)):
    return remove_guest(db, guest_id)
