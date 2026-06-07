class HowToTemplate:
    def __init__(self):
        self.name = "how_to"
        self.structure = [
            "Clear title starting with 'How to'",
            "Introduction explaining the problem",
            "Prerequisites/supplies needed",
            "Step-by-step instructions",
            "Conclusion and tips",
        ]

    def render(self, steps: list[str], title: str, intro: str, supplies: list[str] = None) -> str:
        supplies_section = f"## What You'll Need\n" + "\n".join([f"- {s}" for s in (supplies or [])])
        steps_section = "\n\n".join([f"### Step {i+1}\n{step}" for i, step in enumerate(steps)])
        return f"# {title}\n\n{intro}\n\n{supplies_section}\n\n## Instructions\n\n{steps_section}"
