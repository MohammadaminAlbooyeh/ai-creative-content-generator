class EmailPrompts:
    def get_system_prompt(self, email_type: str) -> str:
        prompts = {
            "welcome": "You are an expert at writing welcome emails.",
            "promotional": "You are an expert at writing promotional emails.",
            "newsletter": "You are an expert at writing newsletters.",
            "transactional": "You are an expert at writing transactional emails.",
            "followup": "You are an expert at writing follow-up emails.",
        }
        return prompts.get(email_type, "You are an email copywriter.")

    def get_user_prompt(self, email_type: str, subject: str, tone: str, key_points: list[str]) -> str:
        prompt = f"Write a {tone} {email_type} email with subject: {subject}"
        if key_points:
            prompt += f"\nKey points to include: {', '.join(key_points)}"
        return prompt
