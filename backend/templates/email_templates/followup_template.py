class FollowupEmailTemplate:
    def __init__(self):
        self.name = "followup"

    def render(self, recipient_name: str, context: str, next_steps: str) -> str:
        return f"Subject: Following up\n\nHi {recipient_name},\n\nI wanted to follow up regarding {context}.\n\n{next_steps}"
