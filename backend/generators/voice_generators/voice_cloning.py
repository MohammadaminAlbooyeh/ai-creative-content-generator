from backend.external_apis.elevenlabs_client import ElevenLabsClient


class VoiceCloning:
    def __init__(self, elevenlabs: ElevenLabsClient):
        self.client = elevenlabs

    async def clone_voice(self, audio_samples: list[str], voice_name: str):
        return await self.client.clone_voice(audio_samples, voice_name)

    async def synthesize_with_cloned_voice(self, text: str, voice_id: str):
        return await self.client.synthesize(text, voice_id)
