from datetime import datetime
from pydantic import BaseModel
from typing import Any, Optional


class Content(BaseModel):
    id: Optional[str] = None
    title: str
    content_type: str
    body: Any
    metadata: Optional[dict] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    user_id: Optional[str] = None
