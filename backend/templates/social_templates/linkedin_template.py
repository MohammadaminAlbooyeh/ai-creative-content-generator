class LinkedInTemplate:
    def __init__(self):
        self.name = "linkedin"

    def render(self, text: str, hashtags: list[str] = None, mention_companies: list[str] = None) -> str:
        result = text
        if mention_companies:
            for company in mention_companies:
                text = text.replace(company, f"@{company}")
        if hashtags:
            result += "\n\n" + " ".join([f"#{h}" for h in hashtags])
        return result
