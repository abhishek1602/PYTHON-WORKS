import json
from schemas import PokemonBase, PokemonType
from model import Pokemon
from typing import List, Optional


class Pokedex:

    def __init__(self):
        self.pokemons = []
        self.load_pokemons()

    def load_pokemons(self):
        json_path = "C:\PYTHON WORKS\Pokemon Api\pokemon_raw_data.json"

        with open(json_path, 'r') as file:
            data = json.load(file)

            for pokemon_data in data:
                pokemon = Pokemon(
                    id=pokemon_data["id"], 
                    name=pokemon_data["name"], 
                    height=pokemon_data["height"], 
                    weight=pokemon_data["weight"], 
                    xp=pokemon_data["xp"], 
                    image_url=pokemon_data["image_url"], 
                    pokemon_url=pokemon_data["pokemon_url"], 
                    abilities=[ability["name"] for ability in pokemon_data["abilities"]], 
                    stats=pokemon_data["stats"], 
                    types=[PokemonType(typ["name"]) for typ in pokemon_data["types"]]
                )
                self.pokemons.append(pokemon)

    
    def add_pokemon(self, pokemon_data : PokemonBase):
        new_pokemon = Pokemon(
            id=len(self.pokemons)+1,
            name=pokemon_data.name,
            height=pokemon_data.height,
            weight=pokemon_data.weight,
            xp=pokemon_data.xp,
            image_url=pokemon_data.image_url,
            pokemon_url=pokemon_data.pokemon_url,
            abilities=pokemon_data.abilities,
            stats=pokemon_data.stats,
            types=[PokemonType(typ) for typ in pokemon_data.types]   
            )
        self.pokemons.append(new_pokemon)
        return new_pokemon
    
    def get_pokemon_by_id(self, pokemon_id : int) -> Optional[Pokemon]:
        for pokemon in self.pokemons:
            if pokemon.id == pokemon_id:
                return pokemon
        return None
        

    def get_pokemon_by_name(self, name: str) -> List[Pokemon]:
        results = []
        for pokemon in self.pokemons:
            if name.lower() in pokemon.name.lower():
                results.append(pokemon)
        return results
    

    def get_pokemon_by_type(self, pokemon_type: PokemonType) -> List[Pokemon]:
        results = []
        for pokemon in self.pokemons:
            if pokemon_type in pokemon.types:
                results.append(pokemon)
        return results
    
    def update_pokemon(self, pokemon_id: int, pokemon_data: PokemonBase) -> Optional[Pokemon]:
        for pokemon in self.pokemons:
            if pokemon.id == pokemon_id:
                pokemon.name = pokemon_data.name 
                pokemon.height = pokemon_data.height 
                pokemon.weight = pokemon_data.weight 
                pokemon.xp = pokemon_data.xp 
                pokemon.image_url = pokemon_data.image_url 
                pokemon.pokemon_url = pokemon_data.pokemon_url 
                pokemon.abilities = pokemon_data.abilities 
                pokemon.stats = pokemon_data.stats 
                pokemon.types = [PokemonType(typ) for typ in pokemon_data.types] 
                return pokemon
        return None
    

    def delete_pokemon(self, pokemon_id: int) -> bool:
        for pokemon in self.pokemons:
            if pokemon.id == pokemon_id:
                self.pokemons.remove(pokemon)
                return True
        return False
    

pokedex = Pokedex()


