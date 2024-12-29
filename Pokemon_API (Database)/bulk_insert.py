import json
from database import sessionlocal, initialize_db
from model import Pokemon

def load_json_to_db(json_path : str):
    with open(json_path, 'r') as file:
        data = json.load(file)


    db = sessionlocal()
    pokemons = [
        Pokemon(
            name=pokemon["name"].lower(),
            height=pokemon["height"],
            weight=pokemon["weight"],
            xp=pokemon["xp"],
            image_url=pokemon["image_url"],
            pokemon_url=pokemon["pokemon_url"],
            abilities=[ability["name"] for ability in pokemon["abilities"]],
            stats=pokemon["stats"],
            types=[typ["name"] for typ in pokemon["types"]]
        )
        for pokemon in data
        ]

    db.add_all(pokemons)
    db.commit()
    db.close()

if __name__ == "__main__":
    initialize_db()
    load_json_to_db("pokemon_data.json")

    