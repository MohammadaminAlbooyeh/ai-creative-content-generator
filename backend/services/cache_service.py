import json
from datetime import timedelta
from typing import Optional
import redis.asyncio as aioredis
from backend.utils.config import settings


class CacheService:
    def __init__(self):
        self._client: Optional[aioredis.Redis] = None
        self._local = {}

    async def _get_client(self) -> aioredis.Redis:
        if self._client is None:
            try:
                self._client = aioredis.from_url(
                    settings.REDIS_URL,
                    decode_responses=True,
                    socket_connect_timeout=2,
                )
                await self._client.ping()
            except Exception:
                self._client = None
        return self._client

    async def get(self, key: str):
        client = await self._get_client()
        if client:
            try:
                value = await client.get(key)
                if value:
                    return json.loads(value)
            except Exception:
                pass
        return self._local.get(key)

    async def set(self, key: str, value, ttl: timedelta = timedelta(hours=1)):
        client = await self._get_client()
        if client:
            try:
                await client.setex(key, int(ttl.total_seconds()), json.dumps(value))
                return
            except Exception:
                pass
        self._local[key] = value

    async def delete(self, key: str):
        client = await self._get_client()
        if client:
            try:
                await client.delete(key)
                return
            except Exception:
                pass
        self._local.pop(key, None)

    async def clear(self):
        client = await self._get_client()
        if client:
            try:
                await client.flushdb()
                return
            except Exception:
                pass
        self._local.clear()
