from pydantic import BaseModel
from typing import Optional


class GenerationRequest(BaseModel):
    prompt: str
    content_type: str
    template: Optional[str] = None
    tone: Optional[str] = "neutral"
    length: Optional[str] = "medium"
    language: Optional[str] = "en"
