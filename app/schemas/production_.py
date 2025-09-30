from pydantic import BaseModel


class ProductionBase(BaseModel):
    nationality: str
    genre: str
    category: str
    year: int
    title: str
    director: str
    studio: str


class ProductionCreate(ProductionBase):
    pass


class ProductionUpdate(ProductionBase):
    nationality: str = None
    genre: str = None
    category: str = None
    year: int = None
    title: str = None
    director: str = None
    studio: str = None


class ProductionData(ProductionBase):
    id: int

    class Config:
        from_attributes = True
