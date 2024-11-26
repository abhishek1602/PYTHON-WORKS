from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from fastapi import status

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

#default statuscode is 200..
@app.post("/calculate", status_code=status.HTTP_200_OK)
async def calculate_pa(rectangle: Rectangle) -> PA:
    # Validation for positive dimensions
    if rectangle.length <= 0 or rectangle.breadth <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Length and breadth must be positive values."
        )
    
    # Calculate area and perimeter
    area = rectangle.length * rectangle.breadth
    perimeter = 2 * (rectangle.length + rectangle.breadth)
    
    # Return the PA object with the area and perimeter
    return PA(area=area, perimeter=perimeter)