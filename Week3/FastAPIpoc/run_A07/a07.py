from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

# Create a Pydantic model for the input (Rectangle)
class Rectangle(BaseModel):
    length: float
    breadth: float

# Create a Pydantic model for the output (PA object with area and perimeter)
class PA(BaseModel):
    area: float
    perimeter: float

# Initialize FastAPI app
app = FastAPI()

@app.post("/calculate")
async def calculate_pa(rectangle: Rectangle) -> PA:
    # Calculate area and perimeter
    area = rectangle.length * rectangle.breadth
    perimeter = 2 * (rectangle.length + rectangle.breadth)
    
    # Return the PA object with the area and perimeter
    return PA(area=area, perimeter=perimeter)