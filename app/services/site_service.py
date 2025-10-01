from repositories.site_repository import SiteRepository
from schemas.site.create import CreateSite
from schemas.site.update import UpdateSite
from schemas.site.details import SiteDetails
from utils.http_message import not_found_error


class SiteService:
    def __init__(self):
        pass

    async def create(
        self,
        site: CreateSite
    ):
        site = await SiteRepository.create(site=site)
        site = await SiteRepository.get_one_by_id(id=site.id)

        return SiteDetails(
            id=site.id,
            name=site.name,
            link=site.link
        )

    async def update(
        self,
        id: int,
        update_info: UpdateSite
    ):
        await SiteRepository.update(id=id, update_info=update_info)

    async def get_details(
        self,
        id: int
    ):
        site = await SiteRepository.get_one_by_id(id=id)

        if not site:
            raise not_found_error(entity="Site")

        return SiteDetails(
            id=site.id,
            name=site.name,
            link=site.link
        )

    async def get_all(
        self
    ):
        sites = await SiteRepository.get_all()

        return [
            SiteDetails(
                id=site.id,
                name=site.name,
                link=site.link
            )
            for site in sites
        ]

    async def delete(
        self,
        id: int
    ):
        await SiteRepository.delete(id=id)
