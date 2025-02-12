from fastapi import FastAPI
from app.routers.api_router import api_router
from app.utils.bulk_insert import bulk_insert

app = FastAPI()

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Quiz Application API"}

if __name__ == "__main__":
    bulk_insert()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
