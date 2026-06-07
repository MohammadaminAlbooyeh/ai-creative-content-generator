from google.cloud import texttospeech
from backend.utils.config import settings


class GoogleTTSClient:
    def __init__(self):
        self._initialized = False
        self.client = None
        if settings.GOOGLE_APPLICATION_CREDENTIALS:
            self.client = texttospeech.TextToSpeechClient.from_service_account_file(
                settings.GOOGLE_APPLICATION_CREDENTIALS
            )
            self._initialized = True

    async def synthesize(self, text: str, voice_name: str = "en-US-Neural2-J", speed: float = 1.0):
        if not self._initialized:
            raise RuntimeError("Google TTS credentials not configured")
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name=voice_name,
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=speed,
        )
        response = self.client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config,
        )
        return response.audio_content
