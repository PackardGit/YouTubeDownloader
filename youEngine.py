from pytubefix import YouTube
from pytubefix.cli import on_progress
import time


class YoutubeDownloader:
    """
    Youtube Class for downloading videos, music etc.
    """

    def __init__(self, urls: tuple = ('https://www.youtube.com/watch?v=jNQXAC9IVRw',),
                 path: str = './music_files/downloaded'):
        """
        :param url: url to Youtube of video or music (str)
        :param path:  path to save Youtube file (str)
        """
        self.urls = urls
        self.save_path = path

    # def download_video(self):
    #     try:
    #         streams = self.yt.streams.filter(progressive=True, file_extension="mp4")
    #         highest_res_stream = streams.get_highest_resolution()
    #         highest_res_stream.download(output_path=self.save_path)
    #         print(f"Successfully Downloaded Video \"{self.title}\"")
    #     except Exception as e:
    #         print(f"Something Went Wrong :( {e}")

    def download_music(self, status_queue):
        try:
            msg = "Downloading has started."
            print(msg)
            status_queue.put(msg)
            for url in self.urls:
                yt = YouTube(url, on_progress_callback=on_progress, use_po_token=False)
                title = yt.title
                streams = yt.streams.get_audio_only()
                streams.download(output_path=self.save_path)
                msg = f"Successfully Downloaded Music \"{title}\""
                print(msg)
                status_queue.put(msg)

        except Exception as e:
            msg = f"Something Went Wrong :( {e}"
            print(msg)
            status_queue.put(msg)

        finally:
            msg = f"Successfully Downloaded All the files"
            print(msg)
            status_queue.put(msg)
