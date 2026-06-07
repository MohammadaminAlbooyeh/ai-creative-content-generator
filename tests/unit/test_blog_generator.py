import pytest
from backend.generators.text_generators.blog_post_generator import BlogPostGenerator


class TestBlogPostGenerator:
    def test_initialization(self, mocker):
        mock_factory = mocker.Mock()
        generator = BlogPostGenerator(mock_factory)
        assert generator is not None

    @pytest.mark.asyncio
    async def test_generate_calls_llm(self, mocker):
        mock_llm = mocker.AsyncMock()
        mock_llm.generate.return_value = "Generated blog content"
        mock_factory = mocker.Mock()
        mock_factory.get_llm.return_value = mock_llm

        generator = BlogPostGenerator(mock_factory)
        result = await generator.generate("Test topic")

        assert result == "Generated blog content"
        mock_llm.generate.assert_called_once()
