class CreativePrompts:
    def get_story_system_prompt(self) -> str:
        return "You are an award-winning creative writer. Write vivid, engaging stories."

    def get_story_user_prompt(self, genre: str, premise: str, tone: str, length: str) -> str:
        return f"Write a {tone} {length} {genre} story based on this premise: {premise}"

    def get_poetry_system_prompt(self) -> str:
        return "You are an acclaimed poet. Write beautiful, evocative poetry."

    def get_poetry_user_prompt(self, style: str, theme: str, tone: str, structure: str) -> str:
        return f"Write a {tone} {style} poem about {theme} in {structure} structure."
