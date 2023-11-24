from datetime import UTC, datetime, timedelta
from typing import Annotated, Any

from fastapi import Depends, HTTPException, Request, status
from jose import JWTError, jwt

from src.config import settings
from src.user.auth import verify_password
from src.user.repository import UserRepository
from src.user.schemas import UserCreateSchema, UserSchema


def create_access_token(
    data: dict[str, str | datetime], expires_delta: timedelta | None = None
) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(tz=UTC) + expires_delta
    else:
        expire = datetime.now(tz=UTC) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)


def get_access_token(request: Request) -> str:
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="no Token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token


async def authenticate_user(email: str, password: str) -> Any | UserCreateSchema:
    user = await UserRepository.get_one_or_none(email=email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


async def get_current_user(
    token: Annotated[str, Depends(get_access_token)]
) -> Any | UserSchema:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        user_id: str | None = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError as exc:
        raise credentials_exception from exc
    user = await UserRepository.get_one_or_none(id=int(user_id))
    if user is None:
        raise credentials_exception
    return user
