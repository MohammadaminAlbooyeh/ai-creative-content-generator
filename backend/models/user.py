from datetime import datetime
from sqlalchemy import Column, String, DateTime, JSON
from sqlalchemy.orm import relationship
from backend.models.database import Base
import uuid


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String(100), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    api_keys = Column(JSON, nullable=True)
    preferences = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    contents = relationship("Content", back_populates="user")

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "preferences": self.preferences,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
