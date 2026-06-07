class SystemPrompts:
    def __init__(self):
        self.prompts = {
            "blog": "You are an expert blog writer. Write engaging, well-structured blog posts.",
            "social": "You are a social media content creator. Write platform-appropriate posts.",
            "email": "You are an email marketing specialist. Write compelling email copy.",
            "creative": "You are a creative writer. Write imaginative and engaging stories.",
            "marketing": "You are a marketing copywriter. Write persuasive marketing copy.",
            "technical": "You are a technical writer. Write clear, accurate technical documentation.",
            "image": "You are an expert at writing image generation prompts.",
            "voice": "You are a voice-over script writer.",
        }

    def get(self, content_type: str) -> str:
        return self.prompts.get(content_type, "You are a helpful AI assistant.")
