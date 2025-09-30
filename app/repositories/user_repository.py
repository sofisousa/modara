from models.models import User, UserRole
from schemas.user.create import CreateUser
from schemas.user.update import UpdateUser
from config.auth_hash import get_password_hash


class UserRepository:
    @classmethod
    async def create(
        cls,
        user: CreateUser
    ) -> User:
        return await User.create(name=user.name, email=user.email, password=get_password_hash(password=user.password), role=UserRole.USER.value)

    @classmethod
    async def update(
        cls,
        id: int,
        update_info: UpdateUser
    ):
        update_info = update_info.model_dump(exclude_none=True)

        if not update_info:
            return await User.get_or_none(id=id)

        await User.filter(id=id).update(**update_info)

    @classmethod
    async def delete(
        cls,
        id: int
    ):
        await User.filter(id=id).delete()

    @classmethod
    async def get_one_by_id(
        cls,
        id: int
    ):
        return await User.get_or_none(id=id)

    @classmethod
    async def get_by_email(
        cls,
        email: str
    ):
        return await User.get_or_none(email=email)

    @classmethod
    async def get_all(
        cls
    ):
        return await User.all()
