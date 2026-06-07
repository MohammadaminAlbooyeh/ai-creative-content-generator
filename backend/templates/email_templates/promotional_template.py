class PromotionalEmailTemplate:
    def __init__(self):
        self.name = "promotional"

    def render(self, subject: str, headline: str, body: str, cta_text: str, cta_link: str) -> str:
        return f"Subject: {subject}\n\n# {headline}\n\n{body}\n\n{cta_text}: {cta_link}"
