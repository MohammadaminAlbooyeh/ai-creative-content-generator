class BlogPrompts:
    def get_system_prompt(self, template: str) -> str:
        prompts = {
            "listicle": "You are an expert at writing listicle blog posts.",
            "how_to": "You are an expert at writing how-to guides.",
            "tutorial": "You are an expert at writing tutorials.",
            "review": "You are an expert product reviewer.",
            "opinion": "You are an expert opinion writer.",
            "news": "You are a news journalist.",
        }
        return prompts.get(template, "You are an expert blog writer.")

    def get_user_prompt(self, topic: str, template: str, tone: str, length: str) -> str:
        return f"Write a {tone} {length}-length {template} blog post about: {topic}"
