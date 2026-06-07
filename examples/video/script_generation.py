"""Example: Generate video scripts."""


async def run_examples():
    from backend.llm.llm_factory import LLMFactory
    from backend.generators.video_generators.video_script_generator import VideoScriptGenerator

    factory = LLMFactory()
    generator = VideoScriptGenerator(factory)

    result = await generator.generate("How to use AI for content creation", video_type="youtube")
    print(result)
