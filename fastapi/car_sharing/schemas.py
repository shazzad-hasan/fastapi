import json
from pydantic import BaseModel 

class Car(BaseModel):
    id: int 
    size: str 
    fuel: str | None = "electric"
    doors: int 
    transmission: str | None = "auto"

def load_db() -> list[Car]:
    """ Load a list of car objects from a JSON file """
    with open("cars.json") as f:
        return [Car.parse_obj(obj) for obj in json.load(f)]