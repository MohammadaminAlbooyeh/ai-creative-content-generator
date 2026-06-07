import httpx
from backend.utils.config import settings


class LocalLLM:
    def __init__(self):
        self.base_url = settings.LOCAL_LLM_URL or "http://localhost:11434"
        self.model = settings.LOCAL_LLM_MODEL or "llama2"

    async def generate(self, system_prompt: str, user_prompt: str, temperature: float = 0.7, max_tokens: int = 2048):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": f"{system_prompt}\n\n{user_prompt}",
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                },
            )
            return response.json().get("response", "")
