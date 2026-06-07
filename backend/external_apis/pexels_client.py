import httpx
from backend.utils.config import settings


class PexelsClient:
    def __init__(self):
        self.api_key = settings.PEXELS_API_KEY
        self.base_url = "https://api.pexels.com/v1"

    async def search(self, query: str, per_page: int = 10):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/search",
                headers={"Authorization": self.api_key},
                params={"query": query, "per_page": per_page},
            )
            return response.json()
