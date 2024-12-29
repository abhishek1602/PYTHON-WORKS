from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import JSON


Base = declarative_base()

class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    xp = Column(Integer, nullable=False)
    image_url = Column(String, nullable=False)
    pokemon_url = Column(String, nullable=False)
    abilities = Column(JSON, nullable=False)
    stats = Column(JSON, nullable=False)
    types = Column(JSON, nullable=False)