from functools import lru_cache

from fastapi import Depends
from app.application.services.text_to_audio_service import TextToAudioService 
from app.domain.infrastructure.openai_tts import OpenAIAudioConverter
from config import get_settings


def get_text_to_audio_service() -> TextToAudioService:
    settings = get_settings()
    extractor = OpenAIAudioConverter(api_key=settings.openai_secret)
    return TextToAudioService(extractor)