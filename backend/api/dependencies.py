from typing import Generator
from fastapi import Depends
from sqlalchemy.orm import Session
from backend.models.database import SessionLocal
from backend.services.generation_service import GenerationService
from backend.services.content_service import ContentService
from backend.services.cache_service import CacheService
from backend.services.analytics_service import AnalyticsService


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_generation_service(db: Session = Depends(get_db)) -> GenerationService:
    return GenerationService(db)


async def get_content_service(db: Session = Depends(get_db)) -> ContentService:
    return ContentService(db)


async def get_cache_service() -> CacheService:
    return CacheService()


async def get_analytics_service(db: Session = Depends(get_db)) -> AnalyticsService:
    return AnalyticsService(db)
