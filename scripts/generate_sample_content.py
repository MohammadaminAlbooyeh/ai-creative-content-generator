"""Generate sample content for demonstration purposes."""


async def main():
    from backend.llm.llm_factory import LLMFactory
    from backend.generators.text_generators.blog_post_generator import BlogPostGenerator

    factory = LLMFactory()
    generator = BlogPostGenerator(factory)

    samples = [
        "The Future of Artificial Intelligence",
        "Top 10 Productivity Tips for Developers",
        "How to Start a Successful Blog",
    ]

    for topic in samples:
        result = await generator.generate(topic, template="listicle")
        print(f"\n{'='*50}")
        print(f"Topic: {topic}")
        print(f"{'='*50}")
        print(result[:500])


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
