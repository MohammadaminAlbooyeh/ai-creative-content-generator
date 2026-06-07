from backend.llm.llm_factory import LLMFactory
from backend.prompts.technical_prompts import TechnicalPrompts


class ScriptGenerator:
    def __init__(self, llm_factory: LLMFactory):
        self.llm = llm_factory.get_llm()
        self.prompts = TechnicalPrompts()

    async def generate(self, topic: str, format: str = "video", duration: str = "medium", tone: str = "engaging"):
        system_prompt = self.prompts.get_script_system_prompt()
        user_prompt = self.prompts.get_script_user_prompt(topic, format, duration, tone)
        return await self.llm.generate(system_prompt, user_prompt)
