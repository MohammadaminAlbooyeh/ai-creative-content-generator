from backend.llm.llm_factory import LLMFactory
from backend.prompts.marketing_prompts import MarketingPrompts


class MarketingCopyGenerator:
    def __init__(self, llm_factory: LLMFactory):
        self.llm = llm_factory.get_llm()
        self.prompts = MarketingPrompts()

    async def generate(self, product: str, channel: str, tone: str = "persuasive", audience: str = "general"):
        system_prompt = "You are an expert marketing copywriter."
        user_prompt = self.prompts.get_marketing_copy_prompt(product, channel, tone, audience)
        return await self.llm.generate(system_prompt, user_prompt)
