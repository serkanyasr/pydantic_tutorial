
from pydantic import BaseModel, Field , EmailStr
from typing import Optional,List

class UserCreate(BaseModel):
    name:str = Field(... , min_length=2)
    email:EmailStr
    
class UserUpdate(BaseModel):
    name:Optional[str] = Field(None, min_length=2)
    email:Optional[EmailStr]
    is_active:Optional[bool]
    
class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    is_active: bool
    
    