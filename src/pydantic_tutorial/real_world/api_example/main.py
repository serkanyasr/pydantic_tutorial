from fastapi import FastAPI, HTTPException, Query
from uuid import uuid4
from models import User
from schemas import UserCreate, UserResponse, UserUpdate
from typing import List
from fastapi.responses import JSONResponse

app = FastAPI()
db = {}

@app.post("/users", response_model=UserResponse)
def create_user(user_data: UserCreate):
    user_id = str(uuid4())
    user = User(id=user_id, name=user_data.name, email=user_data.email)
    db[user_id] = user
    return user

@app.get("/users", response_model=List[UserResponse])
def list_users(is_active: bool = Query(None)):
    users = list(db.values())
    if is_active is not None:
        users = [user for user in users if user.is_active == is_active]
    return users

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: str):
    user = db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: str, update: UserUpdate):
    user = db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = user.copy(update=update.model_dump(exclude_unset=True))
    db[user_id] = updated_user
    return updated_user

@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    if user_id not in db:
        return JSONResponse(status_code=404, content={"detail": "User not found"})
    del db[user_id]
    return {"message": "User deleted"}
