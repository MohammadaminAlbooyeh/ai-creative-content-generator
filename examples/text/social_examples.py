"""Example: Generate social media posts for different platforms."""


async def run_examples():
    from backend.llm.llm_factory import LLMFactory
    from backend.generators.text_generators.social_media_generator import SocialMediaGenerator

    factory = LLMFactory()
    generator = SocialMediaGenerator(factory)

    platforms = ["instagram", "twitter", "linkedin", "facebook"]
    for platform in platforms:
        result = await generator.generate(platform, "AI in everyday life")
        print(f"{platform}: {result[:150]}...\n")
