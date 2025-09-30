from datetime import timedelta
from fastapi import APIRouter

from services.auth_service import AuthService
from schemas.auth.access_data import Token
from schemas.auth.login import Login


router = APIRouter(tags=["Authentication"], prefix="/auth")
auth_service = AuthService()

@router.get("/{nome}")
async def get_welcome(
    name: str
):
    return f"Hello {name}!"

# @router.post("/register", response_model=UserBase, status_code=status.HTTP_201_CREATED)
# async def create_user(
#     user: UserCreate
# ):
#     hashed_password = get_password_hash(user.password)
#     try:
#         await User.create(
#             name=user.name, email=user.email, password=hashed_password
#         )
#         return UserBase(
#             name=user.name,
#             email=user.email
#         )

#     except IntegrityError:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Email already registered",
#         )

@router.post("/login", response_model=Token)
async def login(
    data: Login
):
    return await auth_service.login(login_info=data)
# @router.post("/login", response_model=Token)
# async def login(
#     dto: LoginDto
# ):
#     user = await User.get_or_none(email=dto.email)

#     if not user:
#         raise HTTPException(status_code=400, detail="Email ou senha incorretos!")

#     pass_validation = verify_password(dto.password, user.password)

#     if not user or not pass_validation:
#         raise HTTPException(status_code=400, detail="Email ou senha incorretos!")

#     access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.email}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}

