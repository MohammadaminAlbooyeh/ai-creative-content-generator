from backend.llm.llm_factory import LLMFactory


class ThumbnailGenerator:
    def __init__(self, llm_factory: LLMFactory):
        self.llm = llm_factory.get_llm()

    async def generate_prompt(self, video_title: str, style: str = "eye-catching"):
        system_prompt = "You are an expert at creating YouTube thumbnail prompts for DALL-E."
        user_prompt = f"Create a detailed image generation prompt for a {style} thumbnail for a video titled: '{video_title}'"
        return await self.llm.generate(system_prompt, user_prompt)
