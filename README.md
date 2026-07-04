# 🎧 Audio Language Model (ALM)



**Audio Language Model (ALM)** is an advanced AI-powered system designed to **understand, analyze, and reason over audio conversations**.
It integrates **speech recognition, speaker diarization, audio event detection, emotion/paralinguistic analysis and contextual reasoning**  into a unified pipeline for intelligent audio understanding.

The system provides an **interactive dashboard** where users can upload audio files, visualize waveforms, generate transcriptions, analyze speakers, and ask questions about the audio content.

---

##  Features

 **Audio Upload & Visualization :**
Upload audio files and preview them with an interactive waveform visualizer.

 **Speech-to-Text Transcription :**
Convert audio recordings into accurate textual transcripts.

 **Speaker Diarization :**
Identify and separate multiple speakers within an audio conversation.

 **Speaker Analytics Dashboard :**
Visualize speaker distribution and conversation patterns.

  **Emotion & Paralinguistic Analysis :**
Analyze vocal cues such as tone, pitch, energy, and emotion to understand speaker sentiment and conversational context.


 **Audio Question Answering (Q&A) :**
Ask contextual questions about the uploaded audio.

 **Real-Time Audio Processing Pipeline**

---

##  Interactive Dashboard

Modern Streamlit dashboard featuring:

- Audio Upload
- Audio Recording
- Waveform Visualization
- Transcript Viewer
- Analytics Dashboard
- Audio Q&A

---

##  System Architecture

```text
                  Audio Input
                       │
          Upload / Microphone Recording
                       │
                       ▼
               FastAPI Backend
                       │
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼
 Whisper Transcription        Speaker Segmentation
        │                             │
        └──────────────┬──────────────┘
                       ▼
             Conversation Analysis
        ├── Summary
        ├── Keywords
        ├── Sentiment
        ├── Statistics
        └── Speaker Timeline
                       │
                       ▼
              Streamlit Dashboard
```

---

##  Project Structure

```text
Audio_Language_Model/
│
├── backend/
│   ├── app.py
│   ├── transcriber.py
│   ├── diarization.py
│   ├── reasoning.py
│   ├── uploads/
│   └── requirements.txt
│
├── frontend/
│   └── streamlit_app.py
│
├── install.py
├── model5.py
├── AL.png
└── README.md
```

---

## Technologies Used

### Artificial Intelligence

- OpenAI Whisper
- Transformers
- PyTorch

### Backend

- FastAPI
- Uvicorn
- Python

### Frontend

- Streamlit


### Audio Processing

- Pydub
- FFmpeg
- NumPy

### Data Processing

- Pandas
- JSON

---

## Installation

### Clone Repository

```bash
git clone https://github.com/nitishkumar1407/Audio_Language_Model.git

cd Audio_Language_Model
```

---

### Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

### Install FFmpeg

### macOS

```bash
brew install ffmpeg
```

### Windows

Download:

https://ffmpeg.org/download.html

---

### Running the Backend

```bash
cd backend

uvicorn app:app --reload --port 8000
```

Backend API:

```
http://127.0.0.1:8000
```

---

### Running the Frontend

```bash
cd frontend

streamlit run streamlit_app.py
```

Open:

```
http://localhost:8501
```

---

### API Endpoint

### Analyze Audio

```
POST /analyze
```

Input

```
Multipart Audio File
```

Returns

```json
{
    "transcript":"...",
    "summary":"...",
    "keywords":[...],
    "sentiment":"Positive",
    "statistics":{},
    "segments":[]
}
```

---


 ##  Future Improvements

* Real-time streaming audio processing
* Multilingual speech understanding
* Emotion-aware conversational analysis
* Edge-device optimized inference
*  Offline LLM Integration
* Integration with advanced LLM reasoning systems

---


