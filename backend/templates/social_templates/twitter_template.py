class TwitterTemplate:
    def __init__(self):
        self.name = "twitter"
        self.char_limit = 280

    def render(self, text: str, hashtags: list[str] = None) -> str:
        result = text
        if hashtags:
            result += "\n\n" + " ".join([f"#{h}" for h in hashtags])
        return result[:self.char_limit]
