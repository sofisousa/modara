from pydantic import BaseModel


class CreateProduct(BaseModel):
    description: str
    category_id: int
    production_id: int
