"""Example: Generate images with DALL-E."""


async def run_examples():
    from backend.external_apis.openai_client import OpenAIClient
    from backend.generators.image_generators.dall_e_generator import DallEGenerator

    client = OpenAIClient()
    generator = DallEGenerator(client)

    prompts = [
        "A serene mountain lake at sunset",
        "A futuristic city with flying cars and neon lights",
    ]

    for prompt in prompts:
        images = await generator.generate(prompt)
        print(f"Generated images for: {prompt}")
        print(images)
