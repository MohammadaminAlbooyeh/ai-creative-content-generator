import pytest
from unittest.mock import AsyncMock, patch
from backend.services.generation_service import GenerationService
from backend.services.content_service import ContentService


class TestPerformance:
    @pytest.mark.asyncio
    async def test_generation_service_instantiation(self):
        service = GenerationService()
        assert service is not None

    @pytest.mark.asyncio
    async def test_content_service_save_and_retrieve(self):
        service = ContentService()
        content = await service.save(
            title="Test",
            content_type="blog",
            body="Test body",
        )
        assert content is not None
        assert content.id is not None

        retrieved = await service.get(content.id)
        assert retrieved is not None
        assert retrieved.title == "Test"

    @pytest.mark.asyncio
    async def test_content_service_delete(self):
        service = ContentService()
        content = await service.save(
            title="To Delete",
            content_type="blog",
            body="Delete me",
        )
        deleted = await service.delete(content.id)
        assert deleted is True

        not_found = await service.delete("nonexistent")
        assert not_found is False
