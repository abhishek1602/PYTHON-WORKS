from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model import Base

DATABASE_URL = "postgresql://postgres:admin1234@localhost/pokemon_database"

engine = create_engine(DATABASE_URL)

sessionlocal = sessionmaker(autocommit=False, bind=engine)

def initialize_db():
    
    Base.metadata.create_all(bind=engine)