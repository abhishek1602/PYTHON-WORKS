from router import pokemon_router
from utils.init_db import initialize_db, load_json_to_db
from fastapi import FastAPI

app = FastAPI()
initialize_db()
load_json_to_db("pokemon_data.json")

app.include_router(pokemon_router.router, prefix="/pokemon", tags=["Pokemon"])



