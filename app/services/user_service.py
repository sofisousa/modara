from typing import List
from repositories.user_repository import UserRepository
from schemas.user.create import CreateUser
from schemas.user.update import UpdateUser
from schemas.user.details import UserDetails
from utils.http_message import (
    not_found_error,
    unauthorized_error,
    bad_request_error
)


class UserService:
    def __init__(
        self
    ):
        pass

    async def create(
        self,
        user: CreateUser
    ):
        exist_user = await UserRepository.get_by_email(email=user.email)

        if exist_user:
            raise bad_request_error(message="Este e-mail já está em uso, tente outro")

        await UserRepository.create(user=user)

    async def update(
        self,
        id: int,
        update_info: UpdateUser
    ):
        user = await UserRepository.get_one_by_id(id=id)

        if not user:
            raise not_found_error(entity="Usuário")

        if update_info.email and user.email != update_info.email:
            exist_email = await UserRepository.get_by_email(email=update_info.email)

            if exist_email:
                raise bad_request_error(message="Este e-mail já está em uso, tente outro")

        await UserRepository.update(id=id, update_info=update_info)

    async def get_details(
        self,
        id: int
    ) -> UserDetails:
        user = await UserRepository.get_one_by_id(id=id)

        return UserDetails(
            id=user.id,
            name=user.name,
            email=user.email
        )

    async def delete(
        self,
        id: int
    ):
        await UserRepository.delete(id=id)


