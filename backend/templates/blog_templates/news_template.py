class NewsTemplate:
    def __init__(self):
        self.name = "news"
        self.structure = [
            "Headline",
            "Dateline",
            "Lead paragraph (who, what, when, where, why)",
            "Supporting details",
            "Quotes/sources",
            "Conclusion/outlook",
        ]

    def render(self, headline: str, dateline: str, lead: str, details: list[str], quotes: list[str], conclusion: str) -> str:
        details_text = "\n\n".join(details)
        quotes_text = "\n\n".join([f"> {q}" for q in quotes])
        return f"# {headline}\n\n{dateline}\n\n{lead}\n\n{details_text}\n\n{quotes_text}\n\n{conclusion}"
