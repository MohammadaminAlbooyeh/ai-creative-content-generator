from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Template(BaseModel):
    id: Optional[str] = None
    name: str
    template_type: str
    content: str
    variables: Optional[list[str]] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
