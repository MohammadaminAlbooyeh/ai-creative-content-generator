class YouTubeVideoTemplate:
    def __init__(self):
        self.name = "youtube_video"

    def render(self, title: str, description: str, timestamps: list[tuple], tags: list[str]) -> str:
        ts = "\n".join([f"{t} - {s}" for t, s in timestamps])
        return f"Title: {title}\n\nDescription:\n{description}\n\nTimestamps:\n{ts}\n\nTags: {', '.join(tags)}"
