from pydantic import BaseModel


class SiteDetails(BaseModel):
    name: str
    link: str
