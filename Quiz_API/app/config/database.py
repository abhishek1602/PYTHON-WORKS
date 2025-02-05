from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.quiz_model import Base

DATABASE_URL = 'postgresql://postgres:admin1234@localhost/Quiz_API'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, bind = engine)

def init_db():
    Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close