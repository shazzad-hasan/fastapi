from fastapi import FastAPI 
from enum import Enum

app = FastAPI()

foods = {"American": ["Burger", "Apple Pie", "French Fries", "Hot Dogs", "Pizza"],
         "French": ["Paris-brest", "Steak frites", " Chicken confit", "Croque monsieur"],
         "Chinese": ["Chow Mein", "Fried Rice", "Spring Rolls", "Sweet and sour pork"]
}

class AvailableCuisines(str, Enum):
    american = "American"
    french = "French"
    chinese = "Chinese"

@app.get("/")
def welcome():
    return "welcome"

@app.get("/get_items/{cuisine}")
def get_items(cuisine: AvailableCuisines):
    return foods.get(cuisine)