from sqlalchemy import create_engine
from app.model.model import Base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://postgres:admin1234@localhost/Quiz_app'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

