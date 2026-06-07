import httpx
from backend.utils.config import settings


class StabilityAIClient:
    def __init__(self):
        self.api_key = settings.STABILITY_API_KEY
        self.base_url = "https://api.stability.ai/v1"

    async def generate_image(self, prompt: str, style: str = None):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/generation/stable-diffusion-xl-1024-v1-0/text-to-image",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={
                    "text_prompts": [{"text": prompt}],
                    "cfg_scale": 7,
                    "height": 1024,
                    "width": 1024,
                    "samples": 1,
                },
            )
            return response.json()
