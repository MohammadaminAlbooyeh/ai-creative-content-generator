from backend.llm.llm_factory import LLMFactory
from backend.prompts.social_prompts import SocialPrompts


class SocialMediaGenerator:
    def __init__(self, llm_factory: LLMFactory):
        self.llm = llm_factory.get_llm()
        self.prompts = SocialPrompts()

    async def generate(self, platform: str, topic: str, tone: str = "casual", include_hashtags: bool = True):
        system_prompt = self.prompts.get_system_prompt(platform)
        user_prompt = self.prompts.get_user_prompt(platform, topic, tone, include_hashtags)
        return await self.llm.generate(system_prompt, user_prompt)
