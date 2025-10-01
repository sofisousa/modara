from typing import List

from fastapi import APIRouter, HTTPException, status, Security
from tortoise.exceptions import IntegrityError
from fastapi.responses import JSONResponse

from models.models import (
    User,
    UserRole
)

from utils.get_current_user import get_current_user

from schemas.site.create import CreateSite
from schemas.site.update import UpdateSite
from schemas.site.details import SiteDetails
from services.site_service import SiteService
from schemas.generic.message_response import MessageResponse
from utils.http_message import unauthorized_error


router = APIRouter(tags=["Sites"], prefix="/sites")
site_service = SiteService()

@router.get("", response_model=List[SiteDetails])
async def get_all_sites():
    return await site_service.get_all()


@router.get("/{id}", response_model=SiteDetails)
async def get_site_detail(
    id: int,
):
    return await site_service.get_details(id=id)


@router.post("", response_model=SiteDetails)
async def create_site(
    site: CreateSite,
    current_user: User = Security(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise unauthorized_error()

    return await site_service.create(site=site)


@router.put("/{id}", response_model=SiteDetails)
async def update_site(
    id: int,
    site: UpdateSite,
    current_user: User = Security(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise unauthorized_error()

    await site_service.update(id=id, update_info=site)

    return site_service.get_details(id=id)


@router.delete("/{id}", response_model=MessageResponse)
async def delete_site(
    id: int,
    current_user: User = Security(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise unauthorized_error()

    await site_service.delete(id=id)

    return MessageResponse(
        message="Site deletado com sucesso!"
    )
