from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Guest(Base):
    __tablename__ = 'guests'
    guest_id = Column(Integer, primary_key=True)
    guest_name = Column(String, nullable=False)
    guest_number = Column(Integer, nullable=False)
    guest_status = Column(String)


