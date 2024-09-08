from youEngine import YoutubeVideo


if __name__ == "__main__":
    try:
        video_url = input("Enter a YouTube URL here: ")
        print("Select folder to download")
        save_dir = './musics'
        yt = YoutubeVideo(video_url, save_dir)
        yt.download_music()
    except Exception as e:
        print(e)
