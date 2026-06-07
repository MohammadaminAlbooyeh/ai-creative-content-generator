from backend.prompts.system_prompts import SystemPrompts


class PromptManager:
    def __init__(self):
        self.system_prompts = SystemPrompts()
        self.prompt_templates = {}

    def register_prompt(self, name: str, template: str):
        self.prompt_templates[name] = template

    def get_prompt(self, name: str, **kwargs) -> str:
        template = self.prompt_templates.get(name)
        if not template:
            raise ValueError(f"Prompt template '{name}' not found")
        return template.format(**kwargs)

    def get_system_prompt(self, content_type: str) -> str:
        return self.system_prompts.get(content_type)
