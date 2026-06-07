from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, JSON
from backend.models.database import Base
import uuid


class Template(Base):
    __tablename__ = "templates"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100), nullable=False)
    template_type = Column(String(50), nullable=False, index=True)
    body = Column("content", Text, nullable=False)
    variables = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "template_type": self.template_type,
            "content": self.body,
            "variables": self.variables,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
