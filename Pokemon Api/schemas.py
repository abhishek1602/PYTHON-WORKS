from pydantic import BaseModel
from typing import List, Optional
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


class PokemonUpdate(BaseModel): 
    name: Optional[str] = None 
    height: Optional[int] = None 
    weight: Optional[int] = None 
    xp: Optional[int] = None 
    image_url: Optional[str] = None 
    pokemon_url: Optional[str] = None 
    abilities: Optional[List[str]] = None 
    stats: Optional[List[dict]] = None 
    types: Optional[List[PokemonType]] = None

class PokemonAdd(BaseModel):
    name : str
    height : int
    weight : int
    xp : int
    image_url : str
    pokemon_url : str
    abilities : List[str]
    stats : List[dict]
    types : List[PokemonType]

class PokemonNameId(BaseModel):
    id: int
    name: str