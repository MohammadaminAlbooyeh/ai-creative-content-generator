from backend.llm.llm_factory import LLMFactory
from backend.prompts.blog_prompts import BlogPrompts


class BlogPostGenerator:
    def __init__(self, llm_factory: LLMFactory):
        self.llm = llm_factory.get_llm()
        self.prompts = BlogPrompts()

    async def generate(self, topic: str, template: str = "listicle", tone: str = "professional", length: str = "medium"):
        system_prompt = self.prompts.get_system_prompt(template)
        user_prompt = self.prompts.get_user_prompt(topic, template, tone, length)
        return await self.llm.generate(system_prompt, user_prompt)
