from backend.external_apis.elevenlabs_client import ElevenLabsClient
from backend.external_apis.google_tts_client import GoogleTTSClient


class TextToSpeech:
    def __init__(self, elevenlabs: ElevenLabsClient, google_tts: GoogleTTSClient):
        self.elevenlabs = elevenlabs
        self.google_tts = google_tts

    async def synthesize(self, text: str, voice: str = "default", provider: str = "elevenlabs", speed: float = 1.0):
        if provider == "elevenlabs":
            return await self.elevenlabs.synthesize(text, voice, speed)
        elif provider == "google":
            return await self.google_tts.synthesize(text, voice, speed)
        raise ValueError(f"Unknown TTS provider: {provider}")
