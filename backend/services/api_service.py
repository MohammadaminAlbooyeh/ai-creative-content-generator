from backend.external_apis.openai_client import OpenAIClient
from backend.external_apis.elevenlabs_client import ElevenLabsClient
from backend.external_apis.google_tts_client import GoogleTTSClient
from backend.external_apis.stabilityai_client import StabilityAIClient


class ApiService:
    def __init__(self):
        self.openai = OpenAIClient()
        self.elevenlabs = ElevenLabsClient()
        self.google_tts = GoogleTTSClient()
        self.stability = StabilityAIClient()
