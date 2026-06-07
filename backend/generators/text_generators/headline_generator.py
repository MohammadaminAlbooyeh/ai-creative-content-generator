from backend.llm.llm_factory import LLMFactory
from backend.prompts.marketing_prompts import MarketingPrompts


class HeadlineGenerator:
    def __init__(self, llm_factory: LLMFactory):
        self.llm = llm_factory.get_llm()
        self.prompts = MarketingPrompts()

    async def generate(self, topic: str, style: str = "clickworthy", count: int = 5):
        system_prompt = "You are an expert copywriter specializing in headlines."
        user_prompt = self.prompts.get_headline_prompt(topic, style, count)
        return await self.llm.generate(system_prompt, user_prompt)
