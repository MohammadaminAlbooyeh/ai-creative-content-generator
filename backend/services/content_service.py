from datetime import datetime
from backend.models.content import Content


class ContentService:
    def __init__(self):
        self.storage = {}

    async def save(self, content: Content) -> str:
        content_id = str(datetime.now().timestamp())
        self.storage[content_id] = content
        return content_id

    async def get(self, content_id: str) -> Content:
        return self.storage.get(content_id)

    async def delete(self, content_id: str) -> bool:
        if content_id in self.storage:
            del self.storage[content_id]
            return True
        return False

    async def list_all(self) -> list[Content]:
        return list(self.storage.values())
