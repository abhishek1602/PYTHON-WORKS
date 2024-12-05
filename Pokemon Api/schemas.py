from pydantic import BaseModel
from typing import List
from enum import Enum

class PokemonType(str, Enum):
    grass = "grass"
    fire = "fire"
    water = "water"
    electric = "electric"
    ice = "ice"
    poison = "poison"
    ground = "ground"
    flying = "flying"
    psychic = "psychic"
    bug = "bug"
    rock = "rock"
    ghost = "ghost"
    dragon = "dragon"
    dark = "dark"
    fairy = "fairy"
    steel  = "steel"
    fighting = "fighting"
    normal = "normal"

class PokemonBase(BaseModel):
    id : int
    name : str
    height : int
    weight : int
    xp : int
    image_url : str
    pokemon_url : str
    abilities : List[str]
    stats : List[dict]
    types : List[PokemonType]
