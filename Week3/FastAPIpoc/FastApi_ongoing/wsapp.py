from fastapi import FastAPI,status,HTTPException
from logics import Logic

app = FastAPI()
lgk = Logic()

@app.get("/test",status_code=status.HTTP_200_OK)
def multiply(firstNum: int, secondNum:int):

    if firstNum == 0 or secondNum ==0:
        raise HTTPException(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            detail="Numbers cannot be zero"
        )
    mult = lgk.takeNumber(firstNum, secondNum)
    return {"message": "success", "result":mult}
