from functools import lru_cache

from fastapi import Depends
from app.application.services.image_to_text_service import ImageToTextService
from app.domain.infrastructure.openai_ocr import OpenAITextExtractor
from config import get_settings


def get_image_to_text_service() -> ImageToTextService:
    settings = get_settings()
    extractor = OpenAITextExtractor(api_key=settings.openai_secret)
    return ImageToTextService(extractor)