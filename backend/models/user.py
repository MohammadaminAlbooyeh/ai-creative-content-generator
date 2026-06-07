from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):
    id: Optional[str] = None
    username: str
    email: str
    api_keys: Optional[dict] = None
    preferences: Optional[dict] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
