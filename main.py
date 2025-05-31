from functools import lru_cache
from fastapi import Depends, FastAPI
from fastapi import FastAPI, File, UploadFile
from typing_extensions import Annotated
import config
from openai import OpenAI
import base64
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

app.include_router(image_text.router, prefix="/api/v1", tags=["Image to Text"])
