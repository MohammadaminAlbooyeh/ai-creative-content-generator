import pytest
from fastapi.testclient import TestClient
from backend.main import app


client = TestClient(app)


class TestAPI:
    def test_health_check(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"

    def test_list_templates(self):
        response = client.get("/api/v1/templates")
        assert response.status_code == 200
