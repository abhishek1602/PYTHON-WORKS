from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import sessionlocal
from schemas.schemas import PokemonAdd, PokemonUpdate, PokemonIdNames, PokemonBase, PokemonType
from services.pokemon_services import (
    add_pokemon, all_pokemons, pokemon_by_id, pokemon_by_name,
    pokemon_by_type, update_pokemons, remove_pokemon, pokemon_id_name
)
from models.pokemon_models import Pokemon

# Create the router
router = APIRouter()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PokemonBase)
def create_pokemon(pokemon: PokemonAdd, db: Session = Depends(get_db)):
    existing_pokemon = db.query(Pokemon).filter(Pokemon.name == pokemon.name.lower()).first()
    if existing_pokemon:
        raise HTTPException(status_code=406, detail="Cannot add duplicate pokemon")
    return add_pokemon(db, pokemon)

@router.get("/", response_model=list[PokemonBase])
def get_all_pokemons(page: int = 1, db: Session = Depends(get_db)):
    return all_pokemons(db, page)

@router.get("/{pokemon_id}", response_model=PokemonAdd)
def get_pokemon_by_id(pokemon_id: int, db: Session = Depends(get_db)):
    return pokemon_by_id(db, pokemon_id)

@router.get("/name/{name}", response_model=PokemonBase)
def get_pokemon_by_name(name: str, db: Session = Depends(get_db)):
    return pokemon_by_name(db, name)

@router.get("/type/{pokemon_type}", response_model=list[PokemonBase])
def get_pokemon_by_type(pokemon_type: PokemonType, db: Session = Depends(get_db)):
    return pokemon_by_type(db, pokemon_type)

@router.patch("/{pokemon_id}", response_model=PokemonBase)
def update_pokemon_details(pokemon_id: int, pokemon: PokemonUpdate, db: Session = Depends(get_db)):
    return update_pokemons(db, pokemon_id, pokemon)

@router.delete("/{pokemon_id}")
def delete_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    return remove_pokemon(db, pokemon_id)

@router.get("/id-name/", response_model=list[PokemonIdNames])
def get_pokemon_id_name(page: int = 1, db: Session = Depends(get_db)):
    return pokemon_id_name(db, page)
