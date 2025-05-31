from app.domain.services.text_extractor import TextExtractor
from app.domain.models.image import Image

class ImageToTextService:
    def __init__ (self, extractor: TextExtractor):
        self.extractor = extractor
    
    async def convert(self, image: Image) -> str:
        return await self.extractor.extract_text(image)