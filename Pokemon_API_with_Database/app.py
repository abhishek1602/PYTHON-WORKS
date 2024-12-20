from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import sessionlocal
from schemas import PokemonAdd, PokemonUpdate, PokemonIdNames, PokemonBase, PokemonType
from logics import (
    add_pokemon, get_all_pokemons, get_pokemon_by_id, get_pokemon_by_name,
    get_pokemon_by_type, update_pokemon, delete_pokemon, get_pokemon_id_name
)
from model import Pokemon

app = FastAPI()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/pokemons/", response_model=PokemonBase)
def create_pokemon(pokemon: PokemonAdd, db: Session = Depends(get_db)):
    existing_pokemon = db.query(Pokemon).filter(Pokemon.name == pokemon.name.lower()).first()
    if existing_pokemon:
        raise HTTPException(status_code=406, detail="Cannot add duplicate pokemon")
    return add_pokemon(db, pokemon)

@app.get("/pokemons/", response_model=list[PokemonBase])
def all_pokemons(page: int = 1, db: Session = Depends(get_db)):
    return get_all_pokemons(db, page)

@app.get("/pokemons/{pokemon_id}", response_model=PokemonAdd)
def pokemon_by_id(pokemon_id: int, db: Session = Depends(get_db)):
    return get_pokemon_by_id(db, pokemon_id)

@app.get("/pokemons/name/{name}", response_model=PokemonBase)
def pokemon_by_name(name: str, db: Session = Depends(get_db)):
    return get_pokemon_by_name(db, name)

@app.get("/pokemons/type/{pokemon_type}", response_model=list[PokemonBase])
def pokemon_by_type(pokemon_type: PokemonType, db: Session = Depends(get_db)):
    return get_pokemon_by_type(db, pokemon_type)

@app.patch("/pokemons/{pokemon_id}", response_model=PokemonBase)
def update_pokemon_details(pokemon_id: int, pokemon: PokemonUpdate, db: Session = Depends(get_db)):
    return update_pokemon(db, pokemon_id, pokemon)

@app.delete("/pokemons/{pokemon_id}")
def remove_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    return delete_pokemon(db, pokemon_id)

@app.get("/pokemons/id-name/", response_model=list[PokemonIdNames])
def pokemon_id_name(page: int = 1, db: Session = Depends(get_db)):
    return get_pokemon_id_name(db, page)