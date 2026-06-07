class TechnicalPrompts:
    def get_script_system_prompt(self) -> str:
        return "You are an expert script writer for video and podcast content."

    def get_script_user_prompt(self, topic: str, format: str, duration: str, tone: str) -> str:
        return f"Write a {duration} {format} script about {topic} in a {tone} tone."

    def get_technical_doc_system_prompt(self) -> str:
        return "You are an expert technical writer. Write clear, comprehensive documentation."

    def get_technical_doc_user_prompt(self, topic: str, doc_type: str, audience: str, tone: str) -> str:
        return f"Write {doc_type} documentation about {topic} for {audience} in a {tone} tone."
