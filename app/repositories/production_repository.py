from models.models import (
    Production,
    Nationality,
    Genre,
    ProductionCategory
)
from schemas.production.create import CreateProduction
from schemas.production.update import UpdateProduction


class ProductionRepository:
    @classmethod
    async def create(
        cls,
        production: CreateProduction
    ) -> Production:
        return await Production.create(year=production.year, title=production.title, director=production.director, studio=production.studio, nationality_id=production.nationality_id, genre_id=production.genre_id, category_id=production.category_id)

    @classmethod
    async def update(
        cls,
        id: int,
        update_info: UpdateProduction
    ):
        update_info = update_info.model_dump(exclude_none=True)

        if not update_info:
            return await Production.get_or_none(id=id)

        await Production.filter(id=id).update(**update_info)

    @classmethod
    async def delete(
        cls,
        id: int
    ):
        await Production.filter(id=id).delete()

    @classmethod
    async def get_one_by_id(
        cls,
        id: int
    ):
        return await Production.get_or_none(id=id).prefetch_related("nationality", "genre", "category")

    @classmethod
    async def get_all(
        cls
    ):
        return await Production.all().prefetch_related("nationality", "genre", "category")

    @classmethod
    async def get_all_nationality(
        cls
    ):
        return await Nationality.all()

    @classmethod
    async def get_all_genre(
        cls
    ):
        return await Genre.all()

    @classmethod
    async def get_all_category(
        cls
    ):
        return await ProductionCategory.all()
