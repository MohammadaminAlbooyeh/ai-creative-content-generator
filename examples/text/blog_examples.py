"""Example: Generate various types of blog posts."""


async def run_examples():
    from backend.llm.llm_factory import LLMFactory
    from backend.generators.text_generators.blog_post_generator import BlogPostGenerator

    factory = LLMFactory()
    generator = BlogPostGenerator(factory)

    topics = [
        "The Future of Remote Work",
        "Top 10 Productivity Hacks",
        "How to Start a Podcast",
    ]

    for topic in topics:
        result = await generator.generate(topic, template="listicle")
        print(f"Generated blog post for: {topic}")
        print(result[:200] + "...\n")
