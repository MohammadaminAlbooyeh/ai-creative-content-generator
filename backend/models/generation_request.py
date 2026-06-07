from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, Float, Integer, JSON
from backend.models.database import Base
import uuid


class GenerationRecord(Base):
    __tablename__ = "generation_records"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, nullable=True, index=True)
    content_type = Column(String(50), nullable=False, index=True)
    prompt = Column(Text, nullable=False)
    provider = Column(String(50), nullable=True)
    model = Column(String(100), nullable=True)
    tokens_used = Column(Integer, nullable=True)
    latency_ms = Column(Integer, nullable=True)
    metadata_json = Column("metadata_json", JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "content_type": self.content_type,
            "prompt": self.prompt,
            "provider": self.provider,
            "model": self.model,
            "tokens_used": self.tokens_used,
            "latency_ms": self.latency_ms,
            "metadata": self.metadata_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
