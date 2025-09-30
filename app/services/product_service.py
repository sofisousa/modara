from typing import List
from models.models import ProductCategory_Pydantic
from repositories.product_repository import ProductRepository
from schemas.product.create import CreateProduct
from schemas.product.update import UpdateProduct
from schemas.product.details import ProductDetails
from utils.http_message import (
    not_found_error,
    unauthorized_error,
    bad_request_error
)


class ProductService:
    def __init__(self):
        pass

    async def create(
        self,
        product: CreateProduct
    ):
        await ProductRepository.create(product=product)

    async def update(
        self,
        id: int,
        update_info: UpdateProduct
    ):
        await ProductRepository.update(id=id, update_info=update_info)

    async def get_details(
        self,
        id: int
    ):
        product = await ProductRepository.get_one_by_id(id=id)

        if not product:
            raise not_found_error(entity="Produto")

        return ProductDetails(
            id=product.id,
            description=product.category_id,
            category_name=product.category.name,
            production_id=product.production_id,
            production_name=product.production.title
        )

    async def get_all(
        self
    ):
        products = await ProductRepository.get_all()

        return [
            ProductDetails(
                id=product.id,
                description=product.category_id,
                category_name=product.category.name,
                production_id=product.production_id,
                production_name=product.production.title
            )
            for product in products
        ]

    async def delete(
        self,
        id: int
    ):
        await ProductRepository.delete(id=id)

    async def get_all_category(
        self
    ):
        return await ProductRepository.get_all_category()
