import whisper
import json
import os


def transcribe_audio(audio_path, output_path):
    """
    Transcribes speech from an audio file using Whisper
    and saves the segmented transcript as a JSON file.
    """

    print("Loading Whisper model (tiny)...")
    model = whisper.load_model("tiny")  # lightweight model for low-resource systems

    print("Starting transcription...")
    transcription_result = model.transcribe(audio_path)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            transcription_result["segments"],
            file,
            indent=2,
            ensure_ascii=False
        )

    print(f"Transcription completed successfully!")
    print(f"Transcript saved at: {output_path}")


# ---- Script execution ----
AUDIO_PATH = "audio/extracted.wav"
OUTPUT_PATH = "transcripts/transcript.json"

transcribe_audio(AUDIO_PATH, OUTPUT_PATH)
