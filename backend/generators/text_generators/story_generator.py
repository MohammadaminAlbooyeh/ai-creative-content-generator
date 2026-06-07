from backend.llm.llm_factory import LLMFactory
from backend.prompts.creative_prompts import CreativePrompts


class StoryGenerator:
    def __init__(self, llm_factory: LLMFactory):
        self.llm = llm_factory.get_llm()
        self.prompts = CreativePrompts()

    async def generate(self, genre: str, premise: str, tone: str = "neutral", length: str = "short"):
        system_prompt = self.prompts.get_story_system_prompt()
        user_prompt = self.prompts.get_story_user_prompt(genre, premise, tone, length)
        return await self.llm.generate(system_prompt, user_prompt)
