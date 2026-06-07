import pytest
from unittest.mock import AsyncMock, Mock


@pytest.mark.asyncio
async def test_blog_with_images_generator():
    from backend.generators.multimodal_generators.blog_with_images import BlogWithImagesGenerator
    mock_blog = AsyncMock()
    mock_blog.generate.return_value = "Blog content"
    mock_image = AsyncMock()
    mock_image.generate.return_value = "https://example.com/image.png"

    generator = BlogWithImagesGenerator(mock_blog, mock_image)
    result = await generator.generate("Test topic")
    assert "content" in result
    assert "images" in result
    assert len(result["images"]) == 3


@pytest.mark.asyncio
async def test_social_media_bundle_generator():
    from backend.generators.multimodal_generators.social_media_bundle import SocialMediaBundleGenerator
    mock_social = AsyncMock()
    mock_social.generate.return_value = "Social post"
    mock_image = AsyncMock()
    mock_image.generate.return_value = "https://example.com/img.png"

    generator = SocialMediaBundleGenerator(mock_social, mock_image)
    result = await generator.generate("Test topic", platforms=["twitter", "instagram"])
    assert "twitter" in result
    assert "instagram" in result


@pytest.mark.asyncio
async def test_presentation_generator():
    from backend.generators.multimodal_generators.presentation_generator import PresentationGenerator
    mock_llm = AsyncMock()
    mock_llm.generate.return_value = "Slide content"
    mock_factory = Mock()
    mock_factory.get_llm.return_value = mock_llm

    generator = PresentationGenerator(mock_factory)
    result = await generator.generate("AI Trends", slides=5)
    assert result == "Slide content"


@pytest.mark.asyncio
async def test_content_suite_generator():
    from backend.generators.multimodal_generators.content_suite_generator import ContentSuiteGenerator
    mock_llm = AsyncMock()
    mock_llm.generate.return_value = "Suite content"
    mock_factory = Mock()
    mock_factory.get_llm.return_value = mock_llm

    generator = ContentSuiteGenerator(mock_factory)
    result = await generator.generate("Test", content_types=["blog", "email"])
    assert result == "Suite content"
