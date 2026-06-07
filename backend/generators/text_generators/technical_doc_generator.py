from backend.llm.llm_factory import LLMFactory
from backend.prompts.technical_prompts import TechnicalPrompts


class TechnicalDocGenerator:
    def __init__(self, llm_factory: LLMFactory):
        self.llm = llm_factory.get_llm()
        self.prompts = TechnicalPrompts()

    async def generate(self, topic: str, doc_type: str = "guide", audience: str = "developer", tone: str = "technical"):
        system_prompt = self.prompts.get_technical_doc_system_prompt()
        user_prompt = self.prompts.get_technical_doc_user_prompt(topic, doc_type, audience, tone)
        return await self.llm.generate(system_prompt, user_prompt)
