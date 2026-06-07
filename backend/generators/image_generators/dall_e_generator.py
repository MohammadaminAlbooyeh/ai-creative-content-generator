from backend.external_apis.openai_client import OpenAIClient


class DallEGenerator:
    def __init__(self, openai_client: OpenAIClient):
        self.client = openai_client

    async def generate(self, prompt: str, size: str = "1024x1024", num_images: int = 1, style: str = None):
        return await self.client.generate_image(prompt, size, num_images, style)
