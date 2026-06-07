from elevenlabs import generate, set_api_key, Voice, VoiceSettings, clone
from backend.utils.config import settings


class ElevenLabsClient:
    def __init__(self):
        self._initialized = False
        if settings.ELEVENLABS_API_KEY:
            set_api_key(settings.ELEVENLABS_API_KEY)
            self._initialized = True

    async def synthesize(self, text: str, voice: str = "Rachel", speed: float = 1.0):
        if not self._initialized:
            raise RuntimeError("ElevenLabs API key not configured")
        audio = generate(
            text=text,
            voice=voice,
            model="eleven_monolingual_v1",
        )
        return audio

    async def clone_voice(self, audio_samples: list[str], voice_name: str):
        if not self._initialized:
            raise RuntimeError("ElevenLabs API key not configured")
        voice = clone(
            name=voice_name,
            files=audio_samples,
        )
        return voice.voice_id
