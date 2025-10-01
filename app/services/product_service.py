from typing import List
from models.models import ProductCategory_Pydantic
from repositories.product_repository import ProductRepository
from repositories.site_repository import SiteRepository
from schemas.product.create import CreateProduct
from schemas.product.update import UpdateProduct
from schemas.product.details import ProductDetails
from schemas.site.details import SiteDetails
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

    async def get_all_product_favorites(
        self,
        user_id: int
    ):
        favorite_products = await ProductRepository.get_all_favorite(user_id=user_id)
        id_list = [product.id for product in favorite_products]

        filtered_products = await ProductRepository.get_all_product_by_id_list(id_list=id_list)

        return [
            ProductDetails(
                id=product.id,
                description=product.category_id,
                category_name=product.category.name,
                production_id=product.production_id,
                production_name=product.production.title
            )
            for product in filtered_products
        ]

    async def add_favorite(
        self,
        id: int,
        user_id: int
    ):
        product = await ProductRepository.get_one_by_id(id=id)

        if not product:
            raise not_found_error(entity="Produto")

        await ProductRepository.add_favorite(id=id, user_id=user_id)

    async def remove_favorite(
        self,
        id: int,
        user_id: int
    ):
        favorite = ProductRepository.get_favorite(id=id, user_id=user_id)

        if not favorite:
            return

        await ProductRepository.remove_favorite(id=id, user_id=user_id)

    async def get_all_product_site( # função que pega os sites em que um produto está
        self,
        id: int
    ):
        sites = await ProductRepository.get_all_product_by_id(id=id)

        id_list = [site.id for site in sites]

        return await SiteRepository.get_all_site_by_id_list(id_list=id_list)



    async def get_all_site_product( # função que pega os produtos de determinado site
        self,
        site_id: int
    ):
        products = await ProductRepository.get_all_product_by_site(site_id=site_id)

        id_list = [product.id for product in products]

        filtered_products = await ProductRepository.get_all_product_by_id_list(id_list=id_list)

        return [
            ProductDetails(
                id=product.id,
                description=product.category_id,
                category_name=product.category.name,
                production_id=product.production_id,
                production_name=product.production.title
            )
            for product in filtered_products
        ]
