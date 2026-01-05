import yt_dlp

YOUTUBE_URL = "https://youtu.be/JbORT5Fqbng?si=7r5G1mFo7t1E7w3z"

ydl_opts = {
    "format": "best",
    "outtmpl": "video/source_video.%(ext)s"
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([YOUTUBE_URL])

print("Video downloaded successfully")
