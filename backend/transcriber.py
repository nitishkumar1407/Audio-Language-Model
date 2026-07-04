import whisper

model = whisper.load_model("tiny")


def transcribe_audio(audio_path):

    result = model.transcribe(
        audio_path,
        fp16=False,
        language="en"
    )

    return {
        "text": result["text"],
        "segments": [
            {
                "start": round(seg["start"], 2),
                "end": round(seg["end"], 2),
                "text": seg["text"]
            }
            for seg in result.get("segments", [])
        ]
    }