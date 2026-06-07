from backend.llm.llm_factory import LLMFactory
from backend.prompts.marketing_prompts import MarketingPrompts


class ProductDescriptionGenerator:
    def __init__(self, llm_factory: LLMFactory):
        self.llm = llm_factory.get_llm()
        self.prompts = MarketingPrompts()

    async def generate(self, product_name: str, features: list[str], tone: str = "professional", target_audience: str = "general"):
        system_prompt = "You are an expert e-commerce copywriter."
        user_prompt = self.prompts.get_product_description_prompt(product_name, features, tone, target_audience)
        return await self.llm.generate(system_prompt, user_prompt)
