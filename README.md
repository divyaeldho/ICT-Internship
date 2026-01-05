# ICT-Internship
AI-based Moment Extraction
# YouTube Video Analyzer System

## Project Overview
This project is an AI-based system designed to analyze publicly available YouTube videos such as podcasts, interviews, or talk shows. The system automatically identifies and extracts important conversational moments, including Question–Answer segments, Agreement moments, and Disagreement moments.

The solution uses pre-trained AI models and audio-video processing techniques to build a complete end-to-end AI/ML pipeline.

---

## Problem Statement
Manual analysis of long-form video content is time-consuming and inefficient. This project aims to automate the identification of key conversational moments from YouTube videos to support media analysis and content understanding.

---

## Methodology
1. A YouTube video link is provided as input.
2. Audio is extracted from the video using yt-dlp and FFmpeg.
3. Speech-to-text transcription is performed using a pre-trained Whisper model.
4. Transcribed text is analyzed to detect key conversational events.
5. Contextual video clips (30–60 seconds) are extracted around detected moments.

---

## Technologies Used
- Python
- OpenAI Whisper (pre-trained model)
- yt-dlp
- FFmpeg
- Torch
- NumPy

---

## Project Structure
- `download_audio.py` – Downloads and extracts audio from YouTube videos  
- `transcribe.py` – Converts audio to text using Whisper  
- `extract_clips.py` – Extracts categorized video clips  
- `audio/` – Extracted audio files  
- `transcripts/` – Generated transcripts  
- `clips/` – Output video clips  

---

## Setup Instructions
1. Create and activate a virtual environment
2. Install dependencies:
