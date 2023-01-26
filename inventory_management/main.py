from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
import uvicorn 

app = FastAPI()

class InputItem(BaseModel):
    item: str
    weight: str
    brand: str 
    diet_type: Optional[str] = None
    price: float

inventory = {
    1: {"Item": "Coffee",
        "Item weight": "190 Grams",
        "Brand": "Douwe Egberts",
        "Format": "Instant Coffee",
        "Price": 3},

    2: {"Item": "Cashew Nuts",
        "Item weight": "1 Kilograms",
        "Brand": "Old India",
        "Diet type": "Vegetarian", 
        "Price": 10}
}

@app.get("/")
def home():
    return "Hi!"

@app.get("/get_item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]

@app.get("/get_by_name")
def get_item(name: Optional[str]=None):
    for item_id in inventory:
        if inventory[item_id]["Item"] == name:
            return inventory[item_id]
    return {name: "Not found"}

@app.post("/add_item/{item_id}")
def add_item(item: InputItem, item_id: int):
    if item_id in inventory:
        return {"Error": "Item already exists."}
    inventory[item_id] = {"Item": item.name,
                          "Item weight": item.weight,
                          "Brand": item.brand,
                          "Diet type": item.diet_type,
                          "Price": item.price
                          }
    return inventory[item_id]


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)