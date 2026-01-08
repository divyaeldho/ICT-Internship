import yt_dlp

def download_youtube_video(video_url, save_path="video/source_video"):
    """
    Downloads a YouTube video and saves it locally.
    This function is written for clarity and reuse.
    """

    print("Starting video download...")

    ydl_options = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": f"{save_path}.%(ext)s",
        "quiet": False
    }

    try:
        with yt_dlp.YoutubeDL(ydl_options) as downloader:
            downloader.download([video_url])

        print("Download completed successfully!")

    except Exception as error:
        print("Something went wrong during download.")
        print(f"Error details: {error}")


# ---- Execution starts here ----
YOUTUBE_URL = "https://youtu.be/JbORT5Fqbng?si=7r5G1mFo7t1E7w3z"

download_youtube_video(YOUTUBE_URL)

