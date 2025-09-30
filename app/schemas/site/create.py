from pydantic import BaseModel


class CreateSite(BaseModel):
    name: str
    link: str
