from typing import List, Optional
from sqlalchemy.orm import Session
from models.pokemon_evolution import PokemonEvolution  
from schemas.evolution_schemas import EvolutionBase

def create_evolution(db: Session, evolution: EvolutionBase) -> PokemonEvolution:
    db_evolution = PokemonEvolution(**evolution.model_dump())
    db.add(db_evolution)
    db.commit()
    db.refresh(db_evolution)
    return db_evolution

def get_evolution(db: Session, evolution_id: int) -> Optional[PokemonEvolution]:
    return db.query(PokemonEvolution).filter(PokemonEvolution.id == evolution_id).first()

def search_evolution_by_name(db: Session, name: str) -> List[PokemonEvolution]:
    return db.query(PokemonEvolution).filter(
        (PokemonEvolution.base_form == name) |
        (PokemonEvolution.first_evolution_form == name) |
        (PokemonEvolution.second_evolution_form == name)
    ).all()

def get_evolutions(db: Session, skip: int = 0, limit: int = 10) -> List[PokemonEvolution]:
    return db.query(PokemonEvolution).offset(skip).limit(limit).all()


def update_evolution(db: Session, evolution_id: int, evolution: EvolutionBase) -> Optional[PokemonEvolution]:
    db_evolution = db.query(PokemonEvolution).filter(PokemonEvolution.id == evolution_id).first()
    if db_evolution is None:
        return None
    for key, value in evolution.model_dump(exclude_none = True).items():
        setattr(db_evolution, key, value)
    db.commit()
    db.refresh(db_evolution)
    return db_evolution

def delete_evolution(db: Session, evolution_id: int) -> Optional[PokemonEvolution]:
    db_evolution = db.query(PokemonEvolution).filter(PokemonEvolution.id == evolution_id).first()
    if db_evolution is None:
        return None
    db.delete(db_evolution)
    db.commit()
    return db_evolution

