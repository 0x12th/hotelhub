from pydantic import PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DSN: PostgresDsn
    DB_ECHO: bool = False
    REDIS_DSN: RedisDsn
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ("prod.env", "dev.env")


settings = Settings()
