class TikTokTemplate:
    def __init__(self):
        self.name = "tiktok"

    def render(self, script: str, hashtags: list[str], duration_seconds: int = 60) -> str:
        return f"Duration: ~{duration_seconds}s\n\n{script}\n\n{''.join([f'#{h} ' for h in hashtags])}"
