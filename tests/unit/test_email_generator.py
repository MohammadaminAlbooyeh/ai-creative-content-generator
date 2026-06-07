import pytest
from backend.generators.text_generators.email_generator import EmailGenerator


class TestEmailGenerator:
    def test_initialization(self, mocker):
        mock_factory = mocker.Mock()
        generator = EmailGenerator(mock_factory)
        assert generator is not None

    @pytest.mark.asyncio
    async def test_generate_email(self, mocker):
        mock_llm = mocker.AsyncMock()
        mock_llm.generate.return_value = "Email content"
        mock_factory = mocker.Mock()
        mock_factory.get_llm.return_value = mock_llm

        generator = EmailGenerator(mock_factory)
        result = await generator.generate("welcome", "Welcome to our service")

        assert result == "Email content"
