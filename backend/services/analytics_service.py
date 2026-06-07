from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.models.generation_request import GenerationRecord
from backend.models.usage import Usage
from backend.models.database import SessionLocal


class AnalyticsService:
    def __init__(self, db: Session = None):
        self.db = db or SessionLocal()

    async def track_generation(self, user_id: str, content_type: str, prompt: str,
                                provider: str = None, model: str = None,
                                tokens_used: int = None, latency_ms: int = None,
                                metadata: dict = None):
        record = GenerationRecord(
            user_id=user_id,
            content_type=content_type,
            prompt=prompt,
            provider=provider,
            model=model,
            tokens_used=tokens_used,
            latency_ms=latency_ms,
            metadata_json=metadata,
        )
        self.db.add(record)
        self.db.commit()

    async def get_generation_count(self, since: timedelta = timedelta(days=7)) -> int:
        cutoff = datetime.utcnow() - since
        return self.db.query(func.count(GenerationRecord.id)).filter(
            GenerationRecord.created_at > cutoff
        ).scalar() or 0

    async def get_popular_content_types(self, limit: int = 10) -> list[dict]:
        results = self.db.query(
            GenerationRecord.content_type,
            func.count(GenerationRecord.id).label("count")
        ).group_by(GenerationRecord.content_type).order_by(
            func.count(GenerationRecord.id).desc()
        ).limit(limit).all()
        return [{"content_type": r[0], "count": r[1]} for r in results]

    async def get_usage_stats(self, user_id: str = None) -> dict:
        query = self.db.query(
            func.sum(Usage.tokens).label("total_tokens"),
            func.sum(Usage.cost).label("total_cost"),
            func.count(Usage.id).label("total_requests"),
        )
        if user_id:
            query = query.filter(Usage.user_id == user_id)
        result = query.first()
        return {
            "total_tokens": result[0] or 0,
            "total_cost": result[1] or 0.0,
            "total_requests": result[2] or 0,
        }

    def close(self):
        self.db.close()
