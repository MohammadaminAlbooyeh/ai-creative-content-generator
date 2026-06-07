"""Benchmark generation performance across providers."""


import time


async def benchmark_providers():
    from backend.llm.llm_factory import LLMFactory

    factory = LLMFactory()
    providers = factory.list_providers()
    test_prompt = "Write a short paragraph about AI."

    for provider in providers:
        try:
            llm = factory.get_llm(provider)
            start = time.time()
            await llm.generate("You are helpful.", test_prompt)
            elapsed = time.time() - start
            print(f"{provider}: {elapsed:.2f}s")
        except Exception as e:
            print(f"{provider}: SKIPPED ({e})")


if __name__ == "__main__":
    import asyncio
    asyncio.run(benchmark_providers())
