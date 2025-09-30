from pydantic import BaseModel


class ProductionDetails(BaseModel):
    id: int
    year: int
    title: str
    director: str
    studio: str
    nationality_id: int
    nationality_name: str
    genre_id: int
    genre_name: str
    category_id: int
    category_name: str
