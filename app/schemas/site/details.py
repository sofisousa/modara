from pydantic import BaseModel


class SiteDetails(BaseModel):
    id: int
    name: str
    link: str
