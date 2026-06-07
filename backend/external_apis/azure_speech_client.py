import io
from typing import Optional
import aiohttp
from backend.utils.config import settings


class AzureSpeechClient:
    def __init__(self):
        self.subscription_key = settings.AZURE_SPEECH_KEY
        self.region = settings.AZURE_SPEECH_REGION
        self.base_url = f"https://{self.region}.tts.speech.microsoft.com/cognitiveservices/v1"

    async def synthesize_speech(self, text: str, voice: str = "en-US-JennyNeural",
                                 language: str = "en-US", speed: str = "1.0") -> bytes:
        if not self.subscription_key or not self.region:
            raise ValueError("Azure Speech credentials not configured")

        ssml = f"""
        <speak version='1.0' xml:lang='{language}'>
            <voice name='{voice}'>
                <prosody rate='{speed}'>{text}</prosody>
            </voice>
        </speak>
        """

        headers = {
            "Ocp-Apim-Subscription-Key": self.subscription_key,
            "Content-Type": "application/ssml+xml",
            "X-Microsoft-OutputFormat": "audio-16khz-128kbitrate-mono-mp3",
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url, headers=headers, data=ssml.encode("utf-8")) as response:
                if response.status != 200:
                    error_text = await response.text()
                    raise RuntimeError(f"Azure Speech API error {response.status}: {error_text}")
                audio_data = await response.read()
                return audio_data

    async def list_available_voices(self) -> list[dict]:
        url = f"https://{self.region}.tts.speech.microsoft.com/cognitiveservices/voices/list"
        headers = {"Ocp-Apim-Subscription-Key": self.subscription_key}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    return []
                return await response.json()
