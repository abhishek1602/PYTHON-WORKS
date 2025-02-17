from router import pokemon_router, auth_router, evolution_router
from utils.init_db import initialize_db
from fastapi import FastAPI

app = FastAPI()

initialize_db()
app.include_router(pokemon_router.router, prefix="/pokemon", tags=["Pokemon"])
app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])
app.include_router(evolution_router.router, prefix="/evolutions", tags=["Evolution Chain"])



