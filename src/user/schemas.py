import re

from pydantic import BaseModel, EmailStr, field_validator


class Token(BaseModel):
    access_token: str


class TokenData(BaseModel):
    username: str | None = None


class UserSchema(BaseModel):
    first_name: str | None
    last_name: str | None
    email: EmailStr


class UserWithPasswordSchema(UserSchema):
    password: str

    @field_validator("password", mode="after")
    @classmethod
    def valid_password(cls, password: str) -> str:
        if not re.match(
            re.compile(r"^(?=.*[\d])(?=.*[!@#$%^&*])[\w!@#$%^&*]{6,128}$"), password
        ):
            raise ValueError(
                "Password must contain at least "
                "one lower character, "
                "one upper character, "
                "digit or "
                "special symbol"
            )

        return password


class UserCreateSchema(BaseModel):
    id: int  # noqa: A003


class UserLoginSchema(BaseModel):
    email: str
    password: str
