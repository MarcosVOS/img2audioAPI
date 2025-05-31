import base64
from app.domain.services.text_extractor import TextExtractor
from app.domain.models.image import Image
from openai import OpenAI

class OpenAITextExtractor(TextExtractor):
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
    
    async def extract_text(self, image):
        base64_image = base64.b64encode(image.content).decode("utf-8")
        data_url = f"data:image/{image.filename.split('.')[-1]};base64,{base64_image}"

        prompt = """
            Observe cuidadosamente a imagem enviada. Extraia qualquer texto visível (se houver) e, em seguida, descreva o conteúdo da imagem com base no contexto visual e textual. Responda às seguintes perguntas:

            1. Qual é o texto presente na imagem?
            2. Qual é o tipo de imagem (por exemplo: recibo, anúncio, documento, captura de tela, cena do cotidiano, etc.)?
            3. Qual é o contexto geral da imagem? O que ela parece estar comunicando ou representando?
            4. Há alguma informação importante ou relevante que deve ser destacada?
            5. Se houver elementos humanos, quais são suas possíveis emoções, ações ou intenções?

            Responda de forma clara, organizada e objetiva.
        """

        response = self.client.responses.create(
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
        
        return response.output_text