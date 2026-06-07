class EmotionTTS:
    def __init__(self):
        self.emotions = {
            "neutral": "Speak in a neutral, balanced tone",
            "happy": "Speak with a cheerful, upbeat tone",
            "sad": "Speak with a gentle, melancholic tone",
            "angry": "Speak with a firm, intense tone",
            "excited": "Speak with an enthusiastic, energetic tone",
            "calm": "Speak with a soothing, relaxing tone",
            "professional": "Speak with a confident, authoritative tone",
        }

    async def synthesize_with_emotion(self, text: str, emotion: str, voice: str, provider: str = "elevenlabs"):
        emotion_instruction = self.emotions.get(emotion, self.emotions["neutral"])
        enhanced_text = f"{emotion_instruction}. {text}"
        return enhanced_text

    def list_emotions(self) -> list[str]:
        return list(self.emotions.keys())
