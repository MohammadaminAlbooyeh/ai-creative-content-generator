from backend.llm.llm_factory import LLMFactory


class ContentSuiteGenerator:
    def __init__(self, llm_factory: LLMFactory):
        self.llm = llm_factory.get_llm()

    async def generate(self, topic: str, content_types: list[str] = None):
        if content_types is None:
            content_types = ["blog", "social_post", "email", "description"]
        system_prompt = "You are an all-in-one content creator."
        user_prompt = f"Generate a complete content suite for '{topic}' including: {', '.join(content_types)}"
        return await self.llm.generate(system_prompt, user_prompt)
