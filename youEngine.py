from pytubefix import YouTube
from pytubefix.cli import on_progress


class YoutubeVideo:
    """
    Youtube Class for downloading videos, music etc.
    """

    def __init__(self, url: str = 'https://www.youtube.com/watch?v=jNQXAC9IVRw', path: str = './'):
        """
        :param url: url to Youtube of video or music (str)
        :param path:  path to save Youtube file (str)
        """
        self.url = url
        self.save_path = path

        try:
            self.yt = YouTube(self.url, on_progress_callback=on_progress, use_po_token=False)
            self.title = self.yt.title
            print(f"Starting download...")
        except Exception as e:
            print(f"Someting Went Wrong. Check url address \n {e}")

    def download_video(self):
        try:
            streams = self.yt.streams.filter(progressive=True, file_extension="mp4")
            highest_res_stream = streams.get_highest_resolution()
            highest_res_stream.download(output_path=self.save_path)
            print(f"Successfully Downloaded Video \"{self.title}\"")
        except Exception as e:
            print(f"Someting Went Wrong. {e}")

    def download_music(self):
        try:
            streams = self.yt.streams.get_audio_only()
            streams.download(output_path=self.save_path)
            print(f"Successfully Downloaded Music \"{self.title}\"")
        except Exception as e:
            print(f"Someting Went Wrong. {e}")



