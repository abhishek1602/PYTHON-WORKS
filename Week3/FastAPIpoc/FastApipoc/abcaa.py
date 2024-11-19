from fastapi import FastAPI

app = FastAPI()

@app.get("/abcaa")
async def root():
    return {"Hii": "World"}