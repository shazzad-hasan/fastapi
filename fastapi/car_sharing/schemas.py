import json
from pydantic import BaseModel 

class CarInput(BaseModel):
    size: str 
    fuel: str | None = "electric"
    doors: int 
    transmission: str | None = "auto"

class CarOutput(CarInput):
    id: int 

def load_db() -> list[CarOutput]:
    with open("cars.json") as f:
        return [CarOutput.parse_obj(obj) for obj in json.load(f)]

def save_db(cars: list[CarOutput]):
    with open("cars.json", 'w') as f:
        json.dump([car.dict() for car in cars], f, indent=4)


