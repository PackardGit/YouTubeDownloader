from youEngine import YoutubeVideo


if __name__ == "__main__":
    try:
        f = open("links.txt", "r")
        list_of_links = f.readlines()
        list_of_links = [link.strip() for link in list_of_links]
    except Exception as e:
        list_of_links = []
        print(e)

    for link in list_of_links:
        try:
            # video_url = input("Enter a YouTube URL here: ")
            # print("Select folder to download")
            save_dir = './musics_new'
            yt = YoutubeVideo(link, save_dir)
            yt.download_music()
        except Exception as e:
            print(e)


