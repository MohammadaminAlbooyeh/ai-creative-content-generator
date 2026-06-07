from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes import router
from backend.api.auth_routes import router as auth_router
from backend.middleware.error_handler import register_error_handlers
from backend.middleware.auth_middleware import AuthMiddleware
from backend.middleware.rate_limiter import RateLimiterMiddleware
from backend.utils.config import settings
from backend.models.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered creative content generation platform",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(AuthMiddleware)
app.add_middleware(RateLimiterMiddleware)

register_error_handlers(app)
app.include_router(router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    from backend.models.database import SessionLocal
    from sqlalchemy import text

    db_status = "unhealthy"
    redis_status = "unhealthy"
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
        db_status = "healthy"
    except Exception:
        pass

    try:
        import redis as redis_module
        r = redis_module.from_url(settings.REDIS_URL, socket_connect_timeout=2)
        r.ping()
        r.close()
        redis_status = "healthy"
    except Exception:
        pass

    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "version": "0.1.0",
        "database": db_status,
        "redis": redis_status,
    }
