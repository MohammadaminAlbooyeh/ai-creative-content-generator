class InstagramReelsTemplate:
    def __init__(self):
        self.name = "instagram_reels"

    def render(self, hook: str, key_moments: list[str], song_suggestion: str, caption: str, hashtags: list[str]) -> str:
        moments = "\n".join([f"- {m}" for m in key_moments])
        return f"HOOK: {hook}\n\nKEY MOMENTS:\n{moments}\n\nSONG: {song_suggestion}\n\nCAPTION:\n{caption}\n\n{''.join([f'#{h} ' for h in hashtags])}"
