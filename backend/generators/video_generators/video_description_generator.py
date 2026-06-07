from backend.llm.llm_factory import LLMFactory


class VideoDescriptionGenerator:
    def __init__(self, llm_factory: LLMFactory):
        self.llm = llm_factory.get_llm()

    async def generate(self, title: str, keywords: list[str] = None, include_timestamps: bool = False):
        system_prompt = "You are an expert at writing YouTube video descriptions that rank well."
        keywords_text = ", ".join(keywords) if keywords else ""
        user_prompt = f"Write a compelling YouTube description for '{title}'"
        if keywords_text:
            user_prompt += f" including these keywords: {keywords_text}"
        return await self.llm.generate(system_prompt, user_prompt)
