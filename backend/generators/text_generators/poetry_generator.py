from backend.llm.llm_factory import LLMFactory
from backend.prompts.creative_prompts import CreativePrompts


class PoetryGenerator:
    def __init__(self, llm_factory: LLMFactory):
        self.llm = llm_factory.get_llm()
        self.prompts = CreativePrompts()

    async def generate(self, style: str, theme: str, tone: str = "romantic", structure: str = "free_verse"):
        system_prompt = self.prompts.get_poetry_system_prompt()
        user_prompt = self.prompts.get_poetry_user_prompt(style, theme, tone, structure)
        return await self.llm.generate(system_prompt, user_prompt)
