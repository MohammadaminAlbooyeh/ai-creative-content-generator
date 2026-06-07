"""Example: Generate a complete social media suite."""


async def run_examples():
    from backend.llm.llm_factory import LLMFactory
    from backend.external_apis.openai_client import OpenAIClient
    from backend.generators.text_generators.social_media_generator import SocialMediaGenerator
    from backend.generators.image_generators.dall_e_generator import DallEGenerator
    from backend.generators.multimodal_generators.social_media_bundle import SocialMediaBundleGenerator

    llm_factory = LLMFactory()
    openai = OpenAIClient()
    social_gen = SocialMediaGenerator(llm_factory)
    image_gen = DallEGenerator(openai)
    bundle_gen = SocialMediaBundleGenerator(social_gen, image_gen)

    result = await bundle_gen.generate("AI Content Creation Tips")
    for platform, content in result.items():
        print(f"{platform}: {content['content'][:100]}...")
