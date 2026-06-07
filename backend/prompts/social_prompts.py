class SocialPrompts:
    def get_system_prompt(self, platform: str) -> str:
        prompts = {
            "instagram": "You are an Instagram content creator. Write engaging captions.",
            "twitter": "You are a Twitter/X content creator. Write concise, impactful tweets.",
            "linkedin": "You are a LinkedIn content creator. Write professional posts.",
            "facebook": "You are a Facebook content creator. Write community-engaging posts.",
            "tiktok": "You are a TikTok content creator. Write viral script hooks.",
            "youtube": "You are a YouTube content creator. Write video descriptions.",
        }
        return prompts.get(platform, "You are a social media content creator.")

    def get_user_prompt(self, platform: str, topic: str, tone: str, include_hashtags: bool) -> str:
        prompt = f"Write a {tone} {platform} post about: {topic}"
        if include_hashtags:
            prompt += "\nInclude relevant hashtags."
        return prompt
