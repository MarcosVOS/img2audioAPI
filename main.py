from functools import lru_cache
from fastapi import Depends, FastAPI
from fastapi import FastAPI, File, UploadFile
from typing_extensions import Annotated
import config
from pathlib import Path
from fastapi.responses import FileResponse

from openai import OpenAI
from app.api.v1.endpoints import image_text

app = FastAPI(
    title="Image To Audio API",
    description="An API that converts images to audio using a pre-trained model.", 
    version="1.0.0",
)

@lru_cache
def get_settings():
    return config.Settings()

@app.get("/status")
async def status():
    return {"status": "ok"}

@app.get("/text2audio")
async def text_to_audio(settings: Annotated[config.Settings, Depends(get_settings)]):
    client = OpenAI(api_key=settings.openai_api_key)
    speech_file_path = Path(__file__).parent / "speech.mp3"

    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        input="Olá, este é um teste da conversão de texto para áudio.",
        instructions="Fale em um tom alegre e positivo."
    ) as response: 
        response.stream_to_file(speech_file_path)

    return FileResponse(
        path=speech_file_path,
        media_type="audio/mpeg",
        filename="speech.mp3"
    )

app.include_router(image_text.router, prefix="/api/v1", tags=["Image to Text"])
