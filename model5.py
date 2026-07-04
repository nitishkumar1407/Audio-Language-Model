import os
from faster_whisper import WhisperModel
import ollama

print("====================================")
print("AHNA MODEL STARTING...")
print("====================================")

# Whisper model
model = WhisperModel(
    "base",
    compute_type="int8"
)

# Audio path
audio_path = input(
    "\nEnter audio file path: "
)

if not os.path.exists(audio_path):

    print("File not found")

    exit()

# Transcription
print("\nTranscribing audio...\n")

segments, info = model.transcribe(
    audio_path
)

full_text = ""

for segment in segments:

    text = segment.text.strip()

    print(
        f"[{segment.start:.2f}s -> "
        f"{segment.end:.2f}s] "
        f"{text}"
    )

    full_text += text + " "

print("\n====================================")
print("TRANSCRIPTION COMPLETE")
print("====================================")

print("\nFULL TEXT:\n")
print(full_text)

# Llama reasoning
print("\nRunning Llama3 reasoning...\n")

prompt = f"""
Analyze this conversation/audio.

Give:
1. Summary
2. Main topics
3. Important events
4. Emotion analysis
5. Intent detection

Conversation:
{full_text}
"""

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

reasoning = response["message"]["content"]

print("\n====================================")
print("AI REASONING OUTPUT")
print("====================================\n")

print(reasoning)