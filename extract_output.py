import json
import subprocess
import os
import re


# ---------------- Configuration ----------------
TRANSCRIPT_PATH = "transcripts/transcript.json"
VIDEO_PATH = "video/source_video.webm"

BUFFER_SECONDS = 15
OUTPUT_DURATION = 60


# ---------------- Keyword Definitions ----------------
QUESTION_KEYWORDS = [
    "what", "why", "how", "when", "where",
    "who", "which", "can you", "could you",
    "do you", "is it", "are you"
]

AGREEMENT_KEYWORDS = [
    "i agree",
    "yes",
    "right",
    "correct",
    "exactly",
    "true",
    "makes sense",
    "i think so"
]

DISAGREEMENT_KEYWORDS = [
    "i disagree",
    "no",
    "not correct",
    "not true",
    "wrong",
    "i dont think so"
]


# ---------------- Helper Functions ----------------
def clean_text(text):
    """
    Normalizes transcript text for better keyword matching.
    Removes punctuation and converts to lowercase.
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text


def load_transcript(path):
    """Load transcript segments from JSON file."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def create_output_folders():
    """Create directories for storing outputs."""
    os.makedirs("outputs/question_answer", exist_ok=True)
    os.makedirs("outputs/agreement", exist_ok=True)
    os.makedirs("outputs/disagreement", exist_ok=True)


def extract_video_output(start_time, category, index):
    """
    Extracts a video output segment using FFmpeg
    based on detected conversational moment.
    """

    output_start_time = max(0, start_time - BUFFER_SECONDS)
    output_path = f"outputs/{category}/{category}_{index}.mp4"

    ffmpeg_command = [
        "ffmpeg", "-y",
        "-ss", str(output_start_time),
        "-i", VIDEO_PATH,
        "-t", str(OUTPUT_DURATION),
        "-c:v", "libx264",
        "-c:a", "aac",
        output_path
    ]

    subprocess.run(ffmpeg_command)


# ---------------- Main Processing ----------------
print("Loading transcript...")
segments = load_transcript(TRANSCRIPT_PATH)

create_output_folders()

qa_count = 1
agreement_count = 1
disagreement_count = 1

print("Detecting moments and generating outputs...")

for segment in segments:
    raw_text = segment["text"]
    cleaned_text = clean_text(raw_text)
    start_time = segment["start"]

    if any(word in cleaned_text for word in QUESTION_KEYWORDS):
        extract_video_output(start_time, "question_answer", qa_count)
        qa_count += 1

    elif any(word in cleaned_text for word in AGREEMENT_KEYWORDS):
        extract_video_output(start_time, "agreement", agreement_count)
        agreement_count += 1

    elif any(word in cleaned_text for word in DISAGREEMENT_KEYWORDS):
        extract_video_output(start_time, "disagreement", disagreement_count)
        disagreement_count += 1


print("All conversational outputs generated successfully!")
