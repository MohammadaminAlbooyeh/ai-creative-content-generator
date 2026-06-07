from backend.generators.text_generators.blog_post_generator import BlogPostGenerator
from backend.generators.image_generators.dall_e_generator import DallEGenerator


class BlogWithImagesGenerator:
    def __init__(self, blog_generator: BlogPostGenerator, image_generator: DallEGenerator):
        self.blog_generator = blog_generator
        self.image_generator = image_generator

    async def generate(self, topic: str, sections: int = 3):
        blog_content = await self.blog_generator.generate(topic)
        images = []
        for i in range(sections):
            image = await self.image_generator.generate(f"Image for section {i + 1} of: {topic}")
            images.append(image)
        return {"content": blog_content, "images": images}
