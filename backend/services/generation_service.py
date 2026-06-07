from sqlalchemy.orm import Session
from backend.llm.llm_factory import LLMFactory
from backend.generators.text_generators.blog_post_generator import BlogPostGenerator
from backend.generators.text_generators.social_media_generator import SocialMediaGenerator
from backend.generators.text_generators.email_generator import EmailGenerator
from backend.generators.image_generators.dall_e_generator import DallEGenerator
from backend.generators.voice_generators.text_to_speech import TextToSpeech
from backend.generators.video_generators.video_script_generator import VideoScriptGenerator
from backend.generators.multimodal_generators.blog_with_images import BlogWithImagesGenerator
from backend.generators.multimodal_generators.social_media_bundle import SocialMediaBundleGenerator
from backend.generators.multimodal_generators.presentation_generator import PresentationGenerator
from backend.generators.multimodal_generators.content_suite_generator import ContentSuiteGenerator
from backend.external_apis.openai_client import OpenAIClient
from backend.external_apis.elevenlabs_client import ElevenLabsClient
from backend.external_apis.google_tts_client import GoogleTTSClient
from backend.models.template import Template as TemplateModel
from backend.models.generation_result import GenerationResult
from backend.models.database import SessionLocal


class GenerationService:
    def __init__(self, db: Session = None):
        self.db = db or SessionLocal()
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
        generator = VideoScriptGenerator(self.llm_factory)
        content = await generator.generate(
            topic=request.topic,
            video_type=request.video_type,
            duration=request.duration,
            tone=request.tone,
        )
        return {"content": content, "content_type": "video"}

    async def generate_bundle(self, request):
        if request.bundle_type == "blog_with_images":
            blog_gen = BlogPostGenerator(self.llm_factory)
            img_gen = DallEGenerator(self.openai_client)
            generator = BlogWithImagesGenerator(blog_gen, img_gen)
            result = await generator.generate(topic=request.topic)
        elif request.bundle_type == "social_media_suite":
            social_gen = SocialMediaGenerator(self.llm_factory)
            img_gen = DallEGenerator(self.openai_client)
            generator = SocialMediaBundleGenerator(social_gen, img_gen)
            result = await generator.generate(topic=request.topic)
        elif request.bundle_type == "presentation":
            generator = PresentationGenerator(self.llm_factory)
            result = await generator.generate(topic=request.topic)
        else:
            generator = ContentSuiteGenerator(self.llm_factory)
            result = await generator.generate(topic=request.topic)
        return {"content": result, "content_type": "bundle", "bundle_type": request.bundle_type}

    async def list_templates(self):
        templates = self.db.query(TemplateModel).all()
        return {"templates": [t.to_dict() for t in templates]}

    async def get_templates_by_type(self, template_type: str):
        templates = self.db.query(TemplateModel).filter(
            TemplateModel.template_type == template_type
        ).all()
        return {"type": template_type, "templates": [t.to_dict() for t in templates]}

    async def get_history(self, user_id: str = None):
        query = self.db.query(GenerationResult)
        if user_id:
            query = query.filter(GenerationResult.user_id == user_id)
        results = query.order_by(GenerationResult.created_at.desc()).limit(50).all()
        return {"history": [r.to_dict() for r in results]}

    async def get_content(self, content_id: str):
        result = self.db.query(GenerationResult).filter(
            GenerationResult.id == content_id
        ).first()
        if result:
            return {"id": content_id, "content": result.to_dict()}
        return {"id": content_id, "content": {}}

    def close(self):
        self.db.close()
