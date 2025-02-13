from sqlalchemy import Column, Integer, String
from models.pokemon_models import Base

class PokemonEvolution(Base):
    __tablename__ = "pokemon_evolution"
    id = Column(Integer, primary_key=True, autoincrement=True)
    base_form = Column(String, unique=True)
    evolution_conditions = Column(String)
    first_evolution_form = Column(String)
    evolution_conditions_2 = Column(String)
    second_evolution_form = Column(String)