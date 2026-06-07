"""Example: Generate a full marketing campaign."""


async def run_examples():
    from backend.llm.llm_factory import LLMFactory
    from backend.generators.multimodal_generators.content_suite_generator import ContentSuiteGenerator

    factory = LLMFactory()
    generator = ContentSuiteGenerator(factory)

    content_types = ["blog", "social_post", "email", "landing_page"]
    result = await generator.generate("New Product Launch", content_types)
    print("Marketing campaign generated successfully!")
    for ct in content_types:
        print(f"- {ct} content included")
