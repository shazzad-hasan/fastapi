from fastapi import FastAPI 
import uvicorn
from typing import List 
from uuid import uuid4 
from models import Gender, Role, User 

app = FastAPI()

db: List[User] = [
    User(id = uuid4(),
         first_name = "Jake",
         last_name = "Sully",
         gender = Gender.male,
         roles = [Role.student]
    ),
    User(id = uuid4(),
         first_name = "Neytiri",
         last_name = "Sully",
         gender = Gender.male,
         roles = [Role.admin, Role.user]
    )
]

@app.get("/")
def root():
    return {"Hell": "World"}

@app.get("/api/users")
def get_users():
    return db;

if __name__== "__main__":
    uvicorn.run("main:app", reload = True)