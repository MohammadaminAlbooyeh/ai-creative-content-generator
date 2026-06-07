class YouTubeSocialTemplate:
    def __init__(self):
        self.name = "youtube"

    def render(self, description: str, hashtags: list[str] = None, timestamps: list[tuple] = None) -> str:
        result = description
        if timestamps:
            result += "\n\n## Timestamps\n"
            for time, title in timestamps:
                result += f"{time} - {title}\n"
        if hashtags:
            result += "\n" + " ".join([f"#{h}" for h in hashtags])
        return result
