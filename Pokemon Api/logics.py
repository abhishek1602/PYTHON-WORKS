import json
from schemas import PokemonBase, PokemonType
from model import Pokemon
from typing import List, Optional


class Pokedex:

    def __init__(self):
        self.pokemons = []
        self.load_pokemons()
        self.next_id = len(self.pokemons)+1

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
            id=self.next_id,
            name=pokemon_data.name.lower(),
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
        self.next_id = self.next_id+1
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
                if pokemon_data.name is not None:
                    pokemon.name = pokemon_data.name.lower()
                if pokemon_data.height is not None:
                    pokemon.height = pokemon_data.height 
                if pokemon_data.weight is not None:
                    pokemon.weight = pokemon_data.weight
                if pokemon_data.xp is not None: 
                    pokemon.xp = pokemon_data.xp 
                if pokemon_data.image_url is not None:
                    pokemon.image_url = pokemon_data.image_url 
                if pokemon_data.pokemon_url is not None:
                    pokemon.pokemon_url = pokemon_data.pokemon_url 
                if pokemon_data.abilities is not None:
                    pokemon.abilities = pokemon_data.abilities 
                if pokemon_data.stats is not None:
                    pokemon.stats = pokemon_data.stats 
                if pokemon_data.types is not None:
                    pokemon.types = [PokemonType(typ) for typ in pokemon_data.types] 
                return pokemon
        return None
    

    def delete_pokemon(self, pokemon_id: int) -> bool:
        for pokemon in self.pokemons:
            if pokemon.id == pokemon_id:
                self.pokemons.remove(pokemon)
                return True
        return False
    
    def get_pokemon_pagination(self, page: int, per_page: int) -> List[Pokemon]:

        start = (page - 1) * per_page
        end = start + per_page
        return self.pokemons[start:end]
    
    def get_pokemon_name_and_id(self, page: int, per_page: int) -> List[dict]:  
        start = (page - 1) * per_page 
        end = start + per_page 
        result = [] 
        for pokemon in self.pokemons[start:end]: 
            result.append({"id": pokemon.id, "name": pokemon.name}) 
        return result
    
    

pokedex = Pokedex()