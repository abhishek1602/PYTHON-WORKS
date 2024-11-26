from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Dict
from logics import Logics


# Create a Pydantic model for the input
class Product(BaseModel):
    productId: int
    productName: str
    productPrice: float


# Initialize FastAPI app
app = FastAPI()
lgk = Logics()

@app.post("/addProduct", status_code=status.HTTP_201_CREATED)
async def addProductws(newProduct: Product):
    add = lgk.addProduct(newProduct)
    if not add:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product Not Added (Duplicate ID)"
        )
    return {"message": "Product added successfully"}

@app.put("/updateProduct", status_code=status.HTTP_200_OK)
async def updateProductws(productId: int, newName: str, newPrice: float):
    update = lgk.updateProduct(productId, newName, newPrice)
    if "Not Found" in update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product Not Found"
        )
    return {"message": update}

@app.get("/viewProduct", status_code=status.HTTP_200_OK)
async def viewProductws():
    view = lgk.viewProducts()
    if not view:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No Products Found"
        )
    return view

@app.put("/applyDiscount", status_code=status.HTTP_200_OK)
async def applyDiscws(discAmount: float):
    if discAmount <= 0 or discAmount > 100:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid discount percentage: {discAmount}%"
        )
    result = lgk.applyDiscount(discAmount)
    return result




    


