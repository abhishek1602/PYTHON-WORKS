from router import pokemon_router
from utils.init_db import initialize_db
from fastapi import FastAPI

app = FastAPI()
initialize_db()
app.include_router(pokemon_router.router, prefix="/pokemon", tags=["Pokemon"])



