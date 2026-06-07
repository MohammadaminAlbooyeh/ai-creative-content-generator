from pydantic import BaseModel
from typing import Any, Optional
from datetime import datetime


class GenerationResult(BaseModel):
    id: str
    content: Any
    content_type: str
    provider: str
    model: str
    created_at: datetime = datetime.now()
    metadata: Optional[dict] = None
    tokens_used: Optional[int] = None
    latency_ms: Optional[int] = None
