class ImageVariations:
    def __init__(self):
        self.variation_types = [
            "color palette swap",
            "composition change",
            "style variation",
            "mood variation",
            "seasonal variation",
        ]

    async def generate_variations(self, prompt: str, count: int = 3):
        variations = []
        for i in range(count):
            variation_prompt = f"{prompt} (variation {i + 1}: {self.variation_types[i % len(self.variation_types)]})"
            variations.append(variation_prompt)
        return variations
