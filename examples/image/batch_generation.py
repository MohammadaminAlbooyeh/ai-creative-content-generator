"""Example: Batch generate multiple image variations."""


async def run_examples():
    from backend.generators.image_generators.image_variations import ImageVariations

    generator = ImageVariations()
    variations = await generator.generate_variations("A peaceful garden", count=3)
    for i, v in enumerate(variations):
        print(f"Variation {i + 1}: {v}")
