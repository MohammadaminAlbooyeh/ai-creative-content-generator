import json
from datetime import timedelta


class CacheService:
    def __init__(self):
        self.cache = {}

    async def get(self, key: str):
        return self.cache.get(key)

    async def set(self, key: str, value, ttl: timedelta = timedelta(hours=1)):
        self.cache[key] = value

    async def delete(self, key: str):
        if key in self.cache:
            del self.cache[key]

    async def clear(self):
        self.cache.clear()
