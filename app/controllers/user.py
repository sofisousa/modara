from datetime import timedelta

from fastapi import APIRouter, HTTPException, status, Security
from tortoise.exceptions import IntegrityError
from fastapi.responses import JSONResponse

from config.config import settings
from config.auth_hash import create_access_token, get_password_hash, verify_password
from models.models import User

from utils.get_current_user import get_current_user

from schemas.user.create import CreateUser
from schemas.user.update import UpdateUser
from schemas.user.details import UserDetails
from services.user_service import UserService
from schemas.generic.message_response import MessageResponse


router = APIRouter(tags=["User"], prefix="/user")
user_service = UserService()

@router.get("", response_model=UserDetails)
async def get_current_user_details(
    current_user: User = Security(get_current_user)
):
    print(current_user, "CURRENT USER")
    return await user_service.get_details(id=current_user.id)


@router.post("", response_model=MessageResponse, status_code=status.HTTP_200_OK)
async def create_user(
    user_info: CreateUser
):
    await user_service.create(user=user_info)
    return MessageResponse(message="Conta criada com sucesso!")


@router.put("", response_model=MessageResponse, status_code=status.HTTP_200_OK)
async def update_current_user(
    user_info: UpdateUser,
    current_user: User = Security(get_current_user)
):
    await user_service.update(id=current_user.id, update_info=user_info)
    return MessageResponse(message="Conta atualizada com sucesso!")


@router.delete("", response_model=MessageResponse, status_code=status.HTTP_200_OK)
async def delete_current_user(
    current_user: User = Security(get_current_user)
):
    await user_service.delete(id=current_user.id)
    return MessageResponse(message="Conta excluída com sucesso!")
