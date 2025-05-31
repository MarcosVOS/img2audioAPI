from abc import ABC, abstractmethod
from app.domain.models.image import Image

class TextExtractor(ABC):
    @abstractmethod
    async def extract_text(self, image: Image) -> str:
        pass

