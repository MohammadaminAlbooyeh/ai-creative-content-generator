"""Example: Generate presentation content."""


async def run_examples():
    from backend.llm.llm_factory import LLMFactory
    from backend.generators.multimodal_generators.presentation_generator import PresentationGenerator

    factory = LLMFactory()
    generator = PresentationGenerator(factory)

    result = await generator.generate("AI Strategy for 2024", slides=8, tone="professional")
    print(result)
