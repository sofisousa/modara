from datetime import timedelta
from typing import List

from fastapi import APIRouter, HTTPException, status, Security
from tortoise.exceptions import IntegrityError
from fastapi.responses import JSONResponse

from config.config import settings
from config.auth_hash import create_access_token, get_password_hash, verify_password
from models.models import (
    User,
    UserRole,
    Nationality,
    Nationality_Pydantic,
    Genre_Pydantic,
    ProductionCategory_Pydantic,
    Genre,
    ProductionCategory
)

from utils.get_current_user import get_current_user

from schemas.production.create import CreateProduction
from schemas.production.update import UpdateProduction
from schemas.production.details import ProductionDetails
from services.production_service import ProductionService
from schemas.generic.message_response import MessageResponse
from utils.http_message import unauthorized_error


router = APIRouter(tags=["Productions"], prefix="/products")
production_service = ProductionService()

@router.get("", response_model=List[ProductionDetails])
async def get_all_productions():
    return await production_service.get_all()


@router.get("/nationality", response_model=List[Nationality_Pydantic])
async def get_all_nationality():
    return await production_service.get_all_nationality()


@router.get("/genre", response_model=List[Genre_Pydantic])
async def get_all_genre():
    return await production_service.get_all_genre()


@router.get("/category", response_model=List[ProductionCategory_Pydantic])
async def get_all_production_category():
    return await production_service.get_all_category()


@router.get("/{id}", response_model=ProductionDetails)
async def get_product_detail(
    id: int,
):
    return await production_service.get_details(id=id)


@router.post("", response_model=ProductionDetails)
async def create_product(
    production: CreateProduction,
    current_user: User = Security(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise unauthorized_error()

    return await production_service.create(production=production)


@router.put("/{id}", response_model=ProductionDetails)
async def update_product(
    id: int,
    product: UpdateProduction,
    current_user: User = Security(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise unauthorized_error()

    await production_service.update(id=id, update_info=product)

    return await production_service.get_details(id=id)


@router.delete("/{id}", response_model=MessageResponse)
async def delete_product(
    id: int,
    current_user: User = Security(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise unauthorized_error()

    await production_service.delete(id=id)

    return MessageResponse(
        message="Produção deletado com sucesso!"
    )
