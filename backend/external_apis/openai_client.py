from openai import AsyncOpenAI
from backend.utils.config import settings


class OpenAIClient:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

    async def generate_text(self, prompt: str, model: str = "gpt-4", temperature: float = 0.7, max_tokens: int = 2048):
        response = await self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content

    async def generate_image(self, prompt: str, size: str = "1024x1024", num_images: int = 1, style: str = None):
        kwargs = {
            "model": "dall-e-3",
            "prompt": prompt,
            "size": size,
            "n": num_images,
        }
        if style:
            kwargs["style"] = style
        response = await self.client.images.generate(**kwargs)
        return [img.url for img in response.data]
