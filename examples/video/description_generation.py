"""Example: Generate video descriptions."""


async def run_examples():
    from backend.llm.llm_factory import LLMFactory
    from backend.generators.video_generators.video_description_generator import VideoDescriptionGenerator

    factory = LLMFactory()
    generator = VideoDescriptionGenerator(factory)

    result = await generator.generate("Complete Guide to AI Content Generation")
    print(result)
