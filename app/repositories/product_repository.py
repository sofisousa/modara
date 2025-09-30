from models.models import (
    Product,
    ProductCategory
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
    async def get_all_category(
        cls
    ):
        return await ProductCategory.all()
