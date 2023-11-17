from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, status

from user.auth import get_password_hash
from user.dependencies import get_current_user
from user.repository import UserRepository
from user.schemas import UserCreateSchema, UserSchema, UserWithPasswordSchema

user_router = APIRouter(tags=["User"])


@user_router.post(
    "/users/", status_code=status.HTTP_201_CREATED, response_model=UserCreateSchema
)
async def register_user(user: UserWithPasswordSchema) -> Any:
    existing_user = await UserRepository.get_one_or_none(email=user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    new_user = await UserRepository.add(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=hashed_password,
    )
    return new_user


@user_router.get("/users/me", response_model=UserSchema)
async def read_users_me(
    current_user: Annotated[UserSchema, Depends(get_current_user)]
) -> Any:
    return current_user
