from models.models import Site
from schemas.site.create import CreateSite
from schemas.site.update import UpdateSite
from schemas.site.details import SiteDetails


class SiteRepository:
    @classmethod
    async def create(
        cls,
        site: CreateSite
    ) -> Site:
        return await Site.create(name=site.name, link=site.link)

    @classmethod
    async def update(
        cls,
        id: int,
        update_info: UpdateSite
    ):
        update_info = update_info.model_dump(exclude_none=True)

        if not update_info:
            return await Site.get_or_none(id=id)

        await Site.filter(id=id).update(**update_info)

    @classmethod
    async def delete(
        cls,
        id: int
    ):
        await Site.filter(id=id).delete()

    @classmethod
    async def get_one_by_id(
        cls,
        id: int
    ):
        return await Site.get_or_none(id=id)

    @classmethod
    async def get_all(
        cls
    ):
        return await Site.all()
