from pydub import AudioSegment
import os

# AudioSegment.ffmpeg = r"G:\\Python Projects\\YouTubeDownloader\\ffmpeg-8.0-full_build\\bin\\ffmpeg.exe"
# AudioSegment.ffprobe = r"G:\\Python Projects\\YouTubeDownloader\\ffmpeg-8.0-full_build\\bin\\ffprobe.exe"
# AudioSegment.converter = r"G:\\Python Projects\\YouTubeDownloader\\ffmpeg-8.0-full_build\\bin\\ffmpeg.exe"

files = os.listdir('./musics_new')
# for file in files:
#     file_name = file.split(".")[0]
#     print(file_name)
#     AudioSegment.from_file("./musics/"+file).export("./mp3/"+file_name, format="mp3")

m4a_directory = "./musics_new"
mp3_directory = './mp3/80'
print("Start converting...")
for m4a_file in files:
    audio = AudioSegment.from_file(os.path.join(m4a_directory, m4a_file), format="m4a")
    audio = audio.set_frame_rate(20000)
    audio.export(os.path.join(mp3_directory, m4a_file.replace('.m4a', '.mp3')), format="mp3")
    print("Succesfully converted: " + m4a_file)
