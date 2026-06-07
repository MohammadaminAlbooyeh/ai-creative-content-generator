"""Example: Generate product descriptions."""


async def run_examples():
    from backend.llm.llm_factory import LLMFactory
    from backend.generators.text_generators.product_description_generator import ProductDescriptionGenerator

    factory = LLMFactory()
    generator = ProductDescriptionGenerator(factory)

    result = await generator.generate(
        "Smart Home Speaker",
        features=["voice control", "HD sound", "smart home hub"],
        tone="persuasive",
    )
    print(result)
