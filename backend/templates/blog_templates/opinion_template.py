class OpinionTemplate:
    def __init__(self):
        self.name = "opinion"
        self.structure = [
            "Thought-provoking title",
            "Opening hook/position statement",
            "Supporting arguments",
            "Counterarguments",
            "Conclusion",
        ]

    def render(self, title: str, position: str, arguments: list[str], counterpoints: list[str], conclusion: str) -> str:
        args = "\n\n".join([f"### {a}" for a in arguments])
        counters = "\n".join([f"- {c}" for c in counterpoints])
        return f"# {title}\n\n{position}\n\n## Arguments\n{args}\n\n## Counterarguments\n{counters}\n\n## Conclusion\n{conclusion}"
