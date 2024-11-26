from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import List
from pmslogic import Logic



class ProductIn(BaseModel):
    product_id : int
    product_name : str
    product_price : float

class ProductOut(BaseModel):
    product_id : int
    product_name : str
    product_price : float


app = FastAPI()

lgk = Logic()


@app.post("/products",status_code=status.HTTP_201_CREATED)

def add_prod(new_product : ProductIn):
    added = lgk.add_product(new_product)

    if not added:
        raise HTTPException(status_code=400, detail="Product already exists")
    return {"message": "Product added successfully"}



@app.put("/products", status_code=status.HTTP_200_OK)

def update_product(product_id: int, newproduct_name: str, newproduct_price: float):
    updated = lgk.update_product(product_id, newproduct_name, newproduct_price)
    if "Not Found" in updated:
        raise HTTPException(status_code=404, detail= "Product Not Found")
    return {"message": "Product updated successfully"}



@app.get("/products",status_code=status.HTTP_200_OK)

def view_product():
    products = lgk.view_update()
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products



@app.put("/discount",status_code=status.HTTP_200_OK)

def apply_discount(discount_percentage: float):
    if discount_percentage < 0 or discount_percentage > 100:
        raise HTTPException(status_code=400, detail="Invalid discount percentage")
    price = lgk.apply_discount(discount_percentage)
    return price
    