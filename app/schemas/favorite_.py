from pydantic import BaseModel
from schemas.user_ import UserData
from schemas.product_ import ProductData

class FavoriteBase(BaseModel):
    product_id: int
    user_id: int

class FavoriteCreate(FavoriteBase):
    pass

class FavoriteData(FavoriteBase):
    user_ind: int
    product_id: int
    product_description: str

    class Config:
        from_attributes = True
