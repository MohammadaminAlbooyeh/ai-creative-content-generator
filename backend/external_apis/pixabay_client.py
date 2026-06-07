import httpx
from backend.utils.config import settings


class PixabayClient:
    def __init__(self):
        self.api_key = settings.PIXABAY_API_KEY
        self.base_url = "https://pixabay.com/api"

    async def search(self, query: str, per_page: int = 10):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                self.base_url,
                params={"key": self.api_key, "q": query, "per_page": per_page},
            )
            return response.json()
