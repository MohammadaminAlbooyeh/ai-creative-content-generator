class TikTokVideoTemplate:
    def __init__(self):
        self.name = "tiktok_video"

    def render(self, hook: str, body: str, call_to_action: str, hashtags: list[str]) -> str:
        return f"HOOK: {hook}\n\nCONTENT:\n{body}\n\nCTA: {call_to_action}\n\n{''.join([f'#{h} ' for h in hashtags])}"
