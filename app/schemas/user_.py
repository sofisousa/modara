from pydantic import BaseModel, EmailStr
from models.models import UserRole

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: str = None
    email: EmailStr = None
    password: str = None

class UserData(UserBase):
    id: int
    role: UserRole

    class Config:
        from_attributes = True