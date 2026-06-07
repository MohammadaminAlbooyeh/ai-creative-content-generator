import httpx
from backend.utils.config import settings


class UnsplashClient:
    def __init__(self):
        self.access_key = settings.UNSPLASH_ACCESS_KEY
        self.base_url = "https://api.unsplash.com"

    async def search(self, query: str, per_page: int = 10):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/search/photos",
                headers={"Authorization": f"Client-ID {self.access_key}"},
                params={"query": query, "per_page": per_page},
            )
            return response.json()
