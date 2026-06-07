import pytest
from backend.generators.image_generators.dall_e_generator import DallEGenerator


class TestDallEGenerator:
    def test_initialization(self, mocker):
        mock_client = mocker.Mock()
        generator = DallEGenerator(mock_client)
        assert generator is not None

    @pytest.mark.asyncio
    async def test_generate_image(self, mocker):
        mock_client = mocker.AsyncMock()
        mock_client.generate_image.return_value = ["https://example.com/image.png"]
        generator = DallEGenerator(mock_client)
        result = await generator.generate("Test prompt")
        assert len(result) == 1
