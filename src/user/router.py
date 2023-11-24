from datetime import timedelta
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, Response, status

from src.config import settings
from src.user.auth import get_password_hash
from src.user.dependencies import (
    authenticate_user,
    create_access_token,
    get_current_user,
)
from src.user.repository import UserRepository
from src.user.schemas import (
    Token,
    UserCreateSchema,
    UserLoginSchema,
    UserSchema,
    UserWithPasswordSchema,
)

user_router = APIRouter(tags=["User"])


@user_router.post("/token", response_model=Token)
async def login_for_access_token(
    response: Response, form_data: Annotated[UserLoginSchema, Depends()]
) -> Any:
    user = await authenticate_user(form_data.email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    response.set_cookie(key="access_token", value=access_token, httponly=True)
    return {"access_token": access_token}


@user_router.post(
    "/users/", status_code=status.HTTP_201_CREATED, response_model=UserCreateSchema
)
async def register_user(user: UserWithPasswordSchema) -> Any:
    existing_user = await UserRepository.get_one_or_none(email=user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    return await UserRepository.add(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=hashed_password,
    )


@user_router.get("/users/me", response_model=UserSchema)
async def read_users_me(
    current_user: Annotated[UserSchema, Depends(get_current_user)]
) -> Any:
    return current_user
