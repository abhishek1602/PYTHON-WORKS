import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base
from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

sessionlocal = sessionmaker(autocommit=False, bind=engine)

def initialize_db():
    
    Base.metadata.create_all(bind=engine)