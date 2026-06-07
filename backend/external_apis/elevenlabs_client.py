from elevenlabs import generate, set_api_key, Voice, VoiceSettings, clone
from backend.utils.config import settings


class ElevenLabsClient:
    def __init__(self):
        set_api_key(settings.ELEVENLABS_API_KEY)

    async def synthesize(self, text: str, voice: str = "Rachel", speed: float = 1.0):
        audio = generate(
            text=text,
            voice=voice,
            model="eleven_monolingual_v1",
        )
        return audio

    async def clone_voice(self, audio_samples: list[str], voice_name: str):
        voice = clone(
            name=voice_name,
            files=audio_samples,
        )
        return voice.voice_id
