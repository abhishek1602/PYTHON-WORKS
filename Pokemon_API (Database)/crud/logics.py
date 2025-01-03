from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.model import Pokemon
from schemas.schemas import PokemonAdd, PokemonUpdate, PokemonIdNames, PokemonType

from sqlalchemy.orm import Session


def add_pokemon(db: Session, pokemon_data: PokemonAdd):
    new_pokemon = Pokemon(
        name=pokemon_data.name.lower(),
        height=pokemon_data.height,
        weight=pokemon_data.weight,
        xp=pokemon_data.xp,
        image_url=pokemon_data.image_url,
        pokemon_url=pokemon_data.pokemon_url,
        abilities=pokemon_data.abilities,
        stats=pokemon_data.stats,
        types=pokemon_data.types
    )
    
    db.add(new_pokemon)
    db.commit()
    db.refresh(new_pokemon)
    return new_pokemon


def get_all_pokemons(db: Session, page: int, page_size: int = 20):
    return db.query(Pokemon).offset((page - 1) * page_size).limit(page_size).all()

def get_pokemon_by_id(db: Session, pokemon_id: int):
    pokemon = db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

def get_pokemon_by_name(db: Session, name: str):
    pokemon = db.query(Pokemon).filter(Pokemon.name == name.lower()).first()
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

def get_pokemon_by_type(db: Session, pokemon_type: PokemonType):
    return db.query(Pokemon).filter(Pokemon.types.contains([pokemon_type.lower()])).all()

def update_pokemon(db: Session, pokemon_id: int, update_data: PokemonUpdate):
    pokemon = db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")

    for key, value in update_data.model_dump(exclude_unset=True).items():
        setattr(pokemon, key, value)

    db.commit()
    db.refresh(pokemon)
    return pokemon

def delete_pokemon(db: Session, pokemon_id: int):
    pokemon = db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")

    db.delete(pokemon)
    db.commit()
    return {"detail": "Pokemon deleted successfully"}

def get_pokemon_id_name(db: Session, page: int, page_size: int = 20):
    pokemons = db.query(Pokemon.id, Pokemon.name).offset((page - 1) * page_size).limit(page_size).all()
    return [PokemonIdNames(id=pokemon.id, name=pokemon.name) for pokemon in pokemons]