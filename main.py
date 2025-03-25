from pytube import YouTube

def download_youtube_video(video_url, save_path):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        print(f"Downloading: {yt.title}")
        video_stream.download(output_path=save_path)
        print("Download completed!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace with the URL of the YouTube video you want to download
    video_url = input("Enter the YouTube video URL: ")
    
    # Specify the path where you want to save the video
    save_path = input("Enter the path where you want to save the video: ")

    download_youtube_video(video_url, save_path)