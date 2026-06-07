from backend.services.generation_service import GenerationService


async def get_generation_service() -> GenerationService:
    return GenerationService()
