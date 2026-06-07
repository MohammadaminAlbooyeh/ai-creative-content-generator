class ListicleTemplate:
    def __init__(self):
        self.name = "listicle"
        self.structure = [
            "Catchy title with number",
            "Brief introduction",
            "Numbered items with descriptions",
            "Conclusion",
        ]

    def render(self, items: list[dict]) -> str:
        title = items[0].get("title", "Top List")
        intro = items[0].get("intro", "")
        body = "\n\n".join([f"{i+1}. {item['title']}\n{item['description']}" for i, item in enumerate(items[1:-1])])
        conclusion = items[-1].get("conclusion", "")
        return f"# {title}\n\n{intro}\n\n{body}\n\n{conclusion}"
