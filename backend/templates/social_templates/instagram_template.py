class InstagramTemplate:
    def __init__(self):
        self.name = "instagram"

    def render(self, caption: str, hashtags: list[str], mentions: list[str] = None) -> str:
        text = caption
        if mentions:
            text += "\n\n" + " ".join([f"@{m}" for m in mentions])
        text += "\n\n" + " ".join([f"#{h}" for h in hashtags])
        return text
