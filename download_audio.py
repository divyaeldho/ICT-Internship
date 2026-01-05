import yt_dlp

YOUTUBE_URL = "https://youtu.be/JbORT5Fqbng?si=7r5G1mFo7t1E7w3z"

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'audio/extracted.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([YOUTUBE_URL])

print("Audio downloaded successfully")
