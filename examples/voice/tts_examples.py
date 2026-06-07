"""Example: Text-to-speech generation."""


async def run_examples():
    from backend.generators.voice_generators.text_to_speech import TextToSpeech

    tts = TextToSpeech(None, None)
    print("TTS examples require API keys to be configured.")
