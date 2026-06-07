class VoicePrompts:
    def __init__(self):
        self.emotion_prefixes = {
            "neutral": "",
            "happy": "Say this with a cheerful, upbeat tone: ",
            "sad": "Say this with a gentle, melancholic tone: ",
            "angry": "Say this with firm intensity: ",
            "excited": "Say this with great enthusiasm: ",
            "calm": "Say this in a soothing, relaxed manner: ",
            "professional": "Say this with confident authority: ",
        }

    def get_tts_text(self, text: str, emotion: str = "neutral") -> str:
        prefix = self.emotion_prefixes.get(emotion, "")
        return f"{prefix}{text}"
