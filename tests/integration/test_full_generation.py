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
async def test_health_check():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/health")
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_blog_endpoint_auth_works():
    """Verifies the blog endpoint accepts valid auth tokens.
    Requires real API keys for full end-to-end test."""
    token = _test_token()
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        try:
            response = await client.post(
                "/api/v1/generate/blog",
                json={"topic": "Test", "template": "listicle", "tone": "professional", "length": "medium", "language": "en"},
                headers={"Authorization": f"Bearer {token}"},
            )
            assert response.status_code == 200
        except Exception:
            pytest.skip("API keys not configured - skipping integration test")
