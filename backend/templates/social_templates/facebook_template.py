class FacebookTemplate:
    def __init__(self):
        self.name = "facebook"

    def render(self, text: str, hashtags: list[str] = None, call_to_action: str = None) -> str:
        result = text
        if call_to_action:
            result += f"\n\n{call_to_action}"
        if hashtags:
            result += "\n\n" + " ".join([f"#{h}" for h in hashtags])
        return result
