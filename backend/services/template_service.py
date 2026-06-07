class TemplateService:
    def __init__(self):
        self.templates = {}

    def register(self, name: str, template):
        self.templates[name] = template

    def get(self, name: str):
        return self.templates.get(name)

    def list_by_type(self, template_type: str) -> list[str]:
        return [k for k in self.templates if k.startswith(template_type)]

    def list_all(self) -> list[str]:
        return list(self.templates.keys())
