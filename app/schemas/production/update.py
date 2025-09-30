from pydantic import BaseModel


class UpdateProduction(BaseModel):
    year: int | None = None
    title: str | None = None
    director: str | None = None
    studio: str | None = None
    nationality_id: int | None = None
    genre_id: int | None = None
    category_id: int | None = None
