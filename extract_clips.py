import json
import subprocess
import os

TRANSCRIPT_PATH = "transcripts/transcript.json"
VIDEO_PATH = "video/source_video.mp4"

BUFFER = 15        # seconds before event
CLIP_DURATION = 60 # seconds total clip length

with open(TRANSCRIPT_PATH, "r", encoding="utf-8") as f:
    segments = json.load(f)

os.makedirs("clips/question_answer", exist_ok=True)
os.makedirs("clips/agreement", exist_ok=True)
os.makedirs("clips/disagreement", exist_ok=True)

def extract_clip(start_time, category, index):
    clip_start = max(0, start_time - BUFFER)
    output_path = f"clips/{category}/{category}_{index}.mp4"

    cmd = [
        "ffmpeg",
        "-y",
        "-ss", str(clip_start),
        "-i", VIDEO_PATH,
        "-t", str(CLIP_DURATION),
        "-c:v", "libx264",
        "-c:a", "aac",
        output_path
    ]

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

index = 1

for seg in segments:
    text = seg["text"].lower()
    start = seg["start"]

    if "?" in text:
        extract_clip(start, "question_answer", index)
        index += 1

    elif any(w in text for w in ["i agree", "yes", "exactly"]):
        extract_clip(start, "agreement", index)
        index += 1

    elif any(w in text for w in ["i disagree", "no", "wrong"]):
        extract_clip(start, "disagreement", index)
        index += 1

print("Clip extraction completed with audio")
