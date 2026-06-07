from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer, Float
from backend.models.database import Base
import uuid


class Usage(Base):
    __tablename__ = "usage_records"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, nullable=False, index=True)
    content_type = Column(String(50), nullable=False)
    provider = Column(String(50), nullable=False)
    tokens = Column(Integer, nullable=True)
    cost = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "content_type": self.content_type,
            "provider": self.provider,
            "tokens": self.tokens,
            "cost": self.cost,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
