import redis.asyncio as aioredis

from src.config import settings

redis = aioredis.from_url(str(settings.REDIS_DSN))  # type: ignore
