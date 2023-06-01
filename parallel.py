from pytube import YouTube, Playlist
import os
import time
import concurrent.futures

def download_video(video_url, destination):
    yt = YouTube(video_url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=destination)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

url = input("Enter URL of YouTube video or playlist:\n")

if 'playlist' in url.lower():
    playlist = Playlist(url)
    print("Downloading playlist: " + playlist.title)

    destination = input("Enter the destination address (leave blank to save in the current directory):\n") or '.'

    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for video_url in playlist.video_urls:
            futures.append(executor.submit(download_video, video_url, destination))

        concurrent.futures.wait(futures)

    elapsed_time = time.time() - start_time

    print("Playlist downloaded successfully.")
    print("Elapsed time: {:.2f} seconds.".format(elapsed_time))

else:
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    destination = input("Enter the destination address (leave blank to save in the current directory):\n") or '.'

    start_time = time.time()
    download_video(url, destination)
    elapsed_time = time.time() - start_time

    print(yt.title + " has been successfully downloaded.")
    print("Elapsed time: {:.2f} seconds.".format(elapsed_time))
