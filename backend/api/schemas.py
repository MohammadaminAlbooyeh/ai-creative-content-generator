from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime


class GenerateRequest(BaseModel):
    prompt: str
    content_type: str
    template: Optional[str] = None
    tone: Optional[str] = None
    length: Optional[str] = "medium"
    language: Optional[str] = "en"


class GenerateResponse(BaseModel):
    id: str
    content: Any
    content_type: str
    created_at: datetime
    metadata: Optional[dict] = None


class BlogRequest(BaseModel):
    topic: str
    template: str = "listicle"
    tone: str = "professional"
    length: str = "medium"
    target_audience: Optional[str] = None
    keywords: Optional[list[str]] = None
    language: str = "en"


class SocialRequest(BaseModel):
    platform: str
    topic: str
    tone: str = "casual"
    include_hashtags: bool = True
    include_media_suggestions: bool = False
    language: str = "en"


class EmailRequest(BaseModel):
    email_type: str
    subject: str
    recipient_name: Optional[str] = None
    sender_name: Optional[str] = None
    tone: str = "professional"
    key_points: Optional[list[str]] = None
    language: str = "en"


class ImageRequest(BaseModel):
    prompt: str
    style: Optional[str] = None
    size: str = "1024x1024"
    num_images: int = 1
    provider: str = "dall-e"


class VoiceRequest(BaseModel):
    text: str
    voice: str = "default"
    accent: Optional[str] = None
    emotion: Optional[str] = None
    speed: float = 1.0
    language: str = "en"
    provider: str = "elevenlabs"


class VideoRequest(BaseModel):
    topic: str
    video_type: str = "youtube"
    duration: str = "medium"
    tone: str = "engaging"
    target_audience: Optional[str] = None
    language: str = "en"


class BundleRequest(BaseModel):
    bundle_type: str
    topic: str
    include_images: bool = True
    include_voice: bool = False
    tone: str = "professional"
    language: str = "en"
