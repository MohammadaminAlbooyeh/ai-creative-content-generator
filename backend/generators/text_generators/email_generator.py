from backend.llm.llm_factory import LLMFactory
from backend.prompts.email_prompts import EmailPrompts


class EmailGenerator:
    def __init__(self, llm_factory: LLMFactory):
        self.llm = llm_factory.get_llm()
        self.prompts = EmailPrompts()

    async def generate(self, email_type: str, subject: str, tone: str = "professional", key_points: list[str] = None):
        system_prompt = self.prompts.get_system_prompt(email_type)
        user_prompt = self.prompts.get_user_prompt(email_type, subject, tone, key_points)
        return await self.llm.generate(system_prompt, user_prompt)
