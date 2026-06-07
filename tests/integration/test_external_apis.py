import pytest
from unittest.mock import patch


@pytest.mark.asyncio
async def test_openai_client_initialization():
    from backend.external_apis.openai_client import OpenAIClient
    client = OpenAIClient()
    assert client is not None


@pytest.mark.asyncio
async def test_elevenlabs_client_initialization():
    from backend.external_apis.elevenlabs_client import ElevenLabsClient
    client = ElevenLabsClient()
    assert client is not None
    assert client._initialized is False


@pytest.mark.asyncio
async def test_pexels_client_initialization():
    from backend.external_apis.pexels_client import PexelsClient
    client = PexelsClient()
    assert client is not None


@pytest.mark.asyncio
async def test_pixabay_client_initialization():
    from backend.external_apis.pixabay_client import PixabayClient
    client = PixabayClient()
    assert client is not None


@pytest.mark.asyncio
async def test_unsplash_client_initialization():
    from backend.external_apis.unsplash_client import UnsplashClient
    client = UnsplashClient()
    assert client is not None


@pytest.mark.asyncio
async def test_stabilityai_client_initialization():
    from backend.external_apis.stabilityai_client import StabilityAIClient
    client = StabilityAIClient()
    assert client is not None


@pytest.mark.asyncio
async def test_google_tts_client_initialization():
    from backend.external_apis.google_tts_client import GoogleTTSClient
    client = GoogleTTSClient()
    assert client is not None
    assert client._initialized is False
