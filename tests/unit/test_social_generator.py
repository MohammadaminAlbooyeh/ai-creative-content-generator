import pytest
from backend.generators.text_generators.social_media_generator import SocialMediaGenerator


class TestSocialMediaGenerator:
    def test_initialization(self, mocker):
        mock_factory = mocker.Mock()
        generator = SocialMediaGenerator(mock_factory)
        assert generator is not None

    @pytest.mark.asyncio
    async def test_generate_with_platform(self, mocker):
        mock_llm = mocker.AsyncMock()
        mock_llm.generate.return_value = "Social media post"
        mock_factory = mocker.Mock()
        mock_factory.get_llm.return_value = mock_llm

        generator = SocialMediaGenerator(mock_factory)
        result = await generator.generate("instagram", "Test topic")

        assert result == "Social media post"
