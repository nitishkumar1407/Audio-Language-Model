from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from transcriber import transcribe_audio
from diarization import diarize_audio
from reasoning import analyze_text

import tempfile
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(await file.read())
            temp_path = tmp.name

        # TRANSCRIBE
        transcript = transcribe_audio(temp_path)

        # DIARIZATION
        speakers = diarize_audio(temp_path)

        # REASONING
        reasoning = analyze_text(transcript, speakers)

        return {
            "transcription": transcript["text"],
            "segments": transcript["segments"],
            "speakers": speakers,
            "reasoning": reasoning
        }

    except Exception as e:
        return {"error": str(e)}

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)