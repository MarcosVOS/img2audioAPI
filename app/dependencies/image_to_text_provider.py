from functools import lru_cache

from fastapi import Depends
from app.application.services.image_to_text_service import ImageToTextService
from app.domain.infrastructure.openai_ocr import OpenAITextExtractor
from config import Settings

@lru_cache
def get_settings() -> Settings:
    return Settings()

def get_image_to_text_service(settings: Settings = Depends(get_settings)) -> ImageToTextService:
    extractor = OpenAITextExtractor(api_key=settings.openai_secret)
    return ImageToTextService(extractor)