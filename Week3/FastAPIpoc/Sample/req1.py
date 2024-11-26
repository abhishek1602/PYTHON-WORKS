import requests

# Base URL for the manufacturing API
base_url = "http://127.0.0.1:8000/add"

# 1. GET Request: Fetch all items in the warehouse
def checkadd(numdata):
    response = requests.post(base_url, json=numdata)
    
    if response.status_code == 200:
        print("got result")
        print(response.json())  # Display the added item details
    

# Example Usage


# 2. POST request to add a new item
data = {
    "a": 2,
    "b": 3,
    
}

checkadd(data)