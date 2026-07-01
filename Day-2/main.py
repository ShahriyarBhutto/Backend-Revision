from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class User(BaseModel):
    name:str
    email:str
    age:Optional[int]= None

class UserResponse(BaseModel):
    id:int
    name:str
    email:str

fake_db = []

def get_db():
    db={"connected":True}
    yield db


@app.get("/")
async def get_all_users():
    return fake_db

@app.get("/user/{id}")
async def get_user_by_id(id:int):
    for user in fake_db:
        if user["id"] == id:
            return user
        
@app.get("/db")
async def db_connect(db=Depends(get_db)):
    return {"db":db["connected"],"message":"Db connected hoa"}
        
@app.post("/users")
async def post_user(user:User):
    new_user = {"id":len(fake_db)+1,"name":user.name,"email":user.email,"age":user.age}
    fake_db.append(new_user)
    return new_user
