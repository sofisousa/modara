from datetime import timedelta
from typing import List

from fastapi import APIRouter, HTTPException, status, Security
from tortoise.exceptions import IntegrityError
from fastapi.responses import JSONResponse

from config.config import settings
from config.auth_hash import create_access_token, get_password_hash, verify_password
from models.models import (
    ProductCategory_Pydantic,
    Site_Pydantic,
    User,
    UserRole
)

from utils.get_current_user import get_current_user

from schemas.product.create import CreateProduct
from schemas.product.update import UpdateProduct
from schemas.product.details import ProductDetails
from services.product_service import ProductService
from schemas.generic.message_response import MessageResponse
from utils.http_message import unauthorized_error


router = APIRouter(tags=["Products"], prefix="/products")
product_service = ProductService()

@router.get("", response_model=List[ProductDetails])
async def get_all_products():
    return await product_service.get_all()


@router.get("", response_model=List[ProductCategory_Pydantic])
async def get_all_product_category():
    return await product_service.get_all_category()


@router.get("/{id}", response_model=ProductDetails)
async def get_product_detail(
    id: int,
):
    return await product_service.get_details(id=id)


@router.post("", response_model=ProductDetails)
async def create_product(
    product: CreateProduct,
    current_user: User = Security(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise unauthorized_error()

    return await product_service.create(product=product)


@router.put("/{id}", response_model=ProductDetails)
async def update_product(
    id: int,
    product: UpdateProduct,
    current_user: User = Security(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise unauthorized_error()

    await product_service.update(id=id, update_info=product)

    return product_service.get_details(id=id)


@router.delete("/{id}", response_model=MessageResponse)
async def delete_product(
    id: int,
    current_user: User = Security(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise unauthorized_error()

    await product_service.delete(id=id)

    return MessageResponse(
        message="Produto deletado com sucesso!"
    )


@router.get("/favorites", response_model=List[ProductDetails])
async def get_all_favorite_products(
    current_user: User = Security(get_current_user)
):
    return await product_service.get_all_product_favorites(user_id=current_user.id)


@router.post("/favorites", response_model=MessageResponse)
async def add_favorite_product(
    id: int,
    current_user: User = Security(get_current_user)
):
    await product_service.add_favorite(id=id, user_id=current_user.id)

    return MessageResponse(
        message="Produto favoritado com sucesso!"
    )


@router.delete("/favorites", response_model=MessageResponse)
async def remove_favorite_product(
    id: int,
    current_user: User = Security(get_current_user)
):
    await product_service.remove_favorite(id=id, user_id=current_user.id)

    return MessageResponse(
        message="Produto removido dos favoritos com sucesso!"
    )


@router.get("/site-in", response_model=Site_Pydantic)
async def get_all_sites_of_a_product(
    id: int
):
    return await product_service.get_all_product_site(id=id)


@router.get("/produts-in-site", response_model=List[ProductDetails])
async def get_all_products_of_a_site(
    site_id: int
):
    return await product_service.get_all_site_product(site_id=site_id)


@router.post("/site", response_model=MessageResponse)
async def add_product_site(
    id: int,
    site_id: int,
    current_user: User = Security(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise unauthorized_error()

    await product_service.add_product_site(id=id, site_id=site_id)

    return MessageResponse(
        message="Produto vinculado ao site com sucesso!"
    )


@router.delete("/site", response_model=MessageResponse)
async def remove_product_site(
    id: int,
    site_id: int,
    current_user: User = Security(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise unauthorized_error()

    await product_service.remove_product_site(id=id, site_id=site_id)

    return MessageResponse(
        message="Produto desvinculado ao site com sucesso!"
    )
