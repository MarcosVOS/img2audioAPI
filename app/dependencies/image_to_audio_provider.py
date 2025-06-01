from functools import lru_cache

from fastapi import Depends
from app.application.services.image_to_audio_service import ImageToAudioService
from app.dependencies.image_to_text_provider import get_image_to_text_service
from app.dependencies.text_to_audio_provider import get_text_to_audio_service
from config import Settings

def get_image_to_audio_service() -> ImageToAudioService:
    text_service =  get_image_to_text_service()
    audio_service =  get_text_to_audio_service()
    return ImageToAudioService(text_service=text_service, audio_service=audio_service)