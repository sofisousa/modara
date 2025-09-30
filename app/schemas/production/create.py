from pydantic import BaseModel


class CreateProduction(BaseModel):
    year: int
    title: str
    director: str
    studio: str
    nationality_id: int
    genre_id: int
    category_id: int
