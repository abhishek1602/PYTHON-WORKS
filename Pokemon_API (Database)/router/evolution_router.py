from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db  
from schemas.evolution_schemas import EvolutionBase, EvolutionCreate
from services.evolution_service import (
    get_evolution_service,
    get_evolutions_service,
    create_evolution_service,
    update_evolution_service,
    delete_evolution_service,
    search_evolution_by_name_service
)

router = APIRouter()

@router.get("/{evolution_id}", response_model=EvolutionBase)
def get_evolution(evolution_id: int, db: Session = Depends(get_db)):
    evolution = get_evolution_service(db, evolution_id)
    if evolution is None:
        raise HTTPException(status_code=404, detail="Evolution not found")
    return evolution

@router.get("/", response_model=List[EvolutionBase])
def get_evolutions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_evolutions_service(db, skip, limit)

@router.post("/", response_model=EvolutionBase)
def create_evolution(evolution: EvolutionCreate, db: Session = Depends(get_db)):
    return create_evolution_service(db, evolution)

@router.put("/{evolution_id}", response_model=EvolutionBase)
def update_evolution(evolution_id: int, evolution: EvolutionBase, db: Session = Depends(get_db)):
    updated_evolution = update_evolution_service(db, evolution_id, evolution)
    if updated_evolution is None:
        raise HTTPException(status_code=404, detail="Evolution not found")
    return updated_evolution

@router.delete("/{evolution_id}", response_model=EvolutionBase)
def delete_evolution(evolution_id: int, db: Session = Depends(get_db)):
    deleted_evolution = delete_evolution_service(db, evolution_id)
    if deleted_evolution is None:
        raise HTTPException(status_code=404, detail="Evolution not found")
    return deleted_evolution

@router.get("/search/{name}", response_model=List[EvolutionBase])
def search_evolution_by_name(name: str, db: Session = Depends(get_db)):
    return search_evolution_by_name_service(db, name)