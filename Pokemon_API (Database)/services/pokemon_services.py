# services/pokemon_services.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from schemas.schemas import PokemonAdd, PokemonUpdate, PokemonIdNames, PokemonType
from repositories.pokemon_repository import (
    add_pokemon,
    get_all_pokemons,
    get_pokemon_by_id,
    get_pokemon_by_name,
    get_pokemon_by_type,
    update_pokemon,
    delete_pokemon,
    get_pokemon_id_name
)

def create_pokemon(db: Session, pokemon_data: PokemonAdd):
    return add_pokemon(db, pokemon_data)

def all_pokemons(db: Session, page: int, page_size: int = 20):
    return get_all_pokemons(db, page, page_size)

def pokemon_by_id(db: Session, pokemon_id: int):
    pokemon = get_pokemon_by_id(db, pokemon_id)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

def pokemon_by_name(db: Session, name: str):
    pokemon = get_pokemon_by_name(db, name)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

def pokemon_by_type(db: Session, pokemon_type: PokemonType):
    return get_pokemon_by_type(db, pokemon_type)

def update_pokemons(db: Session, pokemon_id: int, update_data: PokemonUpdate):
    pokemon = update_pokemon(db, pokemon_id, update_data)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

def remove_pokemon(db: Session, pokemon_id: int):
    pokemon = delete_pokemon(db, pokemon_id)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return {"detail": "Pokemon deleted successfully"}

def pokemon_id_name(db: Session, page: int, page_size: int = 20):
    pokemons = get_pokemon_id_name(db, page, page_size)
    return [PokemonIdNames(id=pokemon.id, name=pokemon.name) for pokemon in pokemons]