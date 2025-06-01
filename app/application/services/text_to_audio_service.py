from app.domain.services.audio_converter import AudioConverter

class TextToAudioService:
    def __init__(self, audio_converter: AudioConverter):
        self.AudioConverter = audio_converter
    
    async def convert(self, text: str):
        return await self.AudioConverter.text_to_speech(
            text=text,
            voice="coral",
            instructions="Fale em um tom alegre e positivo."
        )