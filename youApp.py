import tkinter as tk
from lib.style_lib import btn_style, textbox_style
from youEngine import YoutubeDownloader
import threading
import queue
from collections import deque
from converter import MusicConversion


class YouApp(tk.Frame):
    """
    Tkinter application connected with youEngine enabling to download music from YouTube
    No arguments are needed
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.queue = queue.Queue()

        self.icon = tk.PhotoImage(file="./lib/icon.png")
        self.master.iconphoto(True, self.icon)

        self.pack()
        self.master.title("youApp")
        self.master.geometry("800x600")
        self.master.maxsize(800, 600)

        self.welcome_label = tk.Label(self, text="Welcome to YouApp!", font=("TkHeadingFont", 20, 'bold'), fg='red')
        self.welcome_label.pack(padx=10, pady=10)

        self.music_textbox = tk.Text(self, height=10, font=("Arial", 10))
        self.music_textbox.pack(padx=10, pady=10)

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack(pady=5, fill='x')
        self.download_button = tk.Button(self.buttons_frame, text="Download\n📥", **btn_style, command=self.download)
        self.download_button.pack(side="left", padx=5, expand=True, fill='x')
        self.convert_button = tk.Button(self.buttons_frame, text="Convert\n🔄", **btn_style, command=self.convert)
        self.convert_button.pack(side="left", padx=5, expand=True, fill='x')

        self.status = tk.StringVar(value="->")
        self.status_history = deque(maxlen=6)
        self.after(100, self.check_queue)

        status_label = tk.Label(self,textvariable=self.status, **textbox_style)
        status_label.pack(fill="x", padx=10, pady=(5, 10), ipady=20)
        status_label.pack_propagate(False)

    def download(self):
        text = self.music_textbox.get("1.0", "end-1c")
        list_of_links = tuple(text.split('\n'))
        yt_handler = YoutubeDownloader(list_of_links)
        download_thread = threading.Thread(target=yt_handler.download_music, args=(self.queue,), daemon=True)
        download_thread.start()

    def convert(self):
        conversion_handler = MusicConversion()
        conversion_thread = threading.Thread(target=conversion_handler.to_mp3, args=(self.queue,), daemon=True)
        conversion_thread.start()

    def update_status(self, msg):
        self.status_history.append(msg)
        self.status.set("\n".join(self.status_history))

    def check_queue(self):
        try:
            while True:
                msg = self.queue.get_nowait()
                self.update_status(msg)
        except queue.Empty:
            pass

        self.after(100, self.check_queue)


if __name__ == "__main__":
    a = YouApp()
    a.mainloop()
