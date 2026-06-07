from backend.llm.llm_factory import LLMFactory


class PresentationGenerator:
    def __init__(self, llm_factory: LLMFactory):
        self.llm = llm_factory.get_llm()

    async def generate(self, topic: str, slides: int = 10, tone: str = "professional"):
        system_prompt = "You are an expert presentation creator."
        user_prompt = f"Create a {slides}-slide presentation outline about '{topic}' in a {tone} tone. Include title, key points, and speaker notes for each slide."
        return await self.llm.generate(system_prompt, user_prompt)
