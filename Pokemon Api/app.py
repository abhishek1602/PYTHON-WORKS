from fastapi import FastAPI, HTTPException, Query
from schemas import PokemonBase, PokemonType, PokemonUpdate, PokemonAdd, PokemonNameId
from logics import pokedex
from typing import List, Dict


app = FastAPI()

@app.post("/pokemon/", response_model=PokemonBase, status_code=201)
def add_pokemon(pokemon_data : PokemonAdd):
    for pokemon in pokedex.pokemons:
        if pokemon.name == pokemon_data.name.lower():
            raise HTTPException(status_code=406, detail="Pokemon Already Exists")
    pokemon = pokedex.add_pokemon(pokemon_data)
    return pokemon

@app.get("/pokemon/id_and_name", response_model=List[PokemonNameId])
def get_pokemon_only_id_name(page: int=Query(1,gt=0), per_page: int=Query(1,gt=0)):
    get = pokedex.get_pokemon_name_and_id(page, per_page)
    if per_page>20:
        raise HTTPException(status_code=413, detail="Cannot show more than 20 pokemons at a time")
    if not get:
        raise HTTPException(status_code=404, detail="No Pokemons Found")
    return get

@app.get("/pokemon/{pokemon_id}", response_model=PokemonBase)
def get_pokemon_by_id(pokemon_id : int):
    pokemon = pokedex.get_pokemon_by_id(pokemon_id)
    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

@app.get("/pokemon/name/{pokemon_name}", response_model=List[PokemonBase])
def get_pokemon_by_name(pokemon_name : str):
    pokemon = pokedex.get_pokemon_by_name(pokemon_name)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon Not Found")
    return pokemon

@app.get("/pokemon/type/{pokemon_type}", response_model=List[PokemonBase])
def get_pokemon_by_types(pokemon_type : PokemonType):
    pokemon = pokedex.get_pokemon_by_type(pokemon_type)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon Not Found")
    return pokemon

@app.patch("/pokemon/{pokemon_id}", response_model=PokemonBase)
def update_pokemon(pokemon_id : int, pokemon_data: PokemonUpdate):
    pokemon = pokedex.update_pokemon(pokemon_id, pokemon_data)
    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon Not Found")
    return pokemon

@app.delete("/pokemon/{pokemon_id}")
def delete_pokemon(pokemon_id: int):
    deleted = pokedex.delete_pokemon(pokemon_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Pokemon Not Found")
    return {"message": "Pokemon successfully deleted"}


@app.get("/pokemon/", response_model=List[PokemonBase])
def get_all_pokemon(page: int=Query(1,gt=0), per_page: int=Query(1,gt=0)):
    get = pokedex.get_pokemon_pagination(page, per_page)
    if per_page>20:
        raise HTTPException(status_code=413, detail="Cannot show more than 20 pokemons at a time")
    if not get:
        raise HTTPException(status_code=404, detail="No Pokemons Found")
    return get
    
