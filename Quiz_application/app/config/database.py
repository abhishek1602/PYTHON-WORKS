from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.settings import settings  

engine = create_engine(settings.DATABASE_URL)  


try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")

    

SessionLocal = sessionmaker(autocommit=False, bind=engine)



def get_db():
    db = SessionLocal()

    db.commit()
    try:
        yield db
    finally:
        db.close()