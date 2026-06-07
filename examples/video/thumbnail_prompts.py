"""Example: Generate thumbnail prompts for videos."""


async def run_examples():
    from backend.llm.llm_factory import LLMFactory
    from backend.generators.video_generators.thumbnail_generator import ThumbnailGenerator

    factory = LLMFactory()
    generator = ThumbnailGenerator(factory)

    prompt = await generator.generate_prompt("10 AI Tools You Must Try in 2024")
    print(f"Thumbnail prompt: {prompt}")
