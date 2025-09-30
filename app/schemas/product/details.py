from pydantic import BaseModel


class ProductDetails(BaseModel):
    id: int
    description: str
    category_id: int
    category_name: str
    production_id: int
    production_name: str
