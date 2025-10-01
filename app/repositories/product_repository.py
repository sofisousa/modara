from typing import List
from models.models import (
    Product,
    ProductCategory,
    Favorite,
    ProductSite
)
from schemas.product.create import CreateProduct
from schemas.product.update import UpdateProduct


class ProductRepository:
    @classmethod
    async def create(
        cls,
        product: CreateProduct
    ) -> Product:
        return await Product.create(description=product.description, category_id=product.category_id, production_id=product.production_id)

    @classmethod
    async def update(
        cls,
        id: int,
        update_info: UpdateProduct
    ):
        update_info = update_info.model_dump(exclude_none=True)

        if not update_info:
            return await Product.get_or_none(id=id)

        await Product.filter(id=id).update(**update_info)

    @classmethod
    async def delete(
        cls,
        id: int
    ):
        await Product.filter(id=id).delete()

    @classmethod
    async def get_one_by_id(
        cls,
        id: int
    ):
        return await Product.get_or_none(id=id).prefetch_related("category", "production", "favorite")

    @classmethod
    async def get_all(
        cls
    ):
        return await Product.all().prefetch_related("category", "production", "favorite")

    @classmethod
    async def get_all_product_by_id_list(
        cls,
        id_list: List[int]
    ):
        return await Product.filter(id__in=id_list).prefetch_related("category", "production", "favorite")

    @classmethod
    async def get_all_category(
        cls
    ):
        return await ProductCategory.all()

    @classmethod
    async def get_all_favorite(
        cls,
        user_id: int
    ):
        return await Favorite.filter(user_id=user_id).prefetch_related("user", "product")

    @classmethod
    async def get_favorite(
        cls,
        id: int,
        user_id: int
    ):
        return Favorite.filter(product_id=id, user_id=user_id)

    @classmethod
    async def add_favorite(
        cls,
        id: int,
        user_id: int
    ):
        await Favorite.create(product_id=id, user_id=user_id)

    @classmethod
    async def remove_favorite(
        cls,
        id: int,
        user_id: int
    ):
        await Favorite.filter(product_id=id, user_id=user_id).delete()

    @classmethod
    async def get_all_product_by_site(
        cls,
        site_id: int
    ):
        return await ProductSite.filter(site_id=site_id).prefetch_related("product", "site", "product__production", "product__category")

    @classmethod
    async def get_all_product_by_id(
        cls,
        id: int
    ):
        return await ProductSite.filter(product_id=id).prefetch_related("product", "site", "product__production", "product__category")

    @classmethod
    async def add_product_site(
        cls,
        id: int,
        site_id: int
    ):
        await ProductSite.create(product_id=id, site_id=site_id)

    @classmethod
    async def remove_product_site(
        cls,
        id: int,
        site_id: int
    ):
        await ProductSite.filter(product_id=id, site_id=site_id).delete()
