from pydantic import BaseModel
from fastapi import FastAPI

class user(BaseModel):
    id:int
    name:str
    age:int



