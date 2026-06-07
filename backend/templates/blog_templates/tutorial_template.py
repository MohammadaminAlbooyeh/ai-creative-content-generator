class TutorialTemplate:
    def __init__(self):
        self.name = "tutorial"
        self.structure = [
            "Title",
            "Overview/learning objectives",
            "Prerequisites",
            "Main content with code examples",
            "Summary",
        ]

    def render(self, title: str, overview: str, prerequisites: list[str], sections: list[dict]) -> str:
        prereq_section = "\n".join([f"- {p}" for p in prerequisites])
        body = "\n\n".join([f"## {s['heading']}\n\n{s['content']}" for s in sections])
        return f"# {title}\n\n{overview}\n\n## Prerequisites\n{prereq_section}\n\n{body}"
