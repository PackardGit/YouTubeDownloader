from pydub import AudioSegment
import os


class MusicConversion:
    def __init__(self, actual_format: str = '.m4a',
                 music_dir: str = './music_files/downloaded', target_dir: str = './music_files/converted_to_mp3'):
        self.actual_format = actual_format
        self.music_dir = music_dir
        self.target_dir = target_dir
        self.files = os.listdir(self.music_dir)

    def to_mp3(self, status_queue):
        try:
            msg = "Conversion to .mp3 has started..."
            print(msg)
            status_queue.put(msg)
            for m4a_file in self.files:
                audio = AudioSegment.from_file(os.path.join(self.music_dir, m4a_file), format="m4a")
                audio = audio.set_frame_rate(20000)
                audio.export(os.path.join(self.target_dir, m4a_file.replace(self.actual_format, '.mp3')), format="mp3")
                msg = "Successfully converted_to_mp3: " + m4a_file
                status_queue.put(msg)
                print(msg)
        except Exception as e:
            msg = f"Conversion to Mp3 failed. {e}"
            status_queue.put(msg)
            print(msg)
        finally:
            msg = "Successfully converted all the files!"
            status_queue.put(msg)
            print(msg)
