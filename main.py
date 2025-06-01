from functools import lru_cache
from fastapi import Depends, FastAPI
from fastapi import FastAPI, File, UploadFile
from typing_extensions import Annotated
from pathlib import Path
from fastapi.responses import FileResponse

from openai import OpenAI
from app.api.v1.endpoints import image_text
from app.api.v1.endpoints import text_to_audio
from app.api.v1.endpoints import image_to_audio

app = FastAPI(
    title="Image To Audio API",
    description="An API that converts images to audio using a pre-trained model.", 
    version="1.0.0",
)


@app.get("/status")
async def status():
    return {"status": "ok"}

app.include_router(image_text.router, prefix="/api/v1", tags=["Image to Text"])
app.include_router(text_to_audio.router, prefix="/api/v1", tags=["Text to Audio"])
app.include_router(image_to_audio.router, prefix="/api/v1", tags=["Image to Audio"])