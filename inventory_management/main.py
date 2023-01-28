from fastapi import FastAPI, Path, HTTPException, status
from typing import Optional
from pydantic import BaseModel
import uvicorn 

app = FastAPI()

class InputItem(BaseModel):
    name: str
    weight: str
    brand: str 
    diet_type: Optional[str] = None
    price: float

class UpdateItem(BaseModel):
    name: Optional[str] = None
    weight: Optional[str] = None
    brand: Optional[str] = None
    diet_type: Optional[str] = None
    price: Optional[float] = None

# inventory = {
#     1: {"name": "Coffee",
#         "weight": "190 Grams",
#         "brand": "Douwe Egberts",
#         "format": "Instant Coffee",
#         "price": 3},

#     2: {"name": "Cashew Nuts",
#         "weight": "1 Kilograms",
#         "brand": "Old India",
#         "diet_type": "Vegetarian", 
#         "price": 10}
# } 

inventory = {}

@app.get("/")
def home():
    return "Hi!"

@app.get("/get_item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]

@app.get("/get_by_name")
def get_item(name: Optional[str]=None):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=400, detail="Item not found.")

@app.post("/add_item/{item_id}")
def add_item(item_id: int, item: InputItem):
    if item_id in inventory:
        raise HTTPException(status_code=404,  detail="Item already exists.")
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update_item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found.")

    if item.name != None:
        inventory[item_id].name = item.name 
    if item.weight != None:
        inventory[item_id].weight = item.weight
    if item.brand != None:
        inventory[item_id].brand = item.brand 
    if item.diet_type != None:
        inventory[item_id].diet_type = item.diet_type
    if item.price != None:
        inventory[item_id].price = item.price

    return inventory[item_id]

@app.delete("/delete_item")
def delete_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found.")
    del inventory[item_id]
    return {"Success": "Item deleted!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)