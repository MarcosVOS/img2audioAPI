from app.domain.services.audio_converter import AudioConverter
from openai import OpenAI

class OpenAIAudioConverter(AudioConverter):
    def __init__ (self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    async def text_to_speech(self, text: str, voice: str, instructions: str) -> bytes:
        with self.client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice=voice,
            input=text,
            instructions=instructions
        ) as response:
            audio_bytes = response.read() 
        return audio_bytes