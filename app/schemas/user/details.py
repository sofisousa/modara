from pydantic import BaseModel, EmailStr


class UserDetails(BaseModel):
    id: int
    name: str
    email: EmailStr
