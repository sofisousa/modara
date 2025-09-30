from pydantic import BaseModel


class UpdateSite(BaseModel):
    name: str | None = None
    link: str | None = None
