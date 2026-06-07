class NewsletterEmailTemplate:
    def __init__(self):
        self.name = "newsletter"

    def render(self, subject: str, greeting: str, sections: list[dict], farewell: str) -> str:
        body = f"Subject: {subject}\n\n{greeting}\n\n"
        for section in sections:
            body += f"## {section['title']}\n{section['content']}\n\n"
        body += farewell
        return body
