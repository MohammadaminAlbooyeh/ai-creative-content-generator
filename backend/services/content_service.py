from datetime import datetime
from sqlalchemy.orm import Session
from backend.models.content import Content
from backend.models.database import SessionLocal


class ContentService:
    def __init__(self, db: Session = None):
        self.db = db or SessionLocal()

    async def save(self, title: str, content_type: str, body: str, user_id: str = None, metadata: dict = None) -> Content:
        content = Content(
            title=title,
            content_type=content_type,
            body=body,
            metadata_json=metadata,
            user_id=user_id,
        )
        self.db.add(content)
        self.db.commit()
        self.db.refresh(content)
        return content

    async def get(self, content_id: str) -> Content:
        return self.db.query(Content).filter(Content.id == content_id).first()

    async def delete(self, content_id: str) -> bool:
        content = self.db.query(Content).filter(Content.id == content_id).first()
        if content:
            self.db.delete(content)
            self.db.commit()
            return True
        return False

    async def list_all(self, user_id: str = None) -> list[Content]:
        query = self.db.query(Content)
        if user_id:
            query = query.filter(Content.user_id == user_id)
        return query.order_by(Content.created_at.desc()).all()

    async def list_by_type(self, content_type: str, user_id: str = None) -> list[Content]:
        query = self.db.query(Content).filter(Content.content_type == content_type)
        if user_id:
            query = query.filter(Content.user_id == user_id)
        return query.order_by(Content.created_at.desc()).all()

    def close(self):
        self.db.close()
