from app.application.services.image_to_text_service import ImageToTextService
from app.application.services.text_to_audio_service import TextToAudioService
from app.domain.models.image import Image

class ImageToAudioService:
    def __init__(self, text_service: ImageToTextService, audio_service: TextToAudioService):
        self.text_service = text_service
        self.audio_service = audio_service
    
    async def convert(self, image: Image) -> bytes:
        text = await self.text_service.convert(image)
        audio = await self.audio_service.convert(text)
        return audio 