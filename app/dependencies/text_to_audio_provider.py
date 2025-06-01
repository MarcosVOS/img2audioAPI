from functools import lru_cache

from fastapi import Depends
from app.application.services.text_to_audio_service import TextToAudioService 
from app.domain.infrastructure.openai_tts import OpenAIAudioConverter
from config import Settings

@lru_cache
def get_settings() -> Settings:
    return Settings()

def get_text_to_audio_service(settings: Settings = Depends(get_settings)) -> TextToAudioService:
    extractor = OpenAIAudioConverter(api_key=settings.openai_secret)
    return TextToAudioService(extractor)