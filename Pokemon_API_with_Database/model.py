from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import PickleType

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
    abilities = Column(PickleType, nullable=False)
    stats = Column(PickleType, nullable=False)
    types = Column(PickleType, nullable=False)
