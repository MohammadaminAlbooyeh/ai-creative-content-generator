from backend.llm.llm_factory import LLMFactory
from backend.prompts.creative_prompts import CreativePrompts


class VideoScriptGenerator:
    def __init__(self, llm_factory: LLMFactory):
        self.llm = llm_factory.get_llm()
        self.prompts = CreativePrompts()

    async def generate(self, topic: str, video_type: str = "youtube", duration: str = "medium", tone: str = "engaging"):
        system_prompt = "You are an expert video script writer."
        user_prompt = f"Write a {duration} {video_type} video script about {topic} in a {tone} tone."
        return await self.llm.generate(system_prompt, user_prompt)
