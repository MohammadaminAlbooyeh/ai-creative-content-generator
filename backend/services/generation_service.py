from backend.llm.llm_factory import LLMFactory
from backend.generators.text_generators.blog_post_generator import BlogPostGenerator
from backend.generators.text_generators.social_media_generator import SocialMediaGenerator
from backend.generators.text_generators.email_generator import EmailGenerator
from backend.generators.image_generators.dall_e_generator import DallEGenerator
from backend.generators.voice_generators.text_to_speech import TextToSpeech
from backend.external_apis.openai_client import OpenAIClient
from backend.external_apis.elevenlabs_client import ElevenLabsClient
from backend.external_apis.google_tts_client import GoogleTTSClient


class GenerationService:
    def __init__(self):
        self.llm_factory = LLMFactory()
        self.openai_client = OpenAIClient()
        self.elevenlabs = ElevenLabsClient()
        self.google_tts = GoogleTTSClient()

    async def generate(self, request):
        return {"status": "success", "message": "Generation endpoint"}

    async def generate_blog(self, request):
        generator = BlogPostGenerator(self.llm_factory)
        content = await generator.generate(
            topic=request.topic,
            template=request.template,
            tone=request.tone,
            length=request.length,
        )
        return {"content": content, "content_type": "blog"}

    async def generate_social(self, request):
        generator = SocialMediaGenerator(self.llm_factory)
        content = await generator.generate(
            platform=request.platform,
            topic=request.topic,
            tone=request.tone,
            include_hashtags=request.include_hashtags,
        )
        return {"content": content, "content_type": "social", "platform": request.platform}

    async def generate_email(self, request):
        generator = EmailGenerator(self.llm_factory)
        content = await generator.generate(
            email_type=request.email_type,
            subject=request.subject,
            tone=request.tone,
            key_points=request.key_points,
        )
        return {"content": content, "content_type": "email"}

    async def generate_image(self, request):
        generator = DallEGenerator(self.openai_client)
        images = await generator.generate(
            prompt=request.prompt,
            size=request.size,
            num_images=request.num_images,
            style=request.style,
        )
        return {"images": images, "content_type": "image"}

    async def generate_voice(self, request):
        tts = TextToSpeech(self.elevenlabs, self.google_tts)
        audio = await tts.synthesize(
            text=request.text,
            voice=request.voice,
            provider=request.provider,
            speed=request.speed,
        )
        return {"audio": audio, "content_type": "voice"}

    async def generate_video(self, request):
        return {"status": "success", "content_type": "video"}

    async def generate_bundle(self, request):
        return {"status": "success", "content_type": "bundle"}

    async def list_templates(self):
        return {"templates": ["blog", "social", "email", "video"]}

    async def get_templates_by_type(self, template_type: str):
        return {"type": template_type, "templates": []}

    async def get_history(self):
        return {"history": []}

    async def get_content(self, content_id: str):
        return {"id": content_id, "content": {}}
