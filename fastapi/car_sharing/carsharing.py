from fastapi import FastAPI
import uvicorn

from datetime import datetime

app = FastAPI()

db = [
    {"id": 1, "size": "s", "fuel": "gasoline", "doors": 3, "transmission": "auto"},
    {"id": 2, "size": "s", "fuel": "electric", "doors": 3, "transmission": "auto"},
    {"id": 3, "size": "s", "fuel": "gasoline", "doors": 3, "transmission": "manual"},
    {"id": 4, "size": "m", "fuel": "electric", "doors": 5, "transmission": "auto"},
    {"id": 5, "size": "m", "fuel": "hybrid", "doors": 3, "transmission": "auto"},
    {"id": 6, "size": "m", "fuel": "gasoline", "doors": 3, "transmission": "manual"},
    {"id": 7, "size": "l", "fuel": "hybrid", "doors": 5, "transmission": "auto"},
    {"id": 8, "size": "l", "fuel": "diesel", "doors": 3, "transmission": "auto"},
    {"id": 9, "size": "l", "fuel": "hybrid", "doors": 5, "transmission": "manual"},
]

@app.get("/")
def welcome(name):
    return {"message": f"Hi {name}, welcome to the car sharing service!"}

@app.get("/api/cars")
def get_cars(size: str|None = None, doors: int|None = None) -> list:
    
    if size:
        return [car for car in db if car['size'] == size]
    if doors:
        return [car for car in db if car['doors'] >= doors]

    return db


if __name__ == "__main__":
    uvicorn.run("carsharing:app", reload=True)