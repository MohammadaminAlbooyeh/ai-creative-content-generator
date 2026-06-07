class ImagePrompts:
    def __init__(self):
        self.style_descriptors = {
            "realistic": "photorealistic, highly detailed, 8K",
            "artistic": "artistic, creative composition",
            "cartoon": "cartoon style, vibrant, animated",
            "minimalist": "minimalist, clean, simple",
            "fantasy": "fantasy art, magical, ethereal",
            "cyberpunk": "cyberpunk, neon, futuristic",
        }

    def build_prompt(self, subject: str, style: str = "realistic", mood: str = None, extra: list[str] = None) -> str:
        prompt = f"{subject}, {self.style_descriptors.get(style, '')}"
        if mood:
            prompt += f", {mood} atmosphere"
        if extra:
            prompt += ", " + ", ".join(extra)
        return prompt
