from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from backend.models.database import Base
import uuid


class Content(Base):
    __tablename__ = "contents"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(255), nullable=False)
    content_type = Column(String(50), nullable=False, index=True)
    body = Column(Text, nullable=False)
    metadata_json = Column("metadata_json", JSON, nullable=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="contents")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content_type": self.content_type,
            "body": self.body,
            "metadata": self.metadata_json,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
