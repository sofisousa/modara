from datetime import timedelta

from schemas.auth.login import Login
from schemas.auth.access_data import Token
from repositories.user_repository import UserRepository
from config.auth_hash import (
    verify_password,
    create_access_token
)
from config.config import settings
from utils.http_message import bad_request_error


class AuthService:
    async def login(
        self,
        login_info: Login
    ):
        user = await UserRepository.get_by_email(email=login_info.email)

        if not user:
            raise bad_request_error(message="Email ou senha incorretos!")

        pass_validation = verify_password(plain_password=login_info.password, hashed_password=user.password)

        if not pass_validation:
            raise bad_request_error(message="Email ou senha incorretos!")

        return Token(
            access_token=create_access_token(data={"sub": user.email}, expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)),
            token_type="bearer"
        )
