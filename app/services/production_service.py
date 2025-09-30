from typing import List
from repositories.production_repository import ProductionRepository
from schemas.production.create import CreateProduction
from schemas.production.update import UpdateProduction
from schemas.production.details import ProductionDetails
from utils.http_message import (
    not_found_error,
    unauthorized_error,
    bad_request_error
)


class ProductionService:
    def __init__(self):
        pass

    async def create(
        self,
        production: CreateProduction
    ):
        production = await ProductionRepository.create(production=production)
        production = await ProductionRepository.get_one_by_id(id=production.id)

        return ProductionDetails(
            id=production.id,
            year=production.year,
            title=production.title,
            director=production.director,
            studio=production.studio,
            nationality_id=production.nationality_id,
            nationality_name=production.nationality.name,
            genre_id=production.genre_id,
            genre_name=production.genre.name,
            category_id=production.category_id,
            category_name=production.category.name
        )

    async def update(
        self,
        id: int,
        update_info: UpdateProduction
    ):
        await ProductionRepository.update(id=id, update_info=update_info)

    async def get_details(
        self,
        id: int
    ):
        production = await ProductionRepository.get_one_by_id(id=id)

        if not production:
            raise not_found_error(entity="Produção")

        return ProductionDetails(
            id=production.id,
            year=production.year,
            title=production.title,
            director=production.director,
            studio=production.studio,
            nationality_id=production.nationality_id,
            nationality_name=production.nationality.name,
            genre_id=production.genre_id,
            genre_name=production.genre.name,
            category_id=production.category_id,
            category_name=production.category.name
        )

    async def get_all(
        self
    ):
        productions = await ProductionRepository.get_all()

        return [
            ProductionDetails(
                id=production.id,
                year=production.year,
                title=production.title,
                director=production.director,
                studio=production.studio,
                nationality_id=production.nationality_id,
                nationality_name=production.nationality.name,
                genre_id=production.genre_id,
                genre_name=production.genre.name,
                category_id=production.category_id,
                category_name=production.category.name
            )
            for production in productions
        ]

    async def delete(
        self,
        id: int
    ):
        await ProductionRepository.delete(id=id)

    async def get_all_nationality(
        self
    ):
        return await ProductionRepository.get_all_nationality()

    async def get_all_genre(
        self
    ):
        return await ProductionRepository.get_all_genre()

    async def get_all_category(
        self
    ):
        return await ProductionRepository.get_all_category()
