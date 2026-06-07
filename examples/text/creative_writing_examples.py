"""Example: Generate creative stories and poetry."""


async def run_examples():
    from backend.llm.llm_factory import LLMFactory
    from backend.generators.text_generators.story_generator import StoryGenerator
    from backend.generators.text_generators.poetry_generator import PoetryGenerator

    factory = LLMFactory()
    story_gen = StoryGenerator(factory)
    poetry_gen = PoetryGenerator(factory)

    story = await story_gen.generate("sci-fi", "A robot discovers emotions")
    print(f"Story: {story[:300]}...\n")

    poem = await poetry_gen.generate("haiku", "nature", "calm", "haiku")
    print(f"Poem:\n{poem}")
