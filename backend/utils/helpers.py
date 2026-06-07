import uuid
from datetime import datetime


def generate_id() -> str:
    return str(uuid.uuid4())


def generate_timestamp() -> str:
    return datetime.now().isoformat()


def truncate_text(text: str, max_length: int = 100) -> str:
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."
