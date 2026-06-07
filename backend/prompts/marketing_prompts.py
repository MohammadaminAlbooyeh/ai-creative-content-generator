class MarketingPrompts:
    def get_product_description_prompt(self, product: str, features: list[str], tone: str, audience: str) -> str:
        features_text = ", ".join(features)
        return f"Write a {tone} product description for '{product}' targeting {audience}. Key features: {features_text}"

    def get_marketing_copy_prompt(self, product: str, channel: str, tone: str, audience: str) -> str:
        return f"Write {tone} marketing copy for '{product}' on {channel} targeting {audience}."

    def get_headline_prompt(self, topic: str, style: str, count: int) -> str:
        return f"Generate {count} {style} headlines about: {topic}"
