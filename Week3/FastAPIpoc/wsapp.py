from fastapi import FastAPI
from logics import Logic

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/test")
def real():
    lgk = Logic()
    makeRS = lgk.rs()

    return makeRS

@app.get("/input")
def take(num):
    lgk = Logic()
    result = lgk.nextNumber(int(num))
    return f"result: {result}"

