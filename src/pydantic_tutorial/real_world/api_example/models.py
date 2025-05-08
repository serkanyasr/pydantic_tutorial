from pydantic import BaseModel,EmailStr
from typing import List
from uuid import UUID

class User(BaseModel):
    ID:UUID
    name:str
    email:EmailStr
    is_active:bool = True
    
    
class Product(BaseModel):
    ID: UUID
    name: str
    tags:List[str]
    price:float
    stock:int
    