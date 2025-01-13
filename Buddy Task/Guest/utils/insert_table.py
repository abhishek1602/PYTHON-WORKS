from Guest.config.init_db import SessionLocal, initialise_db
from Guest.models.guest_model import Guest
from Guest.schemas.guest_schemas import GuestBase

def insert_guest(guest: GuestBase):
    db = SessionLocal()
    guest = Guest(**guest.model_dump())
    db.add(guest)
    db.commit()
    db.refresh(guest)
    db.close()
    return guest

if __name__ == "__main__":
    initialise_db()