"""Example: Optimize image prompts for better results."""


def run_examples():
    from backend.generators.image_generators.image_prompt_builder import ImagePromptBuilder

    builder = ImagePromptBuilder()

    prompt = builder.build(
        subject="A majestic dragon flying over a medieval castle",
        style="fantasy",
        mood="epic",
        extra_details=["detailed scales", "glowing eyes", "stormy sky"],
    )
    print(f"Optimized prompt: {prompt}")
