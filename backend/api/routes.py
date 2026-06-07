from fastapi import APIRouter, Depends

from backend.api.schemas import (
    GenerateRequest, GenerateResponse,
    BlogRequest, SocialRequest, EmailRequest,
    ImageRequest, VoiceRequest, VideoRequest, BundleRequest,
)
from backend.services.generation_service import GenerationService
from backend.api.dependencies import get_generation_service

router = APIRouter()


@router.post("/content/generate", response_model=GenerateResponse)
async def generate_content(
    request: GenerateRequest,
    service: GenerationService = Depends(get_generation_service),
):
    return await service.generate(request)


@router.post("/generate/blog", response_model=GenerateResponse)
async def generate_blog(
    request: BlogRequest,
    service: GenerationService = Depends(get_generation_service),
):
    return await service.generate_blog(request)


@router.post("/generate/social", response_model=GenerateResponse)
async def generate_social(
    request: SocialRequest,
    service: GenerationService = Depends(get_generation_service),
):
    return await service.generate_social(request)


@router.post("/generate/email", response_model=GenerateResponse)
async def generate_email(
    request: EmailRequest,
    service: GenerationService = Depends(get_generation_service),
):
    return await service.generate_email(request)


@router.post("/generate/image", response_model=GenerateResponse)
async def generate_image(
    request: ImageRequest,
    service: GenerationService = Depends(get_generation_service),
):
    return await service.generate_image(request)


@router.post("/generate/voice", response_model=GenerateResponse)
async def generate_voice(
    request: VoiceRequest,
    service: GenerationService = Depends(get_generation_service),
):
    return await service.generate_voice(request)


@router.post("/generate/video", response_model=GenerateResponse)
async def generate_video(
    request: VideoRequest,
    service: GenerationService = Depends(get_generation_service),
):
    return await service.generate_video(request)


@router.post("/generate/bundle", response_model=GenerateResponse)
async def generate_bundle(
    request: BundleRequest,
    service: GenerationService = Depends(get_generation_service),
):
    return await service.generate_bundle(request)


@router.get("/templates")
async def list_templates(
    service: GenerationService = Depends(get_generation_service),
):
    return await service.list_templates()


@router.get("/templates/{template_type}")
async def get_templates_by_type(
    template_type: str,
    service: GenerationService = Depends(get_generation_service),
):
    return await service.get_templates_by_type(template_type)


@router.get("/history")
async def get_history(
    service: GenerationService = Depends(get_generation_service),
):
    return await service.get_history()


@router.get("/content/{content_id}")
async def get_content(
    content_id: str,
    service: GenerationService = Depends(get_generation_service),
):
    return await service.get_content(content_id)
