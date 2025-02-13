from typing import List, Optional
from sqlalchemy.orm import Session
from repositories.evolution_repository import (
    get_evolution,
    get_evolutions,
    create_evolution,
    update_evolution,
    delete_evolution,
    search_evolution_by_name
)
from schemas.evolution_schemas import EvolutionBase
from models.pokemon_evolution import PokemonEvolution

def search_evolution_by_name_service(db: Session, name: str) -> List[PokemonEvolution]:
    return search_evolution_by_name(db, name)

def get_evolution_service(db: Session, evolution_id: int) -> Optional[PokemonEvolution]:
    return get_evolution(db, evolution_id)

def get_evolutions_service(db: Session, skip: int = 0, limit: int = 10) -> List[PokemonEvolution]:
    return get_evolutions(db, skip, limit)

def create_evolution_service(db: Session, evolution: EvolutionBase) -> PokemonEvolution:
    return create_evolution(db, evolution)

def update_evolution_service(db: Session, evolution_id: int, evolution: EvolutionBase) -> Optional[PokemonEvolution]:
    return update_evolution(db, evolution_id, evolution)

def delete_evolution_service(db: Session, evolution_id: int) -> Optional[PokemonEvolution]:
    return delete_evolution(db, evolution_id)
