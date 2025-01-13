from sqlalchemy.orm import Session
from fastapi import HTTPException
from Guest.schemas.guest_schemas import GuestUpdate, GuestBase, GuestStatus
from Guest.repository.guest_repository import (
    insert_guest,
    get_guest_by_phone,
    get_guest_by_id, 
    get_guests, 
    get_guest_by_name, 
    get_guest_by_status, 
    update_guest, 
    delete_guest
    )

def create_guest(db: Session, guest: GuestBase):
    existing_guest = get_guest_by_phone(db, guest.phone)
    if existing_guest:
        raise HTTPException(status_code=400, detail="Guest already exists")
    return insert_guest(db, guest)  

def read_guest_by_id(db: Session, guest_id: int):
    db_guest = get_guest_by_id(db, guest_id)
    if not db_guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return db_guest

def read_guests(db: Session, page: int = 0, page_size: int = 10):
    return get_guests(db, page, page_size)

def read_guest_by_name(db: Session, name: str):
    db_guest = get_guest_by_name(db, name)
    if not db_guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return db_guest

def read_guest_by_status(db: Session, status: GuestStatus):
    return get_guest_by_status(db, status)

def update_guest_details(db: Session, guest_id: int, guest: GuestUpdate):
    db_guest = update_guest(db, guest_id, guest)
    if not db_guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return db_guest, {"detail" : "Guest updated successfully"}

def remove_guest(db: Session, guest_id: int):
    db_guest = delete_guest(db, guest_id)
    if not db_guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return {"detail" : "Guest removed successfully"}
