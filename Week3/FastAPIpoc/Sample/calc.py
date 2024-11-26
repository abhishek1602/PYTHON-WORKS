

#python -m uvicorn a02app:app --reload

from fastapi import FastAPI
from pydantic import BaseModel
from calculator import add, subtract

#The Swagger UI will be available at http://127.0.0.1:8000/docs.
#pip install fastapi uvicorn



# FastAPI app instance
app = FastAPI()

'''
The code you provided defines a Pydantic model class called Numbers,
 which is a subclass of BaseModel. Pydantic is a data validation and settings 
 management library in Python, which uses Python's type annotations to
   validate data.
'''

# Pydantic model to parse input data
class Numbers(BaseModel):
    a: float
    b: float


'''
input in post request body...

{
  "a": 0,
  "b": 0
}

'''



# Route to add two numbers
@app.post("/add")
def perform_addition(numbers: Numbers):
    result = add(numbers.a, numbers.b)
    return {"result": result}

# Route to subtract two numbers
@app.post("/subtract")
def perform_subtraction(numbers: Numbers):
    result = subtract(numbers.a, numbers.b)
    return {"result": result}

'''
1.have your project folder.
2. change to the project folder.
3. create a virtual environemnt.
python -m venv x #x can is proper nown you can keep it whatever you want..
Set-ExecutionPolicy Unrestricted -Scope Process

4. activate the virtual environemnt
#venv\Scripts\activate
5. install the library for fastapi
pip install fastapi uvicorn

project folder structure
fastapi-calculator/
├── app.py             # FastAPI application
├── calculator.py      # Logic for addition and subtraction
├── x/              # Virtual environment folder (created by `python -m venv x`)
└── requirements.txt   # File to store dependencies (optional but recommended)

create logic.py
create app.py

run the application uvicorn app:app --reload

#to freeze the requirement
pip freeze > requirements.txt

#deactivate the virtual environemnt
deactivate













'''