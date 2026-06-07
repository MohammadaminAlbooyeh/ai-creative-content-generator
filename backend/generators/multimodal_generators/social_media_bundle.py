from backend.generators.text_generators.social_media_generator import SocialMediaGenerator
from backend.generators.image_generators.dall_e_generator import DallEGenerator


class SocialMediaBundleGenerator:
    def __init__(self, social_generator: SocialMediaGenerator, image_generator: DallEGenerator):
        self.social_generator = social_generator
        self.image_generator = image_generator

    async def generate(self, topic: str, platforms: list[str] = None):
        if platforms is None:
            platforms = ["instagram", "twitter", "linkedin", "facebook"]
        posts = {}
        for platform in platforms:
            content = await self.social_generator.generate(platform, topic)
            image = await self.image_generator.generate(f"Social media image for {platform}: {topic}")
            posts[platform] = {"content": content, "image": image}
        return posts
