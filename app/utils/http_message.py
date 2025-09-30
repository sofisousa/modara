from fastapi import HTTPException, status
from fastapi.responses import JSONResponse


def not_found_error(entity: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{entity} não encontrado(a)!"
    )


def unauthorized_error() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=f"Você não tem permissão para essa ação!"
    )


def bad_request_error(message: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=message
    )
