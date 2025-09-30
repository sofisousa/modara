from pydantic import BaseModel


class ProductBase(BaseModel):
    description: str
    category: str
    production_id: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    description: str = None
    category: str = None
    production_id: int = None

class ProductData(ProductBase):
    id: int

    class Config:
        from_attributes = True

