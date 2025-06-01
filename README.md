# Image to Audio API 🎙️🖼️

This project is a Python-based API built with FastAPI that uses OpenAI's APIs to extract text from images and generate audio narrations from that content. It integrates advanced computer vision and text-to-speech techniques to transform visual content into spoken descriptions.

## Features

- 📸 **Image Text Extraction** – Uses OpenAI's vision model to identify and extract text from uploaded images.
- 🗣️ **Text-to-Speech (TTS)** – Converts extracted or provided text into high-quality audio.
- 🔄 **Image to Audio Flow** – Combines both processes to offer an end-to-end experience.
- 🧱 Clean architecture with SOLID principles and DDD (Domain-Driven Design).
- 🔐 Secure API key management via `.env` file.

## Folder Structure

```
app/
├── api/                    # FastAPI routes
├── application/            # Application layer (use cases)
├── dependencies/           # Dependency injection setup
├── domain/                 # Domain logic: services, models, infrastructure
├── main.py                 # Entry point
├── config.py               # App settings
├── requirements.txt        # Dependencies for pip
├── environment.yml         # Conda environment (optional)
└── default.env             # Environment variables
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-user/image-to-audio-api.git
cd image-to-audio-api
```

### 2. Create and activate environment

Using Conda:

```bash
conda env create -f environment.yml
conda activate img2audio
```

Or using `pip`:

```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Add environment variables

Create a `.env` file or use `default.env` as a base:

```env
OPENAI_SECRET=your-openai-api-key
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

Access the API at: [http://localhost:8000/docs](http://localhost:8000/docs)

## Endpoints

| Route                        | Method | Description                         |
|-----------------------------|--------|-------------------------------------|
| `/status`                   | GET    | Health check                        |
| `/api/v1/img2text`          | POST   | Extracts text from an image         |
| `/api/v1/text2audio`        | POST   | Converts text to audio              |
| `/api/v1/image2audio`       | POST   | Extracts text from image and speaks |

## License

This project is licensed under the MIT License.
