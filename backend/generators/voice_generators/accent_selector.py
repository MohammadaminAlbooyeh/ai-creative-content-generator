class AccentSelector:
    def __init__(self):
        self.accents = {
            "american": "en-US",
            "british": "en-GB",
            "australian": "en-AU",
            "indian": "en-IN",
            "french": "fr-FR",
            "german": "de-DE",
            "spanish": "es-ES",
            "japanese": "ja-JP",
            "korean": "ko-KR",
            "chinese": "zh-CN",
        }

    def get_language_code(self, accent: str) -> str:
        return self.accents.get(accent, "en-US")

    def list_accents(self) -> list[str]:
        return list(self.accents.keys())
