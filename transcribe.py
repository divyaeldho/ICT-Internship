import whisper
import json
import os

AUDIO_PATH = "audio/extracted.wav"
OUTPUT_PATH = "transcripts/transcript.json"

# Use lightweight model to avoid system hang
model = whisper.load_model("tiny")

result = model.transcribe(AUDIO_PATH)

os.makedirs("transcripts", exist_ok=True)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(result["segments"], f, indent=2, ensure_ascii=False)

print("Transcription completed and saved to transcripts/transcript.json")

