# repositories/pokemon_repository.py
from sqlalchemy.orm import Session
from models.pokemon_models import Pokemon
from schemas.schemas import PokemonAdd, PokemonUpdate

def add_pokemon(db: Session, pokemon_data):
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
    return db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()

def get_pokemon_by_name(db: Session, name: str):
    return db.query(Pokemon).filter(Pokemon.name == name.lower()).first()

def get_pokemon_by_type(db: Session, pokemon_type):
    return db.query(Pokemon).filter(Pokemon.types.contains(pokemon_type)).all()

def update_pokemon(db: Session, pokemon_id: int, update_data: PokemonUpdate):
    pokemon = db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()
    if not pokemon:
        return None
    for key, value in update_data.model_dump(exclude_none=True).items():
        setattr(pokemon, key, value)
    db.commit()
    db.refresh(pokemon)
    return pokemon

def delete_pokemon(db: Session, pokemon_id: int):
    pokemon = db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()
    if not pokemon:
        return None
    db.delete(pokemon)
    db.commit()
    return pokemon

def get_pokemon_id_name(db: Session, page: int, page_size: int = 20):
    return db.query(Pokemon.id, Pokemon.name).offset((page - 1) * page_size).limit(page_size).all()