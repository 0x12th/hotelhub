from pydantic import PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DSN: PostgresDsn
    REDIS_DSN: RedisDsn

    class Config:
        env_file = ("prod.env", "dev.env")


settings = Settings()
