from sqlalchemy.orm import Session
from Guest.models.guest_model import Guest as Guests
from Guest.schemas.guest_schemas import GuestUpdate, GuestBase, GuestStatus


def insert_guest(db: Session, guest: GuestBase):
    guest = Guests(**guest.model_dump())
    db.add(guest)
    db.commit()
    db.refresh(guest)
    return guest

def get_guest_by_id(db: Session, guest_id: int):
    return db.query(Guests).filter(Guests.id == guest_id).first()

def get_guests(db: Session, page: int = 0, page_size: int = 20):
    return db.query(Guests).offset(page).limit(page_size).all()

def get_guest_by_name(db: Session, name: str):
    return db.query(Guests).filter(Guests.name == name).first()

def get_guest_by_status(db: Session, status: GuestStatus):
    return db.query(Guests).filter(Guests.status == status).all()

def get_guest_by_phone(db: Session, phone: str): 
    return db.query(Guests).filter(Guests.phone == phone).first()  

def update_guest(db: Session, guest_id: int, guestupdate: GuestUpdate):
    guest = db.query(Guests).filter(Guests.id == guest_id).first()
    if not guest:
        return None
    for key, value in guestupdate.model_dump(exclude_none=True).items():
        if getattr(guest, key) != value:
            setattr(guest, key, value)
    db.commit()
    db.refresh(guest)
    return guest

def delete_guest(db: Session, guest_id: int):
    guest = db.query(Guests).filter(Guests.id == guest_id).first()
    if not guest:
        return None
    db.delete(guest)
    db.commit()
    return guest

