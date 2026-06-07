# Deployment Guide

## Docker Deployment

```bash
docker-compose up -d
```

## Manual Deployment

1. Set up PostgreSQL and Redis
2. Configure environment variables
3. Run database migrations: `alembic upgrade head`
4. Start backend: `uvicorn backend.main:app --host 0.0.0.0 --port 8000`
5. Build frontend: `cd frontend && npm run build`
6. Serve frontend build with Nginx or similar

## Environment Variables

See `.env.example` for all required configuration.
