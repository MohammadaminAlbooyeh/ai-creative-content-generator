class ReviewTemplate:
    def __init__(self):
        self.name = "review"
        self.structure = [
            "Title with product name",
            "Introduction/first impressions",
            "Features breakdown",
            "Pros and cons",
            "Rating",
            "Final verdict",
        ]

    def render(self, product: str, intro: str, features: list[str], pros: list[str], cons: list[str], rating: float, verdict: str) -> str:
        features_text = "\n".join([f"- {f}" for f in features])
        pros_text = "\n".join([f"✅ {p}" for p in pros])
        cons_text = "\n".join([f"❌ {c}" for c in cons])
        return f"# {product} Review\n\n{intro}\n\n## Features\n{features_text}\n\n## Pros\n{pros_text}\n\n## Cons\n{cons_text}\n\n## Rating: {rating}/10\n\n{verdict}"
