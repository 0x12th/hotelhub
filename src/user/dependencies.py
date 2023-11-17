from typing import Annotated, Any, Optional

from fastapi import Depends, HTTPException, Request, status
from jose import JWTError, jwt

from config import settings
from user.repository import UserRepository
from user.schemas import UserSchema


def get_token(request: Request) -> str:
    token = request.cookies.get("booking_access_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="no Token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token


async def get_current_user(
    token: Annotated[str, Depends(get_token)]
) -> Any | UserSchema:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        user_id: Optional[str] = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError as exc:
        raise credentials_exception from exc
    user = await UserRepository.get_one_or_none(id=id(user_id))
    if user is None:
        raise credentials_exception
    return user
