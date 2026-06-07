class ImagePromptBuilder:
    def __init__(self):
        self.style_templates = {
            "realistic": "photorealistic, highly detailed, 8K, natural lighting",
            "artistic": "artistic interpretation, creative, expressive",
            "cartoon": "cartoon style, vibrant colors, animated",
            "minimalist": "minimalist, clean lines, simple composition",
            "vintage": "vintage aesthetic, retro style, film grain",
            "fantasy": "fantasy art, magical, ethereal, dreamlike",
            "cyberpunk": "cyberpunk, neon lights, futuristic cityscape",
        }

    def build(self, subject: str, style: str = "realistic", mood: str = None, extra_details: list[str] = None):
        style_desc = self.style_templates.get(style, "")
        prompt = f"{subject}, {style_desc}"
        if mood:
            prompt += f", {mood} mood"
        if extra_details:
            prompt += ", " + ", ".join(extra_details)
        return prompt
