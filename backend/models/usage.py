from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Usage(BaseModel):
    id: Optional[str] = None
    user_id: str
    content_type: str
    provider: str
    tokens: int
    cost: float
    created_at: datetime = datetime.now()
