import yt_dlp
import os


def download_youtube_720p(url, output_path="downloads"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'merge_output_format': 'mp4',
        'postprocessors': [{   # force audio re-encode
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }],
        'postprocessor_args': [
            '-c:v', 'copy',    # keep original video
            '-c:a', 'aac'      # re-encode audio to AAC
        ]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# Example
link = "https://www.youtube.com/watch?v=61a7UkDO50s"
download_youtube_720p(link)
