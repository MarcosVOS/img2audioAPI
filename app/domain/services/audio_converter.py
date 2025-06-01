from abc import ABC, abstractmethod

class AudioConverter(ABC):
    @abstractmethod
    async def text_to_speech(self, text: str, voice: str, instructions: str) -> bytes:
        pass