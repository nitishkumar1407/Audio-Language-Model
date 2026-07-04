import numpy as np
import soundfile as sf


def diarize_audio(audio_path):

    audio, sr = sf.read(audio_path)

    chunk_size = sr * 3

    speakers = []
    speaker_id = 1

    for i in range(0, len(audio), chunk_size):

        chunk = audio[i:i+chunk_size]

        energy = np.mean(np.abs(chunk))

        state = "Speech Detected" if energy > 0.02 else "Silence"

        speakers.append({
            "speaker": f"Speaker {speaker_id}",
            "state": state
        })

        speaker_id += 1

    return speakers