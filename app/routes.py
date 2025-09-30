from fastapi import APIRouter
from controllers import (
    auth,
    favorite,
    product,
    user,
    production
)

api_router = APIRouter()

# Inclui todos os routers dos controllers
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(favorite.router, prefix="/favorites", tags=["Favorites"])
api_router.include_router(product.router, prefix="/products", tags=["Products"])
api_router.include_router(user.router, prefix="/users", tags=["Users"])
api_router.include_router(production.router, prefix="/productions", tags=["Productions"])
