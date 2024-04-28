from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def video_downloader(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        high_res_stream = streams.get_highest_resolution()
        high_res_stream.download(output_path=save_path)
        print(f"'{high_res_stream.title}' downloaded successfully.")
    except Exception as e:
        print(e)


def audio_downloader(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.get_audio_only()
        streams.download(output_path=save_path)
        print(f"'{streams.title}' downloaded successfully.")
    except Exception as e:
        print(e)


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    download_type = input("For video press v, for audio press a: ").upper()
    if download_type == "V":
        video_url = input("Please enter a video url: ")
        save_dir = open_file_dialog()
        if save_dir:
            video_downloader(video_url, save_path=save_dir)
        else:
            print('invalid save location')
    elif download_type == "A":
        audio_url = input("Please enter a video url: ")
        save_dir = open_file_dialog()
        if save_dir:
            audio_downloader(audio_url, save_path=save_dir)
        else:
            print('invalid save location')
    else:
        print("invalid entry")
