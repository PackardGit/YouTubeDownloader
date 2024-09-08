from pytubefix import YouTube
from pytubefix.cli import on_progress


class YoutubeVideo:
    """
    Youtube Class
    """

    def __init__(self, url: str = 'https://www.youtube.com/watch?v=jNQXAC9IVRw', path: str = './videos'):
        self.url = url
        self.save_path = path

        try:
            self.yt = YouTube(self.url, on_progress_callback=on_progress)
            self.title = self.yt.title
        except Exception as e:
            print(f"Someting Went Wrong. Check url address \n {e}")

    def download_video(self):
        try:
            streams = self.yt.streams.filter(progressive=True, file_extension="mp4")
            highest_res_stream = streams.get_highest_resolution()
            print(f"Starting download...")
            highest_res_stream.download(output_path=self.save_path)
            print(f"Successfully Downloaded Video \"{self.title}\"")
        except Exception as e:
            print(f"Someting Went Wrong. {e}")

    def download_music(self):
        try:
            streams = self.yt.streams.get_audio_only()
            print(f"Starting download...")
            streams.download(mp3=True, output_path=self.save_path)
            print(f"Successfully Downloaded Music \"{self.title}\"")
        except Exception as e:
            print(f"Someting Went Wrong. {e}")
