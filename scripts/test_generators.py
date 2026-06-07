"""Test all generators to ensure they work correctly."""


async def main():
    from backend.llm.llm_factory import LLMFactory
    from backend.generators.text_generators.blog_post_generator import BlogPostGenerator
    from backend.generators.text_generators.social_media_generator import SocialMediaGenerator
    from backend.generators.text_generators.email_generator import EmailGenerator

    factory = LLMFactory()

    generators = [
        ("BlogPostGenerator", BlogPostGenerator(factory)),
        ("SocialMediaGenerator", SocialMediaGenerator(factory)),
        ("EmailGenerator", EmailGenerator(factory)),
    ]

    for name, gen in generators:
        try:
            result = await gen.generate("Test topic")
            print(f"✅ {name}: OK")
        except Exception as e:
            print(f"❌ {name}: {e}")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
