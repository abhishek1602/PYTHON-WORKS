from fastapi import FastAPI, HTTPException
from schemas import PokemonBase, PokemonType
from logics import pokedex
from typing import List

app = FastAPI()

@app.post("/pokemon/", response_model=PokemonBase)
def add_pokemon(pokemon_data : PokemonBase):
    pokemon = pokedex.add_pokemon(pokemon_data)
    return pokemon

@app.get("/pokemon/{pokemon_id}", response_model=PokemonBase)
def get_pokemon(pokemon_id : int):
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

@app.put("/pokemon/{pokemon_id}", response_model=PokemonBase)
def update_pokemon(pokemon_id : int, pokemon_data: PokemonBase):
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
    