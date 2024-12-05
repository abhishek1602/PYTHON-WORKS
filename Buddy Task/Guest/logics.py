from sqlalchemy.orm import Session
from models import Guest

class GuestLogic:

    def create_guest(self, db: Session, guest_name: str, guest_number: int, guest_status: str):
        guest = Guest(guest_name=guest_name, guest_number=guest_number, guest_status=guest_status)
        db.add(guest)
        db.commit()
        db.refresh(guest)
        return guest

    def get_guest_by_id(self, db: Session, guest_id: int):
        return db.query(Guest).filter(Guest.guest_id == guest_id).first()

    def get_guest_by_name(self, db: Session, guest_name: str):
        return db.query(Guest).filter(Guest.guest_name == guest_name).all()
    
    def get_guest_by_status(self, db: Session, guest_status: str):
        return db.query(Guest).filter(Guest.guest_status == guest_status).all()

    def update_guest(self, db: Session, guest_id: int, guest_name: str, guest_number: int, guest_status: str):
        guest = db.query(Guest).filter(Guest.guest_id == guest_id).first()
        if guest:
            guest.guest_name = guest_name
            guest.guest_number = guest_number
            guest.guest_status = guest_status
            db.commit()
            db.refresh(guest)
            db.rollback()
        return guest

    

    def get_all_guests(self, db: Session):
        return db.query(Guest).all()
