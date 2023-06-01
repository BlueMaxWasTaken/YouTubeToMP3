from pytube import YouTube, Playlist
import os
import time

url = input("Enter URL of YouTube video or playlist:\n")

if 'playlist' in url.lower():
    playlist = Playlist(url)
    print("Downloading playlist: " + playlist.title)

    destination = input("Enter the destination address (leave blank to save in the current directory):\n") or '.'

    start_time = time.time()
    for video_url in playlist.video_urls:
        yt = YouTube(video_url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=destination)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    elapsed_time = time.time() - start_time

    print("Playlist downloaded successfully.")
    print("Elapsed time: {:.2f} seconds.".format(elapsed_time))

else:
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    destination = input("Enter the destination address (leave blank to save in the current directory):\n") or '.'

    start_time = time.time()
    out_file = video.download(output_path=destination)
    elapsed_time = time.time() - start_time

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(yt.title + " has been successfully downloaded.")
    print("Elapsed time: {:.2f} seconds.".format(elapsed_time))
