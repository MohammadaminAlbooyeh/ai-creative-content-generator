from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Prompt(BaseModel):
    id: Optional[str] = None
    name: str
    content_type: str
    system_prompt: str
    user_prompt_template: str
    variables: Optional[list[str]] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
