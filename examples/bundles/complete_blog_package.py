"""Example: Generate a complete blog package with images."""


async def run_examples():
    from backend.llm.llm_factory import LLMFactory
    from backend.external_apis.openai_client import OpenAIClient
    from backend.generators.text_generators.blog_post_generator import BlogPostGenerator
    from backend.generators.image_generators.dall_e_generator import DallEGenerator
    from backend.generators.multimodal_generators.blog_with_images import BlogWithImagesGenerator

    llm_factory = LLMFactory()
    openai = OpenAIClient()
    blog_gen = BlogPostGenerator(llm_factory)
    image_gen = DallEGenerator(openai)
    bundle_gen = BlogWithImagesGenerator(blog_gen, image_gen)

    result = await bundle_gen.generate("The Future of AI in Education", sections=3)
    print(f"Blog: {result['content'][:200]}...")
    print(f"Images: {len(result['images'])} generated")
