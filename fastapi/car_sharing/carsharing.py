from fastapi import FastAPI, HTTPException
import uvicorn
from schemas import load_db

app = FastAPI()
db = load_db()

@app.get("/")
def welcome(name):
    return {"message": f"Hi {name}, welcome to the car sharing service!"}

@app.get("/api/cars")
def get_cars(size: str|None=None, doors: int|None=None) -> list:
    
    if size:
        return [car for car in db if car['size'] == size]
    if doors:
        return [car for car in db if car['doors'] >= doors]

    return db

@app.get("/api/cars/{id}")
def car_by_id(id: int) -> dict:
    result = [car for car in db if car['id'] == id]

    if result: 
        return result[0]
    else:
        raise HTTPException(status_code=404, detail=f"No car with id = {id}.")

if __name__ == "__main__":
    uvicorn.run("carsharing:app", reload=True)