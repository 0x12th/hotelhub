from datetime import datetime, timedelta
from typing import Annotated, Any, Optional

from fastapi import Depends, HTTPException, Request, status
from jose import JWTError, jwt

from config import settings
from user.auth import verify_password
from user.repository import UserRepository
from user.schemas import UserCreateSchema, UserSchema


def create_access_token(
    data: dict[str, str | datetime], expires_delta: timedelta | None = None
) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt


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
        user_id: Optional[str] = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError as exc:
        raise credentials_exception from exc
    user = await UserRepository.get_one_or_none(id=int(user_id))
    if user is None:
        raise credentials_exception
    return user
