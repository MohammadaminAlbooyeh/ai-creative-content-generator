from backend.llm.openai_llm import OpenAILLM
from backend.llm.claude_llm import ClaudeLLM
from backend.llm.groq_llm import GroqLLM
from backend.llm.cohere_llm import CohereLLM
from backend.llm.local_llm import LocalLLM
from backend.utils.config import settings


class LLMFactory:
    def __init__(self):
        self.providers = {
            "openai": OpenAILLM,
            "claude": ClaudeLLM,
            "groq": GroqLLM,
            "cohere": CohereLLM,
            "local": LocalLLM,
        }
        self.default_provider = settings.DEFAULT_LLM_PROVIDER or "openai"

    def get_llm(self, provider: str = None):
        provider = provider or self.default_provider
        llm_class = self.providers.get(provider)
        if not llm_class:
            raise ValueError(f"Unknown LLM provider: {provider}")
        return llm_class()

    def list_providers(self) -> list[str]:
        return list(self.providers.keys())
