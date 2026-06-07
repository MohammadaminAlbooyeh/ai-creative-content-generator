class WelcomeEmailTemplate:
    def __init__(self):
        self.name = "welcome"

    def render(self, recipient_name: str, company_name: str, next_steps: list[str]) -> str:
        steps = "\n".join([f"{i+1}. {step}" for i, step in enumerate(next_steps)])
        return f"Subject: Welcome to {company_name}!\n\nHi {recipient_name},\n\nWelcome aboard! We're excited to have you.\n\nHere's what to do next:\n{steps}"
