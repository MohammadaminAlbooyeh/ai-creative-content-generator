import cohere
from backend.utils.config import settings


class CohereLLM:
    def __init__(self):
        self.client = cohere.Client(settings.COHERE_API_KEY)
        self.model = "command-r"

    async def generate(self, system_prompt: str, user_prompt: str, temperature: float = 0.7, max_tokens: int = 2048):
        response = self.client.generate(
            model=self.model,
            prompt=f"{system_prompt}\n\n{user_prompt}",
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.generations[0].text
