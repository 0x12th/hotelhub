import redis.asyncio as aioredis
from config import settings

redis = aioredis.from_url(str(settings.REDIS_DSN))  # type: ignore
