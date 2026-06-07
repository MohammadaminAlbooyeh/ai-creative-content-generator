import pytest
from datetime import datetime, timedelta
from httpx import AsyncClient, ASGITransport
from jose import jwt
from backend.main import app
from backend.utils.config import settings


def _test_token():
    expire = datetime.utcnow() + timedelta(hours=1)
    return jwt.encode(
        {"sub": "test-user", "username": "test", "email": "test@test.com", "exp": expire},
        settings.SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )


@pytest.mark.asyncio
async def test_health_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"


@pytest.mark.asyncio
async def test_health_returns_service_name():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/health")
        data = response.json()
        assert "service" in data


@pytest.mark.asyncio
async def test_list_templates_requires_auth():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/api/v1/templates")
        assert response.status_code == 401


@pytest.mark.asyncio
async def test_list_templates_with_auth():
    token = _test_token()
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get(
            "/api/v1/templates",
            headers={"Authorization": f"Bearer {token}"},
        )
        assert response.status_code == 200
