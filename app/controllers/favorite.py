# controllers/favorites.py
from typing import List
from fastapi import APIRouter, HTTPException, status, Security
from tortoise.exceptions import IntegrityError
# from models.favorite import Favorite
# from models.user import User
# from models.product import Product

from utils.get_current_user import get_current_user

router = APIRouter(prefix="/favorites", tags=["Favorites"])

@router.get("/{nome}")
async def get_welcome(
    name: str
):
    return f"Hello {name}!"

# @router.get("", response_model=List[FavoriteData])
# async def get_all_my_favorites(
#     user: User = Security(get_current_user)
# ):
#     favorites = await Favorite.filter(user=user).prefetch_related("product__production", "user")
#     return favorites

# @router.post("", response_model=FavoriteData, status_code=status.HTTP_201_CREATED)
# async def create_favorite(
#     favorite_data: FavoriteCreate,
#     user: User = Security(get_current_user)
# ):
#     product = await Product.get_or_none(id=favorite_data.product_id)

#     if not product:
#         raise HTTPException(status_code=400, detail="Produto não encontrado.")

#     try:
#         favorite = await Favorite.create(user=user, product=product)
#         await favorite.fetch_related("user", "product__production")
#         return favorite
#     except IntegrityError:
#         raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Produto já favoritado!")

# @router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_favorite(
#     product_id: int,
#     user: User = Security(get_current_user)
# ):
#     favorite = await Favorite.get_or_none(product_id=product_id, user=user)
#     if not favorite:
#         raise HTTPException(status_code=404, detail="Favorito não encontrado!")

#     await favorite.delete()
#     return {"message": "Favorito excluído com sucesso!"}