"""Example: Generate different types of emails."""


async def run_examples():
    from backend.llm.llm_factory import LLMFactory
    from backend.generators.text_generators.email_generator import EmailGenerator

    factory = LLMFactory()
    generator = EmailGenerator(factory)

    email_types = ["welcome", "promotional", "newsletter"]
    for email_type in email_types:
        result = await generator.generate(email_type, f"Our {email_type} campaign")
        print(f"=== {email_type} ===\n{result}\n")
