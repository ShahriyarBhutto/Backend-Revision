from pydantic import BaseModel
from fastapi import Depends, FastAPI
from typing import Optional

# uv run python -m fastapi dev
app = FastAPI()

class UserCreate(BaseModel):
    name:str
    email:str
    age:Optional[int] = None


class UserResponse(BaseModel):
    id: int
    name:str
    email:str

fake_db = []

def get_db():
    db = {"connected":True}
    yield db

@app.get("/")
async def all_users():
    return fake_db
    
@app.get("/items")
def get_items(db= Depends(get_db)):
    return {"db_status":db["connected"],"items":[]}



@app.post('/users', response_model=UserResponse)
def create_user(user:UserCreate):
    new_user = {"id":len(fake_db)+1,"name":user.name,"email":user.email}
    fake_db.append(new_user)
    return new_user



