from pydantic import BaseModel


class UpdateProduct(BaseModel):
    description: str | None = None
    category_id: int | None = None
    production_id: int | None = None
