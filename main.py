from functools import lru_cache
from fastapi import Depends, FastAPI
from fastapi import FastAPI, File, UploadFile
from typing_extensions import Annotated
import config
from openai import OpenAI
import base64

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

@app.post("/img2text")
async def img2text(settings: Annotated[config.Settings, Depends(get_settings)],file: UploadFile):

    ext = file.filename.split(".")[-1].lower()
    if ext not in ["jpg", "jpeg", "png"]:
        return {"error": "Unsupported file format. Please upload a JPG or PNG image."}

    content = await file.read()
    size_mb = len(content) / (1024 * 1024)
    if size_mb > 10:
        return {"error": "File size exceeds 10 MB limit."}

    base64_image = base64.b64encode(content).decode("utf-8")
    data_url = f"data:image/{ext};base64,{base64_image}"


    client = OpenAI(
        api_key=settings.openai_secret,
    )

    prompt = """
        Observe cuidadosamente a imagem enviada. Extraia qualquer texto visível (se houver) e, em seguida, descreva o conteúdo da imagem com base no contexto visual e textual. Responda às seguintes perguntas:

        1. Qual é o texto presente na imagem?
        2. Qual é o tipo de imagem (por exemplo: recibo, anúncio, documento, captura de tela, cena do cotidiano, etc.)?
        3. Qual é o contexto geral da imagem? O que ela parece estar comunicando ou representando?
        4. Há alguma informação importante ou relevante que deve ser destacada?
        5. Se houver elementos humanos, quais são suas possíveis emoções, ações ou intenções?

        Responda de forma clara, organizada e objetiva.
    """


    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[{
            "role": "user",
            "content": [
                {"type": "input_text", "text": prompt},
                {
                    "type": "input_image",
                    "image_url": data_url,
                },
            ],
        }],
    )    

    mb = file.size / (1024 * 1024)
    if mb > 10:
        return {"error": "File size exceeds 10 MB limit."}
    if file.filename.split(".")[-1].lower() not in ["jpg", "jpeg", "png"]:
        return {"error": "Unsupported file format. Please upload a JPG or PNG image."}

    return {"message": response.output_text}

