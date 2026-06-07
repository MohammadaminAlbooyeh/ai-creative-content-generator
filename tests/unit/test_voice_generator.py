import pytest
from backend.generators.voice_generators.text_to_speech import TextToSpeech


class TestTextToSpeech:
    def test_initialization(self, mocker):
        tts = TextToSpeech(mocker.Mock(), mocker.Mock())
        assert tts is not None
