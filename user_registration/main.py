from fastapi import FastAPI, HTTPException
import uvicorn
from typing import List 
from uuid import UUID, uuid4 
from models import Gender, Role, User, UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(id = UUID("d036cfcc-b5dd-40de-a3ea-81b00a08c158"),
         first_name = "Jake",
         last_name = "Sully",
         gender = Gender.male,
         roles = [Role.student]
    ),
    User(id = UUID("e0b81bed-523d-421e-b87c-ad52bab56055"),
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

@app.post("/api/users")
def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/users/{user_id}")
def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail = f"user with id: {user_id} doesn't exists."
    )
    
@app.put("/api/users/{user_id}")
def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db: 
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name 
            if user_update.last_name is not None:
                user.last_name = user_update.last_name 
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name 
            if user_update.roles is not None:
                user.roles = user_update.roles 
            return 
    raise HTTPException(
        status_code = 404,
        detail = f"user with id: {user_id} doesn't exists."
    )



if __name__== "__main__":
    uvicorn.run("main:app", reload = True)